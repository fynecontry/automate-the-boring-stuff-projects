# Fetch base image
FROM python:3.9-alpine
WORKDIR /src
COPY img_downloader.py .
RUN pip3 install beautifulsoup4==4.7.1 requests==2.21.0
ENTRYPOINT ["python3", "img_downloader.py"]
