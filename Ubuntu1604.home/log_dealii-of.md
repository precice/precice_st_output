## Status: Failure 
Build: [1423](https://travis-ci.org/precice/systemtests/builds/635300170) 

Job: [1423.6](https://travis-ci.org/precice/systemtests/jobs/635300176) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/150) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/1cefd5edac2aea69ea37978eeb5479db3ada0042...d9a7dc3ed7e75c17e88adc4757c7bd5f44719b24) 

---
Last 100 lines of the job log at the moment of push:
```
[32mdealii-adapter      |[0m 
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
[33mopenfoam-adapter    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/FMJIV3NQRYMVTPBKZM6BHSBARM:/var/lib/docker/overlay2/l/5OG6DUMMMRWGDZUOVPFON2Q5OJ:/var/lib/docker/overlay2/l/X4FRCJYXY2MHX2Z5RPS7H6WC3P:/var/lib/docker/overlay2/l/YF6L4WD56P7C7EGF6QASRFCO5L:/var/lib/docker/overlay2/l/QOBV3HGMQUNDQXQJ2A2BVV772G:/var/lib/docker/overlay2/l/EQI4Y436PYCXZ7IONPIWGWLLM5:/var/lib/docker/overlay2/l/LUMCLTVSU4FWCCYOJM5REL2ZCB:/var/lib/docker/overlay2/l/CHT3HHMPPCMRHIXMVEG4ZSJ6BD:/var/lib/docker/overlay2/l/7IN43PKDRYTNY'
[33mopenfoam-adapter    |[0m Unexpected end of /proc/mounts line `5QTDNRY4S5772:/var/lib/docker/overlay2/l/BI5IVKGEDTCM5OCKVKPVA2DHYF:/var/lib/docker/overlay2/l/TLXRYUF4UZHBONREB5C7DHXITO:/var/lib/docker/overlay2/l/6CLGOVQSHUGODPXXOTNPPZGAHM:/var/lib/docker/overlay2/l/U6FZTJX6OIDXMVBJLTKSDY5XL2:/var/lib/docker/overlay2/l/NTPVZDW77HLKPE43K6NLAUQ2D3:/var/lib/docker/overlay2/l/H6BGYXNN5QA35YG6KXFERJCG6M:/var/lib/docker/overlay2/l/EL4GRHOL2WYWKJAOBNSLMEYJJI:/var/lib/docker/overlay2/l/QNPH4U7FTNAY6PAX4ZKUDDGVCR:/var/lib/docker/overlay2/l/CICT7Z4PLVYMY7J7MEJ2RH6AUX:/var/lib/do'
[32mdealii-adapter      |[0m   Create mesh: 
[32mdealii-adapter      |[0m 	 Number of active cells:       150
[32mdealii-adapter      |[0m   Setup system: 
[32mdealii-adapter      |[0m 	 Number of degrees of freedom: 1116
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
[32mdealii-adapter      |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/IL3OGEULCRBRDOJ6KQP5UXAWOT:/var/lib/docker/overlay2/l/THPH2DBOT3PP5K6ORXYRAPSF52:/var/lib/docker/overlay2/l/M5WQH356MQ4MJ4C2YDN4P3SIHJ:/var/lib/docker/overlay2/l/TINOKJ4QNSDBGPY5NGT2RGK7Z2:/var/lib/docker/overlay2/l/IQXDBTMNPE62ZUBGJFAYTDIRJO:/var/lib/docker/overlay2/l/LUMCLTVSU4FWCCYOJM5REL2ZCB:/var/lib/docker/overlay2/l/CHT3HHMPPCMRHIXMVEG4ZSJ6BD:/var/lib/docker/overlay2/l/7IN43PKDRYTNY5QTDNRY4S5772:/var/lib/docker/overlay2/l/BI5IVKGEDTCM5'
[32mdealii-adapter      |[0m Unexpected end of /proc/mounts line `OCKVKPVA2DHYF:/var/lib/docker/overlay2/l/TLXRYUF4UZHBONREB5C7DHXITO:/var/lib/docker/overlay2/l/6CLGOVQSHUGODPXXOTNPPZGAHM:/var/lib/docker/overlay2/l/U6FZTJX6OIDXMVBJLTKSDY5XL2:/var/lib/docker/overlay2/l/NTPVZDW77HLKPE43K6NLAUQ2D3:/var/lib/docker/overlay2/l/H6BGYXNN5QA35YG6KXFERJCG6M:/var/lib/docker/overlay2/l/EL4GRHOL2WYWKJAOBNSLMEYJJI:/var/lib/docker/overlay2/l/QNPH4U7FTNAY6PAX4ZKUDDGVCR:/var/lib/docker/overlay2/l/CICT7Z4PLVYMY7J7MEJ2RH6AUX:/var/lib/docker/overlay2/l/O3E4YLXWNG3QNK4ONJBKOTBEH4,upperdir=/v'
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
travis_time:end:00e667c8:start=1578668312897760731,finish=1578668390309109251,duration=77411348520,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0a203366[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635300176/log.txt)