FROM python:alpine

WORKDIR /assignment2

COPY . .

RUN pip install NLTK

CMD ["python", "script.py"]