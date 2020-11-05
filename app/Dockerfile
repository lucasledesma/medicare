FROM python:3.8.6-buster as base

FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY ./requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY . /app
ADD start.sh /
RUN chmod +x /start.sh
CMD ["/start.sh"]
