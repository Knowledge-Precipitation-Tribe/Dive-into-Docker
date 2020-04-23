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

![](../.gitbook/assets/image%20%281%29.png)

其中master文件夹存放关于master结点的my.cnf和Dockerfile，slave文件夹存放关于slave结点的my.cnf和Dockerfile。

{% code title="docker-compose.yml" %}
```text
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

## 主从配置

启动之后进入从结点，在从结点上配置主节点信息，然后把当前结点设置为从结点。

```text
mysql> CHANGE MASTER TO MASTER_HOST='192.168.64.3', MASTER_USER='user', MASTER_PASSWORD='password', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=0;
Query OK, 0 rows affected, 2 warnings (0.11 sec)

mysql> start slave;
Query OK, 0 rows affected (0.00 sec)
```

现在查看一下从结点的状态

```text
mysql> show slave status\G;
```



现在我们在主节点创建数据库



然后切换到从结点，可以看到数据已经同步到从结点了



