"""
    Latency test against wallets-api endpoints
"""

import statistics
import requests
import yaml

res_file = "outputs/avgReqTimes-current.yml"

api_key = "<your-api-key-here>"
base_url = "http://localhost:10004"

endpoints = [
    "/ping",
    "/v1/configuration",
    "/v1/encryption/public",
    "/v1/channels",
    "/v1/stablecoins",

    "/v1/businessAccount/balances",

    "/v1/payments",
    "/v1/transfers?returnIdentities=false",
    "/v1/cards",
    "/v1/settlements",
    "/v1/chargebacks",
    "/v1/reversals",
    "/v1/balances",

    "/v1/wallets"
]

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Bearer {api_key}"
}

if __name__ == '__main__':
    res = {}
    num_reqs_per_endpoint = 100

    res["Trials per endpoint"] = num_reqs_per_endpoint
    res["Request times distribution (ms)"] = {}

    # Query all endpoints
    for e in endpoints:
        full_url = base_url + e

        elapsed_times_ms = []

        for _ in range(num_reqs_per_endpoint):
            response = requests.get(full_url, headers=headers)

            # print(response.status_code)
            if response.ok:
                cur_elapsed_ms = response.elapsed.total_seconds() * 1000
                elapsed_times_ms.append(cur_elapsed_ms)

        num_success = len(elapsed_times_ms)

        if num_success < num_reqs_per_endpoint:
            print(f"Warning: only {num_success} request(s) succeeded for {e}")
        
        if num_success > 0:
            # Calculate statistics for requests (i.e. mean, standard deviation)
            stat_summary = { 
                "mean": statistics.mean(elapsed_times_ms),
                "stdev": statistics.stdev(elapsed_times_ms)
            }

            if num_success < num_reqs_per_endpoint:
                stat_summary["trials"] = num_success

            endpoint_key = "GET " + e
            res["Request times distribution (ms)"][endpoint_key] = stat_summary

    # Write out results
    with open(res_file, 'w') as json_file:
        yaml.dump(res, json_file, indent=4, sort_keys=False)

