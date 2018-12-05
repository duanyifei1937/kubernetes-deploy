## kubernetes prometheus 部署：
[toc]

### 适用：
    * 应用于k8s集群外部部署prometheus;
    
### 私有化：
    * prometheus / alertmanager / grafana 部署在kubernetes 集群内；
    
    
    
### 线上及测试环境：

    * prometheus 组件部署于集群外；
    * node-exporter.yml
        * 用于监控kubernetes node metrics;
        * 新建ns: monitoring;
        * DaemonSet;
        * hostPort: 9100;
        
    * kube-state-metrics
        * 用于监控kubernetes cluster metrics;
        * ns: monitoring;
        * service:
            http-metrics: nodePort 30088 --> 8080
            telemetry:    nodePort 30089 --> 8081
        
    * pustgateway.yml
        * multiple nodeselector;
     



