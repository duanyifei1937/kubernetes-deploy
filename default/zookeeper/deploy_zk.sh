#!/usr/bin/env bash

# pssh -l work -h node_ip.txt -i "sudo mkdir -p /data/k8s/zookeeper"

echo "deploy zookeeper ..."

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

# create zk-storage
kubectl apply -f ${SCRIPTPATH}/zk_storage.yaml

# create zookeeper pv for all nodes
kubectl get node| tail -n +2  | awk '{print $1}' \
| while read -ra LINE; do
    cp ${SCRIPTPATH}/zookeeper_pv.yaml ${SCRIPTPATH}/pv_temp.yaml
    sed -i s/NODE_HOSTNAME/${LINE}/g ${SCRIPTPATH}/pv_temp.yaml
    sed -i s/NUM/${i}/g ${SCRIPTPATH}/pv_temp.yaml
    kubectl apply -f ${SCRIPTPATH}/pv_temp.yaml
done
rm ${SCRIPTPATH}/pv_temp.yaml

# create zookeeper statefulset and service

kubectl apply -f ${SCRIPTPATH}/zookeeper.yaml

echo "zookeeper deploy done !"