
import pandas as pd

from src.utils import cfg, MODEL
from src.custom_decorator import error_handler
from src.model_index import insert_in_elastic
from src.preprocessing import clean_sentences

@error_handler
def create_data():
    """
    Create the data to be inserted in elastic search.
    """
    df = pd.read_csv(cfg['DATA_PATH'], sep=',')
    for id, row in df.iterrows():
        data = {
	    "movie_id": id,
	    "movie_name": row["title"],
	    "embedding": MODEL.encode(clean_sentences(row["features"])).tolist(),
	    "genra": row["genres"],
	}
        insert_in_elastic(data)
    print("Data inserted in elastic search.")

if __name__ == "__main__":
    create_data()


