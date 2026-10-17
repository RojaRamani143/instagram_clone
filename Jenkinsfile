pipeline {
    agent any
    environment {
        IMAGE_NAME = 'ramaniroja/instagram-clone'
        IMAGE_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = 'instagram-container'
    }
    stages {
        stage('Code') {
            steps {
                git branch: 'main', url: 'https://github.com/RojaRamani143/instagram-clone.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }
        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        set -eu
                        export DOCKER_CONFIG="$(mktemp -d)"
                        trap 'docker logout >/dev/null 2>&1 || true; rm -rf "$DOCKER_CONFIG"' EXIT
                        printf '%s' "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} --restart unless-stopped -p 9349:5000 ${IMAGE_NAME}:${IMAGE_TAG}
                    sleep 3
                    curl --fail http://localhost:9349/health
                '''
            }
        }
    }
}
