import yaml
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

with open("./config.yaml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

MODEL = SentenceTransformer(cfg['MODEL_NAME'])
ES = Elasticsearch(cfg["ELASTIC_ENDPOINT"])

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
    return wrapper

