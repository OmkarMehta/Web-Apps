FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD exec gunicorn main:app --bind :$PORT