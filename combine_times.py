import yaml


cur_times_file = "outputs/avgReqTimes-current.yml"
new_times_file = "outputs/avgReqTimes-newChanges.yml"

res_file = "outputs/avgReqTimes-compare.yml"


if __name__ == '__main__':

    with open(cur_times_file, "r") as stream:
       res = yaml.safe_load(stream)

    with open(new_times_file, "r") as stream:
       new_times = yaml.safe_load(stream)

    for e in res["Request times distribution (ms)"].values():
        e["cur-mean"] = e["mean"]
        e["cur-stdev"] = e["stdev"]

        del e["mean"]
        del e["stdev"]

    new_reqs = new_times["Request times distribution (ms)"]
    for e_key in new_reqs:
        new_e = new_reqs[e_key]
        res_e = res["Request times distribution (ms)"][e_key]

        res_e["new-mean"] = new_e["mean"]
        res_e["new-stdev"] = new_e["stdev"]

    # Write out results
    with open(res_file, 'w') as json_file:
        yaml.dump(res, json_file, indent=4, sort_keys=False)

