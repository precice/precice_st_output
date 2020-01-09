## Status: Failure 
Build: [1416](https://travis-ci.org/precice/systemtests/builds/634706209) 

Job: [1416.6](https://travis-ci.org/precice/systemtests/jobs/634706215) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/148) 
Last successful commits 
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/1cefd5edac2aea69ea37978eeb5479db3ada0042...d9a7dc3ed7e75c17e88adc4757c7bd5f44719b24)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[33mopenfoam-adapter    |[0m 
[33mopenfoam-adapter    |[0m Courant Number mean: 0 max: 0
[33mopenfoam-adapter    |[0m 
[33mopenfoam-adapter    |[0m Starting time loop
[33mopenfoam-adapter    |[0m 
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
[33mopenfoam-adapter    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/OA53YOOSJN2YRRYRQDKALXNQ4O:/var/lib/docker/overlay2/l/3VNUPSPJIMQT3M3X3T5JXKYUYE:/var/lib/docker/overlay2/l/U6B7K4LKAA3R7KKSYJE7N6IHVI:/var/lib/docker/overlay2/l/HN6SKU2Y5EQBBPMRL2CG57AMDS:/var/lib/docker/overlay2/l/NJWLOVRYFFWWFJYCM6TYNFBGD2:/var/lib/docker/overlay2/l/XPYBFOYNGFRRKG4VUUEDJ3JIBY:/var/lib/docker/overlay2/l/IVRDNAVUVQLEYWGWZFBKFH7YFW:/var/lib/docker/overlay2/l/AJ6VBQSYILIQL6B775J34B6UVU:/var/lib/docker/overlay2/l/2FPUGN4IKTZA3'
[33mopenfoam-adapter    |[0m Unexpected end of /proc/mounts line `3ZWQLUOVCP2TQ:/var/lib/docker/overlay2/l/NIKAS6672D54PFGZKE6ETTLCJJ:/var/lib/docker/overlay2/l/LG4KTTHFH63DD3V75C3HBRV6PP:/var/lib/docker/overlay2/l/WA6NATGBAWDHYEWAHJB7MFY5L7:/var/lib/docker/overlay2/l/BPRM5WBHJTQPHULOKQCJXXG6OH:/var/lib/docker/overlay2/l/J3WQNSJO2XFS652SVNTOVJSNKR:/var/lib/docker/overlay2/l/3YKLG5NCGAQLWRV3KG2N76DC2Z:/var/lib/docker/overlay2/l/EBTBUSQQMA4RPTVBPWD4QRNXHG:/var/lib/docker/overlay2/l/VMTVGX5QBTOGORKHKAZJ6MJ6FE:/var/lib/docker/overlay2/l/2KSJ6XBM3FUSN2UTLNY5QDO6WQ:/var/lib/do'
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
[32mdealii-adapter      |[0m 	 Output written to solution-0.vtk 
[32mdealii-adapter      |[0m 
[32mdealii-adapter      |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/ZN6VXG64EWZW47NDKV25O3Y26P:/var/lib/docker/overlay2/l/ZRUYTZAG6ROC5Y3HXYOGXOV66I:/var/lib/docker/overlay2/l/F46MMIJAU7OESOGMNYRE4MEHZE:/var/lib/docker/overlay2/l/DGK332K2LTHKQCIUCYFD4J4ION:/var/lib/docker/overlay2/l/CB35W6CEQJHAVCKYC7KVQBGURC:/var/lib/docker/overlay2/l/IVRDNAVUVQLEYWGWZFBKFH7YFW:/var/lib/docker/overlay2/l/AJ6VBQSYILIQL6B775J34B6UVU:/var/lib/docker/overlay2/l/2FPUGN4IKTZA33ZWQLUOVCP2TQ:/var/lib/docker/overlay2/l/NIKAS6672D54P'
[32mdealii-adapter      |[0m Unexpected end of /proc/mounts line `FGZKE6ETTLCJJ:/var/lib/docker/overlay2/l/LG4KTTHFH63DD3V75C3HBRV6PP:/var/lib/docker/overlay2/l/WA6NATGBAWDHYEWAHJB7MFY5L7:/var/lib/docker/overlay2/l/BPRM5WBHJTQPHULOKQCJXXG6OH:/var/lib/docker/overlay2/l/J3WQNSJO2XFS652SVNTOVJSNKR:/var/lib/docker/overlay2/l/3YKLG5NCGAQLWRV3KG2N76DC2Z:/var/lib/docker/overlay2/l/EBTBUSQQMA4RPTVBPWD4QRNXHG:/var/lib/docker/overlay2/l/VMTVGX5QBTOGORKHKAZJ6MJ6FE:/var/lib/docker/overlay2/l/2KSJ6XBM3FUSN2UTLNY5QDO6WQ:/var/lib/docker/overlay2/l/XJZDK7YUVFLMBR6CDT7L5KXAGW,upperdir=/v'
[32mdealii-adapter      |[0m ---[[secure]] [31mERROR: [0m Wrong attribute "distribution-type"
[33mopenfoam-adapter exited with code 255
[0m[32mdealii-adapter exited with code 255
[0mOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/referenceOutput: Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Fluid']
Files only in output(right)   : []
travis_time:end:082fdcc0:start=1578571176265927662,finish=1578571252072113498,duration=75806185836,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:16a957dc[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/634706215/log.txt)