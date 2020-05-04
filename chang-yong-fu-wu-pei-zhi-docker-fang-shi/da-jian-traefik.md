# 搭建traefik

```text
docker run --name proxy -p "80:80" -p "8080:8080" -v /var/run/docker.sock:/var/run/docker.sock -v ./traefik.toml:/etc/traefik/traefik.toml -d traefik /bin/bash --api --docker --docker.domain=docker.localhost --logLevel=DEBUG
```

