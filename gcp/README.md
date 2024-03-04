### Setup
Enable billing for your project
Stash OpenWeather API key in SecretsManager

### Set privs
In IAM: enable "Secret Manager, Secret Accessor" privilege for App Engine default service account
```
gcloud projects add-iam-policy-binding <YOUR-PROJECT-ID> --member=serviceAccount:<YOUR-PROJECT-ID>@appspot.gserviceaccount.com --role=roles/secretmanager.secretAccessor
```

### GCP Cloud shell commands to build and deploy
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
