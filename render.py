#!/usr/bin/python

import os
from version import VERSION
from termcolor import colored

def screen(full_process_listing, usable_width, usable_height, cpubar,membar,swapbar):
    usable_width += 25
    os.system("clear")
    print(cpubar)
    print(membar)
    print(swapbar)
    print("%s version %s - written in Python by John Helliwell - nproc %d" % (colored("jtop!", 'green'), VERSION , len(full_process_listing)))
    print()
    print("%s" % colored("   PID  CPU%    MEM%    CMDLINE", attrs=['reverse']), end="")
    for filler in range(31,usable_width):
        print("%s" % colored(" ", attrs=['reverse']), end="")
    print()
    tracker=0
    for individual_process in full_process_listing:
        print('{:>6} '.format(individual_process['pid']),end="")
        print('{:>5}'.format(individual_process['cpu_percent']),end="")
        print('   {:>5.1f}    '.format(individual_process['memory_percent']),end="")
        if individual_process['cmdline'] == None:
            print("[defunct]")
            continue
        if len(individual_process['cmdline']) == 0:
            print('[{}]'.format(individual_process['name']))
        else:
            output=""
            for argu in individual_process['cmdline']:
                output += argu + " "
            count=0
            for char in output:
                print(char, end="")
                count += 1
                if count >= (usable_width - 25):
                    break
            print()
        tracker += 1
        if tracker > usable_height:
            break

def drawbar(title, width, percent):
    bar = int((width - 11) * percent / 100.0)
    barcounter = 0
    rendered_bar = "{} {:2}% ".format(title, percent)
    while barcounter <= bar:
        if percent <= 50.0:
            rendered_bar =  rendered_bar + colored("|", 'green')
        else:
            if percent <= 75.0:
                rendered_bar = rendered_bar + colored("|", 'yellow')
            else:
                rendered_bar = rendered_bar + colored("|", 'red')
        barcounter += 1
    return rendered_bar
