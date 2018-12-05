FROM harbor.qyvideo.net/duanyifei-test/python:3.6.6-alpine3.8
MAINTAINER duanyifei@kingsoft.com

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

COPY gpu_info.py report_module.py titanv_gpu.py ./

CMD [ "python", "./titanv_gpu.py" ]
