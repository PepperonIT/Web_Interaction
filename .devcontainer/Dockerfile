FROM python:2.7.18

RUN apt-get update && apt-get install -y pipenv
RUN wget -P ~/Downloads https://community-static.aldebaran.com/resources/2.5.10/Python%20SDK/pynaoqi-python2.7-2.5.7.1-linux64.tar.gz \
    && mkdir -p ~/lib/python2/ \
    && tar -xf ~/Downloads/pynaoqi-python2.7-2.5.7.1-linux64.tar.gz -C ~/lib/python2 \
    && rm ~/Downloads/pynaoqi-python2.7-2.5.7.1-linux64.tar.gz \

ENV PYTHONPATH=${PYTHONPATH}:/etc/python2.7/python-naoqi-sdk/lib/python2.7/site-packages

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip2 install -r requirements.txt

COPY . .

# Run code test
# RUN pylint *.py
RUN find . -type f -name "*.py" | xargs pylint

CMD [ "python2", "-u", "./main.py" ]
