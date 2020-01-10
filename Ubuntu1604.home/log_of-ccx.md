## Status: Failure 
Build: [1431](https://travis-ci.org/precice/systemtests/builds/635347829) 

Job: [1431.3](https://travis-ci.org/precice/systemtests/jobs/635347832) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/150) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[33mopenfoam-adapter-outer    |[0m Registered objects: 
[33mopenfoam-adapter-outer    |[0m 31
[33mopenfoam-adapter-outer    |[0m (
[33mopenfoam-adapter-outer    |[0m points
[33mopenfoam-adapter-outer    |[0m neighbour
[33mopenfoam-adapter-outer    |[0m thermo:mu
[33mopenfoam-adapter-outer    |[0m MRFProperties
[33mopenfoam-adapter-outer    |[0m thermo:psi
[33mopenfoam-adapter-outer    |[0m ghf
[33mopenfoam-adapter-outer    |[0m h
[33mopenfoam-adapter-outer    |[0m faces
[33mopenfoam-adapter-outer    |[0m U
[33mopenfoam-adapter-outer    |[0m rho
[33mopenfoam-adapter-outer    |[0m radiationProperties
[33mopenfoam-adapter-outer    |[0m turbulenceProperties
[33mopenfoam-adapter-outer    |[0m fvSchemes
[33mopenfoam-adapter-outer    |[0m fvOptions
[33mopenfoam-adapter-outer    |[0m faceZones
[33mopenfoam-adapter-outer    |[0m fvSolution
[33mopenfoam-adapter-outer    |[0m p_rgh
[33mopenfoam-adapter-outer    |[0m thermophysicalProperties
[33mopenfoam-adapter-outer    |[0m phi
[33mopenfoam-adapter-outer    |[0m owner
[33mopenfoam-adapter-outer    |[0m gh
[33mopenfoam-adapter-outer    |[0m data
[33mopenfoam-adapter-outer    |[0m cellZones
[33mopenfoam-adapter-outer    |[0m boundary
[33mopenfoam-adapter-outer    |[0m g
[33mopenfoam-adapter-outer    |[0m p
[33mopenfoam-adapter-outer    |[0m T
[33mopenfoam-adapter-outer    |[0m hRef
[33mopenfoam-adapter-outer    |[0m thermo:rho
[33mopenfoam-adapter-outer    |[0m pointZones
[33mopenfoam-adapter-outer    |[0m thermo:alpha
[33mopenfoam-adapter-outer    |[0m )
[33mopenfoam-adapter-outer    |[0m 
[33mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/VQM3NAYKIOWJZSNJTKDUJRDVLJ:/var/lib/docker/overlay2/l/MQCPLTIDCF2GW2VGGPQSUYMRGR:/var/lib/docker/overlay2/l/U653V55V5S5SCSAFGMOLP7VTVI:/var/lib/docker/overlay2/l/YM3NSIDLV6HYWPXVW2VPS327PS:/var/lib/docker/overlay2/l/IXZRJNDNL45DYTCF4AUWJIABUA:/var/lib/docker/overlay2/l/NGX7HZX4UZR23KYE6UHFMSSCC5:/var/lib/docker/overlay2/l/JBN4C3PC3UJZPQGKD6MGRGKZJC:/var/lib/docker/overlay2/l/TN3KL66JJLPQHKE6GEIWVOJ4XF:/var/lib/docker/overlay2/l/VNBWVCMI5IWWK'
[33mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `O3QWLQQX6DVKC:/var/lib/docker/overlay2/l/NHIDABVX7MZS6ZHIUIOCK5W2R3:/var/lib/docker/overlay2/l/XSHQKKFNAFK53YU43S3UBXP6DK:/var/lib/docker/overlay2/l/PVUTKLGZPECQPG7IDCL2TMPEWZ:/var/lib/docker/overlay2/l/RB2HVW7CU3JRBU4AQSH32TZ3GR:/var/lib/docker/overlay2/l/ZDCJPAZUJFA4QYP3MD6K3GH6G3:/var/lib/docker/overlay2/l/ZC3LXNIVTK2UFXCY332GNON52G:/var/lib/docker/overlay2/l/MPQEKUJXSXOI5OINDOEMIC4FVJ:/var/lib/docker/overlay2/l/YUHHWDKPVHAA4WCMIXZAGGKNUL:/var/lib/docker/overlay2/l/EGR2Q7DOWUZCEK25YAMAAEHA5Z:/var/lib/do'
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] Reading the adapter's YAML configuration file /home/[secure]/Data/Input/[secure]-adapter-config.yml...
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Checking the adapter's YAML configuration file...
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   participant : Outer-Fluid
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   [secure]-config-file : [secure]-config.xml
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   interfaces : 
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Outer-Fluid-to-Solid
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceCenters
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 0
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       interface
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     write-data : 
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Sink-Temperature-Outer-Fluid
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Heat-Transfer-Coefficient-Outer-Fluid
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     read-data : 
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Sink-Temperature-Solid
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]       Heat-Transfer-Coefficient-Solid
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     subcycling : 1
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     prevent early exit : 1
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     evaluate boundaries : 1
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     disable checkpointing : 0
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     CHT module enabled : 1
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     FSI module enabled : 0
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Configuring the CHT module...
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     user-defined solver type : none
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     temperature field name : T
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     transportProperties name : transportProperties
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     conductivity name for basic solvers : k
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     density name for incompressible solvers : rho
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     heat capacity name for incompressible solvers : Cp
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     Prandtl number name for incompressible solvers : Pr
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]     Turbulent thermal diffusivity field name for incompressible solvers : alphat
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Determining the solver type...
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Did not find the transportProperties dictionary.
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Found the turbulenceProperties dictionary.
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Found the thermophysicalProperties dictionary.
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] This is a compressible flow solver, as turbulence and thermophysical properties are provided.
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Checking the timestep type (fixed vs adjustable)...
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   Timestep type: fixed.
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Creating the preCICE solver interface...
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   Number of processes: 1
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   MPI rank: 0
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG]   preCICE solver interface was created.
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] [DEBUG] Configuring preCICE...
[33mopenfoam-adapter-outer    |[0m (0) 16:38:51 [xml::XMLTag]:163 in readAttributes: [31mERROR: [0mWrong attribute "distribution-type"
[35mcalculix-adapter-solid exited with code 255
[0m[33mopenfoam-adapter-outer exited with code 255
[0m[32mopenfoam-adapter-inner exited with code 255
[0mOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Inner-Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Outer-Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Outer-Fluid', 'Inner-Fluid']
Files only in output(right)   : []
travis_time:end:022ce303:start=1578674174882201580,finish=1578674337964428915,duration=163082227335,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:10514be4[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635347832/log.txt)