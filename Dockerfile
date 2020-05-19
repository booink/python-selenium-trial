FROM python:3.7-slim-stretch

RUN apt-get update -q -y && \
    apt-get install -q -y \
    build-essential \
    wget \
    procps

# for chromedriver
RUN apt-get install -q -y \
    libxi6 \
    libgconf-2-4 \
    libnss3-dev

# install Chrome
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN apt-get update -q -y && apt-get install -q -y google-chrome-stable

RUN apt-get install -y libappindicator1 fonts-liberation libasound2 libnspr4 libnss3 libxss1 lsb-release xdg-utils

ADD ./requirements.txt requirements.txt

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

# Adapt google chromedriver to browser's version
RUN google-chrome --version | perl -pe 's/([^0-9]+)([0-9]+\.[0-9]+).+/$2/g' > chrome-version
RUN pip install chromedriver-binary~=`cat chrome-version` && rm chrome-version

# add font
RUN apt-get install -y fonts-ipafont-gothic --no-install-recommends

# install nodejs
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# インストールしたいjupyter labのextensionをインストールする
# ↓は例として toc extensionをインストールしている
RUN jupyter labextension install @jupyterlab/toc

ADD . /app
WORKDIR /app
