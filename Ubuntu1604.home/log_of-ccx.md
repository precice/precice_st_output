## Status: Failure 
Build: [1431](https://travis-ci.org/precice/systemtests/builds/635347829) 

Job: [1431.3](https://travis-ci.org/precice/systemtests/jobs/635347832) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/150) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[35mopenfoam-adapter-outer    |[0m Registered objects: 
[35mopenfoam-adapter-outer    |[0m 31
[35mopenfoam-adapter-outer    |[0m (
[35mopenfoam-adapter-outer    |[0m points
[35mopenfoam-adapter-outer    |[0m neighbour
[35mopenfoam-adapter-outer    |[0m thermo:mu
[35mopenfoam-adapter-outer    |[0m MRFProperties
[35mopenfoam-adapter-outer    |[0m thermo:psi
[35mopenfoam-adapter-outer    |[0m ghf
[35mopenfoam-adapter-outer    |[0m h
[35mopenfoam-adapter-outer    |[0m faces
[35mopenfoam-adapter-outer    |[0m U
[35mopenfoam-adapter-outer    |[0m rho
[35mopenfoam-adapter-outer    |[0m radiationProperties
[35mopenfoam-adapter-outer    |[0m turbulenceProperties
[35mopenfoam-adapter-outer    |[0m fvSchemes
[35mopenfoam-adapter-outer    |[0m fvOptions
[35mopenfoam-adapter-outer    |[0m faceZones
[35mopenfoam-adapter-outer    |[0m fvSolution
[35mopenfoam-adapter-outer    |[0m p_rgh
[35mopenfoam-adapter-outer    |[0m thermophysicalProperties
[35mopenfoam-adapter-outer    |[0m phi
[35mopenfoam-adapter-outer    |[0m owner
[35mopenfoam-adapter-outer    |[0m gh
[35mopenfoam-adapter-outer    |[0m data
[35mopenfoam-adapter-outer    |[0m cellZones
[35mopenfoam-adapter-outer    |[0m boundary
[35mopenfoam-adapter-outer    |[0m g
[35mopenfoam-adapter-outer    |[0m p
[35mopenfoam-adapter-outer    |[0m T
[35mopenfoam-adapter-outer    |[0m hRef
[35mopenfoam-adapter-outer    |[0m thermo:rho
[35mopenfoam-adapter-outer    |[0m pointZones
[35mopenfoam-adapter-outer    |[0m thermo:alpha
[35mopenfoam-adapter-outer    |[0m )
[35mopenfoam-adapter-outer    |[0m 
[35mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/PD3NQZQWSAAC7LOJ4QY5GCEMQQ:/var/lib/docker/overlay2/l/XAGU4TLAD2AULHAWMB4QOQFQSA:/var/lib/docker/overlay2/l/WPVEH7MGMRUNC4SZ4TCB7YOLJT:/var/lib/docker/overlay2/l/EDN7RTAMMFKLSPDXVGIIKSMBL7:/var/lib/docker/overlay2/l/YMFHBX7TT7JQOOOAA7PIAH4F7B:/var/lib/docker/overlay2/l/26WVO726K5FANRHNEZA64ZYL3E:/var/lib/docker/overlay2/l/IE56RM7NFJCCF335C6PUM6D2RD:/var/lib/docker/overlay2/l/DGJKSLYCSU62MG67HBEV5E3BLC:/var/lib/docker/overlay2/l/2FPZ45X6AIRJH'
[35mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `XXTUCGVG4OSS4:/var/lib/docker/overlay2/l/7VIENEJTTZELHYH5UWD7WLTXMA:/var/lib/docker/overlay2/l/DQDARET4PXGXL7KNUW5KW7JKS2:/var/lib/docker/overlay2/l/BS4QNAZXZ4H2TMQPBRC537CZQJ:/var/lib/docker/overlay2/l/623YA4LKTX7FOXJ6ZFYHXAA2HA:/var/lib/docker/overlay2/l/XL2HOEPMFPHA6YSV2SNTUPMDZZ:/var/lib/docker/overlay2/l/PLOWUR6W3U4TVX6S5ZQGO63SWV:/var/lib/docker/overlay2/l/4ZCGS2TJKOJSEJIWPISJOS5465:/var/lib/docker/overlay2/l/VBRLQZ3M5EU3QUZWD3IRZNP4H5:/var/lib/docker/overlay2/l/Z3GAXQ6C7OH76U2PZHCCXGUMIH:/var/lib/do'
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] Reading the adapter's YAML configuration file /home/[secure]/Data/Input/[secure]-adapter-config.yml...
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Checking the adapter's YAML configuration file...
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   participant : Outer-Fluid
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   [secure]-config-file : [secure]-config.xml
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   interfaces : 
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Outer-Fluid-to-Solid
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceCenters
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 0
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       interface
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     write-data : 
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Sink-Temperature-Outer-Fluid
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Heat-Transfer-Coefficient-Outer-Fluid
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     read-data : 
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Sink-Temperature-Solid
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Heat-Transfer-Coefficient-Solid
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     subcycling : 1
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     prevent early exit : 1
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     evaluate boundaries : 1
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     disable checkpointing : 0
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     CHT module enabled : 1
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     FSI module enabled : 0
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Configuring the CHT module...
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     user-defined solver type : none
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     temperature field name : T
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     transportProperties name : transportProperties
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     conductivity name for basic solvers : k
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     density name for incompressible solvers : rho
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     heat capacity name for incompressible solvers : Cp
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     Prandtl number name for incompressible solvers : Pr
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     Turbulent thermal diffusivity field name for incompressible solvers : alphat
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Determining the solver type...
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Did not find the transportProperties dictionary.
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Found the turbulenceProperties dictionary.
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Found the thermophysicalProperties dictionary.
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] This is a compressible flow solver, as turbulence and thermophysical properties are provided.
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Checking the timestep type (fixed vs adjustable)...
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   Timestep type: fixed.
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Creating the preCICE solver interface...
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   Number of processes: 1
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   MPI rank: 0
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   preCICE solver interface was created.
[35mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Configuring preCICE...
[35mopenfoam-adapter-outer    |[0m (0) 22:10:47 [xml::XMLTag]:163 in readAttributes: [31mERROR: [0mWrong attribute "distribution-type"
[33mcalculix-adapter-solid exited with code 255
[0m[35mopenfoam-adapter-outer exited with code 255
[0m[32mopenfoam-adapter-inner exited with code 255
[0mOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Inner-Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Outer-Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Outer-Fluid', 'Inner-Fluid']
Files only in output(right)   : []
travis_time:end:00baf420:start=1578780490598003639,finish=1578780656390963760,duration=165792960121,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0d3f4898[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635347832/log.txt)