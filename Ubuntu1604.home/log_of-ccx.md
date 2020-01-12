## Status: Failure 
Build: [1442](https://travis-ci.org/precice/systemtests/builds/635918218) 

Job: [1442.3](https://travis-ci.org/precice/systemtests/jobs/635918221) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/152) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
[33mopenfoam-adapter-outer    |[0m Reading hRef
[33mopenfoam-adapter-outer    |[0m Calculating field g.h
[33mopenfoam-adapter-outer    |[0m 
[33mopenfoam-adapter-outer    |[0m Reading field p_rgh
[33mopenfoam-adapter-outer    |[0m 
[33mopenfoam-adapter-outer    |[0m No MRF models present
[33mopenfoam-adapter-outer    |[0m 
[33mopenfoam-adapter-outer    |[0m Selecting radiationModel none
[33mopenfoam-adapter-outer    |[0m Creating finite volume options from "system/fvOptions"
[33mopenfoam-adapter-outer    |[0m 
[33mopenfoam-adapter-outer    |[0m 
[33mopenfoam-adapter-outer    |[0m Starting time loop
[33mopenfoam-adapter-outer    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[[secure]Adapter] The [secure]Adapter was loaded.
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
[33mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/4XI3ZFSUQOCLJW25WCVE6PQPBU:/var/lib/docker/overlay2/l/GCVJ6XLMZ74CSDEABQTHEHXAT6:/var/lib/docker/overlay2/l/DSP7PC27EXQHSMIT4WJPJQTISL:/var/lib/docker/overlay2/l/BAC4JOK2WTLESFK6QIUHSDILIZ:/var/lib/docker/overlay2/l/ZMKCZUPFZTUTT2FP5Q4UP53VH7:/var/lib/docker/overlay2/l/DCWXA4JADCQIV4X4CB7TRBDOWG:/var/lib/docker/overlay2/l/3VKI4I5LZVBYO5G267UTOPXD6J:/var/lib/docker/overlay2/l/AKSNSDXA65XFLPQXELB63D24WT:/var/lib/docker/overlay2/l/B4Q2IRNGHUMRS'
[33mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `IYWA54KTABMD7:/var/lib/docker/overlay2/l/EPKEGWLNHK4KU6KTOQIY7BCK7A:/var/lib/docker/overlay2/l/HHRPD75KGCMVXHEZNQZXDT7CPU:/var/lib/docker/overlay2/l/G5QANTVX4VJS54QH2FZ2JQE723:/var/lib/docker/overlay2/l/ZWDPOSQKE4VH3LP24O3PIEVWOP:/var/lib/docker/overlay2/l/GCHVW2XU2YKYC46F7KWYNEVONI:/var/lib/docker/overlay2/l/VEHGEVUFFNU4WP7RH7RT2AGJ5X:/var/lib/docker/overlay2/l/G3CCZV5MSLSJ3SUVI2CLZWQ23O:/var/lib/docker/overlay2/l/SJSK2I2CDVG22GOFDJF3U6UD6K:/var/lib/docker/overlay2/l/3KKT5VPITEWWOHCHIMKR4JMZ3F:/var/lib/do'
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
[33mopenfoam-adapter-outer    |[0m (0) 09:49:57 [xml::XMLTag]:163 in readAttributes: [31mERROR: [0mWrong attribute "distribution-type"
[35mopenfoam-adapter-inner exited with code 255
[0m[32mcalculix-adapter-solid exited with code 255
[0m[33mopenfoam-adapter-outer exited with code 255
[0m
```
[
Full job log](https://api.travis-ci.org/v3/job/635918221/log.txt)