import environ
import urllib


@environ.config(prefix="MLFLOW")
class MlflowConfig:

    host_ip = environ.var(
        "0.0.0.0", help="The host IP address used to start MLFlow Server"
    )
    host_port = environ.var("8080", help="The host port used to start MLFlow Server")

    s3_endpoint_url = environ.var(
        help="The S3 endpoint URL that MLFlow Server will store artifacts"
    )
    s3_bucket = environ.var(
        "mlflow",
        help="The bucket in the S3 instance used by MLFlow Server to store artifacts",
    )
    access_key = environ.var(
        name="AWS_ACCESS_KEY_ID", help="The Access Key for the S3 instance"
    )
    secret_key = environ.var(
        name="AWS_SECRET_KEY_ID", help="The Secret Key for the S3 instance"
    )

    @environ.config
    class DB:
        driver = environ.var("sqlite")
        name = environ.var("mlruns.db")
        host = environ.var("default.host")
        port = environ.var(
            5432, converter=int
        )  # Use attrs's converters and validators!
        user = environ.var("")
        password = environ.var("")

    db = environ.group(DB)

    lang = environ.var(name="LANG")
    lorem = environ.var("ipsum")
    dolor = environ.bool_var(True, help="An example message.")


if __name__ == "__main__":
    print(environ.generate_help(MlflowConfig))
