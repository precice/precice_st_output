 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584268195) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/69fcf48ce4a0) 
## Last succesfull commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/436446ec1401fb5693dc0df2b718330ca26744f9...71eeed0aa3ca179a906793d59f6576c8e42850c1)
* [systemtests](https://github.com/precice/systemtests/compare/32fdbbbc7d35f2395ee394dc8113d538b3dd86a1...04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4) 
## Last 100 lines of the job log at the moment of push...
```
 Building tutorial-data
Step 1/11 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
 ---> 961769676411
Step 2/11 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in ae7068df1d8c
 ---> 0adcec6684bc
Removing intermediate container ae7068df1d8c
Step 3/11 : RUN apk add git
 ---> Running in 0ee696b86704
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20190108-r0)
(2/6) Installing nghttp2-libs (1.39.2-r0)
(3/6) Installing libcurl (7.65.1-r0)
(4/6) Installing expat (2.2.7-r0)
(5/6) Installing pcre2 (10.33-r0)
(6/6) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 21 MiB in 20 packages
 ---> 047deebf0b23
Removing intermediate container 0ee696b86704
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 3502a56a2f5a
[91mCloning into 'tutorials'...
[0m ---> fc6678bdcb7a
Removing intermediate container 3502a56a2f5a
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 8c4a45447c21
 ---> d64f20c6a3c5
Removing intermediate container 8c4a45447c21
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 505345173fdf
 ---> 5586599683fd
Removing intermediate container 505345173fdf
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 73e4713509e5
 ---> dd47078fff80
Removing intermediate container 73e4713509e5
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 0b35ee7495e2
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 979b043dfe4b
Removing intermediate container 0b35ee7495e2
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in e75674a867d7
 ---> 7ceb80ae6644
Removing intermediate container e75674a867d7
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 5e17763a7317
 ---> ebb485c6fd79
Removing intermediate container 5e17763a7317
Step 11/11 : USER [secure]
 ---> Running in 6d06cd613957
 ---> f6bd1c7c5ea6
Removing intermediate container 6d06cd613957
Successfully built f6bd1c7c5ea6
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:193947ff1e590caf032a10505ac90c1462765a1ecdf4025f9099eb1f318998a1
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:1b75e825f5a3a41af29f0024e9bfb467d45705de8a0e646efc0566256f2ffd0a
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
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
Traceback (most recent call last):
  File "system_testing.py", line 199, in <module>
    args.force_rebuild, False)
  File "system_testing.py", line 162, in build_run_compare
    run_compose(test, branch, local_[secure], tag, force_rebuild, rm_all)
  File "system_testing.py", line 101, in run_compose
    test_basename in custom_tolerance.keys() else custom_tolerance[test_basename])
AttributeError: 'set' object has no attribute 'keys'
travis_time:end:0e898282:start=1568315615650842135,finish=1568315885668020734,duration=270017178599,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:262907e0[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584268213/log.txt)