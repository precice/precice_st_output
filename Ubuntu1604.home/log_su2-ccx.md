## Status: Failure 
Build: [1442](https://travis-ci.org/precice/systemtests/builds/635918218) 

Job: [1442.1](https://travis-ci.org/precice/systemtests/jobs/635918219) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/152) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
[32msu2-adapter         |[0m  Computing grid velocities by finite differencing due to preCICE simulation.
[32msu2-adapter         |[0m 
[32msu2-adapter         |[0m Min DT: 6.90855e-05.Max DT: 0.000319416.Dual Time step: 0.01.
[32msu2-adapter         |[0m ----------------------- Residual Evolution Summary ----------------------
[32msu2-adapter         |[0m log10[Maximum residual]: -3.05341.
[32msu2-adapter         |[0m Maximum residual point 53, located at (0.569149, 0.3, 0.505287).
[32msu2-adapter         |[0m -------------------------------------------------------------------------
[32msu2-adapter         |[0m 
[32msu2-adapter         |[0m  IntIter ExtIter     Res[Rho]     Res[RhoE]      CL(Total)      CD(Total)
[32msu2-adapter         |[0m        0     400    -3.831056      1.619262       0.000000       0.000000
[32msu2-adapter         |[0m        1     400    -3.905523      1.539099       0.000000       0.000000
[32msu2-adapter         |[0m        2     400    -4.011551      1.425152       0.000000       0.000000
[32msu2-adapter         |[0m        3     400    -4.156666      1.267519       0.000000       0.000000
[32msu2-adapter         |[0m        4     400    -4.349312      1.053101       0.000000       0.000000
[32msu2-adapter         |[0m        5     400    -4.555565      0.834533       0.000000       0.000000
[32msu2-adapter         |[0m        6     400    -4.566696      0.890016       0.000000       0.000000
[32msu2-adapter         |[0m        7     400    -4.429679      1.051060       0.000000       0.000000
[32msu2-adapter         |[0m        8     400    -4.318016      1.164327       0.000000       0.000000
[32msu2-adapter         |[0m        9     400    -4.242495      1.239121       0.000000       0.000000
[32msu2-adapter         |[0m       10     400    -4.191053      1.290231       0.000000       0.000000
[32msu2-adapter         |[0m 
[32msu2-adapter         |[0m ------------------------ Evaluate Special Output ------------------------
[32msu2-adapter         |[0m Writing the forces breakdown file (forces_breakdown.dat).
[32msu2-adapter         |[0m -------------------------------------------------------------------------
[32msu2-adapter         |[0m 
[32msu2-adapter         |[0m 
[32msu2-adapter         |[0m ---[[secure]] [0m Timestep completed
[32msu2-adapter         |[0m ---[[secure]] [0m it 1 of 50 | dt# 401 of 400 | t 4 | dt 0.01 | max dt 0.01 | ongoing no | dt complete yes | 
[32msu2-adapter         |[0m 
[32msu2-adapter         |[0m -------------------------- File Output Summary --------------------------
[32msu2-adapter         |[0m Writing comma-separated values (CSV) surface files.
[32msu2-adapter         |[0m Loading solution output data locally on each rank.
[32msu2-adapter         |[0m Sorting output data across all ranks.
[32msu2-adapter         |[0m Writing ASCII SU2 native restart file.
[32msu2-adapter         |[0m Preparing element connectivity across all ranks.
[32msu2-adapter         |[0m Writing Paraview ASCII volume solution file.
[32msu2-adapter         |[0m -------------------------------------------------------------------------
[32msu2-adapter         |[0m 
[32msu2-adapter         |[0m 
[32msu2-adapter         |[0m ------------------------- Solver Postprocessing -------------------------
[32msu2-adapter         |[0m Deleted CNumerics container.
[32msu2-adapter         |[0m Deleted CIntegration container.
[32msu2-adapter         |[0m Deleted CSolver container.
[32msu2-adapter         |[0m Deleted CIteration container.
[32msu2-adapter         |[0m Deleted CInterpolator container.
[32msu2-adapter         |[0m Deleted CTransfer container.
[32msu2-adapter         |[0m Deleted CGeometry container.
[32msu2-adapter         |[0m Deleted CFreeFormDefBox class.
[32msu2-adapter         |[0m Deleted CSurfaceMovement class.
[32msu2-adapter         |[0m Deleted CVolumetricMovement class.
[32msu2-adapter         |[0m Deleted CConfig container.
[32msu2-adapter         |[0m Deleted COutput class.
[32msu2-adapter         |[0m -------------------------------------------------------------------------
[32msu2-adapter         |[0m 
[32msu2-adapter         |[0m Completed in 156.463497 seconds on 1 core.
[32msu2-adapter         |[0m Process #0/0: Finalizing preCICE...
[32msu2-adapter         |[0m Run finished at Sun Jan 12 09:52:06 2020
[32msu2-adapter         |[0m Global runtime       = 175253.000000ms / 175.253000s
[32msu2-adapter         |[0m Number of processors = 1
[32msu2-adapter         |[0m # Rank: 0
[32msu2-adapter         |[0m 
[32msu2-adapter         |[0m                                                                          Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
[32msu2-adapter         |[0m --------------------------------------------------------------------------------------------------------------------------------------------------------------
[32msu2-adapter         |[0m                                                                        _GLOBAL |          1 |     175253 |     175253 |     175253 |     175253 |      1.000 |
[32msu2-adapter         |[0m                                                                        advance |        934 |       1337 |         11 |          0 |          1 |      0.008 |
[32msu2-adapter         |[0m                                                        advance/m2n.receiveData |        934 |        162 |          6 |          0 |          0 |      0.001 |
[32msu2-adapter         |[0m                                                           advance/m2n.sendData |        934 |        409 |          9 |          0 |          0 |      0.002 |
[32msu2-adapter         |[0m                     advance/map.nn.computeMapping.FromCalculix_MeshToSU2_Mesh0 |          1 |          0 |          0 |          0 |          0 |      0.000 |
[32msu2-adapter         |[0m  advance/map.nn.computeMapping.FromCalculix_MeshToSU2_Mesh0.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |      0.000 |
[32msu2-adapter         |[0m                     advance/map.nn.computeMapping.FromSU2_Mesh0ToCalculix_Mesh |          1 |          0 |          0 |          0 |          0 |      0.000 |
[32msu2-adapter         |[0m  advance/map.nn.computeMapping.FromSU2_Mesh0ToCalculix_Mesh.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |      0.000 |
[32msu2-adapter         |[0m                            advance/map.nn.mapData.FromCalculix_MeshToSU2_Mesh0 |        934 |          1 |          0 |          0 |          0 |      0.000 |
[32msu2-adapter         |[0m                            advance/map.nn.mapData.FromSU2_Mesh0ToCalculix_Mesh |        934 |          3 |          1 |          0 |          0 |      0.000 |
[32msu2-adapter         |[0m                                                                      configure |          1 |          0 |          0 |          0 |          0 |      0.000 |
[32msu2-adapter         |[0m                                                                       finalize |          1 |         37 |         37 |         37 |         37 |      0.000 |
[32msu2-adapter         |[0m                                                                     initialize |          1 |         48 |         48 |         48 |         48 |      0.000 |
[32msu2-adapter         |[0m                                    initialize/m2n.broadcastVertexDistributions |          1 |          0 |          0 |          0 |          0 |      0.000 |
[32msu2-adapter         |[0m                                           initialize/m2n.buildCommunicationMap |          1 |          0 |          0 |          0 |          0 |      0.000 |
[32msu2-adapter         |[0m                                            initialize/m2n.createCommunications |          1 |          1 |          1 |          1 |          1 |      0.000 |
[32msu2-adapter         |[0m                ----------------------------------------------------------
[32msu2-adapter         |[0m                                                                        _GLOBAL | 175253.000000 |          0 | 175253.000000 |          0 |   1.000000 |
[32msu2-adapter         |[0m                                                                        advance |  11.000000 |          0 |   0.000000 |          0 |   0.000000 |
[32msu2-adapter         |[0m                                                        advance/m2n.receiveData |   6.000000 |          0 |   0.000000 |          0 |   0.000000 |
[32msu2-adapter         |[0m                                                           advance/m2n.sendData |   9.000000 |          0 |   0.000000 |          0 |   0.000000 |
[32msu2-adapter         |[0m                     advance/map.nn.computeMapping.FromCalculix_MeshToSU2_Mesh0 |   0.000000 |          0 |   0.000000 |          0 |   0.000000 |
[32msu2-adapter         |[0m  advance/map.nn.computeMapping.FromCalculix_MeshToSU2_Mesh0.getIndexOnVertices |   0.000000 |          0 |   0.000000 |          0 |   0.000000 |
[32msu2-adapter         |[0m                     advance/map.nn.computeMapping.FromSU2_Mesh0ToCalculix_Mesh |   0.000000 |          0 |   0.000000 |          0 |   0.000000 |
[32msu2-adapter         |[0m  advance/map.nn.computeMapping.FromSU2_Mesh0ToCalculix_Mesh.getIndexOnVertices |   0.000000 |          0 |   0.000000 |          0 |   0.000000 |
[32msu2-adapter         |[0m                            advance/map.nn.mapData.FromCalculix_MeshToSU2_Mesh0 |   0.000000 |          0 |   0.000000 |          0 |   0.000000 |
[32msu2-adapter         |[0m                            advance/map.nn.mapData.FromSU2_Mesh0ToCalculix_Mesh |   1.000000 |          0 |   0.000000 |          0 |   0.000000 |
[32msu2-adapter         |[0m                                                                      configure |   0.000000 |          0 |   0.000000 |          0 |   0.000000 |
[32msu2-adapter         |[0m                                                                       finalize |  37.000000 |          0 |  37.000000 |          0 |   1.000000 |
[32msu2-adapter         |[0m                                                                     initialize |  48.000000 |          0 |  48.000000 |          0 |   1.000000 |
[32msu2-adapter         |[0m                                    initialize/m2n.broadcastVertexDistributions |   0.000000 |          0 |   0.000000 |          0 |   0.000000 |
[32msu2-adapter         |[0m                                           initialize/m2n.buildCommunicationMap |   0.000000 |          0 |   0.000000 |          0 |   0.000000 |
[32msu2-adapter         |[0m                                            initialize/m2n.createCommunications |   1.000000 |          0 |   1.000000 |          0 |   1.000000 |
[32msu2-adapter         |[0m                                      initialize/m2n.exchangeVertexDistribution |  42.000000 |          0 |  42.000000 |          0 |   1.000000 |
[32msu2-adapter         |[0m                                         initialize/m2n.requestMasterConnection |   1.000000 |          0 |   1.000000 |          0 |   1.000000 |
[32msu2-adapter         |[0m      [32msu2-adapter exited with code 0
[0m
```
[
Full job log](https://api.travis-ci.org/v3/job/635918219/log.txt)