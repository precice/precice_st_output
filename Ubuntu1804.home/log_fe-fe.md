 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584268195) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/69fcf48ce4a0) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/32fdbbbc7d35f2395ee394dc8113d538b3dd86a1...04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4)
* [fenics-adapter](https://github.com/precice/fenics-adapter/compare/8231e64b5294...6bfb8a5ba7b3) 
## Last 100 lines of the job log at the moment of push...
```
     networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
    - input:/home/[secure]/Data/Input:rw
  tutorial-data:
    build:
      context: /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home
      dockerfile: Dockerfile.tutorial_data
      network: host
    container_name: tutorial-data
    volumes:
    - output:/Output:rw
    - input:/tutorials/HT/partitioned-heat/fenics-fenics:rw
version: '3.4'
volumes:
  exchange: {}
  input: {}
  output: {}

Creating network "testcomposefefeubuntu1804home_default" with the default driver
Creating network "testcomposefefeubuntu1804home_[secure]comm" with the default driver
Creating volume "testcomposefefeubuntu1804home_output" with default driver
Creating volume "testcomposefefeubuntu1804home_input" with default driver
Creating volume "testcomposefefeubuntu1804home_exchange" with default driver
Building tutorial-data
Step 1/7 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
 ---> 961769676411
Step 2/7 : ENV tutorial_path tutorials/HT/partitioned-heat/fenics-fenics
 ---> Running in dfd4d68beace
 ---> 63d582992bcc
Removing intermediate container dfd4d68beace
Step 3/7 : RUN apk add git
 ---> Running in e129ba991eb0
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
 ---> 1e2274b71253
Removing intermediate container e129ba991eb0
Step 4/7 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 66ef9a648f50
[91mCloning into 'tutorials'...
[0m ---> bb5eac4f80db
Removing intermediate container 66ef9a648f50
Step 5/7 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in 2211ae10b8ca
 ---> e4880bfb4b82
Removing intermediate container 2211ae10b8ca
Step 6/7 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 30279cf7ce62
 ---> 2836cbae4164
Removing intermediate container 30279cf7ce62
Step 7/7 : USER [secure]
 ---> Running in 1672f05f68b1
 ---> 6be005c0086d
Removing intermediate container 1672f05f68b1

Successfully built 6be005c0086d
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:bb8c4f048346796354337c7430048dd648a577e643fb280fe587c6a1bd631d83
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-neumann ... 
Creating fenics-adapter-dirichlet ... 
Creating fenics-adapter-dirichlet
Creating fenics-adapter-neumann
[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
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
travis_time:end:002e933e:start=1568315405415770835,finish=1568315532797664381,duration=127381893546,event=script[0K[31;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1408ed00[0K$ python push.py -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584268211/log.txt)