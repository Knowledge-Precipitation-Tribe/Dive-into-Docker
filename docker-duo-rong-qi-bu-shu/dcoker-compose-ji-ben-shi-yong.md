---
description: 若对你有帮助欢迎Star⬆
---

# Dcoker Compose基本使用

## 启动服务

在创建好`docker-compose.yml`文件后，可以通过这个命令将文件中定义的容器都启动起来，在docker compose中我们更习惯于将每一个容器叫做service。

```bash
docker-compose up
```

命令后会自动接一个默认值`-f docker-compose.yml`，也就是默认是使用docker-compose.yml文件的。我们也可以给文件起名为`docke-test.yml`，这样在使用时指定文件名，但是为了符合规范，还是统一为`docker-compose.yml`。

```bash
docker-compose up -f docer-test.yml
```

但是直接通过这种方式的话会直接将启动时的输出打印到终端，所以我们常会加上`-d`参数。

```bash
docker-compose up -d
```

## 查看服务状态

接下来可以查看一下我们创建的service状态

```bash
docker-compose ps
```

## 停止或删除服务

如何停止已经运行的services呢，可以使用以下两个命令

```bash
docker-compose stop
docker-compose down
```

其中stop是直接停止services，而down则会停止并删除创建的service，volume和network。

## 进入容器呢

```bash
docker-compose exec mysql bash
```

exec后面接的就是我们要进入具体的service的名字，名字后面就是我们要执行的命令。

## 查看服务输出日志

若出现问题无法启动可以使用命令查看日志定位原因

```bash
docker-compose logs
```

