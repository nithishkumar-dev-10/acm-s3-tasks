import yaml

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def load_features():
    with open("config/features.yaml", "r") as f:
        return yaml.safe_load(f)

def load_hyperparams():
    with open("config/hyperparameters.yaml", "r") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    cfg  = load_config()
    feat = load_features()
    hp   = load_hyperparams()

    print(f"config.yaml      : {list(cfg.keys())}")
    print(f"features.yaml    : {list(feat.keys())}")
    print(f"hyperparams.yaml : {list(hp.keys())}")
