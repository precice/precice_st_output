Attaching to calculix-adapter-solid, openfoam-adapter-outer, openfoam-adapter-inner, tutorial-data
[33mopenfoam-adapter-outer    |[0m /*---------------------------------------------------------------------------*\
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m | =========                 |                                                 |
[36mcalculix-adapter-solid    |[0m ************************************************************
[33mopenfoam-adapter-outer    |[0m | \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
[32mopenfoam-adapter-inner    |[0m /*---------------------------------------------------------------------------*\
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m CalculiX Version 2.15, Copyright(C) 1998-2018 Guido Dhondt
[36mcalculix-adapter-solid    |[0m CalculiX comes with ABSOLUTELY NO WARRANTY. This is free
[32mopenfoam-adapter-inner    |[0m | =========                 |                                                 |
[32mopenfoam-adapter-inner    |[0m | \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
[32mopenfoam-adapter-inner    |[0m |  \\    /   O peration     | Version:  4.1                                   |
[32mopenfoam-adapter-inner    |[0m |   \\  /    A nd           | Web:      www.OpenFOAM.org                      |
[33mopenfoam-adapter-outer    |[0m |  \\    /   O peration     | Version:  4.1                                   |
[32mopenfoam-adapter-inner    |[0m |    \\/     M anipulation  |                                                 |
[36mcalculix-adapter-solid    |[0m software, and you are welcome to redistribute it under
[36mcalculix-adapter-solid    |[0m certain conditions, see gpl.htm
[33mopenfoam-adapter-outer    |[0m |   \\  /    A nd           | Web:      www.OpenFOAM.org                      |
[33mopenfoam-adapter-outer    |[0m |    \\/     M anipulation  |                                                 |
[33mopenfoam-adapter-outer    |[0m \*---------------------------------------------------------------------------*/
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m Build  : 4.1
[33mopenfoam-adapter-outer    |[0m Exec   : buoyantSimpleFoam -case /home/precice/Data/Input
[36mcalculix-adapter-solid    |[0m ************************************************************
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m You are using an executable made on Sa 15. Dez 15:34:34 CET 2018
[33mopenfoam-adapter-outer    |[0m Date   : Jan 25 2020
[32mopenfoam-adapter-inner    |[0m \*---------------------------------------------------------------------------*/
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m Time   : 10:27:46
[32mopenfoam-adapter-inner    |[0m Build  : 4.1
[36mcalculix-adapter-solid    |[0m   The numbers below are estimated upper bounds
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m Exec   : buoyantSimpleFoam -case /home/precice/Data/Input
[36mcalculix-adapter-solid    |[0m   number of:
[33mopenfoam-adapter-outer    |[0m Host   : "d6efec35f042"
[32mopenfoam-adapter-inner    |[0m Date   : Jan 25 2020
[32mopenfoam-adapter-inner    |[0m Time   : 10:27:46
[32mopenfoam-adapter-inner    |[0m Host   : "2f7fa3804bea"
[32mopenfoam-adapter-inner    |[0m PID    : 161
[32mopenfoam-adapter-inner    |[0m Case   : /home/precice/Data/Input
[32mopenfoam-adapter-inner    |[0m nProcs : 1
[32mopenfoam-adapter-inner    |[0m sigFpe : Enabling floating point exception trapping (FOAM_SIGFPE).
[32mopenfoam-adapter-inner    |[0m fileModificationChecking : Monitoring run-time modified files using timeStampMaster
[32mopenfoam-adapter-inner    |[0m allowSystemOperations : Allowing user-supplied system call operations
[32mopenfoam-adapter-inner    |[0m 
[32mopenfoam-adapter-inner    |[0m // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
[32mopenfoam-adapter-inner    |[0m Create time
[32mopenfoam-adapter-inner    |[0m 
[32mopenfoam-adapter-inner    |[0m Create mesh for time = 0
[32mopenfoam-adapter-inner    |[0m 
[32mopenfoam-adapter-inner    |[0m 
[32mopenfoam-adapter-inner    |[0m SIMPLE: no convergence criteria found. Calculations will run for 5 steps.
[32mopenfoam-adapter-inner    |[0m 
[32mopenfoam-adapter-inner    |[0m Reading thermophysical properties
[32mopenfoam-adapter-inner    |[0m 
[32mopenfoam-adapter-inner    |[0m Selecting thermodynamics package 
[32mopenfoam-adapter-inner    |[0m {
[33mopenfoam-adapter-outer    |[0m PID    : 168
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m Case   : /home/precice/Data/Input
[32mopenfoam-adapter-inner    |[0m     type            heRhoThermo;
[36mcalculix-adapter-solid    |[0m    nodes:        21153
[33mopenfoam-adapter-outer    |[0m nProcs : 1
[32mopenfoam-adapter-inner    |[0m     mixture         pureMixture;
[36mcalculix-adapter-solid    |[0m    elements:       106550
[33mopenfoam-adapter-outer    |[0m sigFpe : Enabling floating point exception trapping (FOAM_SIGFPE).
[32mopenfoam-adapter-inner    |[0m     transport       const;
[36mcalculix-adapter-solid    |[0m    one-dimensional elements:            0
[33mopenfoam-adapter-outer    |[0m fileModificationChecking : Monitoring run-time modified files using timeStampMaster
[32mopenfoam-adapter-inner    |[0m     thermo          hConst;
[36mcalculix-adapter-solid    |[0m    two-dimensional elements:            0
[32mopenfoam-adapter-inner    |[0m     equationOfState perfectFluid;
[33mopenfoam-adapter-outer    |[0m allowSystemOperations : Allowing user-supplied system call operations
[36mcalculix-adapter-solid    |[0m    integration points per element:            1
[32mopenfoam-adapter-inner    |[0m     specie          specie;
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m     energy          sensibleEnthalpy;
[36mcalculix-adapter-solid    |[0m    degrees of freedom per node:            3
[33mopenfoam-adapter-outer    |[0m // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
[32mopenfoam-adapter-inner    |[0m }
[36mcalculix-adapter-solid    |[0m    layers per element:            1
[33mopenfoam-adapter-outer    |[0m Create time
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m    distributed facial loads:        42172
[32mopenfoam-adapter-inner    |[0m Reading field U
[36mcalculix-adapter-solid    |[0m    distributed volumetric loads:            0
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m 
[32mopenfoam-adapter-inner    |[0m Reading/calculating face flux field phi
[33mopenfoam-adapter-outer    |[0m Create mesh for time = 0
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m    concentrated loads:            0
[33mopenfoam-adapter-outer    |[0m 
[33mopenfoam-adapter-outer    |[0m 
[36mcalculix-adapter-solid    |[0m    single point constraints:            0
[32mopenfoam-adapter-inner    |[0m Creating turbulence model
[36mcalculix-adapter-solid    |[0m    multiple point constraints:            1
[33mopenfoam-adapter-outer    |[0m SIMPLE: no convergence criteria found. Calculations will run for 5 steps.
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m    terms in all multiple point constraints:            1
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m Selecting turbulence model type laminar
[33mopenfoam-adapter-outer    |[0m Reading thermophysical properties
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m    tie constraints:            0
[33mopenfoam-adapter-outer    |[0m 
[36mcalculix-adapter-solid    |[0m    dependent nodes tied by cyclic constraints:            0
[32mopenfoam-adapter-inner    |[0m Reading g
[33mopenfoam-adapter-outer    |[0m Selecting thermodynamics package 
[36mcalculix-adapter-solid    |[0m    dependent nodes in pre-tension constraints:            0
[32mopenfoam-adapter-inner    |[0m 
[33mopenfoam-adapter-outer    |[0m {
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m Reading hRef
[33mopenfoam-adapter-outer    |[0m     type            heRhoThermo;
[36mcalculix-adapter-solid    |[0m    sets:            6
[32mopenfoam-adapter-inner    |[0m Calculating field g.h
[33mopenfoam-adapter-outer    |[0m     mixture         pureMixture;
[36mcalculix-adapter-solid    |[0m    terms in all sets:       212183
[32mopenfoam-adapter-inner    |[0m 
[33mopenfoam-adapter-outer    |[0m     transport       const;
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m Reading field p_rgh
[33mopenfoam-adapter-outer    |[0m     thermo          hConst;
[36mcalculix-adapter-solid    |[0m    materials:            1
[32mopenfoam-adapter-inner    |[0m 
[33mopenfoam-adapter-outer    |[0m     equationOfState perfectFluid;
[32mopenfoam-adapter-inner    |[0m No MRF models present
[36mcalculix-adapter-solid    |[0m    constants per material and temperature:            0
[33mopenfoam-adapter-outer    |[0m     specie          specie;
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m    temperature points per material:            1
[33mopenfoam-adapter-outer    |[0m     energy          sensibleEnthalpy;
[32mopenfoam-adapter-inner    |[0m Selecting radiationModel none
[36mcalculix-adapter-solid    |[0m    plastic data points per material:            0
[33mopenfoam-adapter-outer    |[0m }
[32mopenfoam-adapter-inner    |[0m Creating finite volume options from "system/fvOptions"
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m    orientations:            0
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m    amplitudes:            3
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m    data points in all amplitudes:            3
[33mopenfoam-adapter-outer    |[0m Reading field U
[32mopenfoam-adapter-inner    |[0m Starting time loop
[36mcalculix-adapter-solid    |[0m    print requests:            0
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m    transformations:            0
[33mopenfoam-adapter-outer    |[0m Reading/calculating face flux field phi
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] The preciceAdapter was loaded.
[36mcalculix-adapter-solid    |[0m    property cards:            0
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m Registered objects: 
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m Creating turbulence model
[32mopenfoam-adapter-inner    |[0m 31
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m (
[36mcalculix-adapter-solid    |[0m  STEP            1
[33mopenfoam-adapter-outer    |[0m Selecting turbulence model type laminar
[32mopenfoam-adapter-inner    |[0m points
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m neighbour
[36mcalculix-adapter-solid    |[0m  Static analysis was selected
[33mopenfoam-adapter-outer    |[0m Reading g
[32mopenfoam-adapter-inner    |[0m thermo:mu
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m MRFProperties
[36mcalculix-adapter-solid    |[0m  Newton-Raphson iterative procedure is active
[33mopenfoam-adapter-outer    |[0m Reading hRef
[32mopenfoam-adapter-inner    |[0m thermo:psi
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Decascading the MPC's
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Determining the structure of the matrix:
[36mcalculix-adapter-solid    |[0m  number of equations
[36mcalculix-adapter-solid    |[0m  21153
[36mcalculix-adapter-solid    |[0m  number of nonzero lower triangular matrix elements
[33mopenfoam-adapter-outer    |[0m Calculating field g.h
[32mopenfoam-adapter-inner    |[0m ghf
[36mcalculix-adapter-solid    |[0m  106662
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m h
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m Reading field p_rgh
[32mopenfoam-adapter-inner    |[0m faces
[36mcalculix-adapter-solid    |[0m Starting CHT analysis via preCICE...
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m U
[36mcalculix-adapter-solid    |[0m About to enter preCICE setup in Calculix with names Solid and config.yml 
[33mopenfoam-adapter-outer    |[0m No MRF models present
[32mopenfoam-adapter-inner    |[0m rho
[32mopenfoam-adapter-inner    |[0m radiationProperties
[32mopenfoam-adapter-inner    |[0m turbulenceProperties
[32mopenfoam-adapter-inner    |[0m fvSchemes
[36mcalculix-adapter-solid    |[0m Setting up preCICE participant Solid, using config file: config.yml
[33mopenfoam-adapter-outer    |[0m 
[33mopenfoam-adapter-outer    |[0m Selecting radiationModel none
[33mopenfoam-adapter-outer    |[0m Creating finite volume options from "system/fvOptions"
[33mopenfoam-adapter-outer    |[0m 
[33mopenfoam-adapter-outer    |[0m 
[33mopenfoam-adapter-outer    |[0m Starting time loop
[33mopenfoam-adapter-outer    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] The preciceAdapter was loaded.
[33mopenfoam-adapter-outer    |[0m Registered objects: 
[36mcalculix-adapter-solid    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/5JFWTJLDFJ7O5ZTYTDG4Q4W2SG:/var/lib/docker/overlay2/l/TOR5TYA4GTEMJPCTVXYCYFFNBY:/var/lib/docker/overlay2/l/DALDKUTWBZKYIG4F7FCP5VDHG7:/var/lib/docker/overlay2/l/YNUI53Z34RGNFXZUUJSJMX3KKB:/var/lib/docker/overlay2/l/MIK37KSHQFV53NJNWQBDUNZYGK:/var/lib/docker/overlay2/l/IWP7XVMO7A6KK6ULKDGR5JQJMD:/var/lib/docker/overlay2/l/K45LVJZXVOYKBO3CMZV5BRST2S:/var/lib/docker/overlay2/l/ST4NBLEWUHILKQOHEATNMFDL6I:/var/lib/docker/overlay2/l/ZUZ2ZGHNYGDLQ'
[32mopenfoam-adapter-inner    |[0m fvOptions
[33mopenfoam-adapter-outer    |[0m 31
[36mcalculix-adapter-solid    |[0m Unexpected end of /proc/mounts line `5B3N7JFNWAYK7:/var/lib/docker/overlay2/l/PDBYYHHALY2PK4BMGLLCNHT3XL:/var/lib/docker/overlay2/l/T2U7NJGZUKFSEZRYVLDBPWZ3VA:/var/lib/docker/overlay2/l/EGIK7Q3MONZZJZTY2SR5HNRE43:/var/lib/docker/overlay2/l/JELMZFQ36XH2U4OVOOW6UEZKTG:/var/lib/docker/overlay2/l/QRDNJS5H62QXEV66FAN4K6IJEK:/var/lib/docker/overlay2/l/YZDBA5MUYK7VGT7BN6F2ZFPEHI:/var/lib/docker/overlay2/l/XU2UAZAGIIMLINJIEXLJ5EHVSJ:/var/lib/docker/overlay2/l/CZKBI3KFKX7I7MVJY3SVARGHAU:/var/lib/docker/overlay2/l/HV66XGKRMZ5YWOD4RYBWZMPEYI:/var/lib/do'
[32mopenfoam-adapter-inner    |[0m faceZones
[33mopenfoam-adapter-outer    |[0m (
[36mcalculix-adapter-solid    |[0m ---[precice] [0m This is preCICE version 1.6.1
[32mopenfoam-adapter-inner    |[0m fvSolution
[33mopenfoam-adapter-outer    |[0m points
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Revision info: v1.6.1-216-gc2df0a8
[32mopenfoam-adapter-inner    |[0m p_rgh
[33mopenfoam-adapter-outer    |[0m neighbour
[33mopenfoam-adapter-outer    |[0m thermo:mu
[32mopenfoam-adapter-inner    |[0m thermophysicalProperties
[33mopenfoam-adapter-outer    |[0m MRFProperties
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Configuring preCICE with configuration: "precice-config.xml"
[32mopenfoam-adapter-inner    |[0m phi
[32mopenfoam-adapter-inner    |[0m owner
[32mopenfoam-adapter-inner    |[0m gh
[32mopenfoam-adapter-inner    |[0m data
[32mopenfoam-adapter-inner    |[0m cellZones
[32mopenfoam-adapter-inner    |[0m boundary
[32mopenfoam-adapter-inner    |[0m g
[32mopenfoam-adapter-inner    |[0m p
[32mopenfoam-adapter-inner    |[0m T
[32mopenfoam-adapter-inner    |[0m hRef
[36mcalculix-adapter-solid    |[0m Set ID Found 
[32mopenfoam-adapter-inner    |[0m thermo:rho
[33mopenfoam-adapter-outer    |[0m thermo:psi
[36mcalculix-adapter-solid    |[0m Set ID Found 
[36mcalculix-adapter-solid    |[0m Setting node connectivity for nearest projection mapping: 
[33mopenfoam-adapter-outer    |[0m ghf
[32mopenfoam-adapter-inner    |[0m pointZones
[33mopenfoam-adapter-outer    |[0m h
[36mcalculix-adapter-solid    |[0m Read data 'Sink-Temperature-Inner-Fluid' found.
[32mopenfoam-adapter-inner    |[0m thermo:alpha
[33mopenfoam-adapter-outer    |[0m faces
[32mopenfoam-adapter-inner    |[0m )
[33mopenfoam-adapter-outer    |[0m U
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m Read data 'Heat-Transfer-Coefficient-Inner-Fluid' found.
[32mopenfoam-adapter-inner    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/EFLV4LURMBTEHJN6D2AZCFEI6K:/var/lib/docker/overlay2/l/F72ZT3EFCO3AQVQTYYK7KWO5ES:/var/lib/docker/overlay2/l/3R56N3ZLWKRZLFIPEO4HFDTC34:/var/lib/docker/overlay2/l/M4ZYKICOAZU4OC65BYAZO4YLJC:/var/lib/docker/overlay2/l/DTE4QLXMNZEUR2HYXCRHCRJYDO:/var/lib/docker/overlay2/l/BUSXKGYU7L7VTHZ4BSZKFOLZY6:/var/lib/docker/overlay2/l/PDBYYHHALY2PK4BMGLLCNHT3XL:/var/lib/docker/overlay2/l/T2U7NJGZUKFSEZRYVLDBPWZ3VA:/var/lib/docker/overlay2/l/EGIK7Q3MONZZJ'
[36mcalculix-adapter-solid    |[0m Write data 'Sink-Temperature-Solid' found.
[33mopenfoam-adapter-outer    |[0m rho
[32mopenfoam-adapter-inner    |[0m Unexpected end of /proc/mounts line `ZTY2SR5HNRE43:/var/lib/docker/overlay2/l/JELMZFQ36XH2U4OVOOW6UEZKTG:/var/lib/docker/overlay2/l/QRDNJS5H62QXEV66FAN4K6IJEK:/var/lib/docker/overlay2/l/YZDBA5MUYK7VGT7BN6F2ZFPEHI:/var/lib/docker/overlay2/l/XU2UAZAGIIMLINJIEXLJ5EHVSJ:/var/lib/docker/overlay2/l/CZKBI3KFKX7I7MVJY3SVARGHAU:/var/lib/docker/overlay2/l/HV66XGKRMZ5YWOD4RYBWZMPEYI:/var/lib/docker/overlay2/l/EUEXTNYIGV33IOYZTFEP6G6A2X:/var/lib/docker/overlay2/l/3RCAAIU4WDJAYI2FVYXID4SK26:/var/lib/docker/overlay2/l/NC7DVRAIYHXSQWEHWIMKZ4RMUV:/var/lib/do'
[36mcalculix-adapter-solid    |[0m Write data 'Heat-Transfer-Coefficient-Solid' found.
[33mopenfoam-adapter-outer    |[0m radiationProperties
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] Reading the adapter's YAML configuration file /home/precice/Data/Input/precice-adapter-config.yml...
[36mcalculix-adapter-solid    |[0m Set ID Found 
[33mopenfoam-adapter-outer    |[0m turbulenceProperties
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Checking the adapter's YAML configuration file...
[36mcalculix-adapter-solid    |[0m Set ID Found 
[33mopenfoam-adapter-outer    |[0m fvSchemes
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]   participant : Inner-Fluid
[36mcalculix-adapter-solid    |[0m Setting node connectivity for nearest projection mapping: 
[33mopenfoam-adapter-outer    |[0m fvOptions
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]   precice-config-file : precice-config.xml
[36mcalculix-adapter-solid    |[0m Read data 'Sink-Temperature-Outer-Fluid' found.
[33mopenfoam-adapter-outer    |[0m faceZones
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]   interfaces : 
[36mcalculix-adapter-solid    |[0m Read data 'Heat-Transfer-Coefficient-Outer-Fluid' found.
[33mopenfoam-adapter-outer    |[0m fvSolution
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]   - mesh      : Inner-Fluid-to-Solid
[36mcalculix-adapter-solid    |[0m Write data 'Sink-Temperature-Solid' found.
[33mopenfoam-adapter-outer    |[0m p_rgh
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     locations : faceCenters
[36mcalculix-adapter-solid    |[0m Write data 'Heat-Transfer-Coefficient-Solid' found.
[33mopenfoam-adapter-outer    |[0m thermophysicalProperties
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     Provide mesh connectivity : 0
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Setting up master communication to coupling partner/s
[33mopenfoam-adapter-outer    |[0m phi
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     patches   : 
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Masters are connected
[33mopenfoam-adapter-outer    |[0m owner
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]       interface
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Receive global mesh Inner-Fluid-to-Solid
[33mopenfoam-adapter-outer    |[0m gh
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     write-data : 
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Receive global mesh Outer-Fluid-to-Solid
[33mopenfoam-adapter-outer    |[0m data
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]       Sink-Temperature-Inner-Fluid
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Gather mesh Solid-to-Inner-Fluid
[33mopenfoam-adapter-outer    |[0m cellZones
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]       Heat-Transfer-Coefficient-Inner-Fluid
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Send global mesh Solid-to-Inner-Fluid
[33mopenfoam-adapter-outer    |[0m boundary
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     read-data : 
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Gather mesh Solid-to-Outer-Fluid
[33mopenfoam-adapter-outer    |[0m g
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]       Sink-Temperature-Solid
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Send global mesh Solid-to-Outer-Fluid
[33mopenfoam-adapter-outer    |[0m p
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]       Heat-Transfer-Coefficient-Solid
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Compute partition for mesh Solid-to-Inner-Fluid
[33mopenfoam-adapter-outer    |[0m T
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     subcycling : 1
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Compute partition for mesh Solid-to-Outer-Fluid
[33mopenfoam-adapter-outer    |[0m hRef
[33mopenfoam-adapter-outer    |[0m thermo:rho
[33mopenfoam-adapter-outer    |[0m pointZones
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     prevent early exit : 1
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Setting up slaves communication to coupling partner/s
[33mopenfoam-adapter-outer    |[0m thermo:alpha
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     evaluate boundaries : 1
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Slaves are connected
[33mopenfoam-adapter-outer    |[0m )
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     disable checkpointing : 0
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Inner-Fluid: it 1 of 1 | dt# 1 | t 0 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete no | write-initial-data | 
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     CHT module enabled : 1
[36mcalculix-adapter-solid    |[0m Outer-Fluid: it 1 of 1 | dt# 1 | t 0 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete no | write-initial-data | 
[33mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/D3SHYVKYYTJ3QZMH7O5AD3SMGN:/var/lib/docker/overlay2/l/F72ZT3EFCO3AQVQTYYK7KWO5ES:/var/lib/docker/overlay2/l/3R56N3ZLWKRZLFIPEO4HFDTC34:/var/lib/docker/overlay2/l/M4ZYKICOAZU4OC65BYAZO4YLJC:/var/lib/docker/overlay2/l/DTE4QLXMNZEUR2HYXCRHCRJYDO:/var/lib/docker/overlay2/l/BUSXKGYU7L7VTHZ4BSZKFOLZY6:/var/lib/docker/overlay2/l/PDBYYHHALY2PK4BMGLLCNHT3XL:/var/lib/docker/overlay2/l/T2U7NJGZUKFSEZRYVLDBPWZ3VA:/var/lib/docker/overlay2/l/EGIK7Q3MONZZJ'
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     FSI module enabled : 0
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Configuring the CHT module...
[33mopenfoam-adapter-outer    |[0m Unexpected end of /proc/mounts line `ZTY2SR5HNRE43:/var/lib/docker/overlay2/l/JELMZFQ36XH2U4OVOOW6UEZKTG:/var/lib/docker/overlay2/l/QRDNJS5H62QXEV66FAN4K6IJEK:/var/lib/docker/overlay2/l/YZDBA5MUYK7VGT7BN6F2ZFPEHI:/var/lib/docker/overlay2/l/XU2UAZAGIIMLINJIEXLJ5EHVSJ:/var/lib/docker/overlay2/l/CZKBI3KFKX7I7MVJY3SVARGHAU:/var/lib/docker/overlay2/l/HV66XGKRMZ5YWOD4RYBWZMPEYI:/var/lib/docker/overlay2/l/EUEXTNYIGV33IOYZTFEP6G6A2X:/var/lib/docker/overlay2/l/3RCAAIU4WDJAYI2FVYXID4SK26:/var/lib/docker/overlay2/l/NC7DVRAIYHXSQWEHWIMKZ4RMUV:/var/lib/do'
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     user-defined solver type : none
[36mcalculix-adapter-solid    |[0m Initializing coupling data
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] Reading the adapter's YAML configuration file /home/precice/Data/Input/precice-adapter-config.yml...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     temperature field name : T
[36mcalculix-adapter-solid    |[0m Adapter writing coupling data...
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Checking the adapter's YAML configuration file...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     transportProperties name : transportProperties
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Compute read mapping from mesh "Inner-Fluid-to-Solid" to mesh "Solid-to-Inner-Fluid".
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]   participant : Outer-Fluid
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     conductivity name for basic solvers : k
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Mapping distance min:0.000430952 max:0.0192511 avg: 0.00878207 var: 1.06099e-05 cnt: 17226
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]   precice-config-file : precice-config.xml
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     density name for incompressible solvers : rho
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Compute read mapping from mesh "Outer-Fluid-to-Solid" to mesh "Solid-to-Outer-Fluid".
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]   interfaces : 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]   - mesh      : Outer-Fluid-to-Solid
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Mapping distance min:0.000112137 max:0.0196877 avg: 0.00852088 var: 9.49287e-06 cnt: 24176
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     locations : faceCenters
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     Provide mesh connectivity : 0
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     patches   : 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     heat capacity name for incompressible solvers : Cp
[36mcalculix-adapter-solid    |[0m Adapter reading coupling data...
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]       interface
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     Prandtl number name for incompressible solvers : Pr
[36mcalculix-adapter-solid    |[0m Adjusting time step for steady-state step
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     write-data : 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]     Turbulent thermal diffusivity field name for incompressible solvers : alphat
[36mcalculix-adapter-solid    |[0m Adapter reading coupling data...
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]       Sink-Temperature-Outer-Fluid
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Determining the solver type...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Did not find the transportProperties dictionary.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]       Heat-Transfer-Coefficient-Outer-Fluid
[36mcalculix-adapter-solid    |[0m  increment 1 attempt 1 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Found the turbulenceProperties dictionary.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     read-data : 
[36mcalculix-adapter-solid    |[0m  increment size= 1.000000e+00
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Found the thermophysicalProperties dictionary.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]       Sink-Temperature-Solid
[36mcalculix-adapter-solid    |[0m  sum of previous increments=0.000000e+00
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] This is a compressible flow solver, as turbulence and thermophysical properties are provided.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]       Heat-Transfer-Coefficient-Solid
[36mcalculix-adapter-solid    |[0m  actual step time=1.000000e+00
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Checking the timestep type (fixed vs adjustable)...
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     subcycling : 1
[36mcalculix-adapter-solid    |[0m  actual total time=1.000000e+00
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]   Timestep type: fixed.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     prevent early exit : 1
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Creating the preCICE solver interface...
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     evaluate boundaries : 1
[36mcalculix-adapter-solid    |[0m  iteration 1
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]   Number of processes: 1
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     disable checkpointing : 0
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]   MPI rank: 0
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     CHT module enabled : 1
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]   preCICE solver interface was created.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     FSI module enabled : 0
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Configuring preCICE...
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Configuring the CHT module...
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the symmetric stiffness/mass contributions.
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m This is preCICE version 1.6.1
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     user-defined solver type : none
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m Revision info: v1.6.1-216-gc2df0a8
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     temperature field name : T
[36mcalculix-adapter-solid    |[0m  Factoring the system of equations using the symmetric spooles solver
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     transportProperties name : transportProperties
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m Configuring preCICE with configuration: "precice-config.xml"
[36mcalculix-adapter-solid    |[0m  Using 1 cpu for spooles.
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  average flux= 5.108361
[36mcalculix-adapter-solid    |[0m  time avg. flux= 5.108361
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG]   preCICE was configured.
[36mcalculix-adapter-solid    |[0m  largest residual flux= 226.735266 in node 13966 and dof 0
[36mcalculix-adapter-solid    |[0m  largest increment of temp= 5.689586e+01
[36mcalculix-adapter-solid    |[0m  largest correction to temp= 5.689586e+01 in node 985 and dof 0
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  no convergence
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  iteration 2
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the symmetric stiffness/mass contributions.
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Factoring the system of equations using the symmetric spooles solver
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     conductivity name for basic solvers : k
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     density name for incompressible solvers : rho
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     heat capacity name for incompressible solvers : Cp
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Creating interfaces...
[36mcalculix-adapter-solid    |[0m  Using 1 cpu for spooles.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     Prandtl number name for incompressible solvers : Pr
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Number of face centres: 35384
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]     Turbulent thermal diffusivity field name for incompressible solvers : alphat
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Interface created on mesh Inner-Fluid-to-Solid
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Determining the solver type...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Adding coupling data writers...
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Did not find the transportProperties dictionary.
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Added writer: Sink Temperature.
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Found the turbulenceProperties dictionary.
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Constructed KappaEff_Compressible.
[36mcalculix-adapter-solid    |[0m  average flux= 5.108361
[36mcalculix-adapter-solid    |[0m  time avg. flux= 5.108361
[36mcalculix-adapter-solid    |[0m  largest residual flux= 0.000000 in node 21126 and dof 0
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Added writer: Heat Transfer Coefficient for compressible solvers.
[36mcalculix-adapter-solid    |[0m  largest increment of temp= 5.689586e+01
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Found the thermophysicalProperties dictionary.
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Adding coupling data readers...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Added reader: Sink Temperature.
[36mcalculix-adapter-solid    |[0m  largest correction to temp= 1.586061e-13 in node 9660 and dof 0
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Constructed KappaEff_Compressible.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] This is a compressible flow solver, as turbulence and thermophysical properties are provided.
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  convergence
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Checking the timestep type (fixed vs adjustable)...
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Added reader: Heat Transfer Coefficient for compressible solvers.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]   Timestep type: fixed.
[36mcalculix-adapter-solid    |[0m  the increment size exceeds the remainder of the step and is decreased to 0.000000e+00
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Initalizing the preCICE solver interface...
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Creating the preCICE solver interface...
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m Setting up master communication to coupling partner/s
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]   Number of processes: 1
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m Masters are connected
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]   MPI rank: 0
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m Gather mesh Inner-Fluid-to-Solid
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]   preCICE solver interface was created.
[36mcalculix-adapter-solid    |[0m Adapter writing coupling data...
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m Send global mesh Inner-Fluid-to-Solid
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Configuring preCICE...
[36mcalculix-adapter-solid    |[0m Adapter calling advance()...
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m Receive global mesh Solid-to-Inner-Fluid
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m This is preCICE version 1.6.1
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Inner-Fluid: it 1 of 1 | dt# 2 | t 1 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m Compute partition for mesh Inner-Fluid-to-Solid
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m Revision info: v1.6.1-216-gc2df0a8
[36mcalculix-adapter-solid    |[0m Outer-Fluid: it 1 of 1 | dt# 2 | t 1 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m Setting up slaves communication to coupling partner/s
[36mcalculix-adapter-solid    |[0m Adjusting time step for steady-state step
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m Configuring preCICE with configuration: "precice-config.xml"
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m Slaves are connected
[36mcalculix-adapter-solid    |[0m Adapter reading coupling data...
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m it 1 of 1 | dt# 1 | t 0 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete no | write-initial-data | 
[36mcalculix-adapter-solid    |[0m  increment 2 attempt 1 
[36mcalculix-adapter-solid    |[0m  increment size= 1.000000e+00
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Writing coupling data...
[36mcalculix-adapter-solid    |[0m  sum of previous increments=0.000000e+00
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG]   preCICE was configured.
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Initializing preCICE data...
[36mcalculix-adapter-solid    |[0m  actual step time=1.000000e+00
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Creating interfaces...
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m Compute read mapping from mesh "Solid-to-Inner-Fluid" to mesh "Inner-Fluid-to-Solid".
[36mcalculix-adapter-solid    |[0m  actual total time=1.000000e+00
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Number of face centres: 52809
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m Mapping distance min:0.000430952 max:0.0351746 avg: 0.0130161 var: 2.9614e-05 cnt: 35384
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Interface created on mesh Outer-Fluid-to-Solid
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] preCICE was configured and initialized
[36mcalculix-adapter-solid    |[0m  iteration 1
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Adding coupling data writers...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Reading coupling data...
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Added writer: Sink Temperature.
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Adjusting the solver's timestep...
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Constructed KappaEff_Compressible.
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] The solver's timestep is the same as the coupling timestep.
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Added writer: Heat Transfer Coefficient for compressible solvers.
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] Setting the solver's endTime to infinity to prevent early exits. Only preCICE will control the simulation's endTime. Any functionObject's end() method will be triggered by the adapter. You may disable this behavior in the adapter's configuration.
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the symmetric stiffness/mass contributions.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Adding coupling data readers...
[32mopenfoam-adapter-inner    |[0m Time = 1
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Added reader: Sink Temperature.
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m  Factoring the system of equations using the symmetric spooles solver
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Constructed KappaEff_Compressible.
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Ux, Initial residual = 1, Final residual = 0.003, No Iterations 1
[36mcalculix-adapter-solid    |[0m  Using 1 cpu for spooles.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Added reader: Heat Transfer Coefficient for compressible solvers.
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Uy, Initial residual = 1, Final residual = 0.001, No Iterations 1
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Initalizing the preCICE solver interface...
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m Setting up master communication to coupling partner/s
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Uz, Initial residual = 1, Final residual = 0.002, No Iterations 1
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  average flux= 0.195386
[36mcalculix-adapter-solid    |[0m  time avg. flux= 2.651873
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for h, Initial residual = 1, Final residual = 7e-07, No Iterations 26
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m Masters are connected
[36mcalculix-adapter-solid    |[0m  largest residual flux= 218.803266 in node 13966 and dof 0
[32mopenfoam-adapter-inner    |[0m DICPCG:  Solving for p_rgh, Initial residual = 1, Final residual = 0.009, No Iterations 461
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m Gather mesh Outer-Fluid-to-Solid
[36mcalculix-adapter-solid    |[0m  largest increment of temp= 5.457558e+01
[32mopenfoam-adapter-inner    |[0m time step continuity errors : sum local = 0.003, global = -4e-06, cumulative = -4e-06
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m Send global mesh Outer-Fluid-to-Solid
[32mopenfoam-adapter-inner    |[0m rho max/min : 1e+03 1e+03
[36mcalculix-adapter-solid    |[0m  largest correction to temp= 5.457558e+01 in node 1124 and dof 0
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m Receive global mesh Solid-to-Outer-Fluid
[32mopenfoam-adapter-inner    |[0m ExecutionTime = 2e+01 s  ClockTime = 22 s
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m Compute partition for mesh Outer-Fluid-to-Solid
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m  no convergence
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Writing coupling data...
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m Setting up slaves communication to coupling partner/s
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m Slaves are connected
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Advancing preCICE...
[36mcalculix-adapter-solid    |[0m  iteration 2
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m it 1 of 1 | dt# 1 | t 0 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete no | write-initial-data | 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Writing coupling data...
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Initializing preCICE data...
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m Compute read mapping from mesh "Solid-to-Outer-Fluid" to mesh "Outer-Fluid-to-Solid".
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m it 1 of 1 | dt# 2 | t 1 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m Mapping distance min:0.000112137 max:0.0359417 avg: 0.0131496 var: 3.11294e-05 cnt: 52809
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Reading coupling data...
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the symmetric stiffness/mass contributions.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] preCICE was configured and initialized
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Adjusting the solver's timestep...
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Reading coupling data...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] The solver's timestep is the same as the coupling timestep.
[36mcalculix-adapter-solid    |[0m  Factoring the system of equations using the symmetric spooles solver
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Adjusting the solver's timestep...
[32mopenfoam-adapter-inner    |[0m Time = 2
[36mcalculix-adapter-solid    |[0m  Using 1 cpu for spooles.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] The solver's timestep is the same as the coupling timestep.
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Ux, Initial residual = 0.3, Final residual = 0.004, No Iterations 3
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Uy, Initial residual = 0.4, Final residual = 0.004, No Iterations 3
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] Setting the solver's endTime to infinity to prevent early exits. Only preCICE will control the simulation's endTime. Any functionObject's end() method will be triggered by the adapter. You may disable this behavior in the adapter's configuration.
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Uz, Initial residual = 0.1, Final residual = 0.006, No Iterations 2
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m Time = 1
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for h, Initial residual = 0.8, Final residual = 4e-07, No Iterations 75
[36mcalculix-adapter-solid    |[0m  average flux= 0.195386
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m DICPCG:  Solving for p_rgh, Initial residual = 0.1, Final residual = 0.001, No Iterations 565
[36mcalculix-adapter-solid    |[0m  time avg. flux= 2.651873
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Ux, Initial residual = 0, Final residual = 0, No Iterations 0
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Uy, Initial residual = 1, Final residual = 0.0007, No Iterations 1
[36mcalculix-adapter-solid    |[0m  largest residual flux= 0.000000 in node 3657 and dof 0
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Uz, Initial residual = 0, Final residual = 0, No Iterations 0
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for h, Initial residual = 1, Final residual = 7e-07, No Iterations 23
[36mcalculix-adapter-solid    |[0m  largest increment of temp= 5.457558e+01
[33mopenfoam-adapter-outer    |[0m DICPCG:  Solving for p_rgh, Initial residual = 1, Final residual = 0.009, No Iterations 369
[32mopenfoam-adapter-inner    |[0m time step continuity errors : sum local = 0.01, global = -9e-07, cumulative = -5e-06
[36mcalculix-adapter-solid    |[0m  largest correction to temp= 1.723503e-13 in node 2495 and dof 0
[33mopenfoam-adapter-outer    |[0m time step continuity errors : sum local = 0.0009, global = -3e-07, cumulative = -3e-07
[32mopenfoam-adapter-inner    |[0m rho max/min : 1e+03 1e+03
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m rho max/min : 1e+03 1e+03
[32mopenfoam-adapter-inner    |[0m ExecutionTime = 3e+01 s  ClockTime = 37 s
[36mcalculix-adapter-solid    |[0m  convergence
[33mopenfoam-adapter-outer    |[0m ExecutionTime = 3e+01 s  ClockTime = 29 s
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Writing coupling data...
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Writing coupling data...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Advancing preCICE...
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Advancing preCICE...
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m it 1 of 1 | dt# 3 | t 2 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[36mcalculix-adapter-solid    |[0m Adapter writing coupling data...
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m it 1 of 1 | dt# 2 | t 1 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Reading coupling data...
[36mcalculix-adapter-solid    |[0m Adapter calling advance()...
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Reading coupling data...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Adjusting the solver's timestep...
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Inner-Fluid: it 1 of 1 | dt# 3 | t 2 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Adjusting the solver's timestep...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] The solver's timestep is the same as the coupling timestep.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] The solver's timestep is the same as the coupling timestep.
[36mcalculix-adapter-solid    |[0m Outer-Fluid: it 1 of 1 | dt# 3 | t 2 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[32mopenfoam-adapter-inner    |[0m Time = 3
[33mopenfoam-adapter-outer    |[0m Time = 2
[36mcalculix-adapter-solid    |[0m Adjusting time step for steady-state step
[32mopenfoam-adapter-inner    |[0m 
[33mopenfoam-adapter-outer    |[0m 
[36mcalculix-adapter-solid    |[0m Adapter reading coupling data...
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Ux, Initial residual = 0.3, Final residual = 0.02, No Iterations 2
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Ux, Initial residual = 0.3, Final residual = 0.02, No Iterations 2
[36mcalculix-adapter-solid    |[0m  increment 3 attempt 1 
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Uy, Initial residual = 0.3, Final residual = 0.009, No Iterations 3
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Uy, Initial residual = 0.2, Final residual = 0.01, No Iterations 2
[36mcalculix-adapter-solid    |[0m  increment size= 1.000000e+00
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Uz, Initial residual = 0.5, Final residual = 0.01, No Iterations 2
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Uz, Initial residual = 0.2, Final residual = 0.006, No Iterations 2
[36mcalculix-adapter-solid    |[0m  sum of previous increments=0.000000e+00
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for h, Initial residual = 0.7, Final residual = 9e-07, No Iterations 75
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for h, Initial residual = 0.9, Final residual = 7e-07, No Iterations 92
[36mcalculix-adapter-solid    |[0m  actual step time=1.000000e+00
[32mopenfoam-adapter-inner    |[0m DICPCG:  Solving for p_rgh, Initial residual = 0.04, Final residual = 0.0004, No Iterations 373
[33mopenfoam-adapter-outer    |[0m DICPCG:  Solving for p_rgh, Initial residual = 0.7, Final residual = 0.007, No Iterations 472
[36mcalculix-adapter-solid    |[0m  actual total time=1.000000e+00
[33mopenfoam-adapter-outer    |[0m time step continuity errors : sum local = 0.009, global = -2e-06, cumulative = -2e-06
[32mopenfoam-adapter-inner    |[0m time step continuity errors : sum local = 0.02, global = 0.0002, cumulative = 0.0002
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m rho max/min : 1e+03 1e+03
[32mopenfoam-adapter-inner    |[0m rho max/min : 1e+03 1e+03
[36mcalculix-adapter-solid    |[0m  iteration 1
[33mopenfoam-adapter-outer    |[0m ExecutionTime = 5e+01 s  ClockTime = 55 s
[32mopenfoam-adapter-inner    |[0m ExecutionTime = 4e+01 s  ClockTime = 51 s
[32mopenfoam-adapter-inner    |[0m 
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Writing coupling data...
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Writing coupling data...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Advancing preCICE...
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Advancing preCICE...
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m it 1 of 1 | dt# 4 | t 3 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m it 1 of 1 | dt# 3 | t 2 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Reading coupling data...
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the symmetric stiffness/mass contributions.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Reading coupling data...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Adjusting the solver's timestep...
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Adjusting the solver's timestep...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] The solver's timestep is the same as the coupling timestep.
[36mcalculix-adapter-solid    |[0m  Factoring the system of equations using the symmetric spooles solver
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] The solver's timestep is the same as the coupling timestep.
[32mopenfoam-adapter-inner    |[0m Time = 4
[36mcalculix-adapter-solid    |[0m  Using 1 cpu for spooles.
[33mopenfoam-adapter-outer    |[0m Time = 3
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Ux, Initial residual = 0.2, Final residual = 0.02, No Iterations 2
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Uy, Initial residual = 0.2, Final residual = 0.003, No Iterations 3
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Ux, Initial residual = 0.3, Final residual = 0.02, No Iterations 2
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Uz, Initial residual = 0.3, Final residual = 0.007, No Iterations 2
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Uy, Initial residual = 0.3, Final residual = 0.01, No Iterations 2
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for h, Initial residual = 0.8, Final residual = 8e-07, No Iterations 76
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Uz, Initial residual = 0.3, Final residual = 0.01, No Iterations 2
[32mopenfoam-adapter-inner    |[0m DICPCG:  Solving for p_rgh, Initial residual = 0.05, Final residual = 0.0004, No Iterations 442
[36mcalculix-adapter-solid    |[0m  average flux= 0.908164
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for h, Initial residual = 0.9, Final residual = 5e-07, No Iterations 89
[32mopenfoam-adapter-inner    |[0m time step continuity errors : sum local = 0.02, global = -7e-05, cumulative = 0.0002
[36mcalculix-adapter-solid    |[0m  time avg. flux= 2.070637
[33mopenfoam-adapter-outer    |[0m DICPCG:  Solving for p_rgh, Initial residual = 0.5, Final residual = 0.005, No Iterations 398
[32mopenfoam-adapter-inner    |[0m rho max/min : 1e+03 1e+03
[36mcalculix-adapter-solid    |[0m  largest residual flux= 200.653819 in node 13966 and dof 0
[33mopenfoam-adapter-outer    |[0m time step continuity errors : sum local = 0.02, global = -3e-07, cumulative = -2e-06
[32mopenfoam-adapter-inner    |[0m ExecutionTime = 6e+01 s  ClockTime = 71 s
[36mcalculix-adapter-solid    |[0m  largest increment of temp= 4.921781e+01
[33mopenfoam-adapter-outer    |[0m rho max/min : 1e+03 1e+03
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m  largest correction to temp= 4.921781e+01 in node 2259 and dof 0
[33mopenfoam-adapter-outer    |[0m ExecutionTime = 7e+01 s  ClockTime = 77 s
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Writing coupling data...
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Advancing preCICE...
[36mcalculix-adapter-solid    |[0m  no convergence
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Writing coupling data...
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m it 1 of 1 | dt# 5 | t 4 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Advancing preCICE...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Reading coupling data...
[36mcalculix-adapter-solid    |[0m  iteration 2
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m it 1 of 1 | dt# 4 | t 3 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Adjusting the solver's timestep...
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Reading coupling data...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] The solver's timestep is the same as the coupling timestep.
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the symmetric stiffness/mass contributions.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Adjusting the solver's timestep...
[32mopenfoam-adapter-inner    |[0m Time = 5
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] The solver's timestep is the same as the coupling timestep.
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m  Factoring the system of equations using the symmetric spooles solver
[33mopenfoam-adapter-outer    |[0m Time = 4
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Ux, Initial residual = 0.2, Final residual = 0.01, No Iterations 2
[36mcalculix-adapter-solid    |[0m  Using 1 cpu for spooles.
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Uy, Initial residual = 0.2, Final residual = 0.003, No Iterations 3
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for Uz, Initial residual = 0.06, Final residual = 0.002, No Iterations 2
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Ux, Initial residual = 0.2, Final residual = 0.008, No Iterations 2
[32mopenfoam-adapter-inner    |[0m DILUPBiCG:  Solving for h, Initial residual = 0.7, Final residual = 5e-07, No Iterations 90
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Uy, Initial residual = 0.1, Final residual = 0.006, No Iterations 2
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[32mopenfoam-adapter-inner    |[0m DICPCG:  Solving for p_rgh, Initial residual = 0.3, Final residual = 0.003, No Iterations 431
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Uz, Initial residual = 0.1, Final residual = 0.009, No Iterations 2
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m time step continuity errors : sum local = 0.02, global = -7e-06, cumulative = 0.0002
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for h, Initial residual = 0.9, Final residual = 8e-07, No Iterations 84
[36mcalculix-adapter-solid    |[0m  average flux= 0.908164
[32mopenfoam-adapter-inner    |[0m rho max/min : 1e+03 1e+03
[33mopenfoam-adapter-outer    |[0m DICPCG:  Solving for p_rgh, Initial residual = 0.4, Final residual = 0.004, No Iterations 423
[36mcalculix-adapter-solid    |[0m  time avg. flux= 2.070637
[32mopenfoam-adapter-inner    |[0m ExecutionTime = 7e+01 s  ClockTime = 93 s
[33mopenfoam-adapter-outer    |[0m time step continuity errors : sum local = 0.02, global = 6e-06, cumulative = 4e-06
[36mcalculix-adapter-solid    |[0m  largest residual flux= 0.000000 in node 21118 and dof 0
[32mopenfoam-adapter-inner    |[0m 
[33mopenfoam-adapter-outer    |[0m rho max/min : 1e+03 1e+03
[36mcalculix-adapter-solid    |[0m  largest increment of temp= 4.921781e+01
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Writing coupling data...
[33mopenfoam-adapter-outer    |[0m ExecutionTime = 1e+02 s  ClockTime = 100 s
[36mcalculix-adapter-solid    |[0m  largest correction to temp= 1.417004e-13 in node 11123 and dof 0
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Advancing preCICE...
[33mopenfoam-adapter-outer    |[0m 
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Writing coupling data...
[32mopenfoam-adapter-inner    |[0m ---[precice] [0m it 1 of 1 | dt# 6 | t 5 of 5 | dt 1 | max dt 1 | ongoing no | dt complete yes | 
[36mcalculix-adapter-solid    |[0m  convergence
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Advancing preCICE...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Reading coupling data...
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m it 1 of 1 | dt# 5 | t 4 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Adjusting the solver's timestep...
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Reading coupling data...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] The solver's timestep is the same as the coupling timestep.
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Adjusting the solver's timestep...
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] The coupling completed.
[36mcalculix-adapter-solid    |[0m Adapter writing coupling data...
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] The solver's timestep is the same as the coupling timestep.
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Finalizing the preCICE solver interface...
[36mcalculix-adapter-solid    |[0m Adapter calling advance()...
[33mopenfoam-adapter-outer    |[0m Time = 5
[32mopenfoam-adapter-inner    |[0m Run finished at Sat Jan 25 10:29:42 2020
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Inner-Fluid: it 1 of 1 | dt# 4 | t 3 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m Global runtime       = 1e+05ms / 1e+02s
[32mopenfoam-adapter-inner    |[0m Number of processors = 1
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Ux, Initial residual = 0.09, Final residual = 0.006, No Iterations 2
[36mcalculix-adapter-solid    |[0m Outer-Fluid: it 1 of 1 | dt# 4 | t 3 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[32mopenfoam-adapter-inner    |[0m # Rank: 0
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Uy, Initial residual = 0.05, Final residual = 0.0006, No Iterations 3
[36mcalculix-adapter-solid    |[0m Adjusting time step for steady-state step
[32mopenfoam-adapter-inner    |[0m 
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for Uz, Initial residual = 0.05, Final residual = 0.0007, No Iterations 3
[36mcalculix-adapter-solid    |[0m Adapter reading coupling data...
[32mopenfoam-adapter-inner    |[0m                                                                                                   Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
[36mcalculix-adapter-solid    |[0m  increment 4 attempt 1 
[36mcalculix-adapter-solid    |[0m  increment size= 1.000000e+00
[36mcalculix-adapter-solid    |[0m  sum of previous increments=0.000000e+00
[36mcalculix-adapter-solid    |[0m  actual step time=1.000000e+00
[36mcalculix-adapter-solid    |[0m  actual total time=1.000000e+00
[32mopenfoam-adapter-inner    |[0m ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[33mopenfoam-adapter-outer    |[0m DILUPBiCG:  Solving for h, Initial residual = 0.8, Final residual = 8e-07, No Iterations 85
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m                                                                                                 _GLOBAL |          1 |     110955 |     110955 |     110955 |     110955 |          1 |
[36mcalculix-adapter-solid    |[0m  iteration 1
[33mopenfoam-adapter-outer    |[0m DICPCG:  Solving for p_rgh, Initial residual = 0.5, Final residual = 0.004, No Iterations 432
[32mopenfoam-adapter-inner    |[0m                                                                                                 advance |          5 |      21780 |       7883 |          2 |       4356 |      0.196 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m time step continuity errors : sum local = 0.02, global = -2e-05, cumulative = -2e-05
[32mopenfoam-adapter-inner    |[0m                                                                                 advance/m2n.receiveData |         10 |      21772 |       7882 |          0 |       2177 |      0.196 |
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[32mopenfoam-adapter-inner    |[0m                                                                                    advance/m2n.sendData |         10 |          4 |          1 |          0 |          0 |   3.61e-05 |
[33mopenfoam-adapter-outer    |[0m rho max/min : 1e+03 1e+03
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m                                   advance/map.nn.mapData.FromSolid-to-Inner-FluidToInner-Fluid-to-Solid |         10 |          2 |          1 |          0 |          0 |    1.8e-05 |
[32mopenfoam-adapter-inner    |[0m                                                                                               configure |          1 |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the symmetric stiffness/mass contributions.
[33mopenfoam-adapter-outer    |[0m ExecutionTime = 1e+02 s  ClockTime = 116 s
[32mopenfoam-adapter-inner    |[0m                                                                                                finalize |          1 |      14419 |      14419 |      14419 |      14419 |       0.13 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m                                                                                              initialize |          1 |       3058 |       3058 |       3058 |       3058 |     0.0276 |
[36mcalculix-adapter-solid    |[0m  Factoring the system of equations using the symmetric spooles solver
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Writing coupling data...
[32mopenfoam-adapter-inner    |[0m                                                                   initialize/m2n.acceptMasterConnection |          1 |       2277 |       2277 |       2277 |       2277 |     0.0205 |
[36mcalculix-adapter-solid    |[0m  Using 1 cpu for spooles.
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Advancing preCICE...
[32mopenfoam-adapter-inner    |[0m                                                                   initialize/m2n.acceptSlavesConnection |          1 |         27 |         27 |         27 |         27 |   0.000243 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---[precice] [0m it 1 of 1 | dt# 6 | t 5 of 5 | dt 1 | max dt 1 | ongoing no | dt complete yes | 
[32mopenfoam-adapter-inner    |[0m                                                             initialize/m2n.broadcastVertexDistributions |          2 |          0 |          0 |          0 |          0 |          0 |
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Reading coupling data...
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[32mopenfoam-adapter-inner    |[0m                                                                    initialize/m2n.buildCommunicationMap |          2 |          5 |          2 |          2 |          2 |   4.51e-05 |
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Adjusting the solver's timestep...
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m                                                                     initialize/m2n.createCommunications |          2 |          3 |          2 |          1 |          1 |    2.7e-05 |
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] The solver's timestep is the same as the coupling timestep.
[36mcalculix-adapter-solid    |[0m  average flux= 0.195722
[32mopenfoam-adapter-inner    |[0m                                                               initialize/m2n.exchangeVertexDistribution |          2 |         18 |         12 |          5 |          9 |   0.000162 |
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] The coupling completed.
[32mopenfoam-adapter-inner    |[0m                                                  initialize/partition.feedbackMesh.Inner-Fluid-to-Solid |          1 |          1 |          1 |          1 |          1 |   9.01e-06 |
[36mcalculix-adapter-solid    |[0m  time avg. flux= 1.601908
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Finalizing the preCICE solver interface...
[32mopenfoam-adapter-inner    |[0m                                                    initialize/partition.gatherMesh.Inner-Fluid-to-Solid |          1 |         12 |         12 |         12 |         12 |   0.000108 |
[32mopenfoam-adapter-inner    |[0m                                             initialize/partition.receiveGlobalMesh.Solid-to-Inner-Fluid |          1 |        686 |        686 |        686 |        686 |    0.00618 |
[33mopenfoam-adapter-outer    |[0m Run finished at Sat Jan 25 10:29:42 2020
[32mopenfoam-adapter-inner    |[0m                                                initialize/partition.sendGlobalMesh.Inner-Fluid-to-Solid |          1 |         40 |         40 |         40 |         40 |   0.000361 |
[36mcalculix-adapter-solid    |[0m  largest residual flux= 190.199878 in node 13966 and dof 0
[33mopenfoam-adapter-outer    |[0m Global runtime       = 1e+05ms / 1e+02s
[32mopenfoam-adapter-inner    |[0m                                                                                          initializeData |          1 |        121 |        121 |        121 |        121 |    0.00109 |
[36mcalculix-adapter-solid    |[0m  largest increment of temp= 4.741042e+01
[33mopenfoam-adapter-outer    |[0m Number of processors = 1
[32mopenfoam-adapter-inner    |[0m                                                                          initializeData/m2n.receiveData |          2 |         34 |         33 |          0 |         17 |   0.000306 |
[36mcalculix-adapter-solid    |[0m  largest correction to temp= 4.741042e+01 in node 1124 and dof 0
[33mopenfoam-adapter-outer    |[0m # Rank: 0
[32mopenfoam-adapter-inner    |[0m                                                                             initializeData/m2n.sendData |          2 |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m 
[32mopenfoam-adapter-inner    |[0m                     initializeData/map.nn.computeMapping.FromSolid-to-Inner-FluidToInner-Fluid-to-Solid |          1 |         86 |         86 |         86 |         86 |   0.000775 |
[36mcalculix-adapter-solid    |[0m  no convergence
[33mopenfoam-adapter-outer    |[0m                                                                                                   Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
[32mopenfoam-adapter-inner    |[0m  initializeData/map.nn.computeMapping.FromSolid-to-Inner-FluidToInner-Fluid-to-Solid.getIndexOnVertices |          1 |          4 |          4 |          4 |          4 |   3.61e-05 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[32mopenfoam-adapter-inner    |[0m                            initializeData/map.nn.mapData.FromSolid-to-Inner-FluidToInner-Fluid-to-Solid |          2 |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m  iteration 2
[33mopenfoam-adapter-outer    |[0m                                                                                                 _GLOBAL |          1 |     107959 |     107959 |     107959 |     107959 |          1 |
[32mopenfoam-adapter-inner    |[0m                                                                                          solver.advance |          5 |      57902 |      15805 |          2 |      11580 |      0.522 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m                                                                                                 advance |          5 |          9 |          2 |          1 |          1 |   8.34e-05 |
[32mopenfoam-adapter-inner    |[0m                                                                                       solver.initialize |          1 |      13672 |      13672 |      13672 |      13672 |      0.123 |
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the symmetric stiffness/mass contributions.
[33mopenfoam-adapter-outer    |[0m                                                                                 advance/m2n.receiveData |         10 |          2 |          0 |          0 |          0 |   1.85e-05 |
[32mopenfoam-adapter-inner    |[0m 
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m                                                                                    advance/m2n.sendData |         10 |          3 |          0 |          0 |          0 |   2.78e-05 |
[32mopenfoam-adapter-inner    |[0m 
[32mopenfoam-adapter-inner    |[0m                                                                                                    Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
[33mopenfoam-adapter-outer    |[0m                                   advance/map.nn.mapData.FromSolid-to-Outer-FluidToOuter-Fluid-to-Solid |         10 |          1 |          0 |          0 |          0 |   9.26e-06 |
[32mopenfoam-adapter-inner    |[0m --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[36mcalculix-adapter-solid    |[0m  Factoring the system of equations using the symmetric spooles solver
[33mopenfoam-adapter-outer    |[0m                                                                                               configure |          1 |          0 |          0 |          0 |          0 |          0 |
[32mopenfoam-adapter-inner    |[0m                                                                                                 _GLOBAL |     110955 |          0 |     110955 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m  Using 1 cpu for spooles.
[33mopenfoam-adapter-outer    |[0m                                                                                                finalize |          1 |        121 |        121 |        121 |        121 |    0.00112 |
[32mopenfoam-adapter-inner    |[0m                                                                                                 advance |       7883 |          0 |          2 |          0 | 0.000253711 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m                                                                                              initialize |          1 |        101 |        101 |        101 |        101 |   0.000936 |
[32mopenfoam-adapter-inner    |[0m                                                                                 advance/m2n.receiveData |       7882 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[33mopenfoam-adapter-outer    |[0m                                                                   initialize/m2n.acceptMasterConnection |          1 |          1 |          1 |          1 |          1 |   9.26e-06 |
[32mopenfoam-adapter-inner    |[0m                                                                                    advance/m2n.sendData |          1 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m                                                                   initialize/m2n.acceptSlavesConnection |          1 |         38 |         38 |         38 |         38 |   0.000352 |
[32mopenfoam-adapter-inner    |[0m                                   advance/map.nn.mapData.FromSolid-to-Inner-FluidToInner-Fluid-to-Solid |          1 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m  average flux= 0.195722
[33mopenfoam-adapter-outer    |[0m                                                             initialize/m2n.broadcastVertexDistributions |          2 |          0 |          0 |          0 |          0 |          0 |
[32mopenfoam-adapter-inner    |[0m                                                                                               configure |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m  time avg. flux= 1.601908
[33mopenfoam-adapter-outer    |[0m                                                                    initialize/m2n.buildCommunicationMap |          2 |         14 |          9 |          4 |          7 |    0.00013 |
[36mcalculix-adapter-solid    |[0m  largest residual flux= 0.000000 in node 826 and dof 0
[33mopenfoam-adapter-outer    |[0m                                                                     initialize/m2n.createCommunications |          2 |          3 |          2 |          1 |          1 |   2.78e-05 |
[32mopenfoam-adapter-inner    |[0m                                                                                                finalize |      14419 |          0 |      14419 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m  largest increment of temp= 4.741042e+01
[33mopenfoam-adapter-outer    |[0m                                                               initialize/m2n.exchangeVertexDistribution |          2 |         20 |         17 |          2 |         10 |   0.000185 |
[32mopenfoam-adapter-inner    |[0m                                                                                              initialize |       3058 |          0 |       3058 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m  largest correction to temp= 1.419894e-13 in node 13966 and dof 0
[33mopenfoam-adapter-outer    |[0m                                                  initialize/partition.feedbackMesh.Outer-Fluid-to-Solid |          1 |          1 |          1 |          1 |          1 |   9.26e-06 |
[33mopenfoam-adapter-outer    |[0m                                                    initialize/partition.gatherMesh.Outer-Fluid-to-Solid |          1 |         19 |         19 |         19 |         19 |   0.000176 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m                                             initialize/partition.receiveGlobalMesh.Solid-to-Outer-Fluid |          1 |         27 |         27 |         27 |         27 |    0.00025 |
[32mopenfoam-adapter-inner    |[0m                                                                   initialize/m2n.acceptMasterConnection |       2277 |          0 |       2277 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m  convergence
[33mopenfoam-adapter-outer    |[0m                                                initialize/partition.sendGlobalMesh.Outer-Fluid-to-Solid |          1 |          4 |          4 |          4 |          4 |   3.71e-05 |
[33mopenfoam-adapter-outer    |[0m                                                                                          initializeData |          1 |        241 |        241 |        241 |        241 |    0.00223 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m                                                                          initializeData/m2n.receiveData |          2 |         15 |         15 |          0 |          7 |   0.000139 |
[32mopenfoam-adapter-inner    |[0m                                                                   initialize/m2n.acceptSlavesConnection |         27 |          0 |         27 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[33mopenfoam-adapter-outer    |[0m                                                                             initializeData/m2n.sendData |          2 |          0 |          0 |          0 |          0 |          0 |
[32mopenfoam-adapter-inner    |[0m                                                             initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m                     initializeData/map.nn.computeMapping.FromSolid-to-Outer-FluidToOuter-Fluid-to-Solid |          1 |        223 |        223 |        223 |        223 |    0.00207 |
[32mopenfoam-adapter-inner    |[0m                                                                    initialize/m2n.buildCommunicationMap |          2 |          0 |          2 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m Adapter writing coupling data...
[33mopenfoam-adapter-outer    |[0m  initializeData/map.nn.computeMapping.FromSolid-to-Outer-FluidToOuter-Fluid-to-Solid.getIndexOnVertices |          1 |         15 |         15 |         15 |         15 |   0.000139 |
[32mopenfoam-adapter-inner    |[0m                                                                     initialize/m2n.createCommunications |          2 |          0 |          1 |          0 |        0.5 |
[36mcalculix-adapter-solid    |[0m Adapter calling advance()...
[33mopenfoam-adapter-outer    |[0m                            initializeData/map.nn.mapData.FromSolid-to-Outer-FluidToOuter-Fluid-to-Solid |          2 |          0 |          0 |          0 |          0 |          0 |
[32mopenfoam-adapter-inner    |[0m                                                               initialize/m2n.exchangeVertexDistribution |         12 |          0 |          5 |          0 |   0.416667 |
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Inner-Fluid: it 1 of 1 | dt# 5 | t 4 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[33mopenfoam-adapter-outer    |[0m                                                                                          solver.advance |          5 |      86210 |      25756 |          2 |      17242 |      0.799 |
[32mopenfoam-adapter-inner    |[0m                                                  initialize/partition.feedbackMesh.Inner-Fluid-to-Solid |          1 |          0 |          1 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m Outer-Fluid: it 1 of 1 | dt# 5 | t 4 of 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | 
[32mopenfoam-adapter-inner    |[0m                                                    initialize/partition.gatherMesh.Inner-Fluid-to-Solid |         12 |          0 |         12 |          0 |          1 |
[33mopenfoam-adapter-outer    |[0m                                                                                       solver.initialize |          1 |      21274 |      21274 |      21274 |      21274 |      0.197 |
[36mcalculix-adapter-solid    |[0m Adjusting time step for steady-state step
[32mopenfoam-adapter-inner    |[0m                                             initialize/partition.receiveGlobalMesh.Solid-to-Inner-Fluid |        686 |          0 |        686 |          0 |          1 |
[33mopenfoam-adapter-outer    |[0m 
[36mcalculix-adapter-solid    |[0m Adapter reading coupling data...
[32mopenfoam-adapter-inner    |[0m                                                initialize/partition.sendGlobalMesh.Inner-Fluid-to-Solid |         40 |          0 |         40 |          0 |          1 |
[33mopenfoam-adapter-outer    |[0m 
[36mcalculix-adapter-solid    |[0m  increment 5 attempt 1 
[32mopenfoam-adapter-inner    |[0m                                                                                          initializeData |        121 |          0 |        121 |          0 |          1 |
[33mopenfoam-adapter-outer    |[0m                                                                                                    Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
[36mcalculix-adapter-solid    |[0m  increment size= 1.000000e+00
[32mopenfoam-adapter-inner    |[0m                                                                          initializeData/m2n.receiveData |         33 |          0 |          0 |          0 |          0 |
[33mopenfoam-adapter-outer    |[0m --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[36mcalculix-adapter-solid    |[0m  sum of previous increments=0.000000e+00
[32mopenfoam-adapter-inner    |[0m                                                                             initializeData/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
[33mopenfoam-adapter-outer    |[0m                                                                                                 _GLOBAL |     107959 |          0 |     107959 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m  actual step time=1.000000e+00
[32mopenfoam-adapter-inner    |[0m                     initializeData/map.nn.computeMapping.FromSolid-to-Inner-FluidToInner-Fluid-to-Solid |         86 |          0 |         86 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m  actual total time=1.000000e+00
[33mopenfoam-adapter-outer    |[0m                                                                                                 advance |          2 |          0 |          1 |          0 |        0.5 |
[32mopenfoam-adapter-inner    |[0m  initializeData/map.nn.computeMapping.FromSolid-to-Inner-FluidToInner-Fluid-to-Solid.getIndexOnVertices |          4 |          0 |          4 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m                                                                                 advance/m2n.receiveData |          0 |          0 |          0 |          0 |          0 |
[32mopenfoam-adapter-inner    |[0m                            initializeData/map.nn.mapData.FromSolid-to-Inner-FluidToInner-Fluid-to-Solid |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m  iteration 1
[33mopenfoam-adapter-outer    |[0m                                                                                    advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
[32mopenfoam-adapter-inner    |[0m                                                                                          solver.advance |      15805 |          0 |          2 |          0 | 0.000126542 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m                                   advance/map.nn.mapData.FromSolid-to-Outer-FluidToOuter-Fluid-to-Solid |          0 |          0 |          0 |          0 |          0 |
[32mopenfoam-adapter-inner    |[0m                                                                                       solver.initialize |      13672 |          0 |      13672 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[33mopenfoam-adapter-outer    |[0m                                                                                               configure |          0 |          0 |          0 |          0 |          0 |
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Destroying the preCICE solver interface...
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Deleting the interfaces...
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the symmetric stiffness/mass contributions.
[33mopenfoam-adapter-outer    |[0m                                                                                                finalize |        121 |          0 |        121 |          0 |          1 |
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] [DEBUG] Destroying the CHT module...
[36mcalculix-adapter-solid    |[0m 
[32mopenfoam-adapter-inner    |[0m ---[preciceAdapter] The simulation was ended by preCICE. Calling the end() methods of any functionObject explicitly.
[36mcalculix-adapter-solid    |[0m  Factoring the system of equations using the symmetric spooles solver
[33mopenfoam-adapter-outer    |[0m                                                                                              initialize |        101 |          0 |        101 |          0 |          1 |
[32mopenfoam-adapter-inner    |[0m End
[33mopenfoam-adapter-outer    |[0m                                                                   initialize/m2n.acceptMasterConnection |          1 |          0 |          1 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m  Using 1 cpu for spooles.
[32mopenfoam-adapter-inner    |[0m 
[33mopenfoam-adapter-outer    |[0m                                                                   initialize/m2n.acceptSlavesConnection |         38 |          0 |         38 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m                                                             initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[33mopenfoam-adapter-outer    |[0m                                                                    initialize/m2n.buildCommunicationMap |          9 |          0 |          4 |          0 |   0.444444 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m                                                                     initialize/m2n.createCommunications |          2 |          0 |          1 |          0 |        0.5 |
[36mcalculix-adapter-solid    |[0m  average flux= 0.713499
[36mcalculix-adapter-solid    |[0m  time avg. flux= 1.424226
[36mcalculix-adapter-solid    |[0m  largest residual flux= 179.240770 in node 13966 and dof 0
[36mcalculix-adapter-solid    |[0m  largest increment of temp= 4.282278e+01
[33mopenfoam-adapter-outer    |[0m                                                               initialize/m2n.exchangeVertexDistribution |         17 |          0 |          2 |          0 |   0.117647 |
[33mopenfoam-adapter-outer    |[0m                                                  initialize/partition.feedbackMesh.Outer-Fluid-to-Solid |          1 |          0 |          1 |          0 |          1 |
[33mopenfoam-adapter-outer    |[0m                                                    initialize/partition.gatherMesh.Outer-Fluid-to-Solid |         19 |          0 |         19 |          0 |          1 |
[33mopenfoam-adapter-outer    |[0m                                             initialize/partition.receiveGlobalMesh.Solid-to-Outer-Fluid |         27 |          0 |         27 |          0 |          1 |
[33mopenfoam-adapter-outer    |[0m                                                initialize/partition.sendGlobalMesh.Outer-Fluid-to-Solid |          4 |          0 |          4 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m  largest correction to temp= 4.282278e+01 in node 1124 and dof 0
[33mopenfoam-adapter-outer    |[0m                                                                                          initializeData |        241 |          0 |        241 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  no convergence
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  iteration 2
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the symmetric stiffness/mass contributions.
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Factoring the system of equations using the symmetric spooles solver
[33mopenfoam-adapter-outer    |[0m                                                                          initializeData/m2n.receiveData |         15 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m  Using 1 cpu for spooles.
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  average flux= 0.713499
[36mcalculix-adapter-solid    |[0m  time avg. flux= 1.424226
[36mcalculix-adapter-solid    |[0m  largest residual flux= 0.000000 in node 826 and dof 0
[36mcalculix-adapter-solid    |[0m  largest increment of temp= 4.282278e+01
[33mopenfoam-adapter-outer    |[0m                                                                             initializeData/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m  largest correction to temp= 1.318116e-13 in node 9601 and dof 0
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  convergence
[33mopenfoam-adapter-outer    |[0m                     initializeData/map.nn.computeMapping.FromSolid-to-Outer-FluidToOuter-Fluid-to-Solid |        223 |          0 |        223 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m  initializeData/map.nn.computeMapping.FromSolid-to-Outer-FluidToOuter-Fluid-to-Solid.getIndexOnVertices |         15 |          0 |         15 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[36mcalculix-adapter-solid    |[0m 
[33mopenfoam-adapter-outer    |[0m                            initializeData/map.nn.mapData.FromSolid-to-Outer-FluidToOuter-Fluid-to-Solid |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m Adapter writing coupling data...
[36mcalculix-adapter-solid    |[0m Adapter calling advance()...
[36mcalculix-adapter-solid    |[0m ---[precice] [0m Inner-Fluid: it 1 of 1 | dt# 6 | t 5 of 5 | dt 1 | max dt 1 | ongoing no | dt complete yes | 
[36mcalculix-adapter-solid    |[0m Outer-Fluid: it 1 of 1 | dt# 6 | t 5 of 5 | dt 1 | max dt 1 | ongoing no | dt complete yes | 
[36mcalculix-adapter-solid    |[0m  Using up to 1 cpu(s) for the heat flux calculation.
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m Run finished at Sat Jan 25 10:29:42 2020
[36mcalculix-adapter-solid    |[0m Global runtime       = 109740ms / 109.74s
[36mcalculix-adapter-solid    |[0m Number of processors = 1
[36mcalculix-adapter-solid    |[0m # Rank: 0
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m                                                                                                   Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
[36mcalculix-adapter-solid    |[0m ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[36mcalculix-adapter-solid    |[0m                                                                                                 _GLOBAL |          1 |     109740 |     109740 |     109740 |     109740 |          1 |
[36mcalculix-adapter-solid    |[0m                                                                                                 advance |          5 |      96498 |      22294 |      14301 |      19299 |      0.879 |
[36mcalculix-adapter-solid    |[0m                                                                                 advance/m2n.receiveData |         20 |      96462 |      20947 |          0 |       4823 |      0.879 |
[36mcalculix-adapter-solid    |[0m                                                                                    advance/m2n.sendData |         20 |         25 |          7 |          0 |          1 |   0.000228 |
[36mcalculix-adapter-solid    |[0m                                   advance/map.nn.mapData.FromInner-Fluid-to-SolidToSolid-to-Inner-Fluid |         10 |          1 |          0 |          0 |          0 |   9.11e-06 |
[36mcalculix-adapter-solid    |[0m                                   advance/map.nn.mapData.FromOuter-Fluid-to-SolidToSolid-to-Outer-Fluid |         10 |          2 |          0 |          0 |          0 |   1.82e-05 |
[36mcalculix-adapter-solid    |[0m                                                                                               configure |          1 |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                                                                                finalize |          1 |         10 |         10 |         10 |         10 |   9.11e-05 |
[36mcalculix-adapter-solid    |[0m                                                                                              initialize |          1 |        799 |        799 |        799 |        799 |    0.00728 |
[36mcalculix-adapter-solid    |[0m                                                             initialize/m2n.broadcastVertexDistributions |          4 |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                                                    initialize/m2n.buildCommunicationMap |          4 |         15 |          6 |          1 |          3 |   0.000137 |
[36mcalculix-adapter-solid    |[0m                                                                     initialize/m2n.createCommunications |          4 |         14 |          5 |          2 |          3 |   0.000128 |
[36mcalculix-adapter-solid    |[0m                                                               initialize/m2n.exchangeVertexDistribution |          4 |          9 |          2 |          1 |          2 |    8.2e-05 |
[33mopenfoam-adapter-outer    |[0m                                                                                          solver.advance |      25756 |          0 |          2 |          0 | 7.76518e-05 |
[36mcalculix-adapter-solid    |[0m                                                                  initialize/m2n.requestMasterConnection |          2 |        699 |        697 |          1 |        349 |    0.00637 |
[33mopenfoam-adapter-outer    |[0m                                                                                       solver.initialize |      21274 |          0 |      21274 |          0 |          1 |
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Destroying the preCICE solver interface...
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Deleting the interfaces...
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] [DEBUG] Destroying the CHT module...
[33mopenfoam-adapter-outer    |[0m ---[preciceAdapter] The simulation was ended by preCICE. Calling the end() methods of any functionObject explicitly.
[33mopenfoam-adapter-outer    |[0m End
[36mcalculix-adapter-solid    |[0m                                                                  initialize/m2n.requestSlavesConnection |          2 |         39 |         23 |         16 |         19 |   0.000355 |
[33mopenfoam-adapter-outer    |[0m 
[36mcalculix-adapter-solid    |[0m                                                  initialize/partition.feedbackMesh.Solid-to-Inner-Fluid |          1 |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                                  initialize/partition.feedbackMesh.Solid-to-Outer-Fluid |          1 |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                                    initialize/partition.gatherMesh.Solid-to-Inner-Fluid |          1 |          2 |          2 |          2 |          2 |   1.82e-05 |
[36mcalculix-adapter-solid    |[0m                                                    initialize/partition.gatherMesh.Solid-to-Outer-Fluid |          1 |          6 |          6 |          6 |          6 |   5.47e-05 |
[36mcalculix-adapter-solid    |[0m                                             initialize/partition.receiveGlobalMesh.Inner-Fluid-to-Solid |          1 |         13 |         13 |         13 |         13 |   0.000118 |
[36mcalculix-adapter-solid    |[0m                                             initialize/partition.receiveGlobalMesh.Outer-Fluid-to-Solid |          1 |         22 |         22 |         22 |         22 |     0.0002 |
[36mcalculix-adapter-solid    |[0m                                                initialize/partition.sendGlobalMesh.Solid-to-Inner-Fluid |          1 |          1 |          1 |          1 |          1 |   9.11e-06 |
[36mcalculix-adapter-solid    |[0m                                                initialize/partition.sendGlobalMesh.Solid-to-Outer-Fluid |          1 |          1 |          1 |          1 |          1 |   9.11e-06 |
[36mcalculix-adapter-solid    |[0m                                                                                          initializeData |          1 |        327 |        327 |        327 |        327 |    0.00298 |
[36mcalculix-adapter-solid    |[0m                                                                          initializeData/m2n.receiveData |          4 |          3 |          1 |          0 |          0 |   2.73e-05 |
[36mcalculix-adapter-solid    |[0m                                                                             initializeData/m2n.sendData |          4 |          5 |          5 |          0 |          1 |   4.56e-05 |
[36mcalculix-adapter-solid    |[0m                     initializeData/map.nn.computeMapping.FromInner-Fluid-to-SolidToSolid-to-Inner-Fluid |          1 |        112 |        112 |        112 |        112 |    0.00102 |
[36mcalculix-adapter-solid    |[0m  initializeData/map.nn.computeMapping.FromInner-Fluid-to-SolidToSolid-to-Inner-Fluid.getIndexOnVertices |          1 |         25 |         25 |         25 |         25 |   0.000228 |
[36mcalculix-adapter-solid    |[0m                     initializeData/map.nn.computeMapping.FromOuter-Fluid-to-SolidToSolid-to-Outer-Fluid |          1 |        204 |        204 |        204 |        204 |    0.00186 |
[36mcalculix-adapter-solid    |[0m  initializeData/map.nn.computeMapping.FromOuter-Fluid-to-SolidToSolid-to-Outer-Fluid.getIndexOnVertices |          1 |         45 |         45 |         45 |         45 |    0.00041 |
[36mcalculix-adapter-solid    |[0m                            initializeData/map.nn.mapData.FromInner-Fluid-to-SolidToSolid-to-Inner-Fluid |          2 |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                            initializeData/map.nn.mapData.FromOuter-Fluid-to-SolidToSolid-to-Outer-Fluid |          2 |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                                                                          solver.advance |          5 |       7954 |       3463 |        121 |       1590 |     0.0725 |
[36mcalculix-adapter-solid    |[0m                                                                                       solver.initialize |          1 |       4148 |       4148 |       4148 |       4148 |     0.0378 |
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m                                                                                                    Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
[36mcalculix-adapter-solid    |[0m --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[36mcalculix-adapter-solid    |[0m                                                                                                 _GLOBAL |     109740 |          0 |     109740 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m                                                                                                 advance |      22294 |          0 |      14301 |          0 |   0.641473 |
[36mcalculix-adapter-solid    |[0m                                                                                 advance/m2n.receiveData |      20947 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                                                                    advance/m2n.sendData |          7 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                   advance/map.nn.mapData.FromInner-Fluid-to-SolidToSolid-to-Inner-Fluid |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                   advance/map.nn.mapData.FromOuter-Fluid-to-SolidToSolid-to-Outer-Fluid |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                                                                               configure |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                                                                                finalize |         10 |          0 |         10 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m                                                                                              initialize |        799 |          0 |        799 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m                                                             initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                                                    initialize/m2n.buildCommunicationMap |          6 |          0 |          1 |          0 |   0.166667 |
[36mcalculix-adapter-solid    |[0m                                                                     initialize/m2n.createCommunications |          5 |          0 |          2 |          0 |        0.4 |
[36mcalculix-adapter-solid    |[0m                                                               initialize/m2n.exchangeVertexDistribution |          2 |          0 |          1 |          0 |        0.5 |
[36mcalculix-adapter-solid    |[0m                                                                  initialize/m2n.requestMasterConnection |        697 |          0 |          1 |          0 | 0.00143472 |
[36mcalculix-adapter-solid    |[0m                                                                  initialize/m2n.requestSlavesConnection |         23 |          0 |         16 |          0 |   0.695652 |
[36mcalculix-adapter-solid    |[0m                                                  initialize/partition.feedbackMesh.Solid-to-Inner-Fluid |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                                  initialize/partition.feedbackMesh.Solid-to-Outer-Fluid |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                                    initialize/partition.gatherMesh.Solid-to-Inner-Fluid |          2 |          0 |          2 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m                                                    initialize/partition.gatherMesh.Solid-to-Outer-Fluid |          6 |          0 |          6 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m                                             initialize/partition.receiveGlobalMesh.Inner-Fluid-to-Solid |         13 |          0 |         13 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m                                             initialize/partition.receiveGlobalMesh.Outer-Fluid-to-Solid |         22 |          0 |         22 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m                                                initialize/partition.sendGlobalMesh.Solid-to-Inner-Fluid |          1 |          0 |          1 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m                                                initialize/partition.sendGlobalMesh.Solid-to-Outer-Fluid |          1 |          0 |          1 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m                                                                                          initializeData |        327 |          0 |        327 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m                                                                          initializeData/m2n.receiveData |          1 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                                                             initializeData/m2n.sendData |          5 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                     initializeData/map.nn.computeMapping.FromInner-Fluid-to-SolidToSolid-to-Inner-Fluid |        112 |          0 |        112 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m  initializeData/map.nn.computeMapping.FromInner-Fluid-to-SolidToSolid-to-Inner-Fluid.getIndexOnVertices |         25 |          0 |         25 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m                     initializeData/map.nn.computeMapping.FromOuter-Fluid-to-SolidToSolid-to-Outer-Fluid |        204 |          0 |        204 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m  initializeData/map.nn.computeMapping.FromOuter-Fluid-to-SolidToSolid-to-Outer-Fluid.getIndexOnVertices |         45 |          0 |         45 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m                            initializeData/map.nn.mapData.FromInner-Fluid-to-SolidToSolid-to-Inner-Fluid |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                            initializeData/map.nn.mapData.FromOuter-Fluid-to-SolidToSolid-to-Outer-Fluid |          0 |          0 |          0 |          0 |          0 |
[36mcalculix-adapter-solid    |[0m                                                                                          solver.advance |       3463 |          0 |        121 |          0 |  0.0349408 |
[36mcalculix-adapter-solid    |[0m                                                                                       solver.initialize |       4148 |          0 |       4148 |          0 |          1 |
[36mcalculix-adapter-solid    |[0m 
[36mcalculix-adapter-solid    |[0m  Job finished
[36mcalculix-adapter-solid    |[0m 
