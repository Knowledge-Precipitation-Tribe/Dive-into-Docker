# 搭建traefik代理

```text
version: '2'

services:
  proxy:
    image: traefik
    command: --api --docker --docker.domain=docker.localhost --logLevel=DEBUG
    networks:
      - apinetwork
    ports:
      - "80:80"
      - "8080:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./traefik.toml:/etc/traefik/traefik.toml

networks:
  apinetwork:
    external:
      name: fileserver
```

编写traefik.toml文件

```text
defaultEntryPoints = ["http"]
insecureSkipVerify = true
[entryPoints]
  [entryPoints.http]
  address = ":80"
```

