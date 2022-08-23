#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# MIT License
# Copyright (c) 2017-2022 Jetsonhacks
# Please see accompanying license information
from __future__ import print_function
import os,sys

class terminalColors:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

import pprint
import subprocess

command = ['bash', '-c', 'source scripts/jetson_variables.sh && env']

proc = subprocess.Popen(command, stdout = subprocess.PIPE)
environment_vars = {}
for line in proc.stdout:
  (key, _, value) = line.partition(b"=")
  environment_vars[key.decode()] = value.decode()

proc.communicate() 

# Jetson Model
print("NVIDIA " + environment_vars["JETSON_MODEL"].strip())

#L4T Version
print(' L4T ' + environment_vars['JETSON_L4T'].strip() + ' [ JetPack ' +environment_vars['JETSON_JETPACK'].strip()+' ]')
# Ubuntu version
if os.path.exists('/etc/os-release'):
    with open('/etc/os-release', 'r') as ubuntuVersionFile:
        ubuntuVersionFileText=ubuntuVersionFile.read()
    for line in ubuntuVersionFileText.splitlines(): 
        if 'PRETTY_NAME' in line: 
            # PRETTY_NAME="Ubuntu 16.04 LTS"
            ubuntuRelease=line.split('"')[1]
            print('   ' + ubuntuRelease)       
else:
    print(terminalColors.FAIL + 'Error: Unable to find Ubuntu Version'  + terminalColors.ENDC)
    print('Reason: Unable to find file /etc/os-release')

# Kernel Release
if os.path.exists('/proc/version'):
    with open('/proc/version', 'r') as versionFile:
        versionFileText=versionFile.read()
    kernelReleaseArray=versionFileText.split(' ')
    print('   Kernel Version: ' + kernelReleaseArray[2])
else:
    print(terminalColors.FAIL + 'Error: Unable to find Linux kernel version'  + terminalColors.ENDC)
    print('Reason: Unable to find file /proc/version')


command1 = ['bash', '-c', 'source scripts/jetson_libraries.sh && env']

proc1 = subprocess.Popen(command1, stdout = subprocess.PIPE)
# environment_vars = {}
for line in proc1.stdout:
  (key, _, value) = line.partition(b"=")
  environment_vars[key.decode()] = value.decode()



print(' CUDA ' + environment_vars['JETSON_CUDA'].strip())
print('   CUDA Architecture: ' + environment_vars['JETSON_CUDA_ARCH_BIN'].strip())
print(' OpenCV version: ' + environment_vars['JETSON_OPENCV'].strip())
print('   OpenCV Cuda: ' + environment_vars['JETSON_OPENCV_CUDA'].strip())
print(' CUDNN: ' + environment_vars['JETSON_CUDNN'].strip())
print(' TensorRT: ' + environment_vars['JETSON_TENSORRT'].strip())
print(' Vision Works: ' + environment_vars['JETSON_VISIONWORKS'].strip())
print(' VPI: ' + environment_vars['JETSON_VPI'].strip())
print(' Vulcan: ' + environment_vars['JETSON_VULKAN_INFO'].strip())


