# Build log repository for preCICE/systemtests

This repository serves as storage for TravisCI logs and other output files generated from tests run from the [systemtests repository](https://github.com/precice/systemtests).

Each of the numbered folders corresponds to a specific build on TravisCI, with a new build taking the next higher number. 

## Folder contents

Inside each build folder separate folders for each job are stored. Each job contains:
- a small README with additional job information
- a `Logs` folder containing logs of the TravisCI job and the docker containers
- **[Optional]** an `Output` folder containing result data and iteration/convergence logs created during execution of the test. To enable this, add the argument `-o` or `--output` to the push.py execution for your test in precice/systemtests (Example: `python push.py -t fe-fe --base Ubuntu1804.home -o`). 


## Finding your build folder

To obtain the number associated with your build, first **check your commit/PR on GitHub to find a link to the TravisCI build that was triggered from it** (or directly go to the TravisCI website if you have access rights). There you should find your triggered build and its associated **build number**. This number will match the name of the folder here that contains your build data.

_Note: a build folder will be created only after the first test concludes._
