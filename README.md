# kubernetes-deploy
kubernetes-deploy 项目汇总k8s部署文件

[toc]
## ingress-controller
### nginx-ingress-controller部署

## log-collect
### 1 - DaemonSet方式
#### EFK
* DaemonSet部署filebeat/fluentd,将node log path mount 到容器内上报ES；
* 除了将业务日志打到固定目录下收集，还可收集/data/docker/containers下前台日志；(无用日志过多)
可参考[官网EFK](https://github.com/kubernetes/kubernetes/tree/master/cluster/addons/fluentd-elasticsearch)

```
镜像更换为private harbor image:
gcr.io/fluentd-elasticsearch/elasticsearch:v6.6.1 --> harbor.qyvideo.net/duanyifei-test/elasticsearch:v6.6.1
alpine:3.6	--> harbor.qyvideo.net/duanyifei-test/alpine:3.6
gcr.io/fluentd-elasticsearch/fluentd:v2.5.1 --> harbor.qyvideo.net/duanyifei-test/fluentd:v2.5.1
docker.elastic.co/kibana/kibana-oss:6.6.1 --> harbor.qyvideo.net/duanyifei-test/kibana-oss:6.6.1
docker.elastic.co/beats/filebeat:6.6.1 harbor.qyvideo.net/duanyifei-test/filebeat:6.6.1
```

#### Filebeat
filebeat 也提供了类似从api-server拉取、enrich format的功能插件：
[Shipping Kubernetes Logs to Elasticsearch with Filebeat
](https://www.elastic.co/blog/shipping-kubernetes-logs-to-elasticsearch-with-filebeat)
* 测试中发现存在除kube-system外，其他NS无法收取问题；


### 2 - Pod中附加专用日志收集的容器
* 相同pod共享路径，node通过 `emptyDir: {}` shard dir;
* 在使用nginx-ingress-controller过程中，如果采用方式1，需要修改nginx内部权限，遇错过多，采用附加日志container方式；
* 实例中给出 nginx-ingress-controller + filebeat;

### 3 - 应用程序直接推送日志
~~ null ~~

