# sudo docker build -t netcat-00 .
# sudo docker run -d -p 1026:1026 --rm -it netcat-00

FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install python3 ucspi-tcp -y

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY netcat-00.py .
COPY flag .

RUN chown -R root:root /home/ctf

USER ctf
EXPOSE 1024
CMD tcpserver -t 50 -RHl0 0.0.0.0 1026 python3 netcat-00.py
