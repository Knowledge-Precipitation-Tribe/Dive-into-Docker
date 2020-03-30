# 镜像Image

Image文件可以看作是我们要使用的运行环境的一个模版。任何两台电脑都安装了Docker的话，只要你们使用的image相同，那么加载出来的container就是相同的。Docker的Image是分层的，通过改变某层就可以形成一个新的镜像

每个镜像可能会有很多个版本的tag。

![](../.gitbook/assets/redis-tag.png)

