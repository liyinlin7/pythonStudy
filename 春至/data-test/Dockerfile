FROM python:3.8
COPY . /code
COPY HTMLTestRunnerNew.py /usr/local/lib/python3.8/
WORKDIR /code
RUN ls
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
RUN cat run.py
RUN pip install -r requirement.txt -i https://mirrors.aliyun.com/pypi/simple/
ENTRYPOINT ["python","run.py"]
