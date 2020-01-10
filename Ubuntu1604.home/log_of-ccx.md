## Status: Failure 
Build: [1425](https://travis-ci.org/precice/systemtests/builds/635309603) 

Job: [1425.3](https://travis-ci.org/precice/systemtests/jobs/635309606) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/150) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[33mopenfoam-adapter-outer    |[0m Registered objects: 
[33mopenfoam-adapter-outer    |[0m 31
[33mopenfoam-adapter-outer    |[0m (
[33mopenfoam-adapter-outer    |[0m points
[33mopenfoam-adapter-outer    |[0m neighbour
[33mopenfoam-adapter-outer    |[0m thermo:mu
[33mopenfoam-adapter-outer    |[0m MRFProperties
[33mopenfoam-adapter-outer    |[0m thermo:psi
[33mopenfoam-adapter-outer    |[0m ghf
[33mopenfoam-adapter-outer    |[0m h
[33mopenfoam-adapter-outer    |[0m faces
[33mopenfoam-adapter-outer    |[0m U
[33mopenfoam-adapter-outer    |[0m rho
[33mopenfoam-adapter-outer    |[0m radiationProperties
[33mopenfoam-adapter-outer    |[0m turbulenceProperties
[33mopenfoam-adapter-outer    |[0m fvSchemes
[33mopenfoam-adapter-outer    |[0m fvOptions
[33mopenfoam-adapter-outer    |[0m faceZones
[33mopenfoam-adapter-outer    |[0m fvSolution
[33mopenfoam-adapter-outer    |[0m p_rgh
[33mopenfoam-adapter-outer    |[0m thermophysicalProperties
[33mopenfoam-adapter-outer    |[0m phi
[33mopenfoam-adapter-outer    |[0m owner
[33mopenfoam-adapter-outer    |[0m gh
[33mopenfoam-adapter-outer    |[0m data
[33mopenfoam-adapter-outer    |[0m cellZones
[33mopenfoam-adapter-outer    |[0m boundary
[33mopenfoam-adapter-outer    |[0m g
[33mopenfoam-adapter-outer    |[0m p
[33mopenfoam-adapter-outer    |[0m T
[33mopenfoam-adapter-outer    |[0m hRef
[33mopenfoam-adapter-outer    |[0m thermo:rho
[33mopenfoam-adapter-outer    |[0m pointZones
[33mopenfoam-adapter-outer    |[0m thermo:alpha
[33mopenfoam-adapter-outer    |[0m )
[33mopenfoam-adapter-outer    |[0m 
[33mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/ZGCJZB3WFDUPPFYXNF7L7VCVCC:/var/lib/docker/overlay2/l/FXH3UJ2YGQDAI3VDHEGJDUGHVU:/var/lib/docker/overlay2/l/4KCC2CIBBBRB74LS7T22JJ7NLF:/var/lib/docker/overlay2/l/LKPSJ6WKTU6VDSGJAGC77BFOH5:/var/lib/docker/overlay2/l/T7LD33AD3GL5OPXJFHKFY2IAZJ:/var/lib/docker/overlay2/l/QFO3RLMCW4MFOC2V2NX4IAHOEL:/var/lib/docker/overlay2/l/EBDFTGS75INIQJOND5DWINEQFX:/var/lib/docker/overlay2/l/NX4N6OBAVLLZDQTPKAY3DRADPC:/var/lib/docker/overlay2/l/Z7Y5HRJK7TR3Z'
[33mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `NNDYO5O3YBMAM:/var/lib/docker/overlay2/l/EMV5OK6HBK6KWBKIS3Y3Q6MNXH:/var/lib/docker/overlay2/l/GGB2L5LSGBLS44NX3RZHO4RCXQ:/var/lib/docker/overlay2/l/XHU7B4E7DDHQJFSFHRFWB5AFQO:/var/lib/docker/overlay2/l/3G6MLZEGM6KTB4WRCKQA5KTB4C:/var/lib/docker/overlay2/l/GHTFCJRVTSZWUBR6YUJ774FKVH:/var/lib/docker/overlay2/l/DGMOU6HXD5Y6WRZF7SASFKNKDW:/var/lib/docker/overlay2/l/VE34FZXGBY4RHHVCHASWYMHDHK:/var/lib/docker/overlay2/l/DB4OFDY7NINKVUXH4DSXCMMYIF:/var/lib/docker/overlay2/l/MLPGYXM4DRYCR7SBAGEWVUSODQ:/var/lib/do'
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] Reading the adapter's YAML configuration file /home/[secure]/Data/Input/[secure]-adapter-config.yml...
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Checking the adapter's YAML configuration file...
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   participant : Outer-Fluid
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   [secure]-config-file : [secure]-config.xml
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   interfaces : 
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Outer-Fluid-to-Solid
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceCenters
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 0
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       interface
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     write-data : 
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Sink-Temperature-Outer-Fluid
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Heat-Transfer-Coefficient-Outer-Fluid
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     read-data : 
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Sink-Temperature-Solid
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Heat-Transfer-Coefficient-Solid
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     subcycling : 1
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     prevent early exit : 1
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     evaluate boundaries : 1
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     disable checkpointing : 0
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     CHT module enabled : 1
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     FSI module enabled : 0
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Configuring the CHT module...
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     user-defined solver type : none
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     temperature field name : T
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     transportProperties name : transportProperties
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     conductivity name for basic solvers : k
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     density name for incompressible solvers : rho
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     heat capacity name for incompressible solvers : Cp
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     Prandtl number name for incompressible solvers : Pr
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     Turbulent thermal diffusivity field name for incompressible solvers : alphat
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Determining the solver type...
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Did not find the transportProperties dictionary.
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Found the turbulenceProperties dictionary.
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Found the thermophysicalProperties dictionary.
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] This is a compressible flow solver, as turbulence and thermophysical properties are provided.
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Checking the timestep type (fixed vs adjustable)...
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   Timestep type: fixed.
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Creating the preCICE solver interface...
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   Number of processes: 1
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   MPI rank: 0
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   preCICE solver interface was created.
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Configuring preCICE...
[33mopenfoam-adapter-outer    |[0m (0) 15:37:28 [xml::XMLTag]:163 in readAttributes: [31mERROR: [0mWrong attribute "distribution-type"
[35mcalculix-adapter-solid exited with code 255
[0m[32mopenfoam-adapter-inner exited with code 255
[0m[33mopenfoam-adapter-outer exited with code 255
[0mOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Inner-Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Outer-Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Inner-Fluid', 'Outer-Fluid']
Files only in output(right)   : []
travis_time:end:0ba1dbe6:start=1578670493284375722,finish=1578670656086768178,duration=162802392456,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:03956592[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635309606/log.txt)