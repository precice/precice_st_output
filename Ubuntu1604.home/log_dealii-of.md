## Status: Failure 
Build: [1396](https://travis-ci.org/precice/systemtests/builds/632899723) 

Job: [1396.23](https://travis-ci.org/precice/systemtests/jobs/632899746) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/1cefd5edac2aea69ea37978eeb5479db3ada0042...d9a7dc3ed7e75c17e88adc4757c7bd5f44719b24) 

---
Last 100 lines of the job log at the moment of push:
```
Creating volume "testcomposedealiiof_exchange" with default driver
Building tutorial-data
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
 ---> cc0abc535e36
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in f0d0267a8c76
 ---> c59607e85e3d
Removing intermediate container f0d0267a8c76
Step 3/12 : RUN apk add git
 ---> Running in 1804f135e5cf
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r0)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r1)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r8.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 22 MiB in 20 packages
 ---> 4da7b7940a74
Removing intermediate container 1804f135e5cf
Step 4/12 : ARG branch=develop
 ---> Running in c0de660aac64
 ---> 05e3186b8c8a
Removing intermediate container c0de660aac64
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in cd373a3224b6
[91mCloning into 'tutorials'...
[0m ---> 6fe91f9f2301
Removing intermediate container cd373a3224b6
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in e4dec193af07
 ---> 8d1a5065899a
Removing intermediate container e4dec193af07
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 5660c19ae555
 ---> 6fa2f697df2e
Removing intermediate container 5660c19ae555
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 1182acc5a07c
 ---> 831ef6def1c8
Removing intermediate container 1182acc5a07c
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in c955cc718fb6
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> a5700c163bb0
Removing intermediate container c955cc718fb6
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 06054453d3b8
 ---> c6adc26ae4ea
Removing intermediate container 06054453d3b8
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in aef13e3f40f4
 ---> fe4ac78508a3
Removing intermediate container aef13e3f40f4
Step 12/12 : USER [secure]
 ---> Running in 7c7a8ee6ddce
 ---> 6aebb732b7b6
Removing intermediate container 7c7a8ee6ddce
Successfully built 6aebb732b7b6
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:3ab18c507e8bd47b0be2b872093edcab70bf5a758a63df93a1878c720f6aeddb
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:de7bb62e33a13596f397f653139508a376e588957346c1916006bf4fe6fc8bae
Status: Downloaded newer image for [secure]/dealii-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter ... 
Creating openfoam-adapter
[1A[2KCreating openfoam-adapter ... [32mdone[0m[1BCreating dealii-adapter ... 
Creating dealii-adapter
[1A[2KCreating dealii-adapter ... [32mdone[0m[1BAll adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/referenceOutput: Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Fluid']
Files only in output(right)   : []
travis_time:end:010707a4:start=1578223929930985327,finish=1578224005391007334,duration=75460022007,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:06ea9fe4[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/632899746/log.txt)