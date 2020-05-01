# 搭建MySQL主从复制集群

## 首先创建master结点的Dockerfile

在编写之前我们先要创建一个配置master的my.cnf配置文件

{% code title="my.cnf" %}
```text
[mysqld]
log_bin = mysql-bin
server_id = 10
```
{% endcode %}

之后我们创建master结点的Dockerfile

```text
FROM mysql:5.7
ADD ./master/my.cnf /etc/mysql/my.cnf
```

## 第二创建slave结点的Dockerfile

在编写之前我们先要创建一个配置slave结点my.cnf配置文件

{% code title="my.cnf" %}
```text
[mysqld]
log_bin = mysql-bin
server_id = 11
relay_log = /var/lib/mysql/mysql-relay-bin
log_slave_updates = 1
read_only = 1
```
{% endcode %}

{% hint style="danger" %}
注意要修改server\_id为不同值，否则会发生错误
{% endhint %}

之后我们创建slave结点的Dockerfiel

```text
FROM mysql:5.7
ADD ./slave/my.cnf /etc/mysql/my.cnf
```

## 最终的docker-compose.yml

我们创建这样一个目录结构

![](../.gitbook/assets/image%20%286%29.png)

其中master文件夹存放关于master结点的my.cnf和Dockerfile，slave文件夹存放关于slave结点的my.cnf和Dockerfile。

{% code title="docker-compose.yml" %}
```yaml
version: "3"
services:
  db-master:
    build: 
      context: ./
      dockerfile: master/Dockerfile
    restart: always
    environment:
      MYSQL_DATABASE: 'db'
      # So you don't have to use root, but you can if you like
      MYSQL_USER: 'user'
      # You can use whatever password you like
      MYSQL_PASSWORD: 'password'
      # Password for root access
      MYSQL_ROOT_PASSWORD: 'password'
    ports:
      # <Port exposed> : < MySQL Port running inside container>
      - '3306:3306'
    # Where our data will be persisted
    volumes:
      - my-db-master:/var/lib/mysql
    networks:
      - net-mysql
  
  db-slave:
    build: 
      context: ./
      dockerfile: slave/Dockerfile
    restart: always
    environment:
      MYSQL_DATABASE: 'db'
      # So you don't have to use root, but you can if you like
      MYSQL_USER: 'user'
      # You can use whatever password you like
      MYSQL_PASSWORD: 'password'
      # Password for root access
      MYSQL_ROOT_PASSWORD: 'password'
    ports:
      # <Port exposed> : < MySQL Port running inside container>
      - '3307:3306'
    # Where our data will be persisted
    volumes:
      - my-db-slave:/var/lib/mysql
    networks:
      - net-mysql
  
# Names our volume
volumes:
  my-db-master:
  my-db-slave: 

networks: 
  net-mysql:
    driver: bridge
```
{% endcode %}

现在我们就可以通过docker-compose来启动这两个结点了

```bash
docker-compose up -d
```

接下来我们就可以看到一些镜像的构建信息，当两个结点都启动之后我们来查看一下两个结点的状态

```bash
docker-compose ps -a
```

![&#x5728;&#x8FD9;&#x91CC;&#x63D2;&#x5165;&#x56FE;&#x7247;&#x63CF;&#x8FF0;](https://img-blog.csdnimg.cn/20200423214625226.png)

可以看到两个结点的状态已经是Up了，并且主结点映射在宿主机的3306端口，从结点映射在宿主机的3307端口。

我们再来查看一下这两个结点的网络信息，以便后续使用

```bash
docker network ls
```

![&#x5728;&#x8FD9;&#x91CC;&#x63D2;&#x5165;&#x56FE;&#x7247;&#x63CF;&#x8FF0;](https://img-blog.csdnimg.cn/20200423214906216.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NfODQyNDk5NDY3,size_16,color_FFFFFF,t_70)

这个就是我们刚才创建的网络，刚才创建的两个结点也挂载在这个网络上，我们来查看一下详细信息

```bash
docker inspect 62fa5033ce48
```

![&#x5728;&#x8FD9;&#x91CC;&#x63D2;&#x5165;&#x56FE;&#x7247;&#x63CF;&#x8FF0;](https://img-blog.csdnimg.cn/20200423215125125.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NfODQyNDk5NDY3,size_16,color_FFFFFF,t_70)

这样我们就差看到来两个结点的具体IP地址，因为Docker网络的配置，两个连接到同一network的容器会直接相互连通。

## 主从配置

启动之后进入从结点

```bash
docker-compose exec db-slave bash
```

进入从结点mysql中

```bash
mysql -u root -p
```

在从结点上配置主节点信息，然后把当前结点设置为从结点。

```text
mysql> CHANGE MASTER TO MASTER_HOST='192.168.64.3', MASTER_USER='root', MASTER_PASSWORD='password', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=0;
Query OK, 0 rows affected, 2 warnings (0.11 sec)

mysql> start slave;
Query OK, 0 rows affected (0.00 sec)
```

{% hint style="info" %}
正常情况我们应该创建一个用户然后赋予其相应的权限，而不是将root用户配置给他，关于用户授权相关内容可以参考：[用户授权](https://supeng842499467.gitbook.io/dive-into-mysql/shu-ju-ku-cao-zuo/yong-hu-cao-zuo/yong-hu-shou-quan)。
{% endhint %}

现在查看一下从结点的状态

```text
mysql> show slave status\G;
```

![](../.gitbook/assets/image%20%284%29.png)

都显示为YES的话那么我们的主从配置已经成功，现在我们在主节点创建一个test\_db3数据库

![](../.gitbook/assets/image%20%288%29.png)

然后切换到从结点，可以看到数据已经同步到从结点了

![](../.gitbook/assets/image%20%282%29.png)

到这里一个简单的单主节点单从结点的MySQL架构已经搭建完毕。

