//===========================================================================//
//                  F I L E     D O C U M E N T A T I O N                    //
//===========================================================================//
//                                                                           //
// Author:              Bryant                                               //
//---                                                                        //
// Title:               Palindrome                                           //
// Filename:            main.py                                              //
//---                                                                        //
// Date of Creation:    05/20/22                                             //
// Last Revised By:     N/A                                                  //
// Last Revision Date:  05/20/22                                             //
//                                                                           //
// Copyright:           Copyright © 2020 Bryant.                             //
//                      All rights reserved.                                 //
//---------------------------------------------------------------------------//
//                                                                           //
// ----------------------------------------                                  //
//- FizzBuzz Kata : Pipeline Description  :                                  //
// ----------------------------------------                                  //
//                                                                           //
//    -------------------------------                                        //
// 1 - SCM : GitHub                                                          //
//    -------------------------------                                        //
//    ...                                                                    //
//                                                                           //
//    -------------------------------                                        //
// 2 - CI  : Jenkins                                                         //
//    -------------------------------                                        //
//                                                                           //
//         - [ BUILD/COMPILE      ] : X                                      //
//      -----                                                                //
//         - [ UNIT TEST          ] : X                                      //
//         - [ INTEGRATION TESTS  ] :                                        //
//         - [ SYSTEM      TESTS  ] :                                        //
//         - [ UAD         TESTS  ] :                                        //
//      -----                                                                //
//         - [ ARCHIVE GENERATION ] : X                                      //
//         - [ ARCHIVE DEPLOYMENT ] : X                                      //
//                                                                           //
//                                                                           //
//    -------------------------------                                        //
// 3 - ARCHIVE  : AWS CodeArtifact                                           //
//    -------------------------------                                        //
//    ...                                                                    //
//                                                                           //
//    -------------------------------                                        //
//     RELEASE                                                               //
//    -----------                                                            //
// 4 - CD  : PyPI                                                            //
//   - CD  : INSTALL on LOCAL SERVER                                         //
//    -------------------------------                                        //
//    ...                                                                    //
//                                                                           //
//---------------------------------------------------------------------------//

