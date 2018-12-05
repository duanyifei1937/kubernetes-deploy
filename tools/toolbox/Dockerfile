From harbor.qyvideo.net/k8s/alpine:3.6

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories

RUN apk add --update \
    curl bash \
  && rm -rf /var/cache/apk/*

CMD ["tail", "-f", "/etc/hostname"]