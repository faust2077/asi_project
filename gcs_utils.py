https://console.cloud.google.com/stofrom google.cloud import storage
def download_model(bucket_name, model_name, local_path):
    client = storage.Client() # Inicjalizacja klienta GCP (działa
    na podstawie lokalnych poświadczeń lub zmiennej środowiskowej
    GOOGLE_APPLICATION_CREDENTIALS)
    bucket = client.bucket(bucket_name) # Pobranie wybranego
    bucket z Google Cloud Storage
    blob = bucket.blob(model_name) # Referencja do konkretnego
    pliku w chmurze (tu: model.joblib)
    blob.download_to_filename(local_path) # Pobranie pliku do
    lokalnego systemu plików
    print(f"Pobrano model: {model_name}")raghttps://console.cloud.google.com/storagee
