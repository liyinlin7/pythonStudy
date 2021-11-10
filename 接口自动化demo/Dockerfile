FROM python:3.8
COPY . /code
WORKDIR /code
RUN ls
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
RUN pip install -r requirement.txt -i https://mirrors.aliyun.com/pypi/simple/
ENTRYPOINT ["python","run.py"]
