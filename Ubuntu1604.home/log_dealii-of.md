## Status: Failure 
Build: [1414](https://travis-ci.org/precice/systemtests/builds/634663511) 

Job: [1414.6](https://travis-ci.org/precice/systemtests/jobs/634663517) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/148) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/1cefd5edac2aea69ea37978eeb5479db3ada0042...d9a7dc3ed7e75c17e88adc4757c7bd5f44719b24) 

---
Last 100 lines of the job log at the moment of push:
```
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
[33mopenfoam-adapter    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/XCG44VMM3CEKCCB4JEMRLBMJGC:/var/lib/docker/overlay2/l/T5SCRLWP3BV7AOCJS5ZEVTCGTQ:/var/lib/docker/overlay2/l/4OTEMNQAYU7MSD6PETFPNFKB64:/var/lib/docker/overlay2/l/LTZAFBMPNMYJP3YY6MRP2F2F73:/var/lib/docker/overlay2/l/HJJT3ESMVHHIONRCC2GYX4XA65:/var/lib/docker/overlay2/l/YAHUMQD5IP7RSNAT6TUJGZQ5HH:/var/lib/docker/overlay2/l/JEPBYJ34SRIZGGEVXKCS3LPQ5Q:/var/lib/docker/overlay2/l/ZGWKISTPYPCGOKTINMKLAK7JAH:/var/lib/docker/overlay2/l/SQO4WHTU3DMEE'
[33mopenfoam-adapter    |[0m Unexpected end of /proc/mounts line `TYTJ7M65YQVV4:/var/lib/docker/overlay2/l/MXAEEWXAD3DJUB7XFIQKFEGSHJ:/var/lib/docker/overlay2/l/LVTFHWJU5ZAFDYSYWAVVTTX7FL:/var/lib/docker/overlay2/l/DT5RAQE62KUTRSZUXPC6475FKC:/var/lib/docker/overlay2/l/EZHQOXHLGW5MVHWPE2Z7K2LL57:/var/lib/docker/overlay2/l/5UCLK5FOE6DNHLPEZFIIATFEEE:/var/lib/docker/overlay2/l/PYPP5ZX2PD63DIEXRLTUNNK3EZ:/var/lib/docker/overlay2/l/D7MZV2O6VDSSS3XPV4ZW7ZJIUN:/var/lib/docker/overlay2/l/Z35XILM3JGFMWCH326LUWJHHUC:/var/lib/docker/overlay2/l/ZPZWLFR5MHSR3SQATYJ5W73ZZZ:/var/lib/do'
[32mdealii-adapter      |[0m --------------------------------------------------
[32mdealii-adapter      |[0m              Running deal.ii solver 
[32mdealii-adapter      |[0m --------------------------------------------------
[32mdealii-adapter      |[0m 
[32mdealii-adapter      |[0m   Create mesh: 
[32mdealii-adapter      |[0m 	 Number of active cells:       150
[32mdealii-adapter      |[0m   Setup system: 
[32mdealii-adapter      |[0m 	 Number of degrees of freedom: 1116
[32mdealii-adapter      |[0m 	 Output written to solution-0.vtk 
[32mdealii-adapter      |[0m 
[32mdealii-adapter      |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/47FCVLY6MLSORS3A5KCTZSS3ZX:/var/lib/docker/overlay2/l/I7I4O3ERJR2VXPUBGZST7QDOLT:/var/lib/docker/overlay2/l/HF43Q6HJ6KL7I7KNT4XYFBPO2Q:/var/lib/docker/overlay2/l/I6ECUKHNXZ5SVAGSKRUULFDTDZ:/var/lib/docker/overlay2/l/KH5SVZLDLIT57OOUSUNZINGEYM:/var/lib/docker/overlay2/l/JEPBYJ34SRIZGGEVXKCS3LPQ5Q:/var/lib/docker/overlay2/l/ZGWKISTPYPCGOKTINMKLAK7JAH:/var/lib/docker/overlay2/l/SQO4WHTU3DMEETYTJ7M65YQVV4:/var/lib/docker/overlay2/l/MXAEEWXAD3DJU'
[32mdealii-adapter      |[0m Unexpected end of /proc/mounts line `B7XFIQKFEGSHJ:/var/lib/docker/overlay2/l/LVTFHWJU5ZAFDYSYWAVVTTX7FL:/var/lib/docker/overlay2/l/DT5RAQE62KUTRSZUXPC6475FKC:/var/lib/docker/overlay2/l/EZHQOXHLGW5MVHWPE2Z7K2LL57:/var/lib/docker/overlay2/l/5UCLK5FOE6DNHLPEZFIIATFEEE:/var/lib/docker/overlay2/l/PYPP5ZX2PD63DIEXRLTUNNK3EZ:/var/lib/docker/overlay2/l/D7MZV2O6VDSSS3XPV4ZW7ZJIUN:/var/lib/docker/overlay2/l/Z35XILM3JGFMWCH326LUWJHHUC:/var/lib/docker/overlay2/l/ZPZWLFR5MHSR3SQATYJ5W73ZZZ:/var/lib/docker/overlay2/l/M63WO4K2CMF6T7ESAHI4I7UW73,upperdir=/v'
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
travis_time:end:206da13a:start=1578564101379584172,finish=1578564175621245237,duration=74241661065,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0feec7c0[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/634663517/log.txt)