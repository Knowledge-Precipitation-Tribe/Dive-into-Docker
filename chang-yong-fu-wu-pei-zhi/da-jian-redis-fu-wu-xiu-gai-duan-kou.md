# 搭建redis服务-修改端口

我们现在想要创建开启在6380端口的redis服务。

## 创建并修改redis.conf

![](../.gitbook/assets/image%20%282%29.png)

{% file src="../.gitbook/assets/redis.conf" %}

## 创建Dockerfile

```text
FROM redis 
COPY redis.conf /usr/local/redis/redis/config
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
```

## 创建docker-compose.yml

```yaml
version: "3"

services:
  redis_6380:
    build: 
      context: .
      dockerfile: Dockerfile
    restart: always
    ports:
      - "6380:6380"
    volumes:
      - redis-db:/data

volumes:
  redis-db:
```

启动docker服务

```text
docker-compose up -d
```

