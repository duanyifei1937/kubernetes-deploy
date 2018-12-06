### prometheus in k8s cluster
* 在官网[prometheus.yml](https://github.com/prometheus/prometheus/blob/master/documentation/examples/prometheus-kubernetes.yml)的基础上增加node-exporter;
* 提供示例rules;
    * basic.rule -- node基础rule; 
    * kubernetes.ruls -- 目前只有nodes/pods/containers状态规则;

### DROP问题：

```
# service discover 获取以下信息：
# 其中pods/endpoints/services 状态为DROP;

kubernetes-apiservers (3/153 active targets)
kubernetes-cadvisor (21/21 active targets)
kubernetes-nodes (21/21 active targets)
kubernetes-pods (0/296 active targets)
kubernetes-service-endpoints (0/153 active targets)
kubernetes-services (0/80 active targets)
```
* service & pods 需要使用集群内blackbox-exporter;
* servier 需要增加注释:

```
annotations:
  prometheus.io/probe: "true"

```