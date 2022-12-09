from fastapi import FastAPI

from src.preprocessing import clean_sentences
from src.elastic_search import search_result
from src.custom_decorator import error_handler
from src.user_model import UserQuery, OutputResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@error_handler
@app.post("/recommend/")
async def get_recommendations(query: UserQuery):
    """
    API to get the recommendations for the query.
    It takes query as input and returns the recommendations.
    """
    recommendations = {}
    processed_query = clean_sentences(query.movie_name)
    responses = search_result(processed_query, query.no_of_recommendation)
    for order, response in enumerate(responses):
        recommendations[order+1] = OutputResponse(**response["_source"])

    return recommendations