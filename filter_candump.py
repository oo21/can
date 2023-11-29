import json
log_file = open("candump-2023-11-06_163845_200m.log","r")

#id = input("enter id: ")

unique_pids = {}
ff = open("filter_res.txt","w")
for line in log_file:
    pid = line.split(" ")[-1].split("#")[0]
    if pid == "56B":
        ff.write(f"{line}")
    #unique_pids[pid] = line
#print(json.dumps(unique_pids,indent=4))
#print(len(unique_pids))

#unique_pids = 81