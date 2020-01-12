## Status: Failure 
Build: [1439](https://travis-ci.org/precice/systemtests/builds/635909108) 

Job: [1439.3](https://travis-ci.org/precice/systemtests/jobs/635909111) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/148) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
[32mopenfoam-adapter-outer    |[0m 
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
[32mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/RCF5AVLRSUGPKUKHGWFD3TOK64:/var/lib/docker/overlay2/l/2P3ODHW3SNK22PI7OP2C7UX34L:/var/lib/docker/overlay2/l/MCVK5DRW4QUGSJ2SRTDKE5YNT7:/var/lib/docker/overlay2/l/SIVLK3HDOHZHZ5MFDN3L4JKCHX:/var/lib/docker/overlay2/l/AWWS4UTJGTFAX3CSPM6TBQEBOY:/var/lib/docker/overlay2/l/HJJRPQS2YX7SW3ZJ2VLTDKWWRU:/var/lib/docker/overlay2/l/TPHL3FV4TM63VL5E3MRIF64XMF:/var/lib/docker/overlay2/l/L6ZGQD7ITX7RUKWUDGIEHHVSLV:/var/lib/docker/overlay2/l/XMFK4PUJR6BUO'
[32mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `3MTOAQGXV2EM4:/var/lib/docker/overlay2/l/Q75A64GX6WFVSNVQ5KPBJ3UKAJ:/var/lib/docker/overlay2/l/46AQDGGJSEOKYFFT3BCMJ34MN2:/var/lib/docker/overlay2/l/4X35FCFGXG6QRYK7XU2HFXOR3Q:/var/lib/docker/overlay2/l/TXOQGHYK2HDTPH2PLPXHRWJOZR:/var/lib/docker/overlay2/l/ZKMWKIWQQVGVKKUSJYP2UA3LOG:/var/lib/docker/overlay2/l/74SPVA6O56W5NEUH33YAKDBDYY:/var/lib/docker/overlay2/l/LFBFY3HO3MWTCLUQ7GHX3ODNZD:/var/lib/docker/overlay2/l/ZP2VV72FQ6T6CIY2ABUVNYS5ZX:/var/lib/docker/overlay2/l/ANJIFEEXXWZF7H4LCBI7XWEX6H:/var/lib/do'
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
[32mopenfoam-adapter-outer    |[0m (0) 08:54:14 [xml::XMLTag]:163 in readAttributes: [31mERROR: [0mWrong attribute "distribution-type"
[33mopenfoam-adapter-inner exited with code 255
[0m[35mcalculix-adapter-solid exited with code 255
[0m
```
[
Full job log](https://api.travis-ci.org/v3/job/635909111/log.txt)