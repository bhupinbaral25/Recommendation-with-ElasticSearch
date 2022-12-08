from src.utils import error_handler, cfg, ES, MODEL

@error_handler
def search_result(processed_query, top_k: int=10):
    """
    Search for the query in elastic search using query vector and recommend the similar movie.
    """
    query_vector = MODEL.encode(processed_query).tolist()
    search_result = {
	"query": {
	    "script_score": {
		"query": {"match_all": {}},
		"script": {
		    "params": {"query_vector": query_vector},
		    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
		},
	    }
	},
	}
    custom_response = ES.search(
	index=cfg['ELASTIC_INDEX'],
        body={
		"size": top_k,
		"query": search_result,
		"_source": {"includes": ["movie_name", "genra"]},
	}
    )
    return custom_response
