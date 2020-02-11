## Status: Failure 
Build: [1666](https://travis-ci.org/precice/systemtests/builds/648938191) 

Job: [1666.11](https://travis-ci.org/precice/systemtests/jobs/648938202) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/174) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
Running the simulation...Be patient
Timeout!
Printing logs for services:
Attaching to calculix-adapter-solid
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m ************************************************************
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m CalculiX Version 2.15, Copyright(C) 1998-2018 Guido Dhondt
[36mcalculix-adapter-solid    |[0m CalculiX comes with ABSOLUTELY NO WARRANTY. This is free
[36mcalculix-adapter-solid    |[0m software, and you are welcome to redistribute it under
[36mcalculix-adapter-solid    |[0m certain conditions, see gpl.htm
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m ************************************************************
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m You are using an executable made on Sa 15. Dez 15:34:34 CET 2018
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m   The numbers below are estimated upper bounds
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m   number of:
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m    nodes:        21153
[36mcalculix-adapter-solid    |[0m    elements:       106550
[36mcalculix-adapter-solid    |[0m    one-dimensional elements:            0
[36mcalculix-adapter-solid    |[0m    two-dimensional elements:            0
[36mcalculix-adapter-solid    |[0m    integration points per element:            1
[36mcalculix-adapter-solid    |[0m    degrees of freedom per node:            3
[36mcalculix-adapter-solid    |[0m    layers per element:            1
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m    distributed facial loads:        42172
[36mcalculix-adapter-solid    |[0m    distributed volumetric loads:            0
[36mcalculix-adapter-solid    |[0m    concentrated loads:            0
[36mcalculix-adapter-solid    |[0m    single point constraints:            0
[36mcalculix-adapter-solid    |[0m    multiple point constraints:            1
[36mcalculix-adapter-solid    |[0m    terms in all multiple point constraints:            1
[36mcalculix-adapter-solid    |[0m    tie constraints:            0
[36mcalculix-adapter-solid    |[0m    dependent nodes tied by cyclic constraints:            0
[36mcalculix-adapter-solid    |[0m    dependent nodes in pre-tension constraints:            0
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m    sets:            6
[36mcalculix-adapter-solid    |[0m    terms in all sets:       212183
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m    materials:            1
[36mcalculix-adapter-solid    |[0m    constants per material and temperature:            0
[36mcalculix-adapter-solid    |[0m    temperature points per material:            1
[36mcalculix-adapter-solid    |[0m    plastic data points per material:            0
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m    orientations:            0
[36mcalculix-adapter-solid    |[0m    amplitudes:            3
[36mcalculix-adapter-solid    |[0m    data points in all amplitudes:            3
[36mcalculix-adapter-solid    |[0m    print requests:            0
[36mcalculix-adapter-solid    |[0m    transformations:            0
[36mcalculix-adapter-solid    |[0m    property cards:            0
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  STEP            1
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Static analysis was selected
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Newton-Raphson iterative procedure is active
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Decascading the MPC's
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Determining the structure of the matrix:
[36mcalculix-adapter-solid    |[0m  number of equations
[36mcalculix-adapter-solid    |[0m  21153
[36mcalculix-adapter-solid    |[0m  number of nonzero lower triangular matrix elements
[36mcalculix-adapter-solid    |[0m  106662
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m Starting CHT analysis via preCICE...
[36mcalculix-adapter-solid    |[0m About to enter preCICE setup in Calculix with names Solid and config.yml 
[36mcalculix-adapter-solid    |[0m Setting up preCICE participant Solid, using config file: config.yml
[36mcalculix-adapter-solid    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/DPIST5P5TMPA56BCIE6O7SAAY7:/var/lib/docker/overlay2/l/F4XURGQ57MQQVJA6ZL3B2SJALX:/var/lib/docker/overlay2/l/H46X6CYRTXIOCAPG2OWUNCVT2F:/var/lib/docker/overlay2/l/AL2S23HE4BHWST2EVQ5VA7UZKK:/var/lib/docker/overlay2/l/UDGDWTB6F7PAH35ER2KHQO7XCI:/var/lib/docker/overlay2/l/RDSFGZGJQKUMJ3DCZVJDN2D45L:/var/lib/docker/overlay2/l/BRBI37A2N3VIBXP6PRKUASEEFU:/var/lib/docker/overlay2/l/W6RRGY64W6FY5YMHFVKIE3N3FX:/var/lib/docker/overlay2/l/QUGTISNWXWTDW'
[36mcalculix-adapter-solid    |[0m Unexpected end of /proc/mounts line `2NDQF26PQYXIO:/var/lib/docker/overlay2/l/7RKYH32HPR2XAMPJGF6N54VRYP:/var/lib/docker/overlay2/l/U7QOEFH6UYOQLDPHPAWKNENS5R:/var/lib/docker/overlay2/l/NHETJZZTIZ72WGQY7R6OD74TKC:/var/lib/docker/overlay2/l/LA6IXKZVDY67BJGHDBRK2TS77R:/var/lib/docker/overlay2/l/KKXFRGDZZQDTFNKBE6XM7OT536:/var/lib/docker/overlay2/l/7IGDXXZN63AEGV4WQKKHOO277O:/var/lib/docker/overlay2/l/XSDRWJ6VQFKJPWHWRIQP7QRAPC:/var/lib/docker/overlay2/l/VTJMBZW7CE5ZNQL3DHC6T7GQZA:/var/lib/docker/overlay2/l/7TIPDX6LY5TONEB7XA5SXGAQ4Z:/var/lib/do'
[36mcalculix-adapter-solid    |[0m Unexpected end of /proc/mounts line `cker/overlay2/l/3UZ62MOIKIBL33BRCC3BNU57AW:/var/lib/docker/overlay2/l/AAWP7DYB3EHKL7XKGQA4IQ4KDZ:/var/lib/docker/overlay2/l/4ED72OCEKL7NWVTLAWQGTGNMT6:/var/lib/docker/overlay2/l/EHR6L2YPF5H7WQCDOL23PV2JFM:/var/lib/docker/overlay2/l/NCTWWXDVYCOP47FHN4WHONBFE2:/var/lib/docker/overlay2/l/XAREVTZHQ6DQNU7DMLBNE5S2EK,upperdir=/var/lib/docker/overlay2/e17a31bd34bb951896f0a54f3920d2da72b2ba99d8b1a75e22624d5f0d3f6cde/diff,workdir=/var/lib/docker/overlay2/e17a31bd34bb951896f0a54f3920d2da72b2ba99d8b1a75e22624d5f0d3f6'
[36mcalculix-adapter-solid    |[0m ---[[secure]] [0m This is preCICE version 2.0.0
[36mcalculix-adapter-solid    |[0m ---[[secure]] [0m Revision info: v2.0.0-2-g56832a9
[36mcalculix-adapter-solid    |[0m ---[[secure]] [0m Configuring preCICE with configuration: "[secure]-config.xml"
[36mcalculix-adapter-solid    |[0m Set ID Found 
[36mcalculix-adapter-solid    |[0m Set ID Found 
[36mcalculix-adapter-solid    |[0m Setting node connectivity for nearest projection mapping: 
[36mcalculix-adapter-solid    |[0m Read data 'Sink-Temperature-Inner-Fluid' found.
[36mcalculix-adapter-solid    |[0m Read data 'Heat-Transfer-Coefficient-Inner-Fluid' found.
[36mcalculix-adapter-solid    |[0m Write data 'Sink-Temperature-Solid' found.
[36mcalculix-adapter-solid    |[0m Write data 'Heat-Transfer-Coefficient-Solid' found.
[36mcalculix-adapter-solid    |[0m Set ID Found 
[36mcalculix-adapter-solid    |[0m Set ID Found 
[36mcalculix-adapter-solid    |[0m Setting node connectivity for nearest projection mapping: 
[36mcalculix-adapter-solid    |[0m Read data 'Sink-Temperature-Outer-Fluid' found.
[36mcalculix-adapter-solid    |[0m Read data 'Heat-Transfer-Coefficient-Outer-Fluid' found.
[36mcalculix-adapter-solid    |[0m Write data 'Sink-Temperature-Solid' found.
[36mcalculix-adapter-solid    |[0m Write data 'Heat-Transfer-Coefficient-Solid' found.
[36mcalculix-adapter-solid    |[0m ---[[secure]] [0m Setting up master communication to coupling partner/s
Stopping calculix-adapter-solid ... 
[1A[2KStopping calculix-adapter-solid ... [32mdone[0m[1BEXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh ' returned non-zero exit status 1
travis_time:end:0a169f92:start=1581433076055298857,finish=1581433893599054719,duration=817543755862,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:33ddbd48[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/648938202/log.txt)