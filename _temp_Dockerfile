FROM ubuntu:22.04

RUN apt-get update && \ 
    apt-get install \ 
    bash-completion \
    gcc \
    python3-dev \
    python3-pip \
    libpq-dev \
    poppler-utils \
    libzbar0 \
    libzbar-dev \
    ffmpeg \
    libsm6 \
    libxext6 \
    postgresql-client -y

RUN truncate -s0 /tmp/preseed.cfg && \
    (echo "tzdata tzdata/Areas select America" >> /tmp/preseed.cfg) && \
    (echo "tzdata tzdata/Zones/America select Recife" >> /tmp/preseed.cfg) && \
    debconf-set-selections /tmp/preseed.cfg && \
    rm -f /etc/timezone /etc/localtime && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true \
    apt-get install -y tzdata

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PYTHONUNBUFFERED 1





COPY requirements.txt .

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt