FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

LABEL maintainer='bhupin@fusemachines.com'

# install as a package
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy code
COPY . /app
# run the app
EXPOSE 8000

CMD ["uvicorn", "app:app", "--reload"]