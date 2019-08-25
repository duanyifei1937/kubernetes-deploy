FROM harbor.qyvideo.net/duanyifei-test/logstash:6.1.1

ENV TZ=Asia/Shanghai
#RUN apk update \
#    && apk add tzdata \
#    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN rm -f /usr/share/logstash/pipeline/logstash.conf

ADD config/ /usr/share/logstash/config/

RUN mkdir /usr/share/logstash/custome-config
# 使用configmap形式
# index.yaml
#ADD pipeline/ /usr/share/logstash/pipeline/
#
# logstash config file
#ADD config/ /usr/share/logstash/config/

# configmap mount file 镜像其他文件原有文件无法挂载
