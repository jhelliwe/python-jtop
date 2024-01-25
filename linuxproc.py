#!/usr/bin/python
# read stuff from /proc - like free memory and swap

def memoryproc():
    fh = open("/proc/meminfo", "r")
    for eachline in fh.readlines():
        if eachline.startswith("MemTotal:"):
            memtotal=int((eachline.split()[1]))
        if eachline.startswith("MemAvailable:"):
            memavail=int((eachline.split()[1]))
        if eachline.startswith("SwapTotal:"):
            swaptotal=int((eachline.split()[1]))
        if eachline.startswith("SwapFree:"):
            swapfree=int((eachline.split()[1]))
    fh.close()
    return(memtotal,memavail,swaptotal,swapfree)
