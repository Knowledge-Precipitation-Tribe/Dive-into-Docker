---
description: 若对你有帮助欢迎Star⬆
---

# Dive-into-Docker

## Dive-into-Docker

本项目名称为：**动手学Docker**。Docker 属于容器的一种封装，提供简单易用的容器使用接口。Docker 将应用程序与该程序的依赖，打包在一个文件里面。运行这个文件，就会生成一个虚拟容器。程序在这个虚拟容器里运行，就好像在真实的物理机上运行一样。有了 Docker，就不用担心环境问题。

有人说了，我看你说了半天都是再说Docker怎么怎么好，到底怎么好我也不知道，为什么要用？那我来给你举个例子： 如果我们想要搭建一个网站，传统的做法我们会怎么做？首先会买一个云服务器，然后安装Apache，MySQL，Java/PHP以及他们所需要的依赖环境；之后要对他们进行配置，创建用户，配置合适的端口参数等等；经过大量操作，我们接下来要测试看是否工作正常，有不对的地方我们还要修改，如果配置的东西众多，我相信这是一个非常头疼的问题。

更可怕的情况出现了，一旦现在这个云服务器到期了，或者根据需要要迁移服务器，那我们就要所有都从头来一遍，这些你说难不难，说简单不简单但是极其消耗精力的事是很痛苦的。

Docker要做的就是节约这一成本，通过容器对应用进行打包，解耦应用和运行平台，意味着当我们迁移服务器的时候只需要在新的服务器上启动所需要的容器就可以了，这将为我们**节省大量的宝贵时间。**

总体来说，Docker 的接口相当简单，用户可以方便地创建和使用容器，把自己的应用放入容器。容器还可以进行版本管理、复制、分享、修改，就像管理普通的代码一样。

![](.gitbook/assets/docker_logo.png)



_注：建议使用Linux系统，这样更贴近生产环境。可以使用云服务器或者虚拟机等_

### 开始之前

在阅读此书之前，最好以下一些前置知识：

* Linux常用操作
* 准备好的服务器或虚拟机

### 本书主题

本书以Docker为主要内容，还包括以下几个方面的内容

* 容器编排-k8s
* CI/CD

### 使用方式

您可以通过以下方式使用本书：

* Github地址：[https://github.com/Knowledge-Precipitation-Tribe/Dive-into-Docker](https://github.com/Knowledge-Precipitation-Tribe/Dive-into-Docker)
* GitBook在线浏览：[https://supeng842499467.gitbook.io/dive-into-docker/](https://supeng842499467.gitbook.io/dive-into-docker/)

### 快速开始

有以下几种方式可以快速搭建起开发环境：

* 使用Vagrant+VirtualBox或Vmware等搭建虚拟环境，使用vagrant方式可以参考：[https://github.com/rootsongjc/kubernetes-vagrant-centos-cluster](https://github.com/rootsongjc/kubernetes-vagrant-centos-cluster)
* 使用云服务器搭建开发环境
* 使用自己的电脑搭建开发环境
* 使用Docker playground\(有时间限制\): [https://labs.play-with-docker.com/](https://labs.play-with-docker.com/)
* 使用k8s playground\(有时间限制\): [https://labs.play-with-k8s.com/](https://labs.play-with-k8s.com/)

### 推荐

\[1\] Kubernetes中文指南/云原生应用架构实践手册:[https://jimmysong.io/kubernetes-handbook/](https://jimmysong.io/kubernetes-handbook/)

\[2\] Docker — 从入门到实践：[https://yeasy.gitbooks.io/docker\_practice/](https://yeasy.gitbooks.io/docker_practice/)

\[3\] 系统学习Docker 践行DevOps理念: [https://coding.imooc.com/learn/list/189.html](https://coding.imooc.com/learn/list/189.html)

<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=110 src="//music.163.com/outchain/player?type=0&id=4957781147&auto=0&height=90"></iframe>
