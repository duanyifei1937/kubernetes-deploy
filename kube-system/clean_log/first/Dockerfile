FROM ubuntu:latest
MAINTAINER duanyifei@kingsoft.com

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/cleanlog-cron
RUN chmod 0644 /etc/cron.d/cleanlog-cron \
    && mkdir -p /data/logs

# ubuntu install crontab | start cron | create cron.log
RUN apt-get update \
    && apt-get install -y cron \
    && service cron start \
    && touch /var/log/cron.log

# modify timezone
ENV TZ=Asia/Shanghai
RUN echo $TZ > /etc/timezone \
    && apt-get install -y tzdata \
    && rm /etc/localtime \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get clean

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log
