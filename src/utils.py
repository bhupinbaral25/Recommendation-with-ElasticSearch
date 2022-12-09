import yaml
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

with open("./config.yaml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

MODEL = SentenceTransformer(cfg['MODEL_NAME'])
ES = Elasticsearch(cfg["ELASTIC_ENDPOINT"])
