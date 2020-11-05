FROM python:3.8-alpine as base

FROM base as builder
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN mkdir /install
WORKDIR /install
COPY ./requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY . /app
CMD ["python","app/importdata.py"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]