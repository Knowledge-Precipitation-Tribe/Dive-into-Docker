# 创建k8s集群

## 准备

安装之前准备三台服务器，或者通过虚拟机启动，这里推荐使用vargent的方式启动虚拟机。

> 下面以Centos为例

## 安装Docker

对于docker的安装可以移步

{% page-ref page="../docker-an-zhuang.md" %}

## 安装前准备

```bash
sudo bash -c 'cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF'
```

国内的用户可以将goole换成国内的源，然后分别执行以下命令：

```bash
sudo setenforce 0
sudo yum install -y kubelet kubeadm kubectl

sudo bash -c 'cat <<EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward=1
EOF'
sudo sysctl --system

sudo systemctl stop firewalld
sudo systemctl disable firewalld
# 很重要
sudo swapoff -a

systemctl enable docker.service
systemctl enable kubelet.service
```

## 创建集群

在启动之前先检查一下kubeadm, kubectl, kubelet是否安装成功，并且docker是否启动\(需要在三台服务器上都执行下面的命令\)

```bash
[root@centos ~]$ which kubeadm
/usr/bin/kubeadm
[root@centos ~]$ which kubelet
/usr/bin/kubelet
[root@centos ~]$ which kubectl
/usr/bin/kubectl
[root@centos ~]$ sudo docker version
Client: Docker Engine - Community
 Version:           20.10.7
 API version:       1.41
 Go version:        go1.13.15
 Git commit:        f0df350
 Built:             Wed Jun  2 11:58:10 2021
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.7
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.13.15
  Git commit:       b0f5bc3
  Built:            Wed Jun  2 11:56:35 2021
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.4.6
  GitCommit:        d71fcd7d8303cbf684402823e425e9dd2e99285d
 runc:
  Version:          1.0.0-rc95
  GitCommit:        b9ee9c6314599f1b4a7f497e1f1f856fe433d3b7
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

除了上面的操作，还需要检查三台服务器的k8s版本是否相同。

```bash
[root@centos ~]# kubectl version
Client Version: version.Info{Major:"1", Minor:"21", GitVersion:"v1.21.2", GitCommit:"092fbfbf53427de67cac1e9fa54aaa09a28371d7", GitTreeState:"clean", BuildDate:"2021-06-16T12:59:11Z", GoVersion:"go1.16.5", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"21", GitVersion:"v1.21.2", GitCommit:"092fbfbf53427de67cac1e9fa54aaa09a28371d7", GitTreeState:"clean", BuildDate:"2021-06-16T12:53:14Z", GoVersion:"go1.16.5", Compiler:"gc", Platform:"linux/amd64"}
[root@centos ~]# kubectl version
Client Version: version.Info{Major:"1", Minor:"21", GitVersion:"v1.21.2", GitCommit:"092fbfbf53427de67cac1e9fa54aaa09a28371d7", GitTreeState:"clean", BuildDate:"2021-06-16T12:59:11Z", GoVersion:"go1.16.5", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"21", GitVersion:"v1.21.2", GitCommit:"092fbfbf53427de67cac1e9fa54aaa09a28371d7", GitTreeState:"clean", BuildDate:"2021-06-16T12:53:14Z", GoVersion:"go1.16.5", Compiler:"gc", Platform:"linux/amd64"}
[root@centos ~]# kubelet --version
Kubernetes v1.21.2
```

然后将其中一台服务器作为master，执行初始化集群操作（只需要在master服务器执行下面的操作即可）

其中

* --pod-network-cidr: 为使用的网段
* --apiserver-advertise-address: 为master服务器的ip地址，需要注意的是三台服务器之间需要相互ping通才可以

```bash
[root@centos ~]$ sudo kubeadm init --pod-network-cidr 172.100.0.0/16 --apiserver-advertise-address xxx.xxx.xxx.xxx
[init] Using Kubernetes version: v1.15.3
[preflight] Running pre-flight checks
	[WARNING Service-Docker]: docker service is not enabled, please run 'systemctl enable docker.service'
	[WARNING IsDockerSystemdCheck]: detected "cgroupfs" as the Docker cgroup driver. The recommended driver is "systemd". Please follow the guide at https://kubernetes.io/docs/setup/cri/
	[WARNING SystemVerification]: this Docker version is not on the list of validated versions: 19.03.1. Latest validated version: 18.09
	[WARNING Service-Kubelet]: kubelet service is not enabled, please run 'systemctl enable kubelet.service'
