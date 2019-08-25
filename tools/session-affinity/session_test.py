# -*- coding: utf-8 -*-
# @Time    : 2019/5/18
# @Author  : Yifei Duan
# @Summary :
import requests
from tqdm import tqdm
from collections import defaultdict


env = 'office'
# env = ''

REQ_TOTAL = 1000

# session = requests.Session()
session = None

cookies = dict(toolbox='faf710eb91b238a3e66f86aa93cfc744')
# cookies = None


if env == 'office':
    # for office env
    lb_api = 'http://lb.toolbox.cy.com/tools/pod'
    session_api = 'http://session.toolbox.cy.com/tools/pod'
else:
    # for test K8s
    lb_api = 'http://10.254.98.51:8080/tools/pod'
    session_api = 'http://10.254.23.47:8080/tools/pod'


def get_pod_info(url):
    if not session:
        resp = requests.get(url, cookies=cookies)
    else:
        resp = session.get(url, cookies=cookies)
    return resp.json()['body']


def get_pod_ip(url):
    resp = get_pod_info(url)
    return resp['podIp']


def pod_ip_counter(n, url):
    ips = defaultdict(int)
    for _ in tqdm(range(n), unit='req', leave=False):
        ips[get_pod_ip(url)] += 1
    return ips


def session_test(session_affinity):
    if session_affinity:
        url = session_api
        title = 'session affinity'
    else:
        url = lb_api
        title = 'round robin'
    ips = pod_ip_counter(REQ_TOTAL, url)
    total = sum(ips.values())
    print('{} total: {}'.format(title, total))
    for x in ips.items():
        print('{}\t{}\t{}%'.format(x[0], x[1], x[1]*100.0/total))


if __name__ == '__main__':
    session_test(True)
    print('\n')
    session_test(False)
