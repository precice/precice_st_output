## Status: Failure 
Build: [1666](https://travis-ci.org/precice/systemtests/builds/648938191) 

Job: [1666.17](https://travis-ci.org/precice/systemtests/jobs/648938208) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/174) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
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
[36mcalculix-adapter-solid    |[0m    nodes:          126
[36mcalculix-adapter-solid    |[0m    elements:           40
[36mcalculix-adapter-solid    |[0m    one-dimensional elements:            0
[36mcalculix-adapter-solid    |[0m    two-dimensional elements:            0
[36mcalculix-adapter-solid    |[0m    integration points per element:           27
[36mcalculix-adapter-solid    |[0m    degrees of freedom per node:            3
[36mcalculix-adapter-solid    |[0m    layers per element:            1
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m    distributed facial loads:            0
[36mcalculix-adapter-solid    |[0m    distributed volumetric loads:            0
[36mcalculix-adapter-solid    |[0m    concentrated loads:          258
[36mcalculix-adapter-solid    |[0m    single point constraints:          396
[36mcalculix-adapter-solid    |[0m    multiple point constraints:            1
[36mcalculix-adapter-solid    |[0m    terms in all multiple point constraints:            1
[36mcalculix-adapter-solid    |[0m    tie constraints:            0
[36mcalculix-adapter-solid    |[0m    dependent nodes tied by cyclic constraints:            0
[36mcalculix-adapter-solid    |[0m    dependent nodes in pre-tension constraints:            0
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m    sets:            4
[36mcalculix-adapter-solid    |[0m    terms in all sets:          384
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m    materials:            1
[36mcalculix-adapter-solid    |[0m    constants per material and temperature:            2
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
[36mcalculix-adapter-solid    |[0m  *INFO reading *STEP: nonlinear geometric
[36mcalculix-adapter-solid    |[0m        effects are turned on
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  STEP            1
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Dynamic analysis was selected
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Newton-Raphson iterative procedure is active
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Nonlinear geometric effects are taken into account
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Decascading the MPC's
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Determining the structure of the matrix:
[36mcalculix-adapter-solid    |[0m  number of equations
[36mcalculix-adapter-solid    |[0m  240
[36mcalculix-adapter-solid    |[0m  number of nonzero lower triangular matrix elements
[36mcalculix-adapter-solid    |[0m  3128
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m Starting FSI analysis via preCICE using the geometrically non-linear CalculiX solver...
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the stress calculation.
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the symmetric stiffness/mass contributions.
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Factoring the system of equations using the symmetric spooles solver
[36mcalculix-adapter-solid    |[0m  Using 1 cpu for spooles.
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the stress calculation.
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m About to enter preCICE setup in Calculix with names Calculix and config.yml 
[36mcalculix-adapter-solid    |[0m Setting up preCICE participant Calculix, using config file: config.yml
[36mcalculix-adapter-solid    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/RGKX2IBW7LLEBAYKI5CNYEF5UL:/var/lib/docker/overlay2/l/2FBFP2ZUTNXWXYPAEZCLWC4E4S:/var/lib/docker/overlay2/l/JTUSP237WJH7ECMIRH7SF2LZCX:/var/lib/docker/overlay2/l/AX6D6UPAWBL266SSW5GH6OA3E4:/var/lib/docker/overlay2/l/E4MCHLYXQSC6W4FGDPJRXHULSL:/var/lib/docker/overlay2/l/E3ZA3QIJ6LV7TKEK4RF5NLF4SS:/var/lib/docker/overlay2/l/JJKVDCVAQLWL37JEKICXJTEYB4:/var/lib/docker/overlay2/l/MFYMMYB72W7OMFQR6KBOHNHGTF:/var/lib/docker/overlay2/l/XHAFDSUU6DP3R'
[36mcalculix-adapter-solid    |[0m Unexpected end of /proc/mounts line `B4LFKDKE63S6P:/var/lib/docker/overlay2/l/26ZFYHSJ4MFHAQMYDEIZTJP3GW:/var/lib/docker/overlay2/l/ZTSSE2KU3U3QTFEEOW26KUVNJZ:/var/lib/docker/overlay2/l/7UDKFNRAGHT2LWWEL5O6FX2P4O:/var/lib/docker/overlay2/l/H4DTJR6L6WMDW4HFI3JVPXHDWI:/var/lib/docker/overlay2/l/ZSFOZD5ZW6S4C4VVFBUE3NODZ5:/var/lib/docker/overlay2/l/SLO3KSSN7BWR7T5HZRYX6BFI6G:/var/lib/docker/overlay2/l/SSMMBLUXEAWGBDENB7CKM4BAXZ:/var/lib/docker/overlay2/l/QPE2TGJVPG3CLZDQLM7YYVZKD6:/var/lib/docker/overlay2/l/YK4QDJMATO4SMW4GWFNC57FYDG:/var/lib/do'
[36mcalculix-adapter-solid    |[0m Unexpected end of /proc/mounts line `cker/overlay2/l/O5FY2L6EZRQPBZQAZZF7WUNALW:/var/lib/docker/overlay2/l/6SHHWBHIYDNBMJ4BY6YKRWQXFW:/var/lib/docker/overlay2/l/WDGVQPLLHWTUYP4EI6XN4SSJLF:/var/lib/docker/overlay2/l/6E2UTMUKKSCHLLC7ZV6CRMFI53:/var/lib/docker/overlay2/l/Y54ILD6X6EYK3S54HSXMWMGQ4I:/var/lib/docker/overlay2/l/G7TZUX4OIMAV4ZS4FL4PQENNGJ,upperdir=/var/lib/docker/overlay2/284709f55155f4080c986f10d88a5129243db6e0b78ad53c868b963d6b70829f/diff,workdir=/var/lib/docker/overlay2/284709f55155f4080c986f10d88a5129243db6e0b78ad53c868b963d6b708'
[36mcalculix-adapter-solid    |[0m ---[[secure]] [0m This is preCICE version 1.6.1
[36mcalculix-adapter-solid    |[0m ---[[secure]] [0m Revision info: v1.6.1-406-g87d7093
[36mcalculix-adapter-solid    |[0m ---[[secure]] [0m Configuring preCICE with configuration: "./[secure]-config.xml"
[36mcalculix-adapter-solid    |[0m Set ID Found 
[36mcalculix-adapter-solid    |[0m Read data 'Forces0' found.
[36mcalculix-adapter-solid    |[0m Write data 'Displacements0' found.
[36mcalculix-adapter-solid    |[0m ---[[secure]] [0m Setting up master communication to coupling partner/s
Stopping calculix-adapter-solid ... 
[1A[2KStopping calculix-adapter-solid ... [32mdone[0m[1BEXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop; docker-compose config && bash ../../silent_compose.sh 
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1604.home.petsc-develop; docker-compose config && bash ../../silent_compose.sh ' returned non-zero exit status 1
travis_time:end:1a5b8f30:start=1581433526090068570,finish=1581434215027691188,duration=688937622618,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1105d6a8[0K$ python push.py -t of-ccx_fsi
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/648938208/log.txt)