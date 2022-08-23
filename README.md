# jetsonUtilities
This repository holds utilities for working with NVIDIA Jetson Development Kit

# jetsonInfo
Get information about the NVIDIA Jetson OS environment on NVIDIA Jetson Development Kits (TX1, TX2, AGX Xavier, Xavier NX, Nano, Nano 2GB)

The information about the NVIDIA Jetson Development Kit operating system is spread over a few files. This is a handy tool to use for reference.

The Python script jetsoninfo.py will list the hardware, version of L4T that is running, Ubuntu version, and the Linux kernel revision. To execute:
```
$ python jetsonInfo.py
```
or
```
$ python3 jetsonInfo.py
```
or
```
$ ./jetsonInfo.py 
```
The hardware designator is derived from the file: '/proc/cpuinfo'

The L4T version is derived from the file: '/etc/nv_tegra_release'

The Ubuntu version is derived from the file: '/etc/os-release'

The Linux kernel version is derived from the file: '/proc/version'

Thank you Raffaello Bonghi @rbonghi for jetson_variables and jetson_libraries scripts

### Release Notes:

### August, 2021
* v2.4
* Add support for JetPack 5
* Update to @rbonghi jetson_variables, jetson_libraries

### August, 2021
* v2.3
* Add support for JetPack 4.6
* Update to @rbonghi jetson_variables

### May, 2021
* v2.2
* Add support for JetPack 4.5
* Add support for Python3 - Thank you Patti Vacek! @pattivacek
* Add Vulcan version
* Update to @rbonghi jetson_variables

### July, 2020
* v2.1
* Add support for JetPack 4.4
* Fix issue with TX1/Nano identification
  Thank you Manu Seth! @mseth10
* Update to @rbonghi jetson_libraries and jetson_variables

### January, 2020
* v2.0
* Add support for JetPack 4.3

### November, 2018
* v1.1.2
* Add support for JetPack 4.1.1 (L4T 31.1.0)

### October, 2018
* v1.1.1
* Add support for JetPack 4.1 (L4T 31.0.2)

### September, 2018
* v1.1
* Add support for JetPack 3.3 (L4T 28.2.1)
* Add support for Jetson AGX Xavier
* Add support for JetPack 4.0 (L4T 31.0.1)

### July, 2018
* v1.0
* Add support for JetPack 3.2.1 (L4T 28.2.1)

Original shell script jetson_variables is derived from jetson_easy: https://github.com/rbonghi/jetson_easy ; Now in jtop package

Copyright (c) 2015-2021 Raffaello Bonghi

See license for jetson_easy in scripts folder

