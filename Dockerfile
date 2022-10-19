FROM python:3.8.10-buster

SHELL ["/bin/bash", "-c"]
WORKDIR /opt/app
ENV PWD=/opt/app

COPY . .

RUN pip install virtualenv

RUN make install

EXPOSE 5000

CMD ["make", "run"]