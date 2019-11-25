# Grafana Outof Kubernetes Cluster
> 在k8s集群外安装grafana;
> 使用`grafana-kubernetes-app` plugin进行metrics数据展示；
> 由于原生插件版本过旧，需要自定义metrics query; 修改数据展示


## 插件做法
* 虽然需要添加k8s apiserver地址；用于获取node信息；metrics依然从prometheus中取；

## 插件安装方式
### 二进制安装
`./bin/grafana-cli  --pluginUrl /root/download --pluginsDir ./plugins plugins install grafana-kubernetes-app`


### 打入数据源
* `./datasource`

### supervisor 启动 
* `./supervisor`


## 原生`grafana-kubernetes-app`存在的问题
* plugin中提供多个label不存在，(比如nodename); 也没有必要去relabel; 通过`instance`代替；
* 提供三个修改好的dashboard json;



## 参考`prometheus-operator`进行对plugin的补充



## 自定义一些dashboard
> 业务服务级别；


## reference:
* https://grafana.com/grafana/plugins/grafana-kubernetes-app

