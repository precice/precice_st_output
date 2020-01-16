## Status: Failure 
Build: [1461](https://travis-ci.org/precice/systemtests/builds/637943411) 

Job: [1461.9](https://travis-ci.org/precice/systemtests/jobs/637943420) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/148) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
[32mopenfoam-adapter-fluid    |[0m phi
[32mopenfoam-adapter-fluid    |[0m owner
[32mopenfoam-adapter-fluid    |[0m data
[32mopenfoam-adapter-fluid    |[0m cellZones
[32mopenfoam-adapter-fluid    |[0m boundary
[32mopenfoam-adapter-fluid    |[0m dynamicMeshDict
[32mopenfoam-adapter-fluid    |[0m p
[32mopenfoam-adapter-fluid    |[0m cellDisplacement
[32mopenfoam-adapter-fluid    |[0m pointZones
[32mopenfoam-adapter-fluid    |[0m transportProperties
[32mopenfoam-adapter-fluid    |[0m )
[32mopenfoam-adapter-fluid    |[0m 
[32mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/7QEFUE2GFOKECEZVPML3WJX6JC:/var/lib/docker/overlay2/l/YAQXJZGEC57CA6QXDAYQJPVW32:/var/lib/docker/overlay2/l/KXEHFCGVZTDRIV33FPYUOPQZJ3:/var/lib/docker/overlay2/l/NOWVOHVPCEBFMVH4R5FMBJ6WYM:/var/lib/docker/overlay2/l/T4MHKFNB65JON6FI3R2BWIXG2K:/var/lib/docker/overlay2/l/W46Z6XQXELBGZOMIDZBGNDO4NI:/var/lib/docker/overlay2/l/D4Y3UZMQ45TLDFLR47RHMQ3GPL:/var/lib/docker/overlay2/l/LFXLRNTBXDCCZIC2FSQARWPDYY:/var/lib/docker/overlay2/l/I2XIIEOT3XPGC'
[32mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `AQKOIWJWDRVUC:/var/lib/docker/overlay2/l/ECKNP6Y5O52UX3AF73CU77OYTX:/var/lib/docker/overlay2/l/NYDDILRXWDCJIYT34DZODGIZRG:/var/lib/docker/overlay2/l/Y2ICCL4E3FMLZUTX7BW2QI6OSQ:/var/lib/docker/overlay2/l/XLJPEDWSAPFKFNCKIQJUJ442HF:/var/lib/docker/overlay2/l/4FVCFGEIEBDTORW6Z5BFLFGDMS:/var/lib/docker/overlay2/l/HAXQ7EJCIN6CYCQ3AEEYJ2AOBS:/var/lib/docker/overlay2/l/LOS3Q2OVROE2DEG5ORNEYBGD5U:/var/lib/docker/overlay2/l/RPX7WWDENNFIHAX57TTJYNZGDB:/var/lib/docker/overlay2/l/DPA2I5VKG52KTTX5XMWYII27DS:/var/lib/do'
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] Reading the adapter's YAML configuration file /home/[secure]/Data/Input/[secure]-adapter-config.yml...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Checking the adapter's YAML configuration file...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   participant : Fluid
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   [secure]-config-file : [secure]-config.xml
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   interfaces : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Fluid-Mesh-Faces
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceCenters
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       flap
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     write-data : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       Forces0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Fluid-Mesh-Nodes
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceNodes
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       flap
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     read-data : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       Displacements0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     subcycling : 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     prevent early exit : 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     evaluate boundaries : 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     disable checkpointing : 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     CHT module enabled : 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     FSI module enabled : 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Configuring the FSI module...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     user-defined solver type : none
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     pointDisplacement field name : pointDisplacement
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Determining the solver type...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Found the transportProperties dictionary.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Found the turbulenceProperties dictionary.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Did not find the thermophysicalProperties dictionary.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] This is an incompressible flow solver, as turbulence and transport properties are provided.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Checking the timestep type (fixed vs adjustable)...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   Timestep type: fixed.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Creating the preCICE solver interface...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   Number of processes: 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   MPI rank: 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   preCICE solver interface was created.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Configuring preCICE...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]] [0m This is preCICE version 1.6.1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]] [0m Revision info: v1.6.1-148-g5387fe6
[32mopenfoam-adapter-fluid    |[0m ---[[secure]] [0m Configuring preCICE with configuration: "[secure]-config.xml"
[32mopenfoam-adapter-fluid    |[0m ---[[secure]] [0m Run in coupling mode
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   preCICE was configured.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Creating interfaces...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Number of face centres: 33
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Interface created on mesh Fluid-Mesh-Faces
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Adding coupling data writers...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Added writer: Force.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Adding coupling data readers...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Number of face nodes: 68
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Interface created on mesh Fluid-Mesh-Nodes
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Adding coupling data writers...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Adding coupling data readers...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Added reader: Displacement.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Initalizing the preCICE solver interface...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]] [0m Setting up master communication to coupling partner/s
[33mcalculix-adapter-solid    |[0m ---[[secure]] [0m Masters are connected
[33mcalculix-adapter-solid    |[0m ---[[secure]] [0m Gather mesh Solid
[33mcalculix-adapter-solid    |[0m ---[[secure]] [0m Send global mesh Solid
[33mcalculix-adapter-solid    |[0m ---[[secure]] [0m Compute partition for mesh Solid
[33mcalculix-adapter-solid    |[0m ---[[secure]] [0m Setting up slaves communication to coupling partner/s
[33mcalculix-adapter-solid    |[0m ---[[secure]] [31mERROR: [0m You can only use a point-to-point communication between two participants which both use a master. Please use distribution-type gather-scatter instead.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]] [0m Masters are connected
[32mopenfoam-adapter-fluid    |[0m ---[[secure]] [0m Receive global mesh Solid
[32mopenfoam-adapter-fluid    |[0m ---[[secure]] [0m Compute partition for mesh Fluid-Mesh-Faces
[32mopenfoam-adapter-fluid    |[0m ---[[secure]] [0m Compute partition for mesh Fluid-Mesh-Nodes
[32mopenfoam-adapter-fluid    |[0m ---[[secure]] [0m Setting up slaves communication to coupling partner/s
[32mopenfoam-adapter-fluid    |[0m ---[[secure]] [31mERROR: [0m You can only use a point-to-point communication between two participants which both use a master. Please use distribution-type gather-scatter instead.
[33mcalculix-adapter-solid exited with code 255
[0m[32mopenfoam-adapter-fluid exited with code 255
[0mOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx_fsi.Ubuntu1604.home.PETSc/referenceOutput: Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx_fsi.Ubuntu1604.home.PETSc/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx_fsi.Ubuntu1604.home.PETSc/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Fluid']
Files only in output(right)   : []
travis_time:end:1a076486:start=1579180611695473513,finish=1579180687760803380,duration=76065329867,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:078815f1[0K$ python push.py -t of-ccx_fsi
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/637943420/log.txt)