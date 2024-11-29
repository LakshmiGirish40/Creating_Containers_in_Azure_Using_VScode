from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError
from io import BytesIO
from PIL import Image
import pandas as pd
import os

# Azure Blob Storage configuration
blob_account_url = '--------AzureStoragecontainerurl'
storage_credential = '---------addazuretoken'

blob_service_client = BlobServiceClient(account_url=blob_account_url, credential=storage_credential)

all_containers = blob_service_client.list_containers()
all_containers

all_containers=blob_service_client.list_containers()
for container in all_containers:
    print("deleting:",'mycontainer3')
    blob_service_client.delete_container('mycontainer3')
