# Usage

`Docker build`命令根据 Dockerfile 和上下文构建一个镜像。 构建的上下文是位于指定位置 PATH 或 URL 的文件集。 Path 是本地文件系统上的一个目录。 Url 是一个 Git 存储库位置。

上下文是递归处理的。 因此，PATH 包括所有子目录，URL 包括存储库及其子模块。 这个例子展示了一个使用工作目录作为上下文的 build 命令:

```text
$ docker build .
Sending build context to Docker daemon  6.51 MB
...
```

构建由 Docker 守护进程运行，而不是由 CLI 运行。 构建过程要做的第一件事是将整个上下文\(递归地\)发送到守护进程。 在大多数情况下，最好从一个空目录作为上下文开始，并将 Dockerfile 保存在该目录中。 只添加构建 Dockerfile 所需的文件。

{% hint style="info" %}
不要使用根目录 / ，因为 PATH 会导致构建将硬盘驱动器的全部内容传输到 Docker 守护进程。
{% endhint %}

要在构建上下文中使用文件，Dockerfile 引用指令中指定的文件，例如 COPY 指令。 若要提高生成的性能，请通过添加`.dockerignore` 文件移到上下文目录。 

传统上，Dockerfile 被称为 Dockerfile，位于上下文的根目录中。 在 docker 构建中使用-f 标志指向文件系统中的任何位置的 Dockerfile。

```text
$ docker build -f /path/to/a/Dockerfile .
```

如果构建成功，你可以指定一个存储库和标签来保存新镜像:

```text
$ docker build -t shykes/myapp .
```

要在构建之后将图像标记为多个存储库，请在运行构建命令时添加 multiple-t 参数:

```text
$ docker build -t shykes/myapp:1.0.2 -t shykes/myapp:latest .
```

在 Docker 守护进程运行 Dockerfile 中的指令之前，它会对 Dockerfile 进行初步验证，如果语法不正确，则返回一个错误:

```text
$ docker build -t test/myapp .
Sending build context to Docker daemon 2.048 kB
Error response from daemon: Unknown instruction: RUNCMD
```

Docker 守护进程逐条运行 Dockerfile 中的指令，如果需要，在最终输出新映像的 ID 之前，将每条指令的结果提交到新映像中。 Docker 守护进程将自动清除您发送的上下文。

请注意，每条指令都是独立运行的，并且会创建一个新映像，因此`RUN cd /tmp`不会对下一条指令产生任何影响。

只要有可能，Docker 将重用中间镜像\(缓存\) ，以显著加快 Docker 构建过程。 控制台输出中的 Using cache 消息指示了这一点。 \(有关更多信息，请参见 Dockerfile 最佳实践指南:

```text
$ docker build -t svendowideit/ambassador .
Sending build context to Docker daemon 15.36 kB
Step 1/4 : FROM alpine:3.2
 ---> 31f630c65071
Step 2/4 : MAINTAINER SvenDowideit@home.org.au
 ---> Using cache
 ---> 2a1c91448f5f
Step 3/4 : RUN apk update &&      apk add socat &&        rm -r /var/cache/
 ---> Using cache
 ---> 21ed6e7fbb73
Step 4/4 : CMD env | grep _TCP= | (sed 's/.*_PORT_\([0-9]*\)_TCP=tcp:\/\/\(.*\):\(.*\)/socat -t 100000000 TCP4-LISTEN:\1,fork,reuseaddr TCP4:\2:\3 \&/' && echo wait) | sh
 ---> Using cache
 ---> 7ea8aef582cc
Successfully built 7ea8aef582cc
```

生成缓存仅用于具有本地父级链的镜像。 这意味着这些镜像是由以前的builds创建的，或者整个镜像链加载了`docker load`。 如果希望使用特定映像的构建缓存，可以使用`--cache-from`选项指定它。 使用`--cache-from`指定的映像不需要有父链，可以从其他注册表中提取。

完成构建后，就可以考虑将存储库推送到其注册中心。

