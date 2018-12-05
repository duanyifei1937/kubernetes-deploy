# kubernetes-deploy
kubernetes-deploy 项目汇总k8s部署文件，包括monitoring/kube-system;

[toc]
## monitoring

### prometheus in k8s cluster
* 在官网[prometheus.yml](https://github.com/prometheus/prometheus/blob/master/documentation/examples/prometheus-kubernetes.yml)的基础上增加node-exporter;
* 提供示例rules;
    * basic.rule -- node基础rule; 
    * kubernetes.ruls -- 目前只有nodes/pods/containers status rules;


```



# service discover 获取以下信息：
kubernetes-apiservers (3/153 active targets)
kubernetes-cadvisor (21/21 active targets)
kubernetes-nodes (21/21 active targets)
kubernetes-pods (0/296 active targets)
kubernetes-service-endpoints (0/153 active targets)
kubernetes-services (0/80 active targets)
```
