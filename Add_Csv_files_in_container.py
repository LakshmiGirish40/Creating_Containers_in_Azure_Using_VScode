from azure.storage.blob import BlobServiceClient
import pandas as pd
from io import BytesIO

# Azure Storage credentials
blob_account_url = 'https://lakshmiazureml.blob.core.windows.net'
storage_credential = 'Rgp/QondzZQ42f8nVBXjnHmZGyCwt/GTbnKCT5wdugzHza9/UqFxvvm2vwv3dczixD+RSQq4O+gE+AStGy9dkA=='

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient(account_url=blob_account_url, credential=storage_credential)

# Create a container with public access
container_name = 'mycontainer3'
new_container = blob_service_client.create_container(container_name, public_access="container")
print("Container created:", new_container.get_container_properties())

# List all containers
print("Containers in the account:")
for container in blob_service_client.list_containers():
    print(container.name)

# Upload the file to the blob
blob_name = 'House_data.csv'
file_path = r'lib\House_data.csv'
container_client = blob_service_client.get_container_client(container_name)
blob_client = container_client.get_blob_client(blob_name)

with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
print(f"Uploaded {blob_name} to {container_name}.")

# Download and read the CSV file
blob_client = blob_service_client.get_blob_client(container_name, blob_name)
data = blob_client.download_blob().readall()
df = pd.read_csv(BytesIO(data))
print("Downloaded DataFrame:")
print(df)
