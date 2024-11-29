from azure.storage.blob import BlobServiceClient
import pandas as pd
from PIL import Image
from io import BytesIO
import os
from azure.storage.blob import BlobServiceClient

blob_account_url = '--------AzureStorageurl'
storage_credential = '---------add token'

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient(account_url=blob_account_url, credential=storage_credential)

blob_service_client

# Create a container with public access
new_container = blob_service_client.create_container('mycontainer1', public_access="container")

new_container.get_container_properties()

all_containers = blob_service_client.list_containers()
all_containers

all_containers=blob_service_client.list_containers()
# the variable is a iterator, you need to get outputs by using for loop
for container in all_containers:
    print(container)

    
blob_account_url ='https://lakshmiazureml.blob.core.windows.net'
storage_credential = 'Rgp/QondzZQ42f8nVBXjnHmZGyCwt/GTbnKCT5wdugzHza9/UqFxvvm2vwv3dczixD+RSQq4O+gE+AStGy9dkA=='
blob_service_client=BlobServiceClient(account_url=blob_account_url,credential=storage_credential)

new_container = blob_service_client.create_container('mycontainer1',public_access="container")
new_container

all_containers=blob_service_client.list_containers()


blob_name='sample.txt'
file_path=r'C:\Users\laksh\VS_Code\Deep_learning\myenv\Python_Azure\lib\sample.txt'
container_client = blob_service_client.get_container_client('mycontainer1')
blob_client = container_client.get_blob_client(blob_name)
# Upload the file to the blob
with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

blob_name='happy1.jpg'
file_path=r"C:\Users\laksh\VS_Code\Deep_learning\myenv\Python_Azure\lib\happy1.jpg"
container_client = blob_service_client.get_container_client('mycontainer1')
blob_client = container_client.get_blob_client(blob_name)
# Upload the file to the blob
with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
    
blob_name='emp_sal.csv'
file_path=r'C:\Users\laksh\VS_Code\Deep_learning\myenv\Python_Azure\lib\emp_sal.csv'
container_client = blob_service_client.get_container_client('mycontainer1')
blob_client = container_client.get_blob_client(blob_name)
# Upload the file to the blob
with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
    

container_client = blob_service_client.get_container_client('mycontainer1')
for blob in container_client.list_blobs():
   print(blob) 

blob_client=blob_service_client.get_blob_client('mycontainer1','emp_sal.csv')
data=blob_client.download_blob()
import pandas as pd
pd.read_csv(data)

blob_client=blob_service_client.get_blob_client('mycontainer1','happy1.jpg')
data=blob_client.download_blob()
import PIL as Image
Image.open(data)

