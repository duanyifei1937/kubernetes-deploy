# -*- coding: utf-8 -*-

import os
import time
from gpu_info import parse_gpu_usage_str
from report_module import report


def ai_report(status, api, gpu_card, service):
    report('ai', api, '1 is healthy', status, **{'service': service, 'gpu_card': gpu_card})


def gpu_card_list():
    """
    gpu_card_uuid: card_num
    :return:
    """
    info = os.popen('nvidia-smi -L').read().rstrip("\n")
    lines = info.split('\n')
    uuid_list = {}
    for i in lines:
        gpu_card = i.split()[1].split(':')[0]
        gpu_uuid = i.split()[-1].split(')')[0]
        uuid_list[gpu_uuid] = gpu_card
    return uuid_list


def service_all_label():
    """
    获取modelapi 对应服务名;
    :return: {0: 'ocr', 7: 'acgporn', 3: 'acgporn', 5: 'porn', 4: 'acg'}
    """
    uuid_list = gpu_card_list()
    card_service = {}
    docker_model_list = os.popen("docker ps | grep 'kvision-modelapi' | awk '{print $1}'")\
        .read().rstrip("\n").split('\n')
    for i in docker_model_list:
        try:
            service_name = os.popen("docker ps | grep '" + i + "' | awk '{print $NF}' | awk -F '-' '{print $1}' | "
                                    "awk -F '_' '{print $2}'").read().rstrip("\n")
            docker_uuid = os.popen("docker exec -i '" + i + "' bash -c 'nvidia-smi -L'").read().rstrip("\n").split()[-1].split(')')[0]
        except IndexError:
            pass
        gpu_card = int(uuid_list[docker_uuid])

        card_service[gpu_card] = service_name
    return card_service
    # print(card_service)


def main():
    gpu_info = parse_gpu_usage_str()
    service_label = service_all_label()
    # print(type(gpu_info))
    # gpu card 正常情况参数
    gpu_status_code = 1
    card_sum = 8
    card_mem_sum = 8
    cur_card_sum = int(os.popen("nvidia-smi | grep 'TITAN V' | wc -l").read())
    cur_card_mem_sum = int(os.popen("nvidia-smi | grep '12066MiB' | wc -l").read())

    if (cur_card_sum != card_sum) or (card_mem_sum != cur_card_mem_sum):
        gpu_status_code = 0
        ai_report(gpu_status_code, 'ai_gpu_status_code', 999, 'gpu_error')

    for key in gpu_info:
        gpu_util = gpu_info[key]['usage']
        memory = gpu_info[key]['memory']
        used_memory = gpu_info[key]['used_memory']
        gpu_temp = gpu_info[key]['temp']
        used_memory_precent = used_memory / memory
        cur_process = gpu_info[key]['process']
        try:
            service_name = service_label[key]
        except KeyError:
            service_name = None

        if used_memory != 0 and len(cur_process) == 0:
            gpu_status_code = 0
            ai_report(gpu_status_code, 'ai_gpu_status_code', 999, 'gpu_error')
        ai_report(gpu_util, 'ai_gpu_util', key, service_name)
        ai_report(used_memory_precent, 'ai_gpu_used_memory_precent', key, service_name)
        ai_report(gpu_temp, 'ai_gpu_temp', key, service_name)

        print(key, gpu_util, memory, used_memory, used_memory_precent, gpu_temp, service_name, gpu_status_code)


if __name__ == '__main__':
    for i in range(0, 4):
        main()
        time.sleep(15)
