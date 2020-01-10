## Status: Failure 
Build: [1422](https://travis-ci.org/precice/systemtests/builds/635287877) 

Job: [1422.8](https://travis-ci.org/precice/systemtests/jobs/635287885) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/148) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
[33mopenfoam-adapter-fluid    |[0m points
[33mopenfoam-adapter-fluid    |[0m neighbour
[33mopenfoam-adapter-fluid    |[0m thermo:mu
[33mopenfoam-adapter-fluid    |[0m MRFProperties
[33mopenfoam-adapter-fluid    |[0m thermo:psi
[33mopenfoam-adapter-fluid    |[0m K
[33mopenfoam-adapter-fluid    |[0m ghf
[33mopenfoam-adapter-fluid    |[0m h
[33mopenfoam-adapter-fluid    |[0m faces
[33mopenfoam-adapter-fluid    |[0m U
[33mopenfoam-adapter-fluid    |[0m rho
[33mopenfoam-adapter-fluid    |[0m radiationProperties
[33mopenfoam-adapter-fluid    |[0m turbulenceProperties
[33mopenfoam-adapter-fluid    |[0m fvSchemes
[33mopenfoam-adapter-fluid    |[0m fvOptions
[33mopenfoam-adapter-fluid    |[0m faceZones
[33mopenfoam-adapter-fluid    |[0m fvSolution
[33mopenfoam-adapter-fluid    |[0m p_rgh
[33mopenfoam-adapter-fluid    |[0m thermophysicalProperties
[33mopenfoam-adapter-fluid    |[0m dpdt
[33mopenfoam-adapter-fluid    |[0m phi
[33mopenfoam-adapter-fluid    |[0m owner
[33mopenfoam-adapter-fluid    |[0m gh
[33mopenfoam-adapter-fluid    |[0m data
[33mopenfoam-adapter-fluid    |[0m cellZones
[33mopenfoam-adapter-fluid    |[0m boundary
[33mopenfoam-adapter-fluid    |[0m g
[33mopenfoam-adapter-fluid    |[0m p
[33mopenfoam-adapter-fluid    |[0m T
[33mopenfoam-adapter-fluid    |[0m hRef
[33mopenfoam-adapter-fluid    |[0m thermo:rho
[33mopenfoam-adapter-fluid    |[0m pointZones
[33mopenfoam-adapter-fluid    |[0m thermo:alpha
[33mopenfoam-adapter-fluid    |[0m )
[33mopenfoam-adapter-fluid    |[0m 
[33mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/RFNMC7LWPN67DZDXLUVGYLCG3L:/var/lib/docker/overlay2/l/2ZJOK7KMI6OWAK3GCEBDGX2YYR:/var/lib/docker/overlay2/l/RMJLXOTMV4M4ASNVI2AGL66ATT:/var/lib/docker/overlay2/l/27YB3QVQIIUQJTX7WT3LXSXYSP:/var/lib/docker/overlay2/l/Y2YHZB4RUW37AOGSP7JF6FAEFD:/var/lib/docker/overlay2/l/ET6A6BWOVWIZEKJV2OEWIQMSFE:/var/lib/docker/overlay2/l/DHZHLBWSXWPQ36M43T56PHGGM3:/var/lib/docker/overlay2/l/IEJZEPTWJWYEOPWADVOL7ZZSV4:/var/lib/docker/overlay2/l/A6CXHZ6DAJUAU'
[33mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `IAET4SCBUZNST:/var/lib/docker/overlay2/l/HYAF6NXZQZTAA3PTJN4E5ZRUY6:/var/lib/docker/overlay2/l/7ISP7UBTD2RY4ATIZ4PVNJV3TT:/var/lib/docker/overlay2/l/32SGFFI7OIT4HZOG5VXDIIMDLM:/var/lib/docker/overlay2/l/MOWLL2JDRJBLGSCUIJTER37CVD:/var/lib/docker/overlay2/l/747QQ5477TZQZ7LJHXXBWKRGFS:/var/lib/docker/overlay2/l/PNE7PBDZ5SFVM64BRSFBUEG42C:/var/lib/docker/overlay2/l/VTAWWKC4T65U7CFFU7STCGPC5Y:/var/lib/docker/overlay2/l/YRYQ5DXIOCUQ2EBXTXPRN66PVH:/var/lib/docker/overlay2/l/2FMLG2CE5F4HYVBZ7PE4CCYDSJ:/var/lib/do'
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] Reading the adapter's YAML configuration file ./Fluid/[secure]-adapter-config.yml...
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Checking the adapter's YAML configuration file...
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   participant : Fluid
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   [secure]-config-file : [secure]-config.xml
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   interfaces : 
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Fluid-Mesh-Centers
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceCenters
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 0
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       interface
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     read-data : 
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       Heat-Flux
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Fluid-Mesh-Nodes
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceNodes
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 1
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       interface
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     write-data : 
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       Temperature
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     subcycling : 1
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     prevent early exit : 1
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     evaluate boundaries : 1
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     disable checkpointing : 0
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     CHT module enabled : 1
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     FSI module enabled : 0
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Configuring the CHT module...
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     user-defined solver type : none
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     temperature field name : T
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     transportProperties name : transportProperties
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     conductivity name for basic solvers : k
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     density name for incompressible solvers : rho
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     heat capacity name for incompressible solvers : Cp
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Prandtl number name for incompressible solvers : Pr
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Turbulent thermal diffusivity field name for incompressible solvers : alphat
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Determining the solver type...
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Did not find the transportProperties dictionary.
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Found the turbulenceProperties dictionary.
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Found the thermophysicalProperties dictionary.
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] This is a compressible flow solver, as turbulence and thermophysical properties are provided.
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Checking the timestep type (fixed vs adjustable)...
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   Timestep type: fixed.
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Creating the preCICE solver interface...
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   Number of processes: 1
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   MPI rank: 0
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   preCICE solver interface was created.
[33mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Configuring preCICE...
[33mopenfoam-adapter-fluid    |[0m ---[[secure]] [31mERROR: [0m Wrong attribute "distribution-type"
[33mopenfoam-adapter-fluid exited with code 255
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
travis_time:end:134e159b:start=1578666911462798990,finish=1578666977623981358,duration=66161182368,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:00691aea[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635287885/log.txt)