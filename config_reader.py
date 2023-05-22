import yaml

def config():
    with open('config.yml') as yml:
        config = yaml.safe_load(yml)
        return config