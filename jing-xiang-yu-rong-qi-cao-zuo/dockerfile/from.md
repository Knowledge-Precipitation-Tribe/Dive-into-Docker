# FROM

```text
FROM [--platform=<platform>] <image> [AS <name>]
```

或者

```text
FROM [--platform=<platform>] <image>[:<tag>] [AS <name>]
```

或者

```text
FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]
```

From 指令初始化一个新的构建阶段，并为后续指令设置基本镜像。 因此，有效的 Dockerfile 必须以 FROM 指令开始。 该镜像可以是任何有效的镜像，从Public Repositories中拉取镜像更容易。

### 了解 ARG 和 FROM 是如何相互作用的

From 指令支持由第一个 FROM 之前的任何 ARG 指令声明的变量。

```text
ARG  CODE_VERSION=latest
FROM base:${CODE_VERSION}
CMD  /code/run-app
```

