start1 = 1699278934.0561223
end1 = 1699278994.32991

start2 = 1699279486.7038548
end2 = 1699279573.8200264

start3 = 1699279623.0560853
end3 = 1699279700.275612



f = open('filter_res.txt','r') # make it liosts all log files
#f1 = open('event1','w')
#f2 = open('event2','w')
#f3 = open('event3','w')
res = open('speed','w')
for l in f:
    dl = l.split(" ")  # data list
    # time stamp
    ts = float(dl[0].split('(')[1].split(')')[0])
    # data & PID
    dap = dl[-1].split("#")
    data = dap[-1][:-1]
    # PID
    pid = dap[0]
    print(pid," ",data[:2])
    speed = int(data[:2],16)/2
    res.write(f"{ts},{speed}\n")
    print(speed)
    #print (l,ts,pid,data)
    #if ts > start1 and ts < end1:
    #    f1.write(l)
    #if ts > start2 and ts < end2:
    #    f2.write(l)
    #if ts > start3 and ts < end3:
    #    f3.write(l)