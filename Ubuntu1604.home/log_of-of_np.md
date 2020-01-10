## Status: Failure 
Build: [1420](https://travis-ci.org/precice/systemtests/builds/635276412) 

Job: [1420.8](https://travis-ci.org/precice/systemtests/jobs/635276421) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/149) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
[36mopenfoam-adapter-fluid    |[0m points
[36mopenfoam-adapter-fluid    |[0m neighbour
[36mopenfoam-adapter-fluid    |[0m thermo:mu
[36mopenfoam-adapter-fluid    |[0m MRFProperties
[36mopenfoam-adapter-fluid    |[0m thermo:psi
[36mopenfoam-adapter-fluid    |[0m K
[36mopenfoam-adapter-fluid    |[0m ghf
[36mopenfoam-adapter-fluid    |[0m h
[36mopenfoam-adapter-fluid    |[0m faces
[36mopenfoam-adapter-fluid    |[0m U
[36mopenfoam-adapter-fluid    |[0m rho
[36mopenfoam-adapter-fluid    |[0m radiationProperties
[36mopenfoam-adapter-fluid    |[0m turbulenceProperties
[36mopenfoam-adapter-fluid    |[0m fvSchemes
[36mopenfoam-adapter-fluid    |[0m fvOptions
[36mopenfoam-adapter-fluid    |[0m faceZones
[36mopenfoam-adapter-fluid    |[0m fvSolution
[36mopenfoam-adapter-fluid    |[0m p_rgh
[36mopenfoam-adapter-fluid    |[0m thermophysicalProperties
[36mopenfoam-adapter-fluid    |[0m dpdt
[36mopenfoam-adapter-fluid    |[0m phi
[36mopenfoam-adapter-fluid    |[0m owner
[36mopenfoam-adapter-fluid    |[0m gh
[36mopenfoam-adapter-fluid    |[0m data
[36mopenfoam-adapter-fluid    |[0m cellZones
[36mopenfoam-adapter-fluid    |[0m boundary
[36mopenfoam-adapter-fluid    |[0m g
[36mopenfoam-adapter-fluid    |[0m p
[36mopenfoam-adapter-fluid    |[0m T
[36mopenfoam-adapter-fluid    |[0m hRef
[36mopenfoam-adapter-fluid    |[0m thermo:rho
[36mopenfoam-adapter-fluid    |[0m pointZones
[36mopenfoam-adapter-fluid    |[0m thermo:alpha
[36mopenfoam-adapter-fluid    |[0m )
[36mopenfoam-adapter-fluid    |[0m 
[36mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/Y5FFKS2KYXFS3A43GEBIGZ2UEQ:/var/lib/docker/overlay2/l/YQYHDUKK54NFP3P747CDONTPVR:/var/lib/docker/overlay2/l/HUTI7IAYPZFZRKB4VVF4BFKWIU:/var/lib/docker/overlay2/l/WNXULSDULXOCWZV7GOP4LX7GLQ:/var/lib/docker/overlay2/l/6I3AS3FOIHJOI2IBW4P3FG7KG2:/var/lib/docker/overlay2/l/TZTG5TYFEJV2LNWZXKMMVEGDQS:/var/lib/docker/overlay2/l/4YHJ23P7S264HDOXBG2E5BGKCV:/var/lib/docker/overlay2/l/TCTO36I2OBRCNID24WRMS6VPHM:/var/lib/docker/overlay2/l/2NTBPLS24SE6X'
[36mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `O2VDXBKSSPWUK:/var/lib/docker/overlay2/l/KNOINR33FUAXPHMHCOWEU3NIUY:/var/lib/docker/overlay2/l/KWVAPW2DCCNG2XXN72HL3T5L6P:/var/lib/docker/overlay2/l/CAXLITA3LMO5JUWX47LNUOGRTG:/var/lib/docker/overlay2/l/7MIEFAI3PUYJGG7R336HP4O37R:/var/lib/docker/overlay2/l/NUA5UNFXNWRX64MPPA33ZK77PF:/var/lib/docker/overlay2/l/OQUO4OQRTDPAIOYFZPFH7SH5LL:/var/lib/docker/overlay2/l/PC2MPTX4MWHKMVQYVT2X2KRGQW:/var/lib/docker/overlay2/l/SWSGE7DWWWK7QFL4EDUPEU2TUA:/var/lib/docker/overlay2/l/THE5UVQI4IKJW3IO2WGEDWEIWK:/var/lib/do'
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] Reading the adapter's YAML configuration file ./Fluid/[secure]-adapter-config.yml...
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Checking the adapter's YAML configuration file...
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   participant : Fluid
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   [secure]-config-file : [secure]-config.xml
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   interfaces : 
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Fluid-Mesh-Centers
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceCenters
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 0
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       interface
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     read-data : 
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       Heat-Flux
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Fluid-Mesh-Nodes
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceNodes
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 1
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       interface
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     write-data : 
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       Temperature
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     subcycling : 1
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     prevent early exit : 1
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     evaluate boundaries : 1
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     disable checkpointing : 0
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     CHT module enabled : 1
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     FSI module enabled : 0
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Configuring the CHT module...
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     user-defined solver type : none
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     temperature field name : T
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     transportProperties name : transportProperties
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     conductivity name for basic solvers : k
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     density name for incompressible solvers : rho
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     heat capacity name for incompressible solvers : Cp
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Prandtl number name for incompressible solvers : Pr
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Turbulent thermal diffusivity field name for incompressible solvers : alphat
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Determining the solver type...
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Did not find the transportProperties dictionary.
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Found the turbulenceProperties dictionary.
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Found the thermophysicalProperties dictionary.
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] This is a compressible flow solver, as turbulence and thermophysical properties are provided.
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Checking the timestep type (fixed vs adjustable)...
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   Timestep type: fixed.
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Creating the preCICE solver interface...
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   Number of processes: 1
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   MPI rank: 0
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   preCICE solver interface was created.
[36mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Configuring preCICE...
[36mopenfoam-adapter-fluid    |[0m ---[[secure]] [31mERROR: [0m Wrong attribute "distribution-type"
[36mopenfoam-adapter-fluid exited with code 255
[0mOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Solid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Solid', 'Fluid']
Files only in output(right)   : []
travis_time:end:0d5c7f43:start=1578665215737045200,finish=1578665282496308006,duration=66759262806,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:17d9276e[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635276421/log.txt)