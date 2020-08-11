# etcd-cluster

```yaml
version: '2'
services:

    etcd1:
        image: quay.io/coreos/etcd:v3.1.13
        restart: always
        ports:
            - 23791:2379
            - 23801:2380
        environment:
            ETCD_NAME: infra1
            ETCD_INITIAL_ADVERTISE_PEER_URLS: http://etcd1:2380
            ETCD_INITIAL_CLUSTER: infra3=http://etcd3:2380,infra1=http://etcd1:2380,infra2=http://etcd2:2380
            ETCD_INITIAL_CLUSTER_STATE: new
            ETCD_INITIAL_CLUSTER_TOKEN: etcd-tasting-01
            ETCD_LISTEN_CLIENT_URLS: http://etcd1:2379,http://localhost:2379
            ETCD_LISTEN_PEER_URLS: http://etcd1:2380
            ETCD_ADVERTISE_CLIENT_URLS: http://etcd1:2379

    etcd2:
        image: quay.io/coreos/etcd:v3.1.13
        restart: always
        ports:
            - 23792:2379
            - 23802:2380
        environment:
            ETCD_NAME: infra2
            ETCD_INITIAL_ADVERTISE_PEER_URLS: http://etcd2:2380
            ETCD_INITIAL_CLUSTER: infra3=http://etcd3:2380,infra1=http://etcd1:2380,infra2=http://etcd2:2380
            ETCD_INITIAL_CLUSTER_STATE: new
            ETCD_INITIAL_CLUSTER_TOKEN: etcd-tasting-01
            ETCD_LISTEN_CLIENT_URLS: http://etcd2:2379,http://localhost:2379
            ETCD_LISTEN_PEER_URLS: http://etcd2:2380
            ETCD_ADVERTISE_CLIENT_URLS: http://etcd2:2379

    etcd3:
        image: quay.io/coreos/etcd:v3.1.13
        restart: always
        ports:
            - 23793:2379
            - 23803:2380
        environment:
            ETCD_NAME: infra3
            ETCD_INITIAL_ADVERTISE_PEER_URLS: http://etcd3:2380
            ETCD_INITIAL_CLUSTER: infra3=http://etcd3:2380,infra1=http://etcd1:2380,infra2=http://etcd2:2380
            ETCD_INITIAL_CLUSTER_STATE: new
            ETCD_INITIAL_CLUSTER_TOKEN: etcd-tasting-01
            ETCD_LISTEN_CLIENT_URLS: http://etcd3:2379,http://localhost:2379
            ETCD_LISTEN_PEER_URLS: http://etcd3:2380
            ETCD_ADVERTISE_CLIENT_URLS: http://etcd3:2379
```

