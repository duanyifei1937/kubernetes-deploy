# Prometheus out of kubernetes    

* 介绍prometheus在k8s集群外配置：
    * api_server 指定集群接口地址；
* 使用grafana做资源可视化 [Kubernetes-Grafana](https://github.com/grafana/kubernetes-app)

* 组件：
    * cadvisor: containers resource usage
    * state:  resource info (configmap / cronjob / daemonset / deployment / endpoint / job / container / statefulset)

``` yaml
# -------------------offline-kubernetes--------------------
  - job_name: 'offline-kubernetes-cadvisor'
    # scheme: http
    # tls_config:
    #   ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    # bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    kubernetes_sd_configs:
      - api_server: "http://172.16.0.6:8080"
        role: node
    relabel_configs:
      - source_labels: [__address__]
        regex: '(.*):10250'
        replacement: '${1}:4194'
        target_label: __address__

  # https://github.com/prometheus/prometheus/blob/master/documentation/examples/prometheus-kubernetes.yml#L37
  - job_name: 'offline-kubernetes-nodes'
    kubernetes_sd_configs:
      - api_server: "http://172.16.0.6:8080"
        role: node
    relabel_configs:
      - source_labels: [__address__]
        regex: '(.*):10250'
        replacement: '${1}:10255'
        target_label: __address__

  # node-export:
  - job_name: 'online-kubernetes-nodes-export'
    kubernetes_sd_configs:
      - api_server: "http://10.46.39.150:8080"
        role: node
    relabel_configs:
      - source_labels: [__address__]
        regex: '(.*):10250'
        replacement: '${1}:9100'
        target_label: __address__

    # https://github.com/prometheus/prometheus/blob/master/documentation/examples/prometheus-kubernetes.yml#L119
  - job_name: 'offline-kubernetes-services'
    metrics_path: /probe
    params:
      module: [http_2xx]
    kubernetes_sd_configs:
      - api_server: "http://172.16.0.6:8080"
        role: service
    relabel_configs:
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_probe]
        action: keep
        regex: true
      - source_labels: [__address__]
        target_label: __param_target
      - target_label: __address__
        replacement: blackbox
      - source_labels: [__param_target]
        target_label: instance
      - action: labelmap
        regex: __meta_kubernetes_service_label_(.+)
      - source_labels: [__meta_kubernetes_namespace]
        target_label: kubernetes_namespace
      - source_labels: [__meta_kubernetes_service_name]
        target_label: kubernetes_name

  # https://github.com/prometheus/prometheus/blob/master/documentation/examples/prometheus-kubernetes.yml#L156
  - job_name: 'offline-kubernetes-pods'
    kubernetes_sd_configs:
      - api_server: "http://172.16.0.6:8080"
        role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        regex: (.+):(?:\d+);(\d+)
        replacement: ${1}:${2}
        target_label: __address__
      - action: labelmap
        regex: __meta_kubernetes_pod_label_(.+)
      - source_labels: [__meta_kubernetes_namespace]
        action: replace
        target_label: kubernetes_namespace
      - source_labels: [__meta_kubernetes_pod_name]
        action: replace
        target_label: kubernetes_pod_name
      - source_labels: [__meta_kubernetes_pod_container_port_number]
        action: keep
        regex: 9\d{3}

  - job_name: 'offline-kubernetes-apiservers'
    kubernetes_sd_configs:
    - api_server: "http://172.16.0.6:8080"
      role: endpoints
    scheme: http
    relabel_configs:
    - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
      action: keep
      regex: default;kubernetes;https
    - source_labels: [__address__]
      regex: '(.*):6443'
      replacement: '${1}:8080'
      target_label: __address__

  - job_name: 'offline-kube-state-metrics'
    static_configs:
      - targets: ['172.16.16.11:30088', '172.16.16.11:30089']
```

