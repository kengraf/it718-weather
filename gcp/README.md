Enable billing for your project
In IAM: enable "Secret Manager, Secret Accessor privledge for App Engine default service account

Stash OpenWeather API key in SecretsManager

GCP Cloud shell commands to build and deploy your function
```
gcloud config set project unh-it718
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable artifactregistry.googleapis.com
git clone https://github.com/kengraf/it718-weather.git
cd it718-weather/gcp/
gcloud functions deploy get_weather --runtime python312 --trigger-http --allow-unauthenticated
```

Test the deployment, your URL in output of functions deploy command
```
curl https://<YOUR-REGION>-<YOUR-PROJECT-ID>.cloudfunctions.net/get_weather?zip=03824
```
