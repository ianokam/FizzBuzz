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
                  checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ianokam/FizzBuzz.git']]])
            }
          }
        //-----------------------------------
        // BUILD                            :
        //-----------------------------------
        stage('Build') { 
            steps {
                git 'https://github.com/ianokam/FizzBuzz.git'
                sh  'python3 main.py'
            }
        }
        //-----------------------------------
        // TEST                             :
        //-----------------------------------
        stage('Test') { 
            steps {
                echo "the job has been tested"
            }
        }
        //-----------------------------------
        // DEPLOY                           :
        //-----------------------------------
        stage('Deploy') { 
            steps {
                // 
            }
        }
    }
    //-------------------------------------
    // STAGES BEGIN                       :
    //-------------------------------------
  
}