pipeline {

    //-------------------------------------------------------------------------------------------------------
    // AGENT CREATION                                                                                       :
    //-------------------------------------------------------------------------------------------------------
    agent any 


    //-------------------------------------------------------------------------------------------------------
    // STAGING                                                                                              :
    //-------------------------------------------------------------------------------------------------------
    stages {
        //-----------------------------------------------------------
        //  R A W   D A T A                                         :
        //-----------------------------------------------------------
        // CHECKOUT (PULL)                  :
        //-----------------------------------
        stage('Checkout') { 
            steps { 
                echo "=================== [     GIT PULL REQUEST START     ] =================================================================================================================="   
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ianokam/FizzBuzz.git']]])
                echo "The JOB FILES have been PULLED . . ."                   // ...
                echo "=================== [   GIT PULL REQUEST COMPLETE    ] =================================================================================================================="   
            }
          }
        //-----------------------------------------------------------
        //  L I G H T R O O M   E D I T / B U I L D                 :
        //-----------------------------------------------------------
        // BUILD                            :
        //-----------------------------------
        stage('Build') { 
            steps {
                echo "=================== [          BUILD START           ] =================================================================================================================="   
//                 git 'https://github.com/ianokam/FizzBuzz.git'               //****************CHECK
                sh  'python3 src/program_package/*'     // Singular File := 'python3 src/main.py' 
//                 stash(name: 'compiled-results', includes: 'sources/*.py*')  //****************CHECK
                echo "The JOB has been BUILT . . ."                   // ...
                echo "=================== [         BUILD COMPLETE         ] =================================================================================================================="   
            }
        }
        //-----------------------------------------------------------
        //  L I G H T R O O M   E D I T / B U I L D                 :
        //  T E S T I N G   F O R   I M P E R F E C T I O N         : 
        //-----------------------------------------------------------
        // TEST                             :
        //-----------------------------------
        stage('Unit Tests') { 
            steps {
                echo "=================== [          TEST START            ] =================================================================================================================="   
                sh   'pip3 install pytest'                             // install pytest
                sh   'pip3 install pytest-cov'                         // install pytest-coverage
                sh   'python3 -m pytest --cov src/program_package'                     // Run Tests & Check Coverage | Alt: sh   'python3 -m coverage report'
                echo "The JOB has been TESTED . . ."                   // ...
                echo "=================== [         TEST COMPLETE          ] =================================================================================================================="   
            }//
        }
        stage('Integration Tests') { 
            steps {

                echo ". . ."   
//                   # You have the option to stand up a temporary environment to perform
//                   # these tests and/or run the tests against an existing environment. The
//                   # advantage to the former is you can ensure the environment is clean
//                   # and in a desired initial state. The easiest way to stand up a temporary
//                   # environment is to use Docker and a wrapper script to orchestrate the
//                   # process. This script will handle standing up supporting services like
//                   # MySQL & Redis, running DB migrations, starting the web server, etc.
//                   # You can utilize your existing automation, your custom scripts and Make.
//                   ./standup_testing_environment.sh # Name this whatever you'd like
//                   python -m unittest discover -s tests/integration
            }
        }
        stage('System Tests') { 
            steps {
                
                echo ". . ."             
            }
        }
        stage('Acceptance Tests (UAD)') { 
            steps {
                
                echo ". . ."             
            }
        }
        //-----------------------------------------------------------
        //  C O M P R E S S E D                             (PULL)  :
        //  P R O D U C T I O N   P A C K A G I N G                 :
        //-----------------------------------------------------------
        // ARTIFACT PACKAGING               :
        //-----------------------------------
        // ref: https://packaging.python.org/en/latest/tutorials/packaging-projects/
        stage('Artifact - Generating the Distribution Archives') { 
            steps {
                // Generating distribution archives ::
                echo "=================== [    ARTIFACT PACKAGING START    ] =================================================================================================================="   
                sh   'rm -rf *.tar.gz'                          // Old Artifact Deletion  :  Delete Old instances, if any, of the Build package
                sh   'python3 -m pip install --upgrade build'   // PYPA's                 :  Download the  latest version of PyPA’s build 
                sh   'python3 -m build'                         // New Artifact Packaging :  Run this command from the same directory where pyproject.toml is located
                //------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                //                 sh   'rm -rf *.tar.gz'                                                                           // Artifact Deletion   : Delete Old instances, if any, of the Build package
                //                 sh   'tar czf	FizzBuzz-$BUILD_NUMBER.tar.gz node_modules main.js package.json public LICENSE'  // Artifact Packaging  : Package the web app for Deployment [ ref: https://www.youtube.com/watch?v=XQt4fzt3bUc&t=262s ]
                echo "=================== [  ARTIFACT PACKAGING COMPLETE   ] =================================================================================================================="   
            }
        }
        //-----------------------------------------------------------
        //  D E C O M P R E S S E D                         (GET)   :
        //  P R O D U C T I O N   P A C K A G I N G                 :
        //-----------------------------------------------------------
        // ARTIFACT DEPLOYMENT              :
        //-----------------------------------
        stage('Artifact - Deploying the Distribution Archives') { 
                stage('Publish Build Info') {
            environment {
                JFROG_CLI_OFFER_CONFIG = false
            }
            steps {
                container('jfrog-cli-go'){
                    withCredentials([usernamePassword(credentialsId: 'gociexamplerepo', passwordVariable: 'APIKEY', usernameVariable: 'USER')]) {
                        sh "jfrog rt bce $JOB_NAME $BUILD_NUMBER"
                        sh "jfrog rt bag $JOB_NAME $BUILD_NUMBER"
                        sh "jfrog rt bad $JOB_NAME $BUILD_NUMBER \"go.*\""
                        sh "jfrog rt bp --build-url=https://jenkins.openshiftk8s.com/ --url=https://partnership.jfrog.io/artifactory --user=$USER --apikey=$APIKEY $JOB_NAME $BUILD_NUMBER"
                    }
                }
            }
        }
    }

}
