# 搭建Gitlab服务器

我这里使用的是Centos x86架构的服务器，内存4GB，如果你使用的是aarch64架构的话可能安装不成功。在安装之前可以使用`uname -a`查看自己服务器的架构。

```bash
$ uname -a
```

（1）首先安装依赖软件

```bash
sudo yum install -y git vim gcc glibc-static telnet
sudo yum install -y curl policycoreutils-python openssh-server
sudo systemctl enable sshd
sudo systemctl start sshd

sudo yum install postfix
sudo systemctl enable postfix
sudo systemctl start postfix
```

（2）设置gitlab的安装源

新建 /etc/yum.repos.d/gitlab-ce.repo，内容为

```bash
[gitlab-ce]
name=Gitlab CE Repository
baseurl=https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el$releasever/
gpgcheck=0
enabled=1
```

（3）安装gitlab

如果你有自己域名的话，在安装时可以直接将你自己的域名替换`http://gitlab.example.com`，将自己的域名设置为访问的URL。

```bash
sudo EXTERNAL_URL="http://gitlab.example.com" yum install -y gitlab-ce
```

如果没有域名也可以直接安装，然后通过公网IP访问即可。

```bash
sudo yum install -y gitlab-ce
```

现在的gitlab也推荐大家使用gitlab-ee版本，要是不激活的话应该和ce版本差不多。

安装完成后使用以下命令使配置生效

```bash
sudo gitlab-ctl reconfigure
```

（4）登陆并修改密码

因为我没有配置域名，所以直接使用的公网IP进行登陆，因为需要一定的配置时间，所以你立刻访问的话可能显示的是nginx页面，稍等一会在访问就可以看到如下界面

![](../.gitbook/assets/gitlab-init.png)

设置你自己的管理员密码，然后进入登陆界面

![](../.gitbook/assets/gitlab-init-login.png)

然后酒可以通过用户名：root和自己设置的密码登陆服务器了

![](../.gitbook/assets/gitlab-logined.png)

接下来你可以创建自己的仓库等一些列操作了。

