FROM python:3.7.4-alpine as floursell-backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && apk add postgresql-client \
    g++ \
    freetype-dev \
    jpeg-dev \
    nano \
    zlib-dev \
    linux-headers \
    && apk del build-deps

RUN rm -vrf /var/cache/apk/*
RUN mkdir /app
COPY ./requirements /app/requirements
WORKDIR /app
RUN pip download -r requirements/base.txt -d wheelhouse
RUN pip install -r requirements/base.txt --no-index --find-links wheelhouse || true

RUN pip install --upgrade pip

FROM floursell-backend
ADD . /app
WORKDIR /app
RUN chmod +x entrypoint.sh
RUN ls
ENTRYPOINT ["/app/entrypoint.sh"]
