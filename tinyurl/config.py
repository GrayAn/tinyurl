import dataclasses
import os

from yaml import load, SafeLoader


@dataclasses.dataclass()
class Config:
    db_url: str
    url_length: int


def get_config() -> Config:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    config_file_path = os.path.normpath(os.path.join(current_directory, '..', 'config.yml'))
    with open(config_file_path, 'r') as f:
        config_data = load(f.read(), SafeLoader)

    config = Config(
        db_url=config_data['DBURL'],
        url_length=config_data['URLLength'],
    )

    return config
