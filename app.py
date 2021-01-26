import os

import environ
from dotenv import load_dotenv

from config import MlflowConfig

load_dotenv()

app_cfg = environ.to_config(MlflowConfig)

print(app_cfg.s3.endpoint_url)
