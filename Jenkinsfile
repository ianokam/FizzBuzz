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

        //-----------------------------------
        // CHECKOUT (PULL)                  :
        //-----------------------------------
        stage('Checkout') { 
            steps {
                  checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ianokam/FizzBuzz.git']]])
            }
          }
        //-----------------------------------
        // BUILD                            :
        //-----------------------------------
        stage('Build') { 
            steps {
//                 git 'https://github.com/ianokam/FizzBuzz.git'
                sh  'python -m py_compile main.py' 
//                 stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
//         //-----------------------------------
//         // TEST                             :
//         //-----------------------------------
//         stage('Test') { 
//             steps {
//                 echo "the job has been tested"
//             }
//         }
//         //-----------------------------------
//         // DEPLOY                           :
//         //-----------------------------------
//         stage('Deploy') { 
//             steps {
//                 echo "the job has been deployed" 
//             }
//         }
    }
    //-------------------------------------
    // STAGES END.                        :
    //-------------------------------------
  
}
