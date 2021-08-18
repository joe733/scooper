FROM python:latest

COPY Pipfile /Pipfile

RUN pip install pipenv
RUN pipenv install

COPY main.py /main.py

CMD ["python", "/main.py"]
