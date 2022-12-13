
# Recommendation system using Elastic-Search

Here, The project is all about movie recommendation with content base filtering technique. For similarity score, Cosine similarity is used. 

This repo contain all python code with docker and docker compose to start a Fast API and Elastic search. 




## Installation

You need to have ```python``` version 3.9 
Clone the repository then Run these command to create a virtualenv to manage the ```dependencies``` in python

```bash
cd ./Recommendation-with-ElasticSearch
python3 -m venv venv
  
```
Then activate the ```venv```
```bash
source venv/bin/activate
```

Then Install all the dependencies
```bash 
pip install -r requirements.txt
```

Then Start your docker desktop and run the command
```bash 
docker-compose up --build
```
After running the two different container for Fast API and Elastic search create an index for ElasticSearch. 
To create the index simply run 
```python
python main.py
```

It will take few moments to create an index in ElasticSearch

After completing the above process open the browser and start 
```
http://localhost:8000/docs
```
You will the UI just click on recommendation and enter the input and see the desired result


## API Reference

#### Get all recommendation

```http
  post /recommend/
```

| Parameter     | Type     | Description                       |
| :------------ | :------- | :-------------------------------- |
| `movie_name`  | `string` | **Required**. name of the movie of item to fetch |
| `no of recommendation`| `int` | **Required**. how many number of recommendation you want |
