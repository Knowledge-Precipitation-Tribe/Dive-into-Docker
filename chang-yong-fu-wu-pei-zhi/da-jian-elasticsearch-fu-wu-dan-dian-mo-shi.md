---
description: 若对你有帮助欢迎Star⬆
---

# 搭建elasticsearch服务-单点模式

安装中文分词插件-待完善

{% code title="docker-compose.yml" %}
```yaml
version: "3"

services:

  elastic:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.6.2
    ports: 
        - "9200:9200"
        - "9300:9300"
    volumes: 
        - elastic-data:/data
    environment: 
        - discovery.type=single-node
        
volumes:
    elastic-data: 
```
{% endcode %}

