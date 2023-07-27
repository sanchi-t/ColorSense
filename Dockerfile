FROM python:3.9

WORKDIR /kmeanai


COPY requirements.txt .
COPY src src
COPY ./src/utils.py ./utils.py
RUN pip install -r requirements.txt

# Set the entrypoint command
CMD ["python", "src/main.py"]