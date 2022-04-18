"""Configuration file for managing environment variables."""

import environ


@environ.config(prefix="MLFLOW")
class AppConfig:
    """Application configuration object used for managing environment variables."""

    host = environ.var(
        default="0.0.0.0", help="The host address for MLFlow server to start."
    )

    port = environ.var(default="8080", help="The port for MLFlow server to start.")


    @environ.config()
    class Database:
        """Configuration object for the database."""

        url = environ.var(help="The url for the database")

        host = environ.var(help="The hostname of the database")

        username = environ.var(help="The username for the database")

        password = environ.var(help="The password for the database")

    database = environ.group(Database)

    @environ.config()
    class S3:
        """App configuration object used for managing s3 objects."""

        endpoint_url = environ.var(
            help="The S3 endpoint url that MLFlow will utilize for artifact storage",
        )

        bucket_name = environ.var(
            help="The name of the S3 bucket that MLFlow will utilize for artifact storage",
        )

        access_key = environ.var(
            name="AWS_ACCESS_KEY_ID",
            help="The Access Key ID for the S3 source bucket instance",
        )
        secret_key = environ.var(
            name="AWS_SECRET_ACCESS_KEY",
            help="The Secret Access Key for the S3 source bucket instance",
        )

    s3 = environ.group(S3)


if __name__ == "__main__":
    print(environ.generate_help(AppConfig, display_defaults=True))
