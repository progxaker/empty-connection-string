# Empty connection string

## Run locally

1. Install required packages: `pip install -r requirements.txt`
2. Run `pytest`:
   1. Failure case: `pytest --disable-warnings -q --tb=short`
   2. Successful case:
      ```bash
      export APPLICATIONINSIGHTS_CONNECTION_STRING="<connection-string>"
      python main.py
      ```

## Build an image

1. Run `docker build`: `docker build -t empty-connection-string:v1 .`

## Run the image

1. Failure case: `docker run -ti empty-connection-string:v1 pytest --disable-warnings -q --tb=short`
2. Successful case: `docker run --env APPLICATIONINSIGHTS_CONNECTION_STRING="<connection-string>" -ti empty-connection-string:v1 python main.py`
