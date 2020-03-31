# flask-redis实战

我们这个应用是使用flask搭建一个应用，这个应用是我们每访问一次网址就会在redis的数据库上加1。

首先我们创建一个启动redis服务的容器

```bash
docker run -d --name redis redis
```

之后我们编写一下python文件，名字叫做app.py

{% code title="app.py" %}
```python
from flask import Flask
from redis import Redis
import os
import socket

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', '127.0.0.1'), port=6379)


@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello Container World! I have been seen %s times and my hostname is %s.\n' % (redis.get('hits'),socket.gethostname())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```
{% endcode %}

再创建Dockerfile，并编辑里面的内容

{% code title="Dockerfile" %}
```text
FROM python:2.7
COPY . /app
WORKDIR /app
RUN pip install flask redis
EXPOSE 5000
CMD [ "python", "app.py" ]
```
{% endcode %}

然后根据Dockerfile创建我们自己的镜像

```bash
docker build -t su/flask-redis .
```

最后将我们自己创建的镜像加载成容器对外提供服务，并且将容器的5000端口映射到服务器的5000端口

```bash
docker run -d --link redis -p 5000:5000 --name flask-redis -e REDIS_HOST=redis su/flask-redis
```

我们来看一下效果，首次访问

![](../.gitbook/assets/flask-redis1.png)

再访问一次看一下效果

![](../.gitbook/assets/flask-redis2.png)

可以看到我们已经实现了多容器应用的部署💯。

