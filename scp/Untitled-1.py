# %%
import glob
import os

current_dir = os.path.dirname(os.path.abspath('.'))
arquivos = glob.glob(os.path.join(current_dir, 'data', '*.csv'))
arquivos.sort()



print("Arquivos encontrados:", arquivos)

# %%
dfs = {}

# %%
import pandas as pd



for arquivo in arquivos:

    ano = arquivo.split("_")[-1].split(".")[0]

    dfs[ano] = pd.read_csv(arquivo)



print("Anos disponíveis:", list(dfs.keys()))

# %%
from dotenv import load_dotenv
load_dotenv()

aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key")
region_name = os.getenv("region_name")

# %%
import boto3

boto3.setup_default_session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# %%
s3 = boto3.client('s3')

# %%
# Upload DataFrames as Parquet files to S3

from io  import BytesIO

for ano, df in dfs.items():
    parquet_buffer = BytesIO()
    df.to_parquet(parquet_buffer)

    s3.put_object(
    Bucket="awsboston-datalake",
    Key=f"bronze/dados_{ano}.parquet",
    Body=parquet_buffer.getvalue()
    
    )


