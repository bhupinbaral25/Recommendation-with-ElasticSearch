from src.utils import cfg, ES, MODEL
from src.custom_decorator import error_handler

@error_handler
def search_result(processed_query, top_k: int=10):
    """
    Search for the query in elastic search using query vector and recommend the similar movie.
    """
    query_vector = MODEL.encode(processed_query).tolist()
    print(query_vector)
    search_result = {
	    "script_score": {
		"query": {"match_all": {}},
		"script": {
		    
		    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
		    "params": {"query_vector": query_vector}
		}
	    }
	}
    print(search_result)
    custom_response = ES.search(
	index=cfg['ELASTIC_INDEX'],
        body={
		"size": top_k,
		"query": search_result,
		"_source": ["movie_name", "genra"],
		
	}
	
    )
    return custom_response["hits"]["hits"]
