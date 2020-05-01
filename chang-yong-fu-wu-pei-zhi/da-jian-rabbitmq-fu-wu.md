# 搭建RabbitMQ服务

```text
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

