pipeline {
    agent any // L'agent spécifie où le pipeline sera exécuté (dans ce cas, n'importe quel agent disponible).

    stages {
        stage('Checkout') {
            steps {
                // Étape pour récupérer le code source du référentiel Git
                script {
                    git branch: 'main', // Branche Git à vérifier
                        url: 'https://github.com/ameni56/ProjectDjango' // URL du référentiel Git
                }
            }
        }

        stage('Build') {
            steps {
                // Étape pour construire votre application (par exemple, compilation, assemblage)
                sh 'npm install' // Exemple d'instruction de construction
            }
        }

        stage('Test') {
            steps {
                // Étape pour exécuter des tests automatisés
                sh 'npm test' // Exemple d'instruction de test
            }
        }

        stage('Deploy') {
            steps {
                // Étape pour déployer votre application (par exemple, sur un serveur)
                sh 'npm deploy' // Exemple d'instruction de déploiement
            }
        }
    }

    post {
        success {
            // Étape exécutée en cas de succès du pipeline
            echo 'Le pipeline a réussi !'
        }

        failure {
            // Étape exécutée en cas d'échec du pipeline
            echo 'Le pipeline a échoué.'
        }
    }
}