[preflight] Pulling images required for setting up a Kubernetes cluster
[preflight] This might take a minute or two, depending on the speed of your internet connection
[preflight] You can also perform this action in beforehand using 'kubeadm config images pull'
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Activating the kubelet service
[certs] Using certificateDir folder "/etc/kubernetes/pki"
[certs] Generating "ca" certificate and key
[certs] Generating "apiserver-kubelet-client" certificate and key
[certs] Generating "apiserver" certificate and key
[certs] apiserver serving cert is signed for DNS names [k8s-master kubernetes kubernetes.default kubernetes.default.svc kubernetes.default.svc.cluster.local] and IPs [10.96.0.1 192.168.205.120]
[certs] Generating "front-proxy-ca" certificate and key
[certs] Generating "front-proxy-client" certificate and key
[certs] Generating "etcd/ca" certificate and key
[certs] Generating "etcd/server" certificate and key
[certs] etcd/server serving cert is signed for DNS names [k8s-master localhost] and IPs [192.168.205.120 127.0.0.1 ::1]
[certs] Generating "etcd/healthcheck-client" certificate and key
[certs] Generating "apiserver-etcd-client" certificate and key
[certs] Generating "etcd/peer" certificate and key
[certs] etcd/peer serving cert is signed for DNS names [k8s-master localhost] and IPs [192.168.205.120 127.0.0.1 ::1]
[certs] Generating "sa" key and public key
[kubeconfig] Using kubeconfig folder "/etc/kubernetes"
[kubeconfig] Writing "admin.conf" kubeconfig file
[kubeconfig] Writing "kubelet.conf" kubeconfig file
[kubeconfig] Writing "controller-manager.conf" kubeconfig file
[kubeconfig] Writing "scheduler.conf" kubeconfig file
[control-plane] Using manifest folder "/etc/kubernetes/manifests"
[control-plane] Creating static Pod manifest for "kube-apiserver"
[control-plane] Creating static Pod manifest for "kube-controller-manager"
[control-plane] Creating static Pod manifest for "kube-scheduler"
[etcd] Creating static Pod manifest for local etcd in "/etc/kubernetes/manifests"
[wait-control-plane] Waiting for the kubelet to boot up the control plane as static Pods from directory "/etc/kubernetes/manifests". This can take up to 4m0s
[apiclient] All control plane components are healthy after 23.002991 seconds
[upload-config] Storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
[kubelet] Creating a ConfigMap "kubelet-config-1.15" in namespace kube-system with the configuration for the kubelets in the cluster
[upload-certs] Skipping phase. Please see --upload-certs
[mark-control-plane] Marking the node k8s-master as control-plane by adding the label "node-role.kubernetes.io/master=''"
[mark-control-plane] Marking the node k8s-master as control-plane by adding the taints [node-role.kubernetes.io/master:NoSchedule]
[bootstrap-token] Using token: snipoh.vxfykjsi7e7rbtna
[bootstrap-token] Configuring bootstrap tokens, cluster-info ConfigMap, RBAC Roles
[bootstrap-token] configured RBAC rules to allow Node Bootstrap tokens to post CSRs in order for nodes to get long term certificate credentials
[bootstrap-token] configured RBAC rules to allow the csrapprover controller automatically approve CSRs from a Node Bootstrap Token
[bootstrap-token] configured RBAC rules to allow certificate rotation for all node client certificates in the cluster
[bootstrap-token] Creating the "cluster-info" ConfigMap in the "kube-public" namespace
[addons] Applied essential addon: CoreDNS
[addons] Applied essential addon: kube-proxy

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join xxx.xxx.xxx.xxx:6443 --token snipoh.vxfykjsi7e7rbtna \
    --discovery-token-ca-cert-hash sha256:e202fbfa3eed1e1d6c646dd568285947d67e99b51e824c99aeb6f45080d284c1
