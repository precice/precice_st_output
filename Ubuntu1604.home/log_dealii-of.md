## Status: Failure 
Build: [1431](https://travis-ci.org/precice/systemtests/builds/635347829) 

Job: [1431.6](https://travis-ci.org/precice/systemtests/jobs/635347835) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/150) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
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
[33mopenfoam-adapter    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/QHJ2HAXYPGBF3YUG3SLM3GC6XO:/var/lib/docker/overlay2/l/ENAIQB7QDUOHGIQOTD5VGO4MDD:/var/lib/docker/overlay2/l/Y4MSDX3XN7GBVHHLEDE7YCGZPV:/var/lib/docker/overlay2/l/ZZ5Z4BK4SHZNZ63ONZZJ4WXA3W:/var/lib/docker/overlay2/l/N6OFYEMD3A7DPSMN5ELBQDCRKR:/var/lib/docker/overlay2/l/WGPNBWWMATVO6SO4VOUSPMHYQV:/var/lib/docker/overlay2/l/RHL54GPHL55GLMTTZ3LPCEPE3Q:/var/lib/docker/overlay2/l/W7GVW4ZMNHRWCJ7R7B2QBY4CBH:/var/lib/docker/overlay2/l/FD4W4SM6SH7BI'
[33mopenfoam-adapter    |[0m Unexpected end of /proc/mounts line `OMFXYDQ2ZBVLG:/var/lib/docker/overlay2/l/KJ4GGO3BFEYQE2EB4LNKHRJ6MT:/var/lib/docker/overlay2/l/MP6M4YPMMFK2J7XF34HOXFQOLM:/var/lib/docker/overlay2/l/SO7VVOJHDANHQOOJDBJ7MRGKVZ:/var/lib/docker/overlay2/l/42XAFC5EZOB3IZ5GN5L3KGICTT:/var/lib/docker/overlay2/l/XTOVKEWUMRQB72UDNDECQ22NMU:/var/lib/docker/overlay2/l/QVVKKTI7X4DUAKHB2XO2XC4HJZ:/var/lib/docker/overlay2/l/YHZ2NICMPFISRXC4RUSETKLZO3:/var/lib/docker/overlay2/l/XFSWOQTQITR72L3FSJ6SJKDHK5:/var/lib/docker/overlay2/l/2WA434EBLNU6I5DN7OYRSRZF2I:/var/lib/do'
[32mdealii-adapter      |[0m --------------------------------------------------
[32mdealii-adapter      |[0m              Running deal.ii solver 
[32mdealii-adapter      |[0m --------------------------------------------------
[32mdealii-adapter      |[0m 
[32mdealii-adapter      |[0m   Create mesh: 
[32mdealii-adapter      |[0m 	 Number of active cells:       150
[32mdealii-adapter      |[0m   Setup system: 
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
[32mdealii-adapter      |[0m 	 Number of degrees of freedom: 1116
[32mdealii-adapter      |[0m 	 Output written to solution-0.vtk 
[32mdealii-adapter      |[0m 
[32mdealii-adapter      |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/4TYS3M3PZ5W2PEN5DVXCCIH6PJ:/var/lib/docker/overlay2/l/NG5JRHPBYEXPHTV7B3VUDQ3NGC:/var/lib/docker/overlay2/l/7M5NGNYFFHD4IDRM52H5UKC7EZ:/var/lib/docker/overlay2/l/M56XTBSMXZHZLQ5MP76NJJ734J:/var/lib/docker/overlay2/l/WAR7J7AKDXTEHI2Q6FZBNA3X4I:/var/lib/docker/overlay2/l/RHL54GPHL55GLMTTZ3LPCEPE3Q:/var/lib/docker/overlay2/l/W7GVW4ZMNHRWCJ7R7B2QBY4CBH:/var/lib/docker/overlay2/l/FD4W4SM6SH7BIOMFXYDQ2ZBVLG:/var/lib/docker/overlay2/l/KJ4GGO3BFEYQE'
[32mdealii-adapter      |[0m Unexpected end of /proc/mounts line `2EB4LNKHRJ6MT:/var/lib/docker/overlay2/l/MP6M4YPMMFK2J7XF34HOXFQOLM:/var/lib/docker/overlay2/l/SO7VVOJHDANHQOOJDBJ7MRGKVZ:/var/lib/docker/overlay2/l/42XAFC5EZOB3IZ5GN5L3KGICTT:/var/lib/docker/overlay2/l/XTOVKEWUMRQB72UDNDECQ22NMU:/var/lib/docker/overlay2/l/QVVKKTI7X4DUAKHB2XO2XC4HJZ:/var/lib/docker/overlay2/l/YHZ2NICMPFISRXC4RUSETKLZO3:/var/lib/docker/overlay2/l/XFSWOQTQITR72L3FSJ6SJKDHK5:/var/lib/docker/overlay2/l/2WA434EBLNU6I5DN7OYRSRZF2I:/var/lib/docker/overlay2/l/IOH5DPXHG4JKKMF2YSAQTRVWGO,upperdir=/v'
[33mopenfoam-adapter exited with code 255
[0m[32mdealii-adapter      |[0m ---[[secure]] [31mERROR: [0m Wrong attribute "distribution-type"
[32mdealii-adapter exited with code 255
[0mOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/referenceOutput: Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Fluid']
Files only in output(right)   : []
travis_time:end:156fd25a:start=1578674326188760552,finish=1578674403621165246,duration=77432404694,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:05377790[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635347835/log.txt)