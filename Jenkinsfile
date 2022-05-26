pipeline {
    //-------------------------------------
    // AGENT                              :
    //-------------------------------------
    agent any 

//-------------------------------------------------
    //-------------------------------------
    // STAGES BEGIN                       :
    //-------------------------------------
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
                sh  'python3 Program/*'     // Singular File := 'python3 Program/main.py' 
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
                sh   'python3 -m pytest --cov Program'                               // Run Tests & Check Coverage | Alt: sh   'python3 -m coverage report'
                echo "The JOB has been TESTED . . ."                   // ...
                echo "=================== [         TEST COMPLETE          ] =================================================================================================================="   
            }
        }
        stage('Integration Tests') { 
            steps {

                echo ". . ."   
            }
        }
        stage('System Tests') { 
            steps {
                
                echo ". . ."             
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
        stage('Artifact-Package') { 
            steps {
                
                echo ". . ."             
            }
        }
        //-----------------------------------------------------------
        //  D E C O M P R E S S E D                         (GET)   :
        //  P R O D U C T I O N   P A C K A G I N G                 :
        //-----------------------------------------------------------
        // ARTIFACT DEPLOYMENT              :
        //-----------------------------------
        stage('Artifact-Deploy') { 
            steps {
                
                echo ". . ."             
            }
        }
    }
    //-------------------------------------
    // STAGES END.                        :
    //-------------------------------------
  
}