```

如果服务器最后的输出结果如上所示，那么代表集群已经初始化成功了。

> 需要保存好下面这个字符串，另外的服务器会通过它来加入集群
>
> ```bash
> kubeadm join xxx.xxx.xxx.xxx:6443 --token snipoh.vxfykjsi7e7rbtna \
>     --discovery-token-ca-cert-hash sha256:e202fbfa3eed1e1d6c646dd568285947d67e99b51e824c99aeb6f45080d284c1
> ```

还需要执行下面的命令：

```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

然后通过kubectl检查pod状态

```bash
[root@centos ~]$ kubectl get pod --all-namespaces
NAMESPACE     NAME                                 READY   STATUS    RESTARTS   AGE
kube-system   coredns-5c98db65d4-f4kjf             0/1     Pending   0          58m
kube-system   coredns-5c98db65d4-xqpwd             0/1     Pending   0          58m
kube-system   etcd-k8s-master                      1/1     Running   0          57m
kube-system   kube-apiserver-k8s-master            1/1     Running   0          57m
kube-system   kube-controller-manager-k8s-master   1/1     Running   0          57m
kube-system   kube-proxy-9l9vr                     1/1     Running   0          58m
kube-system   kube-scheduler-k8s-master            1/1     Running   0          57m
```

终端会输出类似这样的结果，其中两个仍处于pending状态，这是由于没有添加网络插件导致的，通过下面的命令即可添加网络插件

```bash
kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"
```

命令执行后过一段时间再检查pod状态就可以发现全部运行了，如下

```bash
[root@centos ~]$ kubectl get pod --all-namespaces
NAMESPACE     NAME                                 READY   STATUS    RESTARTS   AGE
kube-system   coredns-5c98db65d4-gpsvq             1/1     Running   0          7h31m
kube-system   coredns-5c98db65d4-st4pf             1/1     Running   0          7h31m
kube-system   etcd-k8s-master                      1/1     Running   0          7h30m
kube-system   kube-apiserver-k8s-master            1/1     Running   0          7h30m
kube-system   kube-controller-manager-k8s-master   1/1     Running   0          7h30m
kube-system   kube-proxy-kx5mv                     1/1     Running   0          7h31m
kube-system   kube-scheduler-k8s-master            1/1     Running   0          7h30m
kube-system   weave-net-57dtf                      2/2     Running   0          59s=
```

再查看当前node状态，可以发现只有master节点在集群当中

```bash
[root@centos ~]$ kubectl get nodes
NAME                           STATUS   ROLES                  AGE   VERSION
copy-of-vm-ee-centos76-v1.05   Ready    control-plane,master   16h   v1.21.2
```

接下来在另外两台服务器执行下面的命令：

```bash
# 可以通过 --node-name 来自己指定添加到k8s集群的名称
# 这里的字符串为master节点初始化集群后的输出
[root@centos ~]$ sudo kubeadm join xxx.xxx.xxx.xxx:6443 --token tte278.145ozal6u6e26ypm --discovery-token-ca-cert-hash sha256:cbb168e0665fe1b14e96a87c2da5dc1eeda04c70932ac1913d989753703277bb
[preflight] Running pre-flight checks
	[WARNING IsDockerSystemdCheck]: detected "cgroupfs" as the Docker cgroup driver. The recommended driver is "systemd". Please follow the guide at https://kubernetes.io/docs/setup/cri/
	[WARNING SystemVerification]: this Docker version is not on the list of validated versions: 19.03.1. Latest validated version: 18.09
[preflight] Reading configuration from the cluster...
[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -oyaml'
[kubelet-start] Downloading configuration for the kubelet from the "kubelet-config-1.15" ConfigMap in the kube-system namespace
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Activating the kubelet service
[kubelet-start] Waiting for the kubelet to perform the TLS Bootstrap...

This node has joined the cluster:
* Certificate signing request was sent to apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the control-plane to see this node join the cluster.
```

两台服务器都执行成功后，在master节点查看node状态即可发现另外两个节点已经添加到集群中了

```bash
[root@centos ~]$ kubectl get nodes
NAME                           STATUS   ROLES                  AGE   VERSION
copy-of-vm-ee-centos76-v1.05   Ready    control-plane,master   16h   v1.21.2
k8s-node1                      Ready    <none>                 16h   v1.21.2
k8s-node2                      Ready    <none>                 16h   v1.21.2
```

## 新手推荐

{% embed url="https://github.com/kubernetes/minikube" %}

{% embed url="https://github.com/fanux/sealos" %}



