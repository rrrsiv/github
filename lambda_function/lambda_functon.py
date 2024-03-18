import os
import requests

def lambda_handler(event, context):
    terraform_url = "https://releases.hashicorp.com/terraform/1.0.0/terraform_1.0.0_linux_amd64.zip"
    download_path = "/tmp/terraform.zip"

    try:
        # Download Terraform binary
        response = requests.get(terraform_url)
        if response.status_code == 200:
            with open(download_path, 'wb') as f:
                f.write(response.content)
            print("Terraform downloaded successfully!")
        else:
            print("Failed to download Terraform. Status code:", response.status_code)
    except Exception as e:
        print("Error:", e)
