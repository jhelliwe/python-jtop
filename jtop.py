#!/usr/bin/python

import linuxproc
import render
import terminfo
import psutil
import time
import version

while True:
    # Calclate the terminal session size
    session_width, session_height=terminfo.termsize()
    usable_width = session_width - 25   # Usable size calculated from the
    usable_height = session_height - 8  # screen space left after the headers
    # Calculate CPU%, MEM% and SWAP%
    cpuperc = int(psutil.cpu_percent())
    memtotal, memfree, swaptotal, swapfree = linuxproc.memoryproc()
    memperc = 100-int((memfree / memtotal) * 100.0)
    swapperc = 100-int((swapfree / swaptotal) * 100.0)
    # Render the bars into String variables
    cpubar = render.drawbar("CPU%", usable_width, cpuperc)
    membar = render.drawbar("MEM%", usable_width, memperc)
    swapbar = render.drawbar("SWP%", usable_width, swapperc)
    # Populate a list of running processes and then sort the list by CPU usage
    full_process_listing = {p.pid: p.info for p in psutil.process_iter(['pid', 'cpu_percent', 'memory_percent', 'cmdline', 'name' ] )}
    values = list(full_process_listing.values())
    values.sort(key=lambda x: x['cpu_percent'], reverse=True)
    # Render the screen output
    render.screen(values, usable_width, usable_height, cpubar,membar,swapbar)
    time.sleep(2)
