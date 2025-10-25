import requests
import os


def extract_data(url, local_file):
    # define a user-agent to mimic a browser request e extrair os dados do site
    header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()
        
        directory_path = os.path.dirname(local_file) or '.'
        os.makedirs(directory_path, exist_ok=True)

        with open(local_file, 'wb') as file:
            file.write(response.content)
        print(f"Data extracted and saved to {local_file}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
urls =[
        ("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/e6013a93-1321-4f2a-bf91-8d8a02f1e62f/download/tmpwbgyud93.csv", "data/dados_2023.csv"),
        ("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/dff4d804-5031-443a-8409-8344efd0e5c8/download/tmpm461rr5o.csv", "data/dados_2024.csv"),
        ("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/9d7c2214-4709-478a-a2e8-fb2020a5bb94/download/tmp9asser41.csv", "data/dados_2025.csv")
    ]
for url, local_file in urls:
    extract_data(url, local_file)



