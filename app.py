from fastapi import FastAPI

from src.preprocessing import clean_sentences
from src.user_model import Query, OutputResponse
from src.elastic_search import search_result

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/recommend/", response_model=dict[int, OutputResponse])
def get_recommendations(query: Query):
    """
    API to get the recommendations for the query.
    """
    recommendations = {}
    processed_query = clean_sentences(query.movie_name)
    responses = search_result(processed_query, query.num_recommendations)

    for response in responses:
        recommendations[response["_id"]] = OutputResponse(**response["_source"])

    return recommendations