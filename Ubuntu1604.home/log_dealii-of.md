## Status: Failure 
Build: [1422](https://travis-ci.org/precice/systemtests/builds/635287877) 

Job: [1422.6](https://travis-ci.org/precice/systemtests/jobs/635287883) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/148) 
Last successful commits 
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/1cefd5edac2aea69ea37978eeb5479db3ada0042...d9a7dc3ed7e75c17e88adc4757c7bd5f44719b24)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[33mopenfoam-adapter    |[0m 
[33mopenfoam-adapter    |[0m Reading/calculating face velocity Uf
[33mopenfoam-adapter    |[0m 
[33mopenfoam-adapter    |[0m No finite volume options present
[33mopenfoam-adapter    |[0m 
[33mopenfoam-adapter    |[0m Courant Number mean: 0 max: 0
[33mopenfoam-adapter    |[0m 
[33mopenfoam-adapter    |[0m Starting time loop
[33mopenfoam-adapter    |[0m 
[32mdealii-adapter      |[0m ---[[secure]] [31mERROR: [0m Wrong attribute "distribution-type"
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] The [secure]Adapter was loaded.
[33mopenfoam-adapter    |[0m Registered objects: 
[33mopenfoam-adapter    |[0m 25
[33mopenfoam-adapter    |[0m (
[33mopenfoam-adapter    |[0m points
[33mopenfoam-adapter    |[0m neighbour
[33mopenfoam-adapter    |[0m faceDiffusivity
[33mopenfoam-adapter    |[0m MRFProperties
[33mopenfoam-adapter    |[0m pointMesh
[33mopenfoam-adapter    |[0m pointDisplacement
[33mopenfoam-adapter    |[0m faces
[33mopenfoam-adapter    |[0m U
[33mopenfoam-adapter    |[0m turbulenceProperties
[33mopenfoam-adapter    |[0m fvSchemes
[33mopenfoam-adapter    |[0m fvOptions
[33mopenfoam-adapter    |[0m faceZones
[33mopenfoam-adapter    |[0m fvSolution
[33mopenfoam-adapter    |[0m Uf
[33mopenfoam-adapter    |[0m nu
[33mopenfoam-adapter    |[0m phi
[33mopenfoam-adapter    |[0m owner
[33mopenfoam-adapter    |[0m data
[33mopenfoam-adapter    |[0m cellZones
[33mopenfoam-adapter    |[0m boundary
[33mopenfoam-adapter    |[0m dynamicMeshDict
[33mopenfoam-adapter    |[0m p
[33mopenfoam-adapter    |[0m cellDisplacement
[33mopenfoam-adapter    |[0m pointZones
[33mopenfoam-adapter    |[0m transportProperties
[33mopenfoam-adapter    |[0m )
[33mopenfoam-adapter    |[0m 
[33mopenfoam-adapter    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/W3KIAGZXQQLKB2USIG2DP7A4PX:/var/lib/docker/overlay2/l/2HGCSGXU3CJ3L7PL53ECAYRVN6:/var/lib/docker/overlay2/l/BDCHZUXFNNL5I4N3PZBMN3XH36:/var/lib/docker/overlay2/l/BLVOO6XLHSLCTMCCLQFWGEM4TI:/var/lib/docker/overlay2/l/4DYPVTIC5PJBKABTGSUEYC7ASM:/var/lib/docker/overlay2/l/NCFYXL2LVP3WWQMFFVONT6VSZ6:/var/lib/docker/overlay2/l/2HNHMIGJUMPFZTP4RWY2BKYQJK:/var/lib/docker/overlay2/l/ETO7JVV3EBXNHXHJ44HOQXBI5R:/var/lib/docker/overlay2/l/SB6N3TCAS2Y4E'
[33mopenfoam-adapter    |[0m Unexpected end of /proc/mounts line `EOKLXUKJKZKDK:/var/lib/docker/overlay2/l/BMBWBWQTWQBEM3BXBU4H36DVZQ:/var/lib/docker/overlay2/l/GBR5TBBZSC7E6YGFXZSDAZ25OF:/var/lib/docker/overlay2/l/BH2OXN7LH4D47RWFGRR56IWEDJ:/var/lib/docker/overlay2/l/Q3TH7A5RW7AAMYOIK6P3FXXOWP:/var/lib/docker/overlay2/l/A5GQIJWYR57BRTTSB73AJY7ROZ:/var/lib/docker/overlay2/l/2BD7WXRQ67LRRTTKN4KETYJNUG:/var/lib/docker/overlay2/l/ADGZE2GL3NM2YVLYW4RL23FBGH:/var/lib/docker/overlay2/l/5XFCLNMZ4YM4GQQA43DZO5DEXG:/var/lib/docker/overlay2/l/GVH4RJ5TTRH32L57R25XXYZSVP:/var/lib/do'
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] Reading the adapter's YAML configuration file /home/[secure]/Data/Input/[secure]-adapter-config.yml...
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG] Checking the adapter's YAML configuration file...
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]   participant : Fluid
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]   [secure]-config-file : [secure]-config.xml
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]   interfaces : 
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Fluid-Mesh-Centers
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceCenters
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 0
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]       flap
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     write-data : 
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]       Force
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Fluid-Mesh-Nodes
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceNodes
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 0
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]       flap
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     read-data : 
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]       Displacement
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     subcycling : 1
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     prevent early exit : 1
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     evaluate boundaries : 1
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     disable checkpointing : 0
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     CHT module enabled : 0
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     FSI module enabled : 1
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG] Configuring the FSI module...
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     user-defined solver type : none
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]     pointDisplacement field name : pointDisplacement
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG] Determining the solver type...
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG] Found the transportProperties dictionary.
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG] Found the turbulenceProperties dictionary.
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG] Did not find the thermophysicalProperties dictionary.
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG] This is an incompressible flow solver, as turbulence and transport properties are provided.
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG] Checking the timestep type (fixed vs adjustable)...
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]   Timestep type: fixed.
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG] Creating the preCICE solver interface...
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]   Number of processes: 1
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]   MPI rank: 0
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG]   preCICE solver interface was created.
[33mopenfoam-adapter    |[0m ---[[secure]Adapter] [DEBUG] Configuring preCICE...
[33mopenfoam-adapter    |[0m ---[[secure]] [31mERROR: [0m Wrong attribute "distribution-type"
[32mdealii-adapter exited with code 255
[0m[33mopenfoam-adapter exited with code 255
[0mOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/referenceOutput: Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Fluid']
Files only in output(right)   : []
travis_time:end:042d95c0:start=1578666814393541549,finish=1578666888430768900,duration=74037227351,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:14af8268[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635287883/log.txt)