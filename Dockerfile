FROM amancevice/pandas:1.0.0-alpine
#conector com o neo4j
RUN pip3 install py2neo
RUN mkdir /home/script
WORKDIR /home/script
