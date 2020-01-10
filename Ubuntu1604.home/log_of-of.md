## Status: Failure 
Build: [1422](https://travis-ci.org/precice/systemtests/builds/635287877) 

Job: [1422.2](https://travis-ci.org/precice/systemtests/jobs/635287879) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/148) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[32mopenfoam-adapter-fluid    |[0m 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] The [secure]Adapter was loaded.
[32mopenfoam-adapter-fluid    |[0m Registered objects: 
[32mopenfoam-adapter-fluid    |[0m 33
[32mopenfoam-adapter-fluid    |[0m (
[32mopenfoam-adapter-fluid    |[0m points
[32mopenfoam-adapter-fluid    |[0m neighbour
[32mopenfoam-adapter-fluid    |[0m thermo:mu
[32mopenfoam-adapter-fluid    |[0m MRFProperties
[32mopenfoam-adapter-fluid    |[0m thermo:psi
[32mopenfoam-adapter-fluid    |[0m K
[32mopenfoam-adapter-fluid    |[0m ghf
[32mopenfoam-adapter-fluid    |[0m h
[32mopenfoam-adapter-fluid    |[0m faces
[32mopenfoam-adapter-fluid    |[0m U
[32mopenfoam-adapter-fluid    |[0m rho
[32mopenfoam-adapter-fluid    |[0m radiationProperties
[32mopenfoam-adapter-fluid    |[0m turbulenceProperties
[32mopenfoam-adapter-fluid    |[0m fvSchemes
[32mopenfoam-adapter-fluid    |[0m fvOptions
[32mopenfoam-adapter-fluid    |[0m faceZones
[32mopenfoam-adapter-fluid    |[0m fvSolution
[32mopenfoam-adapter-fluid    |[0m p_rgh
[32mopenfoam-adapter-fluid    |[0m thermophysicalProperties
[32mopenfoam-adapter-fluid    |[0m dpdt
[32mopenfoam-adapter-fluid    |[0m phi
[32mopenfoam-adapter-fluid    |[0m owner
[32mopenfoam-adapter-fluid    |[0m gh
[32mopenfoam-adapter-fluid    |[0m data
[32mopenfoam-adapter-fluid    |[0m cellZones
[32mopenfoam-adapter-fluid    |[0m boundary
[32mopenfoam-adapter-fluid    |[0m g
[32mopenfoam-adapter-fluid    |[0m p
[32mopenfoam-adapter-fluid    |[0m T
[32mopenfoam-adapter-fluid    |[0m hRef
[32mopenfoam-adapter-fluid    |[0m thermo:rho
[32mopenfoam-adapter-fluid    |[0m pointZones
[32mopenfoam-adapter-fluid    |[0m thermo:alpha
[32mopenfoam-adapter-fluid    |[0m )
[32mopenfoam-adapter-fluid    |[0m 
[32mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/YCIFEY7U6UDZAZJH6G2IW4GRQV:/var/lib/docker/overlay2/l/ZDN65JBIBZTC7HNBJGTOSBQZJK:/var/lib/docker/overlay2/l/YULC4WDEPFMUKBRATCF6YP6L4P:/var/lib/docker/overlay2/l/RW2DOIV3WRKITPNLVKSAE4OJCN:/var/lib/docker/overlay2/l/7WI5DLMJSOS6I5GIMLLZTKJ33E:/var/lib/docker/overlay2/l/TIMIROTZLGNSUFATOYRN4J3WZC:/var/lib/docker/overlay2/l/CLVRZVLX6CII2B6GVLDJVIBV3W:/var/lib/docker/overlay2/l/VDB4XKOWYMS7A73IADZRUGT2NH:/var/lib/docker/overlay2/l/5UTK53I37VRPO'
[32mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `QUE3ITW2CPU2B:/var/lib/docker/overlay2/l/PYVRQYHW4ZI3LIUHJVJKJQVJTK:/var/lib/docker/overlay2/l/7RZM3ZLVMUOVNO37MX3GV6W2RH:/var/lib/docker/overlay2/l/IMWZHJ3DHWXYHSXKOHKIZWKS7W:/var/lib/docker/overlay2/l/KJMR75HNUOVKD3REQ5LST4JQJQ:/var/lib/docker/overlay2/l/TMXJDF7Q4LVA576G4WBDMRB5RC:/var/lib/docker/overlay2/l/AWGNLMOQFQI2C6UJSSYGJOQPSR:/var/lib/docker/overlay2/l/OB25SKJUDRWIZGIJ4GFI42NT6O:/var/lib/docker/overlay2/l/WNYQROKBLT64LIISSO54ZCNYKV:/var/lib/docker/overlay2/l/7BICGNSBJSHTFTTOF5YPQF5H6Y:/var/lib/do'
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] Reading the adapter's YAML configuration file ./Fluid/[secure]-adapter-config.yml...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Checking the adapter's YAML configuration file...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   participant : Fluid
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   [secure]-config-file : [secure]-config.xml
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   interfaces : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Fluid-Mesh
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceCenters
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       interface
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     write-data : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       Temperature
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     read-data : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       Heat-Flux
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     subcycling : 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     prevent early exit : 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     evaluate boundaries : 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     disable checkpointing : 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     CHT module enabled : 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     FSI module enabled : 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Configuring the CHT module...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     user-defined solver type : none
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     temperature field name : T
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     transportProperties name : transportProperties
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     conductivity name for basic solvers : k
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     density name for incompressible solvers : rho
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     heat capacity name for incompressible solvers : Cp
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Prandtl number name for incompressible solvers : Pr
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Turbulent thermal diffusivity field name for incompressible solvers : alphat
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Determining the solver type...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Did not find the transportProperties dictionary.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Found the turbulenceProperties dictionary.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Found the thermophysicalProperties dictionary.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] This is a compressible flow solver, as turbulence and thermophysical properties are provided.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Checking the timestep type (fixed vs adjustable)...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   Timestep type: fixed.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Creating the preCICE solver interface...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   Number of processes: 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   MPI rank: 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   preCICE solver interface was created.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Configuring preCICE...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]] [31mERROR: [0m Wrong attribute "distribution-type"
[32mopenfoam-adapter-fluid exited with code 255
[0mOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput: Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput: Solid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Solid', 'Fluid']
Files only in output(right)   : []
travis_time:end:087da796:start=1578666589735533584,finish=1578666646358789007,duration=56623255423,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:003d7f66[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635287879/log.txt)