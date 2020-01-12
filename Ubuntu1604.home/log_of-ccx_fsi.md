## Status: Failure 
Build: [1450](https://travis-ci.org/precice/systemtests/builds/635929000) 

Job: [1450.9](https://travis-ci.org/precice/systemtests/jobs/635929009) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/154) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
[32mopenfoam-adapter-fluid    |[0m cellZones
[32mopenfoam-adapter-fluid    |[0m boundary
[32mopenfoam-adapter-fluid    |[0m dynamicMeshDict
[32mopenfoam-adapter-fluid    |[0m p
[32mopenfoam-adapter-fluid    |[0m cellDisplacement
[32mopenfoam-adapter-fluid    |[0m pointZones
[32mopenfoam-adapter-fluid    |[0m transportProperties
[32mopenfoam-adapter-fluid    |[0m )
[32mopenfoam-adapter-fluid    |[0m 
[32mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/VSJQMOKNETPQ2OTANNNTE4B2SF:/var/lib/docker/overlay2/l/O5WXTF3WCUARYNLACRKUPXS45Q:/var/lib/docker/overlay2/l/K3IIRXGNVK7I56DLMT7Z6D2HSF:/var/lib/docker/overlay2/l/2FUKW4CMUQHQEJUY5BQAYOCNZJ:/var/lib/docker/overlay2/l/KMPU3BRLSLHVLAOACEGD6XKBPV:/var/lib/docker/overlay2/l/WYVRVTUYY75UAINGOO5SUESG5W:/var/lib/docker/overlay2/l/5N43X3QSE6RU2HUPFRRMJAE3GJ:/var/lib/docker/overlay2/l/PWOKDM6ZFWJ6CYAGXUIEOZVED3:/var/lib/docker/overlay2/l/ANCOQSLH4E2FM'
[32mopenfoam-adapter-fluid    |[0m Unexpected end of /proc/mounts line `EW2P7LV2SIX7Y:/var/lib/docker/overlay2/l/32L5AAQH7YMKI25E2UWNOS54CA:/var/lib/docker/overlay2/l/UBFKFALANKSEI2DPGQC7RCKTVX:/var/lib/docker/overlay2/l/ARIZWXXUB4VGTLWKX7LSA4TFV5:/var/lib/docker/overlay2/l/J4QK7K4QAHSEZJU3BYHWPNUG6Z:/var/lib/docker/overlay2/l/MKDLK24X4VSVE6QZGW46XJFDMT:/var/lib/docker/overlay2/l/O2NHGN3TXUQ5A2A6CR2GDI3DAO:/var/lib/docker/overlay2/l/2OMU3W2UY7FSAOFXZVZYUJHKXM:/var/lib/docker/overlay2/l/2ZIH3JJJUXWSN63HUOOLT5PV2G:/var/lib/docker/overlay2/l/I76EBKLR7LYXELLPIPVJKR5G56:/var/lib/do'
[33mcalculix-adapter-solid exited with code 134
[0m[32mopenfoam-adapter-fluid    |[0m terminate called after throwing an instance of 'std::runtime_error'
[32mopenfoam-adapter-fluid    |[0m   what():  No m2n communication configured between "Fluid" and "Calculix"!
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] Reading the adapter's YAML configuration file /home/[secure]/Data/Input/[secure]-adapter-config.yml...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Checking the adapter's YAML configuration file...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   participant : Fluid
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   [secure]-config-file : [secure]-config.xml
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   interfaces : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Fluid-Mesh-Faces
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceCenters
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       flap
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     write-data : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       Forces0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   - mesh      : Fluid-Mesh-Nodes
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     locations : faceNodes
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     Provide mesh connectivity : 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     patches   : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       flap
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     read-data : 
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]       Displacements0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     subcycling : 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     prevent early exit : 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     evaluate boundaries : 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     disable checkpointing : 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     CHT module enabled : 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     FSI module enabled : 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Configuring the FSI module...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     user-defined solver type : none
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]     pointDisplacement field name : pointDisplacement
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Determining the solver type...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Found the transportProperties dictionary.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Found the turbulenceProperties dictionary.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Did not find the thermophysicalProperties dictionary.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] This is an incompressible flow solver, as turbulence and transport properties are provided.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Checking the timestep type (fixed vs adjustable)...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   Timestep type: fixed.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Creating the preCICE solver interface...
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   Number of processes: 1
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   MPI rank: 0
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG]   preCICE solver interface was created.
[32mopenfoam-adapter-fluid    |[0m ---[[secure]Adapter] [DEBUG] Configuring preCICE...
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] *** Process received signal ***
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] Signal: Aborted (6)
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] Signal code:  (-6)
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [ 0] /lib/x86_64-linux-gnu/libc.so.6(+0x354b0)[0x7f519af714b0]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [ 1] /lib/x86_64-linux-gnu/libc.so.6(gsignal+0x38)[0x7f519af71428]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [ 2] /lib/x86_64-linux-gnu/libc.so.6(abort+0x16a)[0x7f519af7302a]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [ 3] /usr/lib/x86_64-linux-gnu/libstdc++.so.6(_ZN9__gnu_cxx27__verbose_terminate_handlerEv+0x16d)[0x7f519b8b484d]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [ 4] /usr/lib/x86_64-linux-gnu/libstdc++.so.6(+0x8d6b6)[0x7f519b8b26b6]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [ 5] /usr/lib/x86_64-linux-gnu/libstdc++.so.6(+0x8d701)[0x7f519b8b2701]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [ 6] /usr/lib/x86_64-linux-gnu/libstdc++.so.6(+0x8d919)[0x7f519b8b2919]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [ 7] /home/[secure]/[secure]-install/lib/lib[secure].so.1.6.1(_ZN7[secure]3m2n16M2NConfiguration6getM2NERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES9_+0x406)[0x7f5194e1e456]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [ 8] /home/[secure]/[secure]-install/lib/lib[secure].so.1.6.1(_ZNK7[secure]9cplscheme27CouplingSchemeConfiguration34createSerialExplicitCouplingSchemeERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x44)[0x7f5194de3964]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [ 9] /home/[secure]/[secure]-install/lib/lib[secure].so.1.6.1(_ZN7[secure]9cplscheme27CouplingSchemeConfiguration17xmlEndTagCallbackERKNS_3xml20ConfigurationContextERNS2_6XMLTagE+0x2cb)[0x7f5194de5d2b]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [10] /home/[secure]/[secure]-install/lib/lib[secure].so.1.6.1(_ZN7[secure]3xml12ConfigParser11connectTagsERKNS0_20ConfigurationContextERSt6vectorISt10shared_ptrINS0_6XMLTagEESaIS8_EERS5_IS6_INS1_4CTagEESaISD_EE+0xa60)[0x7f5194f61b00]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [11] /home/[secure]/[secure]-install/lib/lib[secure].so.1.6.1(_ZN7[secure]3xml12ConfigParser11connectTagsERKNS0_20ConfigurationContextERSt6vectorISt10shared_ptrINS0_6XMLTagEESaIS8_EERS5_IS6_INS1_4CTagEESaISD_EE+0x76a)[0x7f5194f6180a]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [12] /home/[secure]/[secure]-install/lib/lib[secure].so.1.6.1(_ZN7[secure]3xml12ConfigParser11connectTagsERKNS0_20ConfigurationContextERSt6vectorISt10shared_ptrINS0_6XMLTagEESaIS8_EERS5_IS6_INS1_4CTagEESaISD_EE+0x76a)[0x7f5194f6180a]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [13] /home/[secure]/[secure]-install/lib/lib[secure].so.1.6.1(_ZN7[secure]3xml12ConfigParserC1ERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERKNS0_20ConfigurationContextESt10shared_ptrINS0_6XMLTagEE+0x178)[0x7f5194f629b8]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [14] /home/[secure]/[secure]-install/lib/lib[secure].so.1.6.1(_ZN7[secure]3xml9configureERNS0_6XMLTagERKNS0_20ConfigurationContextERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x1a3)[0x7f5194f6a283]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [15] /home/[secure]/[secure]-install/lib/lib[secure].so.1.6.1(_ZN7[secure]4impl19SolverInterfaceImpl9configureERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x98)[0x7f5194f3f168]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [16] /home/[secure]/OpenFOAM/root-4.1/platforms/linux64GccDPInt32Opt/lib/lib[secure]AdapterFunctionObject.so(_ZN14[secure]Adapter7Adapter9configureEv+0x46b)[0x7f51954ce91b]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [17] /home/[secure]/OpenFOAM/root-4.1/platforms/linux64GccDPInt32Opt/lib/lib[secure]AdapterFunctionObject.so(_ZN4Foam15functionObjects28[secure]AdapterFunctionObject4readERKNS_10dictionaryE+0xd)[0x7f5195506a1d]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [18] /home/[secure]/OpenFOAM/root-4.1/platforms/linux64GccDPInt32Opt/lib/lib[secure]AdapterFunctionObject.so(_ZN4Foam15functionObjects28[secure]AdapterFunctionObjectC2ERKNS_4wordERKNS_4TimeERKNS_10dictionaryE+0x44)[0x7f5195506ad4]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [19] /home/[secure]/OpenFOAM/root-4.1/platforms/linux64GccDPInt32Opt/lib/lib[secure]AdapterFunctionObject.so(_ZN4Foam14functionObject31adddictionaryConstructorToTableINS_15functionObjects28[secure]AdapterFunctionObjectEE3NewERKNS_4wordERKNS_4TimeERKNS_10dictionaryE+0x32)[0x7f5195506bd2]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [20] /opt/openfoam4/platforms/linux64GccDPInt32Opt/lib/libOpenFOAM.so(_ZN4Foam14functionObject3NewERKNS_4wordERKNS_4TimeERKNS_10dictionaryE+0x52c)[0x7f519c141eec]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [21] /opt/openfoam4/platforms/linux64GccDPInt32Opt/lib/libOpenFOAM.so(_ZN4Foam18functionObjectList4readEv+0xa0d)[0x7f519c1455bd]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [22] /opt/openfoam4/platforms/linux64GccDPInt32Opt/lib/libOpenFOAM.so(_ZNK4Foam4Time3runEv+0xcd)[0x7f519c155d9d]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [23] pimpleDyMFoam[0x424d13]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [24] /lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf0)[0x7f519af5c830]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] [25] pimpleDyMFoam[0x4286c9]
[32mopenfoam-adapter-fluid    |[0m [6f77c194037c:00164] *** End of error message ***
[32mopenfoam-adapter-fluid    |[0m /bin/bash: line 1:   164 Aborted                 (core dumped) pimpleDyMFoam -case /home/[secure]/Data/Input
[32mopenfoam-adapter-fluid exited with code 134
[0mOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx_fsi.Ubuntu1604.home.PETSc/referenceOutput: Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx_fsi.Ubuntu1604.home.PETSc/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx_fsi.Ubuntu1604.home.PETSc/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Fluid']
Files only in output(right)   : []
travis_time:end:1e6821be:start=1578827922060652481,finish=1578828001076626638,duration=79015974157,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1068c5c0[0K$ python push.py -t of-ccx_fsi
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635929009/log.txt)