## Status: Failure 
Build: [1423](https://travis-ci.org/precice/systemtests/builds/635300170) 

Job: [1423.2](https://travis-ci.org/precice/systemtests/jobs/635300172) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/150) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

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
[32mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/UFZ7BVH6Z3FQMOVVHZC3VRDJVY:/var/lib/docker/overlay2/l/YVCHBOOQRTDY5A7A34ZS6E7Y6B:/var/lib/docker/overlay2/l/NNJPKWJHLPA3Y5KPUQPXVQ2B6V:/var/lib/docker/overlay2/l/KGMKND5NK2DHEKQ7HM4O4I4DJ4:/var/lib/docker/overlay2/l/IMKREEY2NL4QP6LQTU47KDACPC:/var/lib/docker/overlay2/l/P4UEI7BSHQV66WCPORNKY3SUSX:/var/lib/docker/overlay2/l/LGVZHH3ZSDXMGLAMKNEQXQGUIQ:/var/lib/docker/overlay2/l/QLA6ZGIPUEFUPBVJUIQL3UJYUL:/var/lib/docker/overlay2/l/NS65SAX3YIH4O'
[32mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `VEDZJ3FBQQFUQ:/var/lib/docker/overlay2/l/65WYRC7JJKTBLFJI2YYEJ7WLAT:/var/lib/docker/overlay2/l/YP22UBIIKWJ33ICUJYMBYUWD2S:/var/lib/docker/overlay2/l/DJFQUYIS7PSPPYO2U52A4SDYAH:/var/lib/docker/overlay2/l/EF7ZTOPQJIBKOVDLQ3BN23VR2H:/var/lib/docker/overlay2/l/KPTA2BOJFNFWGQVU2YLVKSIEBT:/var/lib/docker/overlay2/l/QKCVIOG2VWXRDLHPD4GNL4QISZ:/var/lib/docker/overlay2/l/DY5AFJCVRFYI47IQ4TSXIQKKAW:/var/lib/docker/overlay2/l/H2Z2BKRAGZHAXFLVCWWJFA7NMD:/var/lib/docker/overlay2/l/VWCUEKAAMNNV2CPYW4H6Y27WPE:/var/lib/do'
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
travis_time:end:1544094c:start=1578668171937171468,finish=1578668239059518163,duration=67122346695,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:11300047[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635300172/log.txt)