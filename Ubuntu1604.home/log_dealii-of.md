## Status: Failure 
Build: [1666](https://travis-ci.org/precice/systemtests/builds/648938191) 

Job: [1666.14](https://travis-ci.org/precice/systemtests/jobs/648938205) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/174) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/1cefd5edac2aea69ea37978eeb5479db3ada0042...d9a7dc3ed7e75c17e88adc4757c7bd5f44719b24) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> 0cdf4c8577b0
Removing intermediate container d6ed4ba944be
Step 4/12 : ARG branch=develop
 ---> Running in e797448ee2ed
 ---> f060e366927f
Removing intermediate container e797448ee2ed
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 10e9873d41b7
[91mCloning into 'tutorials'...
[0m ---> 81d534db662c
Removing intermediate container 10e9873d41b7
Step 6/12 : RUN mkdir configs && sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\" to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g' 		$tutorial_path/[secure]-config.xml > configs/[secure]-config.xml
 ---> Running in d62d8d0a4be7
 ---> e01555ce4647
Removing intermediate container d62d8d0a4be7
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 73f5459e467b
 ---> c50d3d6a1a43
Removing intermediate container 73f5459e467b
Step 8/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 1987eb4b11bc
 ---> 450435f5945d
Removing intermediate container 1987eb4b11bc
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in ff50b610d8be
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 6ce84ca31168
Removing intermediate container ff50b610d8be
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 5e70aa97f0a8
 ---> fab844969364
Removing intermediate container 5e70aa97f0a8
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0f29e98f4bda
 ---> 5803c412bd86
Removing intermediate container 0f29e98f4bda
Step 12/12 : USER [secure]
 ---> Running in a7c23432dccf
 ---> 10fefbfe193e
Removing intermediate container a7c23432dccf
Successfully built 10fefbfe193e
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:f4a35c80e3584b3e11b7da5bf50b88da768fe5fe965b027645946b3c174412f9
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:19176a829af9af3c822d8d605e0070dd65bbd2a499986da38faa316b9859bee0
Status: Downloaded newer image for [secure]/dealii-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter ... 
Creating openfoam-adapter
[1A[2KCreating openfoam-adapter ... [32mdone[0m[1BCreating dealii-adapter ... 
Creating dealii-adapter
[1A[2KCreating dealii-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Timeout!
Printing logs for services:
Attaching to dealii-adapter
[36mdealii-adapter      |[0m --------------------------------------------------
[36mdealii-adapter      |[0m              Running deal.ii solver 
[36mdealii-adapter      |[0m --------------------------------------------------
[36mdealii-adapter      |[0m 
[36mdealii-adapter      |[0m Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/IL4LD5XVKBSWJD5F5ZTBPMRCN7:/var/lib/docker/overlay2/l/7T6YSTBZTBTHZGU7XUYKZ4U6IK:/var/lib/docker/overlay2/l/7ZMDNGSH22W2KR6COVN4IJ64UK:/var/lib/docker/overlay2/l/O37T2ZKL2PPAQQ55SOQQWTWGOP:/var/lib/docker/overlay2/l/Q3G3HOR7ZVZVSVOOXSYQY2P32B:/var/lib/docker/overlay2/l/3MSCRPOV3VW42GESEYNWJXZD3Z:/var/lib/docker/overlay2/l/SFLO5O2IGY4OHCCA66CYIEZLZX:/var/lib/docker/overlay2/l/M64EDGM7GE7BVD7HG7KWPYF3O5:/var/lib/docker/overlay2/l/Z2PBXTBIHBL4B'
[36mdealii-adapter      |[0m Unexpected end of /proc/mounts line `JLFBBOUX5TLQP:/var/lib/docker/overlay2/l/T7X4DCDP5LJPBCQCLH5GRZCJJE:/var/lib/docker/overlay2/l/6OVYDCFUAKSVBJP23SIJVDLJB4:/var/lib/docker/overlay2/l/22LKFUIGU2LN5YCHK57HUXMWQY:/var/lib/docker/overlay2/l/FMBLUV223C26RQXXVGQM7SPDOF:/var/lib/docker/overlay2/l/OHLBWAL75XGL5XR2ADMWHK4KWN:/var/lib/docker/overlay2/l/FAVQOFUC52DHNYRNTG4GPI5CV6:/var/lib/docker/overlay2/l/HPGFTPZKUETQOPIRLT57OKHDQR:/var/lib/docker/overlay2/l/ZRQKPKJ2JRKHPQNILNJPELU74E:/var/lib/docker/overlay2/l/V74PLCS6GB7GHWB3XFEWW7WISJ:/var/lib/do'
[36mdealii-adapter      |[0m ---[[secure]] [0m This is preCICE version 2.0.0
[36mdealii-adapter      |[0m ---[[secure]] [0m Revision info: v2.0.0-2-g56832a9
[36mdealii-adapter      |[0m ---[[secure]] [0m Configuring preCICE with configuration: "[secure]-config.xml"
[36mdealii-adapter      |[0m   Create mesh: 
[36mdealii-adapter      |[0m 	 Number of active cells:       150
[36mdealii-adapter      |[0m   Setup system: 
[36mdealii-adapter      |[0m 	 Number of degrees of freedom: 1116
[36mdealii-adapter      |[0m 	 Output written to solution-0.vtk 
[36mdealii-adapter      |[0m 
[36mdealii-adapter      |[0m 	 Number of coupling nodes:     132
[36mdealii-adapter      |[0m 	 Number of coupling faces:     65
[36mdealii-adapter      |[0m ---[[secure]] [0m Setting up master communication to coupling partner/s
Stopping dealii-adapter ... 
[1A[2KStopping dealii-adapter ... [32mdone[0m[1BEXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh ' returned non-zero exit status 1
travis_time:end:3402ba5a:start=1581433359891948695,finish=1581434093894874496,duration=734002925801,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:08d85d30[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/648938205/log.txt)