import environ


@environ.config(prefix="MLFLOW")
class MlflowConfig:
    @environ.config
    class Host:
        ip = environ.var(
            "0.0.0.0", help="The host IP address used to start MLFlow Server"
        )
        port = environ.var(
            8080, converter=int, help="The host port used to start MLFlow Server"
        )

    host = environ.group(Host)

    @environ.config
    class Log:
        level = environ.var("INFO")
        format = environ.var(
            "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"
        )

    log = environ.group(Log)

    @environ.config
    class S3:
        endpoint_url = environ.var(
            help="The S3 endpoint URL that MLFlow Server will store artifacts"
        )
        bucket = environ.var(
            "mlflow",
            help="The bucket in the S3 instance used by MLFlow Server to store artifacts",
        )
        access_key = environ.var(
            name="AWS_ACCESS_KEY_ID", help="The Access Key for the S3 instance"
        )
        secret_key = environ.var(
            name="AWS_SECRET_KEY_ID", help="The Secret Key for the S3 instance"
        )

    s3 = environ.group(S3)

    @environ.config
    class DB(object):
        schema = environ.var("sqlite")
        name = environ.var("mlruns.db")
        host = environ.var(None)
        port = environ.var(5432, converter=int)
        user = environ.var(None)
        password = environ.var(None)

        # url = environ.var(help="The connection string URL for the database")

    db = environ.group(DB)


if __name__ == "__main__":
    print(environ.generate_help(MlflowConfig, display_defaults=True))
