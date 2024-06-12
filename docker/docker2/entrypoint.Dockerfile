FROM ubuntu

RUN mkdir /test
RUN touch /test/file.txt

ENTRYPOINT ls