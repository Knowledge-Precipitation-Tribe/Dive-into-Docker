# 搭建服务注册发现中心consul集群

## 启动第一个结点

```text
docker run --name consul1 -d -p 8300:8300 -p 8302:8302 -p 8600:8600 consul agent -server -bootstrap-expect 2 -ui -bind=0.0.0.0 -client=0.0.0.0
```

查看第一个结点的IP地址

```text
docker network ls
```

![](../.gitbook/assets/image%20%285%29.png)

查看详细信息

```text
docker inspect 931249c1387b
```

![](../.gitbook/assets/image%20%287%29.png)

## 启动第二个结点

启动第二个结点，并加入到第一个consul1

```text
docker run --name consul2 -d -p 8501:8500 consul agent -server -ui -bind=0.0.0.0 -client=0.0.0.0 -join 172.17.0.3
```

## 启动第三个结点

启动第三个结点，并加入到第一个consul1

```text
docker run --name consul3 -d -p 8502:8500 consul agent -server -ui -bind=0.0.0.0 -client=0.0.0.0 -join 172.17.0.3
```

## 进入界面

在浏览器输入http://localhost:8501，就可以打开对应的ui界面

![](../.gitbook/assets/image.png)

