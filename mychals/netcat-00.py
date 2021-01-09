#!/usr/bin/env python3

#     sudo docker build -t netcat-00 .
#     sudo docker run -d -p 1026:1026 --rm -it netcat-00


flag_file = open('flag','r')
print(flag_file.readline())
