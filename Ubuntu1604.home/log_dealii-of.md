## Status: Passing 
Build: [1484](https://travis-ci.org/precice/systemtests/builds/641298046) 

Job: [1484.23](https://travis-ci.org/precice/systemtests/jobs/641298091) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4c749ac41fec1ac0cc04f8e71fcd731e33705ab1...e37a006c80df4226e1d22b4d0f731f7780eae018) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> e7d92cdc71fe
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 9e9a7d44b684
 ---> 0127b84332ec
Removing intermediate container 9e9a7d44b684
Step 3/12 : RUN apk add git
 ---> Running in 06deec34c479
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r0)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r1)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 22 MiB in 20 packages
 ---> 9f8a406c6a08
Removing intermediate container 06deec34c479
Step 4/12 : ARG branch=develop
 ---> Running in aae8e4afde4b
 ---> 0e839662e248
Removing intermediate container aae8e4afde4b
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 527c65920e47
[91mCloning into 'tutorials'...
[0m ---> 403c611bc13f
Removing intermediate container 527c65920e47
Step 6/12 : RUN mkdir configs && sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\" to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g' 		$tutorial_path/[secure]-config.xml > configs/[secure]-config.xml
 ---> Running in ad9156645d5c
 ---> 427ad3907716
Removing intermediate container ad9156645d5c
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in d286efd8f0f8
 ---> 3dd53bf6d01e
Removing intermediate container d286efd8f0f8
Step 8/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 063af04e1154
 ---> c4abce81cb8d
Removing intermediate container 063af04e1154
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 2f25532d7fb2
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> b7b9e07440c0
Removing intermediate container 2f25532d7fb2
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in bde641a798a6
 ---> 7bf4548dd1d1
Removing intermediate container bde641a798a6
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 294bf458afb6
 ---> 6ffe216a5023
Removing intermediate container 294bf458afb6
Step 12/12 : USER [secure]
 ---> Running in d42fc52a4b7a
 ---> b52d37c12b1f
Removing intermediate container d42fc52a4b7a
Successfully built b52d37c12b1f
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:def31d1013d65c817c17d7798573862b7a630e67d5d5ba870507c83d187b879c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:56f045c657a7b7917e7a61f4dcb2751a32719bb7d96a80a0b2fcf543cc025a8d
Status: Downloaded newer image for [secure]/dealii-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter ... 
Creating openfoam-adapter
[1A[2KCreating openfoam-adapter ... [32mdone[0m[1BCreating dealii-adapter ... 
Creating dealii-adapter
[1A[2KCreating dealii-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
Test succeeded! No difference to referenceOutput found.
travis_time:end:166bcad4:start=1579866765408827560,finish=1579866961346466849,duration=195937639289,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:28c75620[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/641298091/log.txt)