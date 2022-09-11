#!/bin/sh

echo "---> Connecting to database..."

# hacky way to make the password URL safe
ENCODED_DATABASE_PASSWORD=$(python3 -c "import urllib.parse; print(urllib.parse.quote(input()), end='')" <<< ${MLFLOW_DATABASE_PASSWORD})

DATABASE_URI="postgresql://${MLFLOW_DATABASE_USERNAME}:${ENCODED_DATABASE_PASSWORD}@${MLFLOW_DATABASE_HOST}/${MLFLOW_DATABASE_NAME}"
REDACTED_DATABASE_URI="postgresql://${MLFLOW_DATABASE_USERNAME}:<database-password>@${MLFLOW_DATABASE_HOST}/${MLFLOW_DATABASE_NAME}"
echo ${REDACTED_DATABASE_URI}
echo ""

echo "---> Migrating MLFlow DB"
mlflow db upgrade $DATABASE_URI
