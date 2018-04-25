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

import pprint
import subprocess

command = ['bash', '-c', 'source jetson/jetson_variables && env']

proc = subprocess.Popen(command, stdout = subprocess.PIPE)

for line in proc.stdout:
  (key, _, value) = line.partition("=")
  os.environ[key] = value

proc.communicate()

# Jetson Model
print " NVIDIA Jetson " + os.environ["JETSON_BOARD"].strip() 

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
        elif 'REVISION' in entry:
            # Example: 'REVISION: 2.1'
            l4tRevision=entry.split(' ')[2]
        elif 'BOARD' in entry:
            # Example: 'BOARD: t210ref'
            board=entry.split(' ')[2]
    print ' L4T ' + l4tRelease + '.' + l4tRevision + " [ JetPack " +os.environ["JETSON_JETPACK"].strip()+" ]"
    print ' Board: ' + board  
else:
    print terminalColors.FAIL + "Error: Unable to find L4T Version"  + terminalColors.ENDC
    print "Reason: Unable to find file /etc/nv_tegra_release"

# Ubuntu version
if os.path.exists('/etc/os-release'):
    with open("/etc/os-release","r") as ubuntuVersionFile:
        ubuntuVersionFileText=ubuntuVersionFile.read()
    for line in ubuntuVersionFileText.splitlines(): 
        if 'PRETTY_NAME' in line: 
            # PRETTY_NAME="Ubuntu 16.04 LTS"
            ubuntuRelease=line.split('"')[1]
            print ' ' + ubuntuRelease            
else:
    print terminalColors.FAIL + "Error: Unable to find Ubuntu Version"  + terminalColors.ENDC
    print "Reason: Unable to find file /etc/os-release"



# Kernel Release
if os.path.exists('/proc/version'):
    with open("/proc/version","r") as versionFile:
        versionFileText=versionFile.read()
    kernelReleaseArray=versionFileText.split(" ")
    print " Kernel Version: " + kernelReleaseArray[2]
else:
    print terminalColors.FAIL + "Error: Unable to find Linux kernel version"  + terminalColors.ENDC
    print "Reason: Unable to find file /proc/version"

print " CUDA " + os.environ["JETSON_CUDA"].strip() 
