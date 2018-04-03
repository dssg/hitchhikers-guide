FROM ubuntu:16.04

ENV PATH=$PATH:~/.local/bin
#ENV SHELL=/bin/bash

RUN apt-get update && \
    apt-get install -y python3 \
                       python3-pip

RUN pip3 install --upgrade pip && \
    pip3 install jupyter --user && \
    pip3 install numpy --user && \
    pip3 install pandas --user && \
    pip3 install plotnine --user && \
    pip3 install sklearn --user

ADD GDP.csv /
ADD predicting_GDP.ipynb /

EXPOSE 8898

CMD ['sh', '-c', 'jupyter notebook --ip=0.0.0.0 --allow-root --no-browser --port=8898']
