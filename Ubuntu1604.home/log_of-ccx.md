## Status: Failure 
Build: [1438](https://travis-ci.org/precice/systemtests/builds/635907468) 

Job: [1438.3](https://travis-ci.org/precice/systemtests/jobs/635907471) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/150) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
[32mopenfoam-adapter-outer    |[0m Reading hRef
[32mopenfoam-adapter-outer    |[0m Calculating field g.h
[32mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-outer    |[0m Reading field p_rgh
[32mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-outer    |[0m No MRF models present
[32mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-outer    |[0m Selecting radiationModel none
[32mopenfoam-adapter-outer    |[0m Creating finite volume options from "system/fvOptions"
[32mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-outer    |[0m Starting time loop
[32mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] The [secure]Adapter was loaded.
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
[32mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/ZIOQAMJJUL27PETBJIKTCOTRFA:/var/lib/docker/overlay2/l/WDSLK4K4IWIZSWFUABAJTMCH2Q:/var/lib/docker/overlay2/l/QKMM3GOUIFEH4IO3CYIUDRGELW:/var/lib/docker/overlay2/l/CYKC7QMKSVQJTSCB3Q7SGH6YEK:/var/lib/docker/overlay2/l/DWKBVYA5PPHNKX2OMTBP5GV5WA:/var/lib/docker/overlay2/l/5VZKEVRGPT7JCJC7TKGB5WDDD6:/var/lib/docker/overlay2/l/DR7NA2PZJMBRZL4X3T75N5JC2R:/var/lib/docker/overlay2/l/KW525TNDXEPXWFRHGIPGCI3HZC:/var/lib/docker/overlay2/l/CICJV3OVL2QOM'
[32mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `DYGLFSSKDBA26:/var/lib/docker/overlay2/l/IBBMVOLVPPXLTRUPNT7V6ERLIU:/var/lib/docker/overlay2/l/AUQS2NT3JEMDW3PR44PJA7EORL:/var/lib/docker/overlay2/l/XZZ2RT6QB7FEHWE6NAEMEASV4I:/var/lib/docker/overlay2/l/QCJ5IN76BGWHNLMP2UM4XR4KIG:/var/lib/docker/overlay2/l/YUGH7SRCYPGQX3TUT7R2I2HYVT:/var/lib/docker/overlay2/l/SSC65ICK5H2CEXKEBKCZDWH7UJ:/var/lib/docker/overlay2/l/HP7BZLYPC6MOH75UIAPWRLQ3GN:/var/lib/docker/overlay2/l/7MW5OWDPEOU446B2MU45CVAJIJ:/var/lib/docker/overlay2/l/4UCYF3ZHGNU7VT62VRT7PQ5ZYA:/var/lib/do'
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
[32mopenfoam-adapter-outer    |[0m (0) 08:41:28 [xml::XMLTag]:163 in readAttributes: [31mERROR: [0mWrong attribute "distribution-type"
[33mopenfoam-adapter-inner exited with code 255
[0m[35mcalculix-adapter-solid exited with code 255
[0m[32mopenfoam-adapter-outer exited with code 255
[0m
```
[
Full job log](https://api.travis-ci.org/v3/job/635907471/log.txt)