FROM python:3.9
ARG FLASK_APP
ARG DATABASE_HOSTNAME

RUN mkdir -p /app
WORKDIR /app
COPY . /app

ENV FLASK_APP=${FLASK_APP}
RUN pip install -r requirements.txt
RUN echo ${DATABASE_HOSTNAME}
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
