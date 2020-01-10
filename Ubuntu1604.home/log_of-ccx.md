## Status: Failure 
Build: [1420](https://travis-ci.org/precice/systemtests/builds/635276412) 

Job: [1420.3](https://travis-ci.org/precice/systemtests/jobs/635276416) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/149) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
[32mopenfoam-adapter-outer    |[0m Registered objects: 
[32mopenfoam-adapter-outer    |[0m 31
[32mopenfoam-adapter-outer    |[0m (
[32mopenfoam-adapter-outer    |[0m points
[32mopenfoam-adapter-outer    |[0m neighbour
[32mopenfoam-adapter-outer    |[0m thermo:mu
[32mopenfoam-adapter-outer    |[0m MRFProperties
[32mopenfoam-adapter-outer    |[0m thermo:psi
[32mopenfoam-adapter-outer    |[0m ghf
[32mopenfoam-adapter-outer    |[0m h
[32mopenfoam-adapter-outer    |[0m faces
[32mopenfoam-adapter-outer    |[0m U
[32mopenfoam-adapter-outer    |[0m rho
[32mopenfoam-adapter-outer    |[0m radiationProperties
[32mopenfoam-adapter-outer    |[0m turbulenceProperties
[32mopenfoam-adapter-outer    |[0m fvSchemes
[32mopenfoam-adapter-outer    |[0m fvOptions
[32mopenfoam-adapter-outer    |[0m faceZones
[32mopenfoam-adapter-outer    |[0m fvSolution
[32mopenfoam-adapter-outer    |[0m p_rgh
[32mopenfoam-adapter-outer    |[0m thermophysicalProperties
[32mopenfoam-adapter-outer    |[0m phi
[32mopenfoam-adapter-outer    |[0m owner
[32mopenfoam-adapter-outer    |[0m gh
[32mopenfoam-adapter-outer    |[0m data
[32mopenfoam-adapter-outer    |[0m cellZones
[32mopenfoam-adapter-outer    |[0m boundary
[32mopenfoam-adapter-outer    |[0m g
[32mopenfoam-adapter-outer    |[0m p
[32mopenfoam-adapter-outer    |[0m T
[32mopenfoam-adapter-outer    |[0m hRef
[32mopenfoam-adapter-outer    |[0m thermo:rho
[32mopenfoam-adapter-outer    |[0m pointZones
[32mopenfoam-adapter-outer    |[0m thermo:alpha
[32mopenfoam-adapter-outer    |[0m )
[32mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/XNB4PUAD5A4QUEBUCTCWF63CAV:/var/lib/docker/overlay2/l/D54QKCC6VL7AP2DIJNDWIYRXOQ:/var/lib/docker/overlay2/l/QTPYGGKM6A7VOMAYIJS6YT52KT:/var/lib/docker/overlay2/l/3EBARTKTYCIT33QW6RXN3UUF3W:/var/lib/docker/overlay2/l/HENFPPVYIZWBDJCWXLBGQSCJ3L:/var/lib/docker/overlay2/l/ZVX6OTBDTIRGVV3AFCEPJN4BKM:/var/lib/docker/overlay2/l/LC5EK3QYMZSMFTYK72NBYWKYG3:/var/lib/docker/overlay2/l/2Y3YV3WSWKJFJNCBQTVZXWYTTT:/var/lib/docker/overlay2/l/BYS5FWRMF5LDI'
[32mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `E2NPWLNCUOCGY:/var/lib/docker/overlay2/l/7JYWLWVSZ2K5NIGEO2MLESVLSD:/var/lib/docker/overlay2/l/HAM46Z3T2VANQLQWNNUEYIOMAE:/var/lib/docker/overlay2/l/AYZIIGB6FRXMI5JA7V3BNH5EJU:/var/lib/docker/overlay2/l/GT6IS2T6GALJ5ZBDGO2G4D7TIF:/var/lib/docker/overlay2/l/P76X6VWGZMEBIO7NGYAHNIXMDB:/var/lib/docker/overlay2/l/FTHT2CBTEAEV5Z4MP4CNG7CN65:/var/lib/docker/overlay2/l/ZUBH2KNPRTXTLHDFFB7YJORT5U:/var/lib/docker/overlay2/l/WDQKQLSIVB62DJVBYQMHX4TQ3B:/var/lib/docker/overlay2/l/MB3CSXG5VRWZEQN6TRXTEXHMB2:/var/lib/do'
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] Reading the adapter's YAML configuration file /home/[secure]/Data/Input/[secure]-adapter-config.yml...
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Checking the adapter's YAML configuration file...
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   participant : Outer-Fluid
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   [secure]-config-file : [secure]-config.xml
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   interfaces : 
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Outer-Fluid-to-Solid
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceCenters
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 0
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       interface
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     write-data : 
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Sink-Temperature-Outer-Fluid
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Heat-Transfer-Coefficient-Outer-Fluid
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     read-data : 
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Sink-Temperature-Solid
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Heat-Transfer-Coefficient-Solid
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     subcycling : 1
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     prevent early exit : 1
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     evaluate boundaries : 1
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     disable checkpointing : 0
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     CHT module enabled : 1
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     FSI module enabled : 0
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Configuring the CHT module...
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     user-defined solver type : none
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     temperature field name : T
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     transportProperties name : transportProperties
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     conductivity name for basic solvers : k
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     density name for incompressible solvers : rho
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     heat capacity name for incompressible solvers : Cp
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     Prandtl number name for incompressible solvers : Pr
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     Turbulent thermal diffusivity field name for incompressible solvers : alphat
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Determining the solver type...
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Did not find the transportProperties dictionary.
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Found the turbulenceProperties dictionary.
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Found the thermophysicalProperties dictionary.
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] This is a compressible flow solver, as turbulence and thermophysical properties are provided.
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Checking the timestep type (fixed vs adjustable)...
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   Timestep type: fixed.
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Creating the preCICE solver interface...
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   Number of processes: 1
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   MPI rank: 0
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   preCICE solver interface was created.
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Configuring preCICE...
[32mopenfoam-adapter-outer    |[0m (0) 14:06:38 [xml::XMLTag]:163 in readAttributes: [31mERROR: [0mWrong attribute "distribution-type"
[33mopenfoam-adapter-inner exited with code 255
[0m[35mcalculix-adapter-solid exited with code 255
[0m[32mopenfoam-adapter-outer exited with code 255
[0mOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Inner-Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Outer-Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Inner-Fluid', 'Outer-Fluid']
Files only in output(right)   : []
travis_time:end:0ea20568:start=1578665040959263094,finish=1578665204449307440,duration=163490044346,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1d8ab56c[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635276416/log.txt)