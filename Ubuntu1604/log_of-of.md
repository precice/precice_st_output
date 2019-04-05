System testing at Fri Apr  5 21:10:54 2019
 # Status : Failing
 # [Job url](https://travis-ci.org/shkodm/systemtests/builds/516380490)
## Triggered by: [push](https://github.com/shkodm/systemtests/compare/4555d077c941...b16a26eb6775)
## Last succesfull commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/67)
* [systemtests](https://github.com/precice/systemtests/compare/57b164a8d4112c5e57a4eef1f636d3c109524d69...269012c2748bf5513bc244ad9f50d886de05a18b)
## Last 100 lines of the job log...
```

     0K .                                [0m[91m                     100%  266M=0s

2019-04-05 21:09:59 (266 MB/s) - written to stdout [1710/1710]

[0mOK
 ---> bdb7ed693e36
Removing intermediate container 6566f70c6eea
Step 8/18 : RUN add-apt-repository http://dl.openfoam.org/ubuntu && apt update
 ---> Running in b4cf7fc78f17
[91m
WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

[0mGet:1 http://security.ubuntu.com/ubuntu xenial-security InRelease [109 kB]
Get:2 http://archive.ubuntu.com/ubuntu xenial InRelease [247 kB]
Get:3 http://dl.openfoam.org/ubuntu xenial InRelease [6337 B]
Get:4 http://security.ubuntu.com/ubuntu xenial-security/main amd64 Packages [815 kB]
Get:5 http://dl.openfoam.org/ubuntu xenial/main amd64 Packages [5083 B]
Get:6 http://security.ubuntu.com/ubuntu xenial-security/restricted amd64 Packages [12.7 kB]
Get:7 http://security.ubuntu.com/ubuntu xenial-security/universe amd64 Packages [551 kB]
Get:8 http://security.ubuntu.com/ubuntu xenial-security/multiverse amd64 Packages [6117 B]
Get:9 http://dl.openfoam.org/ubuntu xenial/dev amd64 Packages [63.2 kB]
Get:10 http://archive.ubuntu.com/ubuntu xenial-updates InRelease [109 kB]
Get:11 http://archive.ubuntu.com/ubuntu xenial-backports InRelease [107 kB]
Get:12 http://archive.ubuntu.com/ubuntu xenial/main amd64 Packages [1558 kB]
Get:13 http://archive.ubuntu.com/ubuntu xenial/restricted amd64 Packages [14.1 kB]
Get:14 http://archive.ubuntu.com/ubuntu xenial/universe amd64 Packages [9827 kB]
Get:15 http://archive.ubuntu.com/ubuntu xenial/multiverse amd64 Packages [176 kB]
Get:16 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 Packages [1210 kB]
Get:17 http://archive.ubuntu.com/ubuntu xenial-updates/restricted amd64 Packages [13.1 kB]
Get:18 http://archive.ubuntu.com/ubuntu xenial-updates/universe amd64 Packages [962 kB]
Get:19 http://archive.ubuntu.com/ubuntu xenial-updates/multiverse amd64 Packages [19.1 kB]
Get:20 http://archive.ubuntu.com/ubuntu xenial-backports/main amd64 Packages [7942 B]
Get:21 http://archive.ubuntu.com/ubuntu xenial-backports/universe amd64 Packages [8532 B]
Fetched 15.8 MB in 2s (6043 kB/s)
Reading package lists...
Building dependency tree...
Reading state information...
5 packages can be upgraded. Run 'apt list --upgradable' to see them.
 ---> b8759add9f0a
Removing intermediate container b4cf7fc78f17
Step 9/18 : RUN apt-get -y install openfoam4 --no-install-recommends &&     rm -rf /var/lib/apt/lists/*
 ---> Running in 3f87e95c38c5
Reading package lists... lm-sensors libsm-doc libxcb-doc libxt-doc
Recommended packages:
  libtxc-dxtn-s2tc | libtxc-dxtn-s2tc0 | libtxc-dxtn0 libx11-doc
  paraviewopenfoam50
The following NEW packages will be installed:
  binutils-dev flex libboost-atomic1.58-dev libboost-atomic1.58.0
  libboost-chrono1.58-dev libboost-chrono1.58.0 libboost-date-time1.58-dev
  libboost-date-time1.58.0 libboost-program-options-dev
  libboost-program-options1.58-dev libboost-program-options1.58.0
  libboost-serialization1.58-dev libboost-serialization1.58.0
  libboost-system-dev libboost-system1.58-dev libboost-system1.58.0
  libboost-thread-dev libboost-thread1.58-dev libboost-thread1.58.0
  libcgal-dev libcgal11v5 libdrm-amdgpu1 libdrm-common libdrm-intel1
  libdrm-nouveau2 libdrm-radeon1 libdrm2 libelf1 libfl-dev libgl1-mesa-dri
  libgl1-mesa-glx libglapi-mesa libgmp-dev libgmpxx4ldbl libice-dev libice6
  libllvm6.0 libmpfr-dev libpthread-stubs0-dev libreadline-dev
  libreadline6-dev libsensors4 libsigsegv2 libsm-dev libsm6 libtinfo-dev
  libx11-dev libx11-xcb1 libxau-dev libxcb-dri2-0 libxcb-dri3-0 libxcb-glx0
  libxcb-present0 libxcb-sync1 libxcb1-dev libxdamage1 libxdmcp-dev libxfixes3
  libxshmfence1 libxt-dev libxt6 libxxf86vm1 m4 openfoam4 x11-common
  x11proto-core-dev x11proto-input-dev x11proto-kb-dev xorg-sgml-doctools
  xtrans-dev
0 upgraded, 70 newly installed, 0 to remove and 5 not upgraded.
Need to get 110 MB of archives.
After this operation, 774 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial/main amd64 libsigsegv2 amd64 2.10-4 [14.1 kB]
Get:3 http://archive.ubuntu.com/ubuntu xenial/main amd64 m4 amd64 1.4.17-5 [195 kB]
Get:6 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 x11-common all 1:7.7+13ubuntu3.1 [22.9 kB]
Get:7 http://archive.ubuntu.com/ubuntu xenial/main amd64 libice6 amd64 2:1.0.9-1 [39.2 kB]
Get:8 http://archive.ubuntu.com/ubuntu xenial/main amd64 libsm6 amd64 2:1.2.2-1 [15.8 kB]
Get:9 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxdamage1 amd64 1:1.1.4-2 [6946 B]
Get:10 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxfixes3 amd64 1:5.0.1-2 [11.1 kB]
Get:11 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxshmfence1 amd64 1.2-1 [5042 B]
Get:12 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxxf86vm1 amd64 1:1.1.4-1 [10.6 kB]
Get:13 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libdrm-common all 2.4.91-2~16.04.1 [4764 B]
Get:14 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libdrm2 amd64 2.4.91-2~16.04.1 [30.8 kB]
Get:15 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libelf1 amd64 0.165-3ubuntu1.1 [43.0 kB]
Get:16 http://archive.ubuntu.com/ubuntu xenial-updates/universe amd64 libboost-atomic1.58.0 amd64 1.58.0+dfsg-5ubuntu3.1 [7120 B]
Get:17 http://archive.ubuntu.com/ubuntu xenial-updates/universe amd64 libboost-atomic1.58-dev amd64 1.58.0+dfsg-5ubuntu3.1 [5026 B]
Get:18 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libboost-system1.58.0 amd64 1.58.0+dfsg-5ubuntu3.1 [9146 B]
Get:19 http://archive.ubuntu.com/ubuntu xenial-updates/universe amd64 libboost-chrono1.58.0 amd64 1.58.0+dfsg-5ubuntu3.1 [13.2 kB]
Get:20 http://archive.ubuntu.com/ubuntu xenial-updates/universe amd64 libboost-chrono1.58-dev amd64 1.58.0+dfsg-5ubuntu3.1 [15.6 18.0.5-0ubuntu0~16.04.1 [23.4 kB]
Get:34 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx11-xcb1 amd64 2:1.6.3-1ubuntu2.1 [9044 B]
Get:35 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxcb-dri2-0 amd64 1.11.1-1ubuntu1 [6882 B]
Get:36 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxcb-dri3-0 amd64 1.11.1-1ubuntu1 [5218 B]
Get:37 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxcb-glx0 amd64 1.11.1-1ubuntu1 [20.9 kB]
Get:38 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxcb-present0 amd64 1.11.1-1ubuntu1 [5218 B]
Get:39 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxcb-sync1 amd64 1.11.1-1ubuntu1 [8324 B]
Get:40 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libdrm-amdgpu1 amd64 2.4.91-2~16.04.1 [18.9 kB]
Get:41 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libdrm-intel1 amd64 2.4.91-2~16.04.1 [59.9 kB]
Get:42 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libdrm-nouveau2 amd64 2.4.91-2~16.04.1 [16.3 kB]
Get:43 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libdrm-radeon1 amd64 2.4.91-2~16.04.1 [21.5 kB]
Get:44 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libllvm6.0 amd64 1:6.0-1ubuntu2~16.04.1 [14.3 MB]
Get:68 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxt6 amd64 1:1.1.5-0ubuntu1 [160 kB]
Get:69 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxt-dev amd64 1:1.1.5-0ubuntu1 [394 kB]
Get:70 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 binutils-dev amd64 2.26.1-1ubuntu1~16.04.8 [2178 kB]
```
[Full job log](https://api.travis-ci.org/v3/job/516380495/log.txt)