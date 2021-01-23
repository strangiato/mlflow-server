import environ

@environ.config(prefix="MLFLOW")
class MlflowConfig:

    @environ.config
    class DB:
        name = environ.var("default_db")
        host = environ.var("default.host")
        port = environ.var(5432, converter=int)  # Use attrs's converters and validators!
        user = environ.var("default_user")
        password = environ.var("default_user")

    db = environ.group(DB)

    lorem = environ.var('ipsum')
    dolor = environ.bool_var(True, help="An example message.")

@environ.config(prefix="AWS")
class AwsConfig:
    access_key_id = environ.var()
    secret_key_id = environ.var()

if __name__ == "__main__":
    print(environ.generate_help(MlflowConfig))
    print(environ.generate_help(AwsConfig))