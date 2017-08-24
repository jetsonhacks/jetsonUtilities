#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# MIT License
# Copyright (c) 2017 Jetsonhacks
# Please see accompanying license information

import os,sys

class terminalColors:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
  
# Print out the hardware information, e.g. jetson_tx1
if os.path.exists('/proc/cpuinfo'):
    with open("/proc/cpuinfo","r") as cpuInfoFile:
        cpuInfoFileText=cpuInfoFile.read()
    # print cpuInfoFileText
    foundHardware = False
    for line in cpuInfoFileText.splitlines():
        if ':' in line:
            left, right = line.split(':', 1)
            left = left.strip().lower()
            right = right.strip()
            if left == "hardware" and len(right) > 0:
                print " Hardware: " + right
                foundHardware = True
                break 
    if foundHardware == False :
        print terminalColors.FAIL + "Error: Unable to find Hardware entry" + terminalColors.ENDC
        print "Reason: Unable to find in file /proc/cpuinfo"
else:
    print terminalColors.FAIL + "Error: Unable to find hardware information" + terminalColors.ENDC
    print "Reason: Unable to find file /proc/cpuinfo"

#L4T Version
if os.path.exists('/etc/nv_tegra_release'):
    with open("/etc/nv_tegra_release","r") as l4tVersionFile:
        l4tVersionFileText=l4tVersionFile.read()
    textLines=l4tVersionFileText.splitlines() 
    l4tVersionInfo=textLines[0].split(',')
    for entry in l4tVersionInfo:
        if 'release' in entry: 
            # Example: '# R24 (release)'
            l4tRelease=entry.split(' ')[1]
            l4tRelease=filter(str.isdigit,l4tRelease)
            print ' ' + entry            
        elif 'REVISION' in entry:
            # Example: 'REVISION: 2.1'
            l4tRevision=entry.split(' ')[2]
            print entry
        elif 'BOARD' in entry:
            # Example: 'BOARD: t210ref'
            board=entry
            print entry

    print ' L4T ' + l4tRelease + '.' + l4tRevision   
    # print l4tVersionInfo
else:
    print terminalColors.FAIL + "Error: Unable to find L4T Version"  + terminalColors.ENDC
    print "Reason: Unable to find file /etc/nv_tegra_release"



# Kernel Release
if os.path.exists('/proc/version'):
    with open("/proc/version","r") as versionFile:
        versionFileText=versionFile.read()
    kernelReleaseArray=versionFileText.split(" ")
    print " Kernel Version: " + kernelReleaseArray[2]
else:
    print terminalColors.FAIL + "Error: Unable to find Linux kernel version"  + terminalColors.ENDC
    print "Reason: Unable to find file /proc/version"

 
