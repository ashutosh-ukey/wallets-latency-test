# Instructions

The final output is `outputs/avgReqTimes-compare.yml`. To generate it


1. Clone this repo. From the root folder, run 
```bash
python3 -m pip install -r requirements.txt
```

2. Start a local instance of `wallets-api` from the master branch. 

3. Generate an API key and fill it out in the `api_key` in  `send_reqs.py`. In the same file, set the `res_file` variable to `outputs/avgReqTimes-current.yml`.

4. Generate the latency distrubtion for the current local instance by running
```bash
python3 send_reqs.py
```

5. Start a local instance of `wallets-api` from the branches with the new changes. 

6. Generate and fill out the `api_key` again in `send_reqs.py`. Set the `res_file` variable to `outputs/avgReqTimes-newChanges.yml`.

7. Generate the latency distrubtion for the current local instance by running
```bash
python3 send_reqs.py
```

8. Combine the result into a single file for easy side-by-side comparison by running 
```bash
python3 combine_times.py
```