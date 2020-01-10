## Status: Failure 
Build: [1425](https://travis-ci.org/precice/systemtests/builds/635309603) 

Job: [1425.6](https://travis-ci.org/precice/systemtests/jobs/635309609) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/150) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/1cefd5edac2aea69ea37978eeb5479db3ada0042...d9a7dc3ed7e75c17e88adc4757c7bd5f44719b24)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

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
[33mopenfoam-adapter    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/UU5KNBXPTEIJSIYHN3MC6AOBMI:/var/lib/docker/overlay2/l/C32V22W6QPSFWZEJO6HKONTQGS:/var/lib/docker/overlay2/l/HSC7VR2PFLB6OC4RAVCDKJDMEX:/var/lib/docker/overlay2/l/ALZ7F7UDBLRSJ7HWWZH7QYILSA:/var/lib/docker/overlay2/l/N27NWIGZPIW6H2PGAWTJMQO7M7:/var/lib/docker/overlay2/l/QMMT62ILDSI4T4HEE3IO7PJ7GA:/var/lib/docker/overlay2/l/CRL6UK4OBPGPUKQDC6VIWYGOCP:/var/lib/docker/overlay2/l/PA26A64Y2C2SJNVNA4FXA2MYR5:/var/lib/docker/overlay2/l/G7JMG6A5EFBJK'
[33mopenfoam-adapter    |[0m Unexpected end of /proc/mounts line `O7XYEEX2GAJB5:/var/lib/docker/overlay2/l/TV4VDYFXP7HXHEL7JOMTGZLN6A:/var/lib/docker/overlay2/l/D53JH5M5XEBLAN357NSRCW6TJS:/var/lib/docker/overlay2/l/TNZKPHMHD5SVXTZ5MHEPVVBXUM:/var/lib/docker/overlay2/l/V42VGXRETAXHE3AEXJAFHKIU5V:/var/lib/docker/overlay2/l/4LNNOOX5WDJMPIDX35M4HZ7WUZ:/var/lib/docker/overlay2/l/GEUZTTHOXYMO5CV2YVYGVZS5OM:/var/lib/docker/overlay2/l/KK46QWU6NXPRQKZKE7DZFGAD7P:/var/lib/docker/overlay2/l/YVBTMY24Z443RCPHAOJWONUJUX:/var/lib/docker/overlay2/l/3CAUZCZRX5PO5WCWCI7BUZ6FN3:/var/lib/do'
[32mdealii-adapter      |[0m --------------------------------------------------
[32mdealii-adapter      |[0m              Running deal.ii solver 
[32mdealii-adapter      |[0m --------------------------------------------------
[32mdealii-adapter      |[0m 
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
[32mdealii-adapter      |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/F6WOCGAVHRZNQGNKTON3KGBU2B:/var/lib/docker/overlay2/l/BPRUN4M43FVZRHMAMS4Y7CWP3G:/var/lib/docker/overlay2/l/PH7PYS32X4A6UPMEWHKCFFGXUL:/var/lib/docker/overlay2/l/APLUAGJ72Q2XUFYK74PZZM273C:/var/lib/docker/overlay2/l/XDODOMRYFJ4JEZNFSHV7YD67MV:/var/lib/docker/overlay2/l/CRL6UK4OBPGPUKQDC6VIWYGOCP:/var/lib/docker/overlay2/l/PA26A64Y2C2SJNVNA4FXA2MYR5:/var/lib/docker/overlay2/l/G7JMG6A5EFBJKO7XYEEX2GAJB5:/var/lib/docker/overlay2/l/TV4VDYFXP7HXH'
[32mdealii-adapter      |[0m Unexpected end of /proc/mounts line `EL7JOMTGZLN6A:/var/lib/docker/overlay2/l/D53JH5M5XEBLAN357NSRCW6TJS:/var/lib/docker/overlay2/l/TNZKPHMHD5SVXTZ5MHEPVVBXUM:/var/lib/docker/overlay2/l/V42VGXRETAXHE3AEXJAFHKIU5V:/var/lib/docker/overlay2/l/4LNNOOX5WDJMPIDX35M4HZ7WUZ:/var/lib/docker/overlay2/l/GEUZTTHOXYMO5CV2YVYGVZS5OM:/var/lib/docker/overlay2/l/KK46QWU6NXPRQKZKE7DZFGAD7P:/var/lib/docker/overlay2/l/YVBTMY24Z443RCPHAOJWONUJUX:/var/lib/docker/overlay2/l/3CAUZCZRX5PO5WCWCI7BUZ6FN3:/var/lib/docker/overlay2/l/ZDH3NFU7Y33X5ZVM5QMA2EMEV4,upperdir=/v'
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
travis_time:end:149cfbe6:start=1578670735905982896,finish=1578670812536434130,duration=76630451234,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:089cf29a[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635309609/log.txt)