# Empty connection string

## Run locally

1. Install required packages: `pip install -r requirements.txt`
2. Run `pytest`: `pytest --disable-warnings -q --tb=short`

## Build an image

`docker build -t empty-connection-string:v1 .`

## Run the image

`docker run -ti empty-connection-string:v1 pytest --disable-warnings -q --tb=short`
