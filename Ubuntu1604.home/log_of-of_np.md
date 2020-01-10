## Status: Failure 
Build: [1429](https://travis-ci.org/precice/systemtests/builds/635333660) 

Job: [1429.8](https://travis-ci.org/precice/systemtests/jobs/635333668) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/150) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

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
[36mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/RNPAIK6XNQKZS3WH5TSMYZQTUA:/var/lib/docker/overlay2/l/AGG4MYJNOFAVUJBUZGF2WMJL6Y:/var/lib/docker/overlay2/l/VNGIE3VVIIZODOZNN2I3ZO6XHE:/var/lib/docker/overlay2/l/BKNDTLWY5KYKSKNRR54P3HCCKY:/var/lib/docker/overlay2/l/33K42XBS4ZOXXFEFWV46Y3ZYFM:/var/lib/docker/overlay2/l/HIZTC2XCU2X446QAT33HBJ4IFZ:/var/lib/docker/overlay2/l/VJMGAYQR6IRK7NYSLLYVWI43AU:/var/lib/docker/overlay2/l/7CZIPZRORXVIRUNVJG2HL2IUSV:/var/lib/docker/overlay2/l/5UBGBMBWDUKOY'
[36mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `LNMFPY6ZRHDNY:/var/lib/docker/overlay2/l/3SMFWWX32BBVH42FWRMQALQ4EZ:/var/lib/docker/overlay2/l/7VLZNZW7MV6BMY3OU4DCWLGA7R:/var/lib/docker/overlay2/l/AJXLSX5CXP5EZZF44H2KBNSWQR:/var/lib/docker/overlay2/l/43CQVDZIDPJPBVNN3ZHJ2QIYAF:/var/lib/docker/overlay2/l/ADCRIQVY5CAF374MAVW6ZFFPIF:/var/lib/docker/overlay2/l/F4KXOMP7EDOSYIVGOY2R74T3I6:/var/lib/docker/overlay2/l/PFJTTYLSOD7SOQATP5KSZVZPHD:/var/lib/docker/overlay2/l/4OB5M4FNDBD2INQYSC4MX4ANFW:/var/lib/docker/overlay2/l/3J5C6WLL5S5EYZTTR6KL5WLFAQ:/var/lib/do'
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
[36mopenfoam-adapter-fluid    |[0m ---[[secure]] [31mERROR: [0m Tag <post-processing:IQN-ILS> is unknown
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
travis_time:end:16f29930:start=1578672573178023164,finish=1578672640408437758,duration=67230414594,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:077f372e[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635333668/log.txt)