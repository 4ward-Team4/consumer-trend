import yaml
from box import Box

class Config:

    def __init__(self):
        conf_url = 'config/configuration.yml'
        with open(conf_url, 'r') as f:
            config_yaml = yaml.load(f, Loader=yaml.FullLoader)
            self.config = Box(config_yaml)
