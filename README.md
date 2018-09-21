# jetsonUtilities
This repository holds utilities for working with NVIDIA Jetson Development Kit

# jetsonInfo
Get information about the NVIDIA Jetson OS environment on NVIDIA Jetson Development Kits (TK1, TX1, TX2, Xavier)

The information about the NVIDIA Jetson Development Kit operating system is spread over a few files. This is a handy tool to use for reference.

The Python script jetsoninfo.py will list the hardware, version of L4T that is running, Ubuntu version, and the Linux kernel revision. To execute:

$ python jetsonInfo.py

or

$ ./jetsonInfo.py

The hardware designator is derived from the file: '/proc/cpuinfo'

The L4T version is derived from the file: '/etc/nv_tegra_release'

The Ubuntu version is derived from the file: '/etc/os-release'

The Linux kernel version is derived from the file: '/proc/version'

Release Notes:
September, 2018
* v1.1
* Add support for JetPack 3.3 (L4T 28.2.1)
* Add support for Jetson AGX Xavier
* Add support for JetPack 4.0 (L4T 31.0.1)

July, 2018
* v1.0
* Add support for JetPack 3.2.1 (L4T 28.2.1)

The shell script jetson_variables is derived from jetson_easy: https://github.com/rbonghi/jetson_easy

Copyright (c) 2015-2018 Raffaello Bonghi

See license for jetson_easy in scripts folder

