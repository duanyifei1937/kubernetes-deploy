# kubernetes-deploy
kubernetes-deploy 项目汇总k8s部署文件

[toc]

## dashboard
kubernetes-dashboard
* nodeport 方式
* https ingress 方式

## ingress-controller
* ingress controller install
* 日志格式自定义
* ingress controller grpc [example](https://duanyifei.cn/2019/04/07/Kubernetes-Ingress-GRPC/)
* nginx-ingress-controll监控方案

## log-collect
* 三种日志收集方式
* EFK
* ingress的sidecar日志收集方式

## log-clean
* 日志定期清除，只保留三天

## PresistentVolumes
### External Storage
* **why need external**:
一些用户会使用kubeadm来部署集群，或者将kube-controller-manager以容器的方式运行,问题来自gcr.io提供的kube-controller-manager容器镜像未打包ceph-common组件，缺少了rbd命令，因此无法通过rbd命令为pod创建rbd image，查了github的相关文章，目前kubernetes官方在kubernetes-incubator/external-storage项目通过External Provisioners的方式来解决此类问题
* [**external-storage cepy deploy**](https://github.com/kubernetes-incubator/external-storage/blob/master/ceph/rbd/deploy/README.md)

### Ceph-RBD
* **example**: ceph/external-storage/ceph-rbd-sample.yaml

## Q&A：
### configmap热更新
* ENV方式不会热更新；
* volume subpath 不会热更新；
* volume 更新需要延时>10s;


