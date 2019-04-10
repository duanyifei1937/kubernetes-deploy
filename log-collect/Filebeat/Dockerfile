FROM harbor.qyvideo.net/duanyifei-test/filebeat:6.1.1

USER root
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD filebeat -c /usr/share/filebeat/filebeat.yml