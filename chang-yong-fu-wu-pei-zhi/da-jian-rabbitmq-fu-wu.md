# 搭建RabbitMQ服务

{% code title="docker-compose.yml" %}
```yaml
version: "3"

services:

  rabbitmq:
    image: rabbitmq:management
    hostname: myrabbitmq
    ports: 
        - "5672:5672"
        - "15672:15672"
    volumes: 
        - rabbitmq-data:/var/lib/rabbitmq
        
volumes:
    rabbitmq-data: 
```
{% endcode %}

查看服务状态

![](../.gitbook/assets/image%20%289%29.png)

确定服务正常启动后在浏览器输入网址[http://localhost:15672](http://localhost:15672/#/)，进入RabbitMQ的登陆界面

![](../.gitbook/assets/image%20%2810%29.png)

默认用户名密码都是guest。登陆之后就可以进入到主界面了

![](../.gitbook/assets/image%20%2812%29.png)



