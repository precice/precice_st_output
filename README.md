# Build log repository for preCICE/systemtests

This repository serves as storage for TravisCI logs and other output files generated from tests run from the [systemtests repository](https://github.com/precice/systemtests).

Each of the numbered folders corresponds to a specific build on TravisCI, with a new build taking the next higher number. Inside each build folder separate folders for each job are stored.
## Finding your build folder

To obtain the number associated with your build, first **check your commit/PR on GitHub to find a link to the TravisCI build that was triggered from it** (or directly go to the TravisCI website if you have access rights). There you should find your triggered build and its associated **build number**. This number will match the name of the folder here that contains your build data.

_Note: a build folder will be created only after the conclusion of its tests._
