# MLFlow Server

An MLFlow Server designed to work with OpenShift.

## Environmnet Variables

The following environment variables are configurable in this image:

MLFLOW_HOST (Optional, Default=0.0.0.0): The host address for MLFlow server to start.
MLFLOW_PORT (Optional, Default=8080): The port for MLFlow server to start.
MLFLOW_DATABASE_URL (Required): The url for the database
MLFLOW_DATABASE_NAME (Required): The name of the database
MLFLOW_DATABASE_USERNAME (Required): The username for the database
MLFLOW_DATABASE_PASSWORD (Required): The password for the database
MLFLOW_S3_ENDPOINT_URL (Required): The S3 endpoint url that MLFlow will utilize for artifact storage
MLFLOW_S3_BUCKET_NAME (Required): The name of the S3 bucket that MLFlow will utilize for artifact storage
AWS_ACCESS_KEY_ID (Required): The Access Key ID for the S3 source bucket instance
AWS_SECRET_ACCESS_KEY (Required): The Secret Access Key for the S3 source bucket instance
