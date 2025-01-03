# Creating_Containers_in_Azure_Using_VScode
- **Project Title:** Azure Blob Storage File Management Using Python and VS Code
- **Project Overview:**
  - This project demonstrates how to manage files in Azure Blob Storage using Python and VS Code. Specifically, it focuses on the creation of containers, and the uploading of both a CSV file and an image file to the cloud. The project also includes retrieving and processing these files.
  - Azure Blob Storage is a Microsoft cloud service designed for scalable object storage. It is ideal for handling unstructured data, such as documents, images, videos, and CSV files.
- **Key Objectives:**
  - Connect to Azure Blob Storage using the Azure Python SDK.
  - Programmatically create a blob storage container.
  - Upload and store a CSV file and an image file in the container.
  - Retrieve and process the uploaded files:
  - Read and display the CSV as a Pandas DataFrame.
  - Display the image using PIL (Python Imaging Library).
- **Features:**
   - **Container Management:**
     - Create a container in Azure Blob Storage.
     - Verify the existence of the container.
- **File Upload:**
  - Upload a CSV file to the container.
  - Upload an image file to the container.
  - File Download and Processing:
  - Download and display the contents of the CSV file using Pandas.
  - Download and display the image using PIL.
- **Tools and Libraries:**
   - **Azure Python SDK:** For interacting with Azure Blob Storage.
   - **Library:** azure-storage-blob
   - **Pandas:** For CSV file processing.
   - **PIL (Pillow):** For image file handling.
   - **VS Code:** As the development environment.
   - **Azure Cloud Portal:** To create and manage blob storage resources.
- **Workflow:**
   - **Setup:**
    - Install the necessary Python libraries (pip install azure-storage-blob pandas pillow).
    - Configure your Azure Blob Storage account and obtain the account URL and access key.
  - **Development Steps:**
    - Step 1: Establish a connection to Azure Blob Storage using the Azure Python SDK.
    - Step 2: Create a new blob storage container.
    - Step 3: Upload the CSV file and the image file to the container.
    - Step 4: List the files in the container for verification.
    - Step 5: Download and process the uploaded files:
        - Parse and display the CSV file as a Pandas DataFrame.
        - Open and display the image using PIL.
- **Testing:**
  - Run the Python script in VS Code to ensure all functionalities work.
  - Validate that files are correctly uploaded and processed.
- **Expected Outputs:**
   - A new container named (e.g., mycontainer) in Azure Blob Storage.
   - Uploaded files visible in the Azure Blob Storage container:
   - A CSV file (e.g., data.csv).
   - An image file (e.g., image.jpg).
- **Displayed outputs:**
  - The CSV file as a Pandas DataFrame in the terminal.
  - The image displayed using the system's default image viewer.
- **Sample Use Case:**
   - This project can be extended for use in:
     - Cloud-based data pipelines where CSV files are processed and stored.
     - Cloud-hosted image repositories for web or mobile applications.
     - A foundation for building serverless applications with Azure Functions for automated file processing.





