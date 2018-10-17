import yaml


def read_config(fname):
    with open(fname, 'r') as f:
        config = yaml.load(f)
    return config
