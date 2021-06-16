FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install djangorestframework
RUN pip install markdown
RUN pip install django-filter
RUN pip install django-cors-headers
COPY . /code/