Enable billing for your project

Stash OpenWeather API key in SecretsManager


```
gcloud config set project unh-it718
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud functions deploy get_weather --runtime python37 --trigger-http --allow-unauthenticated
```
