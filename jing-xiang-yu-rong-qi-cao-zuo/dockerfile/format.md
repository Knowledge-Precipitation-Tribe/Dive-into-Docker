# Format

Docker 按顺序在 Dockerfile 中运行指令。 文件必须以“FROM”指令开头。 这可能是在解析器指令、注释和全局范围的 ARGs 之后。 From指令指定要从中构建的父映像。 From 之前只能有一个或多个 ARG 指令，这些指令声明 Dockerfile 中 FROM 行中使用的参数。

Docker 将以`#`开头的行视为注释，除非该行是有效的解析器指令。 一行中其他任何地方的`#`标记都被视为参数。 允许这样的语句:

```text
# Comment
RUN echo 'we are running some # of cool things'
```

