from google.cloud import storage

def download_model(bucket_name, model_name, local_path):
    client = storage.Client() 
    bucket = client.bucket(bucket_name) 
    blob = bucket.blob(model_name) 
    blob.download_to_filename(local_path) 
