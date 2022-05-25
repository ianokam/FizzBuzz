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
                sh  'python3 main.py' 
//                 stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
        //-----------------------------------
        // TEST                             :
        //-----------------------------------
        stage('Test') { 
            steps {
                echo "the job has been tested"
                sh   'pip3 install pytest'           // install pytest
                sh   'pip3 install pytest-cov'       // install pytest-coverage
                export PATH="/Users/ibeawuchi/Library/Python/3.8/bin/:$PATH"
                sh   'pytest --cov FizzBuzz'   // Run Tests & Check Coverage
            }
        }
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
