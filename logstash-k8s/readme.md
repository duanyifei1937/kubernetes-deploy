# docker.elastic.co/logstash/logstash:6.1.1
# harbor.qyvideo.net/duanyifei-test/logstash:6.1.1
# harbor.qyvideo.net/duanyifei-test/logstash:6.1.1_v0.1

# harbor.qyvideo.net/duanyifei-test/logstash:6.1.1_v0.2
* shanghai timezone
* 自定义logstash config file
* 取消xpack

# harbor.qyvideo.net/duanyifei-test/logstash:6.1.1_v0.3
* 经过测试
    采用默认配置时 
        cpu 2core 
        mem 2G
    只使用了
        mem:  767.2MiB / 2GiB       37.46%
        cpu:   6.40%
    尝试修改配置：
        pipeline.workers: 4
        pipeline.output.workers: 2
    测试效果:
        使用率无变化，就像配置没生效

# harbor.qyvideo.net/duanyifei-test/logstash:6.1.1_v0.4
* 使用configmap形式 暴露 config logstash.yaml & pipeline index.yaml
* configmap 使用必须目标路径空

