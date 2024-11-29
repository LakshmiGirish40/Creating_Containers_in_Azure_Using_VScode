from azure.storage.blob import BlobServiceClient
import pandas as pd
from PIL import Image
from io import BytesIO

# Azure Storage credentials
blob_account_url = 'https://lakshmiazureml.blob.core.windows.net'
storage_credential = 'Rgp/QondzZQ42f8nVBXjnHmZGyCwt/GTbnKCT5wdugzHza9/UqFxvvm2vwv3dczixD+RSQq4O+gE+AStGy9dkA=='

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient(account_url=blob_account_url, credential=storage_credential)

# Create a container with public access
container_name = 'mycontainer'

# List all containers
print("Containers in the account:")
for container in blob_service_client.list_containers():
    print(container.name)

# Upload the image file to the blob
blob_name = 'image.jpg'
file_path = r'lib\happy1.jpg'
container_client = blob_service_client.get_container_client(container_name)
blob_client = container_client.get_blob_client(blob_name)

with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
print(f"Uploaded {blob_name} to {container_name}.")

# Download and process the image file
blob_client = blob_service_client.get_blob_client(container_name, blob_name)
data = blob_client.download_blob().readall()
image = Image.open(BytesIO(data))
image.show()  # Display the image