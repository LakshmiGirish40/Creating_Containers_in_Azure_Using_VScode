from azure.storage.blob import BlobServiceClient
import pandas as pd
from PIL import Image
from io import BytesIO
import os
from azure.storage.blob import BlobServiceClient

blob_account_url = 'https://lakshmiazureml.blob.core.windows.net'
storage_credential = 'Rgp/QondzZQ42f8nVBXjnHmZGyCwt/GTbnKCT5wdugzHza9/UqFxvvm2vwv3dczixD+RSQq4O+gE+AStGy9dkA=='

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient(account_url=blob_account_url, credential=storage_credential)

blob_service_client

# Create a container with public access
new_container = blob_service_client.create_container('mycontainer3', public_access="container")

new_container.get_container_properties()

all_containers = blob_service_client.list_containers()
all_containers

all_containers=blob_service_client.list_containers()
# the variable is a iterator, you need to get outputs by using for loop
for container in all_containers:
    print(container)

