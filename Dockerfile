FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install discord.py

ENV HOME /home

COPY dbot.py /home/dbot.py

STOPSIGNAL SIGTERM

WORKDIR /home

ENTRYPOINT ["python3"]

CMD ["dbot.py", "${TOKEN}"]
