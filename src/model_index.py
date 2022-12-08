from src.utils import cfg, ES
from src.utils import error_handler

@error_handler
def create_index():
    """
    Create the index in elastic search with the mapping.
    """
    model_body = {
        "settings": {
            "number_of_shards": 2,
            "number_of_replicas": 1,
        },
        "mappings": {
            "properties": {
                "movie_id": {"type": "text"},
                "movie_name": {
                    "type": "text",
                },
                "embedding": {"type": "dense_vector", "dims": 384},
                "genra": {
                    "type": "text",
                }
            }
        },
    }
    ES.indices.create(index=cfg['ELASTIC_INDEX'], body=model_body)

def insert_in_elastic(data):
    """
    Insert the data in the elastic search.
    """
    if not ES.indices.exists(index=cfg['index']):
        create_index()
    ES.index(index=cfg['ELASTIC_INDEX'], body=data)

