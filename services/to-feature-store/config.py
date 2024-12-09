from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='settings.env')

    kafka_broker_address: str
    kafka_input_topic: str
    kafka_consumer_group: str

    feature_group_name: str
    feature_group_version: int


class HopsworksCredentials(BaseSettings):
    model_config = SettingsConfigDict(env_file='credentials.env')
    hopsworks_api_key: str


class AwsCredentials(BaseSettings):
    model_config = SettingsConfigDict(env_file='aws.env')
    aws_access_key_id: str
    aws_secret_access_key: str


config = Settings()
hopsworks_credentials = HopsworksCredentials()
aws_credentials = AwsCredentials()
