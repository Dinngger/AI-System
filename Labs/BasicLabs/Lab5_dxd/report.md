# Lab 5 - 配置Container进行云上训练或推理

### 实验环境

||||
|--------|--------------|--------------------------|
|硬件环境|CPU（vCPU数目）|Intel® Core™ i7-9700K CPU @ 3.60GHz × 8  &nbsp; |
||GPU(型号，数目)|GeForce RTX 2070 SUPER|
|软件环境|OS版本|Ubuntu 18.04.5 LTS|
||深度学习框架<br>python包名称及版本|Python 3.6.10<br>PyTorch 1.6.0|
||CUDA版本|11.0|
||||

### 实验结果

1.	使用Docker部署PyTorch MNIST 训练程序，以交互的方式在容器中运行训练程序。

    1. 创建模型训练镜像[Dockerfile](Dockerfile.gpu)
    2. 镜像构建成功的日志

<pre><font color="#8AE234"><b>dinger@dinger-ubuntu</b></font>:<font color="#729FCF"><b>~/mine/UniversityClass/AI-System/Labs/BasicLabs/Lab5_dxd</b></font>$ DOCKER_BUILDKIT=1 docker build --file Dockerfile.gpu -t torch .
[+] Building 477.2s (17/17) FINISHED                                                                                                                                                                               
<font color="#3465A4"> =&gt; [internal] load build definition from Dockerfile.gpu                                                                                                                                                      0.0s</font>
<font color="#3465A4"> =&gt; =&gt; transferring dockerfile: 1.54kB                                                                                                                                                                        0.0s</font>
<font color="#3465A4"> =&gt; [internal] load .dockerignore                                                                                                                                                                             0.0s</font>
<font color="#3465A4"> =&gt; =&gt; transferring context: 2B                                                                                                                                                                               0.0s</font>
<font color="#3465A4"> =&gt; [internal] load metadata for docker.io/nvidia/cuda:10.2-cudnn7-runtime-ubuntu18.04                                                                                                                        0.0s</font>
<font color="#3465A4"> =&gt; [stage-0  1/12] FROM docker.io/nvidia/cuda:10.2-cudnn7-runtime-ubuntu18.04                                                                                                                                0.0s</font>
<font color="#3465A4"> =&gt; [internal] load build context                                                                                                                                                                             0.0s</font>
<font color="#3465A4"> =&gt; =&gt; transferring context: 44B                                                                                                                                                                              0.0s</font>
<font color="#3465A4"> =&gt; CACHED [stage-0  2/12] RUN mkdir -p /src/app                                                                                                                                                              0.0s</font>
<font color="#3465A4"> =&gt; CACHED [stage-0  3/12] WORKDIR /src/app                                                                                                                                                                   0.0s</font>
<font color="#3465A4"> =&gt; CACHED [stage-0  4/12] COPY pytorch_mnist_basic.py /src/app                                                                                                                                               0.0s</font>
<font color="#3465A4"> =&gt; CACHED [stage-0  5/12] RUN sed -i &quot;s@http://.*archive.ubuntu.com@http://repo.huaweicloud.com@g&quot; /etc/apt/sources.list                                                                                     0.0s</font>
<font color="#3465A4"> =&gt; CACHED [stage-0  6/12] RUN sed -i &quot;s@http://.*security.ubuntu.com@http://repo.huaweicloud.com@g&quot; /etc/apt/sources.list                                                                                    0.0s</font>
<font color="#3465A4"> =&gt; CACHED [stage-0  7/12] RUN --mount=type=cache,id=apt-dev,target=/var/cache/apt     apt-get update &amp;&amp;     DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y     ca-certificates    0.0s</font>
<font color="#3465A4"> =&gt; CACHED [stage-0  8/12] RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1     &amp;&amp; update-alternatives --install /usr/local/bin/pip pip /usr/local/bin/pip3 1                      0.0s</font>
<font color="#3465A4"> =&gt; CACHED [stage-0  9/12] RUN export USE_CUDA=1                                                                                                                                                              0.0s</font>
<font color="#3465A4"> =&gt; CACHED [stage-0 10/12] RUN pip install --no-cache-dir pip -U                                                                                                                                              0.0s</font>
<font color="#3465A4"> =&gt; CACHED [stage-0 11/12] RUN pip config set global.index-url https://repo.huaweicloud.com/repository/pypi/simple                                                                                            0.0s</font>
<font color="#3465A4"> =&gt; [stage-0 12/12] RUN pip install --no-cache-dir install torch torchvision                                                                                                                                472.6s</font>
<font color="#3465A4"> =&gt; exporting to image                                                                                                                                                                                        4.6s</font> 
<font color="#3465A4"> =&gt; =&gt; exporting layers                                                                                                                                                                                       4.6s</font> 
<font color="#3465A4"> =&gt; =&gt; writing image sha256:a2dde5c2613b2766a58e55c3342fe71b8c5fd30ef335cbbee1e5797996c10700                                                                                                                  0.0s</font> 
<font color="#3465A4"> =&gt; =&gt; naming to docker.io/library/torch                                                                                                                                                                      0.0s</font></pre>

1.	
    1. 启动训练程序，训练成功日志
```bash
nvidia-docker run -e NVIDIA_VISIBLE_DEVICES=all --name training -it torch
```
<pre><font color="#8AE234"><b>dinger@dinger-ubuntu</b></font>:<font color="#729FCF"><b>~/mine/UniversityClass/AI-System/Labs/BasicLabs/Lab5_dxd</b></font>$ docker ps -a
CONTAINER ID   IMAGE                              COMMAND       CREATED          STATUS                  PORTS     NAMES
14134595d61f   torch                              &quot;/bin/bash&quot;   36 seconds ago   Up 1 second                       training
</pre>

    docker cp data training:src/app/data

<pre><font color="#8AE234"><b>dinger@dinger-ubuntu</b></font>:<font color="#729FCF"><b>~/mine/UniversityClass/AI-System/Labs/BasicLabs/Lab5_dxd</b></font>$ docker attach training
root@14134595d61f:/src/app# ls
<span style="background-color:#4E9A06"><font color="#3465A4">data</font></span>  pytorch_mnist_basic.py
root@14134595d61f:/src/app# python pytorch_mnist_basic.py --no-cuda
Train Epoch: 1 [0/60000 (0%)]	Loss: 2.305400
Train Epoch: 1 [640/60000 (1%)]	Loss: 1.359780
Train Epoch: 1 [1280/60000 (2%)]	Loss: 0.830733
Train Epoch: 1 [1920/60000 (3%)]	Loss: 0.613777
Train Epoch: 1 [2560/60000 (4%)]	Loss: 0.362320
Train Epoch: 1 [3200/60000 (5%)]	Loss: 0.449934
Train Epoch: 1 [3840/60000 (6%)]	Loss: 0.287096
Train Epoch: 1 [4480/60000 (7%)]	Loss: 0.284359
Train Epoch: 1 [5120/60000 (9%)]	Loss: 0.603375
Train Epoch: 1 [5760/60000 (10%)]	Loss: 0.227686
Train Epoch: 1 [6400/60000 (11%)]	Loss: 0.262790
Train Epoch: 1 [7040/60000 (12%)]	Loss: 0.333342
Train Epoch: 1 [7680/60000 (13%)]	Loss: 0.190327
Train Epoch: 1 [8320/60000 (14%)]	Loss: 0.234681
Train Epoch: 1 [8960/60000 (15%)]	Loss: 0.275586
Train Epoch: 1 [9600/60000 (16%)]	Loss: 0.100516
Train Epoch: 1 [10240/60000 (17%)]	Loss: 0.283203
Train Epoch: 1 [10880/60000 (18%)]	Loss: 0.098579
Train Epoch: 1 [11520/60000 (19%)]	Loss: 0.401096
Train Epoch: 1 [12160/60000 (20%)]	Loss: 0.279153
Train Epoch: 1 [12800/60000 (21%)]	Loss: 0.250224
Train Epoch: 1 [13440/60000 (22%)]	Loss: 0.185345
Train Epoch: 1 [14080/60000 (23%)]	Loss: 0.135799
Train Epoch: 1 [14720/60000 (25%)]	Loss: 0.402020
Train Epoch: 1 [15360/60000 (26%)]	Loss: 0.170696
Train Epoch: 1 [16000/60000 (27%)]	Loss: 0.121911
Train Epoch: 1 [16640/60000 (28%)]	Loss: 0.173890
Train Epoch: 1 [17280/60000 (29%)]	Loss: 0.054309
Train Epoch: 1 [17920/60000 (30%)]	Loss: 0.163902
Train Epoch: 1 [18560/60000 (31%)]	Loss: 0.204727
Train Epoch: 1 [19200/60000 (32%)]	Loss: 0.233742
Train Epoch: 1 [19840/60000 (33%)]	Loss: 0.084305
Train Epoch: 1 [20480/60000 (34%)]	Loss: 0.040015
Train Epoch: 1 [21120/60000 (35%)]	Loss: 0.247981
Train Epoch: 1 [21760/60000 (36%)]	Loss: 0.004915
Train Epoch: 1 [22400/60000 (37%)]	Loss: 0.065618
Train Epoch: 1 [23040/60000 (38%)]	Loss: 0.186516
Train Epoch: 1 [23680/60000 (39%)]	Loss: 0.205678
Train Epoch: 1 [24320/60000 (41%)]	Loss: 0.014292
Train Epoch: 1 [24960/60000 (42%)]	Loss: 0.131396
Train Epoch: 1 [25600/60000 (43%)]	Loss: 0.071628
Train Epoch: 1 [26240/60000 (44%)]	Loss: 0.086914
Train Epoch: 1 [26880/60000 (45%)]	Loss: 0.280320
Train Epoch: 1 [27520/60000 (46%)]	Loss: 0.238889
Train Epoch: 1 [28160/60000 (47%)]	Loss: 0.099054
Train Epoch: 1 [28800/60000 (48%)]	Loss: 0.122408
Train Epoch: 1 [29440/60000 (49%)]	Loss: 0.046899
Train Epoch: 1 [30080/60000 (50%)]	Loss: 0.145611
Train Epoch: 1 [30720/60000 (51%)]	Loss: 0.055009
Train Epoch: 1 [31360/60000 (52%)]	Loss: 0.121668
Train Epoch: 1 [32000/60000 (53%)]	Loss: 0.176140
Train Epoch: 1 [32640/60000 (54%)]	Loss: 0.132509
Train Epoch: 1 [33280/60000 (55%)]	Loss: 0.073534
Train Epoch: 1 [33920/60000 (57%)]	Loss: 0.033309
Train Epoch: 1 [34560/60000 (58%)]	Loss: 0.028644
Train Epoch: 1 [35200/60000 (59%)]	Loss: 0.228100
Train Epoch: 1 [35840/60000 (60%)]	Loss: 0.191699
Train Epoch: 1 [36480/60000 (61%)]	Loss: 0.062068
Train Epoch: 1 [37120/60000 (62%)]	Loss: 0.129702
Train Epoch: 1 [37760/60000 (63%)]	Loss: 0.162997
Train Epoch: 1 [38400/60000 (64%)]	Loss: 0.125742
Train Epoch: 1 [39040/60000 (65%)]	Loss: 0.052491
Train Epoch: 1 [39680/60000 (66%)]	Loss: 0.023839
Train Epoch: 1 [40320/60000 (67%)]	Loss: 0.083350
Train Epoch: 1 [40960/60000 (68%)]	Loss: 0.102641
Train Epoch: 1 [41600/60000 (69%)]	Loss: 0.133655
Train Epoch: 1 [42240/60000 (70%)]	Loss: 0.105386
Train Epoch: 1 [42880/60000 (71%)]	Loss: 0.077996
Train Epoch: 1 [43520/60000 (72%)]	Loss: 0.201702
Train Epoch: 1 [44160/60000 (74%)]	Loss: 0.055983
Train Epoch: 1 [44800/60000 (75%)]	Loss: 0.155848
Train Epoch: 1 [45440/60000 (76%)]	Loss: 0.228331
Train Epoch: 1 [46080/60000 (77%)]	Loss: 0.120221
Train Epoch: 1 [46720/60000 (78%)]	Loss: 0.159441
Train Epoch: 1 [47360/60000 (79%)]	Loss: 0.114924
Train Epoch: 1 [48000/60000 (80%)]	Loss: 0.046828
Train Epoch: 1 [48640/60000 (81%)]	Loss: 0.020038
Train Epoch: 1 [49280/60000 (82%)]	Loss: 0.070051
Train Epoch: 1 [49920/60000 (83%)]	Loss: 0.078943
Train Epoch: 1 [50560/60000 (84%)]	Loss: 0.074607
Train Epoch: 1 [51200/60000 (85%)]	Loss: 0.302636
Train Epoch: 1 [51840/60000 (86%)]	Loss: 0.009190
Train Epoch: 1 [52480/60000 (87%)]	Loss: 0.023378
Train Epoch: 1 [53120/60000 (88%)]	Loss: 0.166928
Train Epoch: 1 [53760/60000 (90%)]	Loss: 0.063319
Train Epoch: 1 [54400/60000 (91%)]	Loss: 0.112947
Train Epoch: 1 [55040/60000 (92%)]	Loss: 0.040906
Train Epoch: 1 [55680/60000 (93%)]	Loss: 0.104862
Train Epoch: 1 [56320/60000 (94%)]	Loss: 0.077306
Train Epoch: 1 [56960/60000 (95%)]	Loss: 0.088751
Train Epoch: 1 [57600/60000 (96%)]	Loss: 0.150158
Train Epoch: 1 [58240/60000 (97%)]	Loss: 0.035516
Train Epoch: 1 [58880/60000 (98%)]	Loss: 0.012775
Train Epoch: 1 [59520/60000 (99%)]	Loss: 0.001479

Test set: Average loss: 0.0458, Accuracy: 9848/10000 (98%)
</pre>

2.	使用Docker部署MNIST模型的推理服务，并进行推理。
    1. 创建模型推理镜像[Dockerfile](Dockerfile.infer.gpu)

<pre><font color="#8AE234"><b>dinger@dinger-ubuntu</b></font>:<font color="#729FCF"><b>~/mine/UniversityClass/AI-System/Labs/BasicLabs/Lab5_dxd</b></font>$ DOCKER_BUILDKIT=1 docker build --file Dockerfile.infer.gpu -t torchserve .
[+] Building 531.3s (26/26) FINISHED                                                                                                                                                                               
<font color="#3465A4"> =&gt; [internal] load build definition from Dockerfile.infer.gpu                                                                                                                                                0.0s</font>
<font color="#3465A4"> =&gt; =&gt; transferring dockerfile: 3.44kB                                                                                                                                                                        0.0s</font>
<font color="#3465A4"> =&gt; [internal] load .dockerignore                                                                                                                                                                             0.0s</font>
<font color="#3465A4"> =&gt; =&gt; transferring context: 2B                                                                                                                                                                               0.0s</font>
<font color="#3465A4"> =&gt; resolve image config for docker.io/docker/dockerfile:experimental                                                                                                                                         3.6s</font>
<font color="#3465A4"> =&gt; CACHED docker-image://docker.io/docker/dockerfile:experimental@sha256:600e5c62eedff338b3f7a0850beb7c05866e0ef27b2d2e8c02aa468e78496ff5                                                                    0.0s</font>
<font color="#3465A4"> =&gt; [internal] load metadata for docker.io/nvidia/cuda:10.2-cudnn7-runtime-ubuntu18.04                                                                                                                        0.0s</font>
<font color="#3465A4"> =&gt; [internal] load build context                                                                                                                                                                             0.0s</font>
<font color="#3465A4"> =&gt; =&gt; transferring context: 80B                                                                                                                                                                              0.0s</font>
<font color="#3465A4"> =&gt; [compile-image  1/11] FROM docker.io/nvidia/cuda:10.2-cudnn7-runtime-ubuntu18.04                                                                                                                          0.0s</font>
<font color="#3465A4"> =&gt; CACHED [runtime-image 2/9] RUN --mount=type=cache,target=/var/cache/apt     apt-get update &amp;&amp;     DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y     python3     python3-dist  0.0s</font>
<font color="#3465A4"> =&gt; CACHED [runtime-image 3/9] RUN useradd -m model-server     &amp;&amp; mkdir -p /home/model-server/tmp                                                                                                             0.0s</font>
<font color="#3465A4"> =&gt; CACHED [compile-image  2/11] RUN sed -i &quot;s@http://.*archive.ubuntu.com@http://repo.huaweicloud.com@g&quot; /etc/apt/sources.list                                                                               0.0s</font>
<font color="#3465A4"> =&gt; CACHED [compile-image  3/11] RUN sed -i &quot;s@http://.*security.ubuntu.com@http://repo.huaweicloud.com@g&quot; /etc/apt/sources.list                                                                              0.0s</font>
<font color="#3465A4"> =&gt; CACHED [compile-image  4/11] RUN --mount=type=cache,id=apt-dev,target=/var/cache/apt     apt-get update &amp;&amp;     DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y     ca-certific  0.0s</font>
<font color="#3465A4"> =&gt; CACHED [compile-image  5/11] RUN python3 -m venv /home/venv                                                                                                                                               0.0s</font>
<font color="#3465A4"> =&gt; CACHED [compile-image  6/11] RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1     &amp;&amp; update-alternatives --install /usr/local/bin/pip pip /usr/local/bin/pip3 1                0.0s</font>
<font color="#3465A4"> =&gt; CACHED [compile-image  7/11] RUN export USE_CUDA=1                                                                                                                                                        0.0s</font>
<font color="#3465A4"> =&gt; CACHED [compile-image  8/11] RUN pip install --no-cache-dir pip -U                                                                                                                                        0.0s</font>
<font color="#3465A4"> =&gt; CACHED [compile-image  9/11] RUN pip config set global.index-url https://repo.huaweicloud.com/repository/pypi/simple                                                                                      0.0s</font>
<font color="#3465A4"> =&gt; [compile-image 10/11] RUN pip install --no-cache-dir torch torchvision                                                                                                                                  478.7s</font>
<font color="#3465A4"> =&gt; [compile-image 11/11] RUN pip install --no-cache-dir captum torchtext torchserve torch-model-archiver                                                                                                    37.3s</font>
<font color="#3465A4"> =&gt; [runtime-image 4/9] COPY --chown=model-server --from=compile-image /home/venv /home/venv                                                                                                                  1.8s</font> 
<font color="#3465A4"> =&gt; [runtime-image 5/9] COPY dockerd-entrypoint.sh /usr/local/bin/dockerd-entrypoint.sh                                                                                                                       0.0s</font> 
<font color="#3465A4"> =&gt; [runtime-image 6/9] RUN chmod +x /usr/local/bin/dockerd-entrypoint.sh     &amp;&amp; chown -R model-server /home/model-server                                                                                     0.3s</font> 
<font color="#3465A4"> =&gt; [runtime-image 7/9] COPY config.properties /home/model-server/config.properties                                                                                                                           0.0s</font> 
<font color="#3465A4"> =&gt; [runtime-image 8/9] RUN mkdir /home/model-server/model-store &amp;&amp; chown -R model-server /home/model-server/model-store                                                                                      0.4s</font> 
<font color="#3465A4"> =&gt; [runtime-image 9/9] WORKDIR /home/model-server                                                                                                                                                            0.0s</font> 
<font color="#3465A4"> =&gt; exporting to image                                                                                                                                                                                        5.1s</font>
<font color="#3465A4"> =&gt; =&gt; exporting layers                                                                                                                                                                                       5.1s</font>
<font color="#3465A4"> =&gt; =&gt; writing image sha256:1c7b8e00dd4edde7b0e2cbd5a31cb22bd270cdb2958f4c4ea0191e472e113239                                                                                                                  0.0s</font>
<font color="#3465A4"> =&gt; =&gt; naming to docker.io/library/torchserve                                                                                                                                                                 0.0s</font>
</pre>

2.	
    1. 启动容器，访问TorchServe API，提交返回结果日志

<pre><font color="#8AE234"><b>dinger@dinger-ubuntu</b></font>:<font color="#729FCF"><b>~/mine/UniversityClass/AI-System/Labs/BasicLabs/Lab5_dxd</b></font>$ nvidia-docker run -e NVIDIA_VISIBLE_DEVICES=all -p 8080:8080 -p 8081:8081 --name server torchserve
2021-03-23 14:24:08,061 [INFO ] main org.pytorch.serve.ModelServer - 
Torchserve version: 0.3.1
TS Home: /home/venv/lib/python3.6/site-packages
Current directory: /home/model-server
Temp directory: /home/model-server/tmp
Number of GPUs: 1
Number of CPUs: 8
Max heap size: 8010 M
Python executable: /home/venv/bin/python3
Config file: /home/model-server/config.properties
Inference address: http://0.0.0.0:8080
Management address: http://0.0.0.0:8081
Metrics address: http://0.0.0.0:8082
Model Store: /home/model-server/model-store
Initial Models: N/A
Log dir: /home/model-server/logs
Metrics dir: /home/model-server/logs
Netty threads: 32
Netty client threads: 0
Default workers per model: 1
Blacklist Regex: N/A
Maximum Response Size: 6553500
Maximum Request Size: 6553500
Prefer direct buffer: false
Allowed Urls: [file://.*|http(s)?://.*]
Custom python dependency for model allowed: false
Metrics report format: prometheus
Enable metrics API: true
2021-03-23 14:24:08,089 [INFO ] main org.pytorch.serve.ModelServer - Initialize Inference server with: EpollServerSocketChannel.
2021-03-23 14:24:08,133 [INFO ] main org.pytorch.serve.ModelServer - Inference API bind to: http://0.0.0.0:8080
2021-03-23 14:24:08,133 [INFO ] main org.pytorch.serve.ModelServer - Initialize Management server with: EpollServerSocketChannel.
2021-03-23 14:24:08,134 [INFO ] main org.pytorch.serve.ModelServer - Management API bind to: http://0.0.0.0:8081
2021-03-23 14:24:08,134 [INFO ] main org.pytorch.serve.ModelServer - Initialize Metrics server with: EpollServerSocketChannel.
2021-03-23 14:24:08,135 [INFO ] main org.pytorch.serve.ModelServer - Metrics API bind to: http://0.0.0.0:8082
Model server started.
2021-03-23 14:24:08,320 [INFO ] pool-2-thread-1 TS_METRICS - CPUUtilization.Percent:50.0|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509448
2021-03-23 14:24:08,321 [INFO ] pool-2-thread-1 TS_METRICS - DiskAvailable.Gigabytes:30.741596221923828|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509448
2021-03-23 14:24:08,321 [INFO ] pool-2-thread-1 TS_METRICS - DiskUsage.Gigabytes:169.38091278076172|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509448
2021-03-23 14:24:08,321 [INFO ] pool-2-thread-1 TS_METRICS - DiskUtilization.Percent:84.6|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509448
2021-03-23 14:24:08,321 [INFO ] pool-2-thread-1 TS_METRICS - MemoryAvailable.Megabytes:28127.078125|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509448
2021-03-23 14:24:08,321 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUsed.Megabytes:3396.859375|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509448
2021-03-23 14:24:08,321 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUtilization.Percent:12.2|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509448
2021-03-23 14:25:08,360 [INFO ] pool-2-thread-1 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509508
2021-03-23 14:25:08,361 [INFO ] pool-2-thread-1 TS_METRICS - DiskAvailable.Gigabytes:30.733585357666016|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509508
2021-03-23 14:25:08,361 [INFO ] pool-2-thread-1 TS_METRICS - DiskUsage.Gigabytes:169.38892364501953|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509508
2021-03-23 14:25:08,361 [INFO ] pool-2-thread-1 TS_METRICS - DiskUtilization.Percent:84.6|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509508
2021-03-23 14:25:08,361 [INFO ] pool-2-thread-1 TS_METRICS - MemoryAvailable.Megabytes:28071.1171875|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509508
2021-03-23 14:25:08,361 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUsed.Megabytes:3444.1015625|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509508
2021-03-23 14:25:08,361 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUtilization.Percent:12.4|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509508
2021-03-23 14:26:08,360 [INFO ] pool-2-thread-1 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509568
2021-03-23 14:26:08,360 [INFO ] pool-2-thread-1 TS_METRICS - DiskAvailable.Gigabytes:30.733394622802734|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509568
2021-03-23 14:26:08,361 [INFO ] pool-2-thread-1 TS_METRICS - DiskUsage.Gigabytes:169.3891143798828|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509568
2021-03-23 14:26:08,361 [INFO ] pool-2-thread-1 TS_METRICS - DiskUtilization.Percent:84.6|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509568
2021-03-23 14:26:08,361 [INFO ] pool-2-thread-1 TS_METRICS - MemoryAvailable.Megabytes:28124.35546875|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509568
2021-03-23 14:26:08,361 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUsed.Megabytes:3399.5703125|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509568
2021-03-23 14:26:08,361 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUtilization.Percent:12.2|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509568
2021-03-23 14:26:14,490 [INFO ] pool-1-thread-1 ACCESS_LOG - /172.17.0.1:37362 "GET /ping HTTP/1.1" 200 4
2021-03-23 14:26:14,490 [INFO ] pool-1-thread-1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:ef6c7de9495d,timestamp:null
2021-03-23 14:27:08,360 [INFO ] pool-2-thread-1 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509628
2021-03-23 14:27:08,361 [INFO ] pool-2-thread-1 TS_METRICS - DiskAvailable.Gigabytes:30.733192443847656|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509628
2021-03-23 14:27:08,361 [INFO ] pool-2-thread-1 TS_METRICS - DiskUsage.Gigabytes:169.3893165588379|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509628
2021-03-23 14:27:08,361 [INFO ] pool-2-thread-1 TS_METRICS - DiskUtilization.Percent:84.6|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509628
2021-03-23 14:27:08,361 [INFO ] pool-2-thread-1 TS_METRICS - MemoryAvailable.Megabytes:28092.10546875|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509628
2021-03-23 14:27:08,361 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUsed.Megabytes:3427.87890625|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509628
2021-03-23 14:27:08,361 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUtilization.Percent:12.3|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509628
2021-03-23 14:28:08,360 [INFO ] pool-2-thread-2 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509688
2021-03-23 14:28:08,360 [INFO ] pool-2-thread-2 TS_METRICS - DiskAvailable.Gigabytes:30.73299789428711|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509688
2021-03-23 14:28:08,361 [INFO ] pool-2-thread-2 TS_METRICS - DiskUsage.Gigabytes:169.38951110839844|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509688
2021-03-23 14:28:08,361 [INFO ] pool-2-thread-2 TS_METRICS - DiskUtilization.Percent:84.6|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509688
2021-03-23 14:28:08,361 [INFO ] pool-2-thread-2 TS_METRICS - MemoryAvailable.Megabytes:28087.984375|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509688
2021-03-23 14:28:08,361 [INFO ] pool-2-thread-2 TS_METRICS - MemoryUsed.Megabytes:3435.88671875|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509688
2021-03-23 14:28:08,361 [INFO ] pool-2-thread-2 TS_METRICS - MemoryUtilization.Percent:12.3|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509688
2021-03-23 14:29:08,360 [INFO ] pool-2-thread-1 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509748
2021-03-23 14:29:08,360 [INFO ] pool-2-thread-1 TS_METRICS - DiskAvailable.Gigabytes:30.732803344726562|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509748
2021-03-23 14:29:08,360 [INFO ] pool-2-thread-1 TS_METRICS - DiskUsage.Gigabytes:169.38970565795898|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509748
2021-03-23 14:29:08,360 [INFO ] pool-2-thread-1 TS_METRICS - DiskUtilization.Percent:84.6|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509748
2021-03-23 14:29:08,360 [INFO ] pool-2-thread-1 TS_METRICS - MemoryAvailable.Megabytes:28067.97265625|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509748
2021-03-23 14:29:08,360 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUsed.Megabytes:3456.8515625|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509748
2021-03-23 14:29:08,360 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUtilization.Percent:12.4|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509748
2021-03-23 14:30:08,325 [INFO ] pool-2-thread-1 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509808
2021-03-23 14:30:08,325 [INFO ] pool-2-thread-1 TS_METRICS - DiskAvailable.Gigabytes:30.724796295166016|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509808
2021-03-23 14:30:08,325 [INFO ] pool-2-thread-1 TS_METRICS - DiskUsage.Gigabytes:169.39771270751953|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509808
2021-03-23 14:30:08,325 [INFO ] pool-2-thread-1 TS_METRICS - DiskUtilization.Percent:84.6|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509808
2021-03-23 14:30:08,325 [INFO ] pool-2-thread-1 TS_METRICS - MemoryAvailable.Megabytes:28065.1640625|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509808
2021-03-23 14:30:08,325 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUsed.Megabytes:3459.53515625|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509808
2021-03-23 14:30:08,325 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUtilization.Percent:12.4|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509808
2021-03-23 14:31:08,325 [INFO ] pool-2-thread-2 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509868
2021-03-23 14:31:08,326 [INFO ] pool-2-thread-2 TS_METRICS - DiskAvailable.Gigabytes:30.724605560302734|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509868
2021-03-23 14:31:08,326 [INFO ] pool-2-thread-2 TS_METRICS - DiskUsage.Gigabytes:169.3979034423828|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509868
2021-03-23 14:31:08,326 [INFO ] pool-2-thread-2 TS_METRICS - DiskUtilization.Percent:84.6|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509868
2021-03-23 14:31:08,326 [INFO ] pool-2-thread-2 TS_METRICS - MemoryAvailable.Megabytes:28033.36328125|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509868
2021-03-23 14:31:08,326 [INFO ] pool-2-thread-2 TS_METRICS - MemoryUsed.Megabytes:3491.171875|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509868
2021-03-23 14:31:08,326 [INFO ] pool-2-thread-2 TS_METRICS - MemoryUtilization.Percent:12.5|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616509868

</pre>

<pre><font color="#8AE234"><b>dinger@dinger-ubuntu</b></font>:<font color="#729FCF"><b>~/mine</b></font>$ curl http://localhost:8080/ping
{
  &quot;status&quot;: &quot;Healthy&quot;
}
</pre>

2.	
    1. 使用训练好的模型，启动TorchServe，在新的终端中，使用一张图片进行推理服务。提交图片和推理程序返回结果截图。

#### 使用model archiver进行模型归档

<pre><font color="#8AE234"><b>dinger@dinger-ubuntu</b></font>:<font color="#729FCF"><b>~/mine</b></font>$ docker exec -it server /bin/bash
model-server@ef6c7de9495d:~$ cd model-store/
model-server@ef6c7de9495d:~/model-store$ wget https://download.pytorch.org/models/densenet161-8d451a50.pth
--2021-03-23 14:34:06--  https://download.pytorch.org/models/densenet161-8d451a50.pth
Resolving download.pytorch.org (download.pytorch.org)... 13.224.160.89, 13.224.160.39, 13.224.160.7, ...
Connecting to download.pytorch.org (download.pytorch.org)|13.224.160.89|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 115730790 (110M) [application/x-www-form-urlencoded]
Saving to: &apos;densenet161-8d451a50.pth&apos;

densenet161-8d451a50.pth                             100%[=====================================================================================================================&gt;] 110.37M  2.85MB/s    in 42s     

2021-03-23 14:34:50 (2.60 MB/s) - &apos;densenet161-8d451a50.pth&apos; saved [115730790/115730790]
model-server@ef6c7de9495d:~/model-store$ torch-model-archiver --model-name densenet161 --version 1.0 --model-file ../model.py --serialized-file ./densenet161-8d451a50.pth --export-path ./ --extra-files ../index_to_name.json --handler image_classifier
model-server@ef6c7de9495d:~/model-store$ ls
densenet161-8d451a50.pth  densenet161.mar
</pre>

#### 启动TorchServe进行推理模型

<pre>
model-server@ef6c7de9495d:~$ torchserve --stop
TorchServe has stopped.
model-server@ef6c7de9495d:~$ torchserve --start --ncs --model-store model-store --models densenet161.mar
model-server@ef6c7de9495d:~$ 2021-03-23 14:45:38,365 [INFO ] main org.pytorch.serve.ModelServer - 
Torchserve version: 0.3.1
TS Home: /home/venv/lib/python3.6/site-packages
Current directory: /home/model-server
Temp directory: /home/model-server/tmp
Number of GPUs: 1
Number of CPUs: 8
Max heap size: 8010 M
Python executable: /home/venv/bin/python3
Config file: config.properties
Inference address: http://0.0.0.0:8080
Management address: http://0.0.0.0:8081
Metrics address: http://0.0.0.0:8082
Model Store: /home/model-server/model-store
Initial Models: densenet161.mar
Log dir: /home/model-server/logs
Metrics dir: /home/model-server/logs
Netty threads: 32
Netty client threads: 0
Default workers per model: 1
Blacklist Regex: N/A
Maximum Response Size: 6553500
Maximum Request Size: 6553500
Prefer direct buffer: false
Allowed Urls: [file://.*|http(s)?://.*]
Custom python dependency for model allowed: false
Metrics report format: prometheus
Enable metrics API: true
2021-03-23 14:45:38,391 [INFO ] main org.pytorch.serve.ModelServer - Loading initial models: densenet161.mar
2021-03-23 14:45:39,658 [INFO ] main org.pytorch.serve.archive.ModelArchive - eTag 637dc5dd617b4840b4994da2ea826fd5
2021-03-23 14:45:39,664 [DEBUG] main org.pytorch.serve.wlm.ModelVersionedRefs - Adding new version 1.0 for model densenet161
2021-03-23 14:45:39,664 [DEBUG] main org.pytorch.serve.wlm.ModelVersionedRefs - Setting default version to 1.0 for model densenet161
2021-03-23 14:45:39,664 [INFO ] main org.pytorch.serve.wlm.ModelManager - Model densenet161 loaded.
2021-03-23 14:45:39,665 [DEBUG] main org.pytorch.serve.wlm.ModelManager - updateModel: densenet161, count: 1
2021-03-23 14:45:39,672 [INFO ] main org.pytorch.serve.ModelServer - Initialize Inference server with: EpollServerSocketChannel.
2021-03-23 14:45:39,718 [INFO ] main org.pytorch.serve.ModelServer - Inference API bind to: http://0.0.0.0:8080
2021-03-23 14:45:39,718 [INFO ] main org.pytorch.serve.ModelServer - Initialize Management server with: EpollServerSocketChannel.
2021-03-23 14:45:39,719 [INFO ] main org.pytorch.serve.ModelServer - Management API bind to: http://0.0.0.0:8081
2021-03-23 14:45:39,719 [INFO ] main org.pytorch.serve.ModelServer - Initialize Metrics server with: EpollServerSocketChannel.
2021-03-23 14:45:39,719 [INFO ] main org.pytorch.serve.ModelServer - Metrics API bind to: http://0.0.0.0:8082
2021-03-23 14:45:39,743 [INFO ] W-9000-densenet161_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - Listening on port: /home/model-server/tmp/.ts.sock.9000
2021-03-23 14:45:39,744 [INFO ] W-9000-densenet161_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - [PID]719
2021-03-23 14:45:39,744 [INFO ] W-9000-densenet161_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - Torch worker started.
2021-03-23 14:45:39,744 [INFO ] W-9000-densenet161_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - Python runtime: 3.6.9
2021-03-23 14:45:39,745 [DEBUG] W-9000-densenet161_1.0 org.pytorch.serve.wlm.WorkerThread - W-9000-densenet161_1.0 State change null -> WORKER_STARTED
2021-03-23 14:45:39,747 [INFO ] W-9000-densenet161_1.0 org.pytorch.serve.wlm.WorkerThread - Connecting to: /home/model-server/tmp/.ts.sock.9000
2021-03-23 14:45:39,754 [INFO ] W-9000-densenet161_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - Connection accepted: /home/model-server/tmp/.ts.sock.9000.
Model server started.
2021-03-23 14:45:39,891 [INFO ] pool-2-thread-1 TS_METRICS - CPUUtilization.Percent:100.0|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616510739
2021-03-23 14:45:39,892 [INFO ] pool-2-thread-1 TS_METRICS - DiskAvailable.Gigabytes:30.115676879882812|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616510739
2021-03-23 14:45:39,892 [INFO ] pool-2-thread-1 TS_METRICS - DiskUsage.Gigabytes:170.00683212280273|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616510739
2021-03-23 14:45:39,892 [INFO ] pool-2-thread-1 TS_METRICS - DiskUtilization.Percent:85.0|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616510739
2021-03-23 14:45:39,892 [INFO ] pool-2-thread-1 TS_METRICS - MemoryAvailable.Megabytes:27729.90234375|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616510739
2021-03-23 14:45:39,892 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUsed.Megabytes:3646.5|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616510739
2021-03-23 14:45:39,892 [INFO ] pool-2-thread-1 TS_METRICS - MemoryUtilization.Percent:13.4|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616510739
2021-03-23 14:45:40,199 [INFO ] W-9000-densenet161_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - Generating new fontManager, this may take some time...
2021-03-23 14:45:42,768 [INFO ] W-9000-densenet161_1.0 org.pytorch.serve.wlm.WorkerThread - Backend response time: 2993
2021-03-23 14:45:42,768 [DEBUG] W-9000-densenet161_1.0 org.pytorch.serve.wlm.WorkerThread - W-9000-densenet161_1.0 State change WORKER_STARTED -> WORKER_MODEL_LOADED
2021-03-23 14:45:42,768 [INFO ] W-9000-densenet161_1.0 TS_METRICS - W-9000-densenet161_1.0.ms:3100|#Level:Host|#hostname:ef6c7de9495d,timestamp:1616510742
2021-03-23 14:45:42,769 [INFO ] W-9000-densenet161_1.0 TS_METRICS - WorkerThreadTime.ms:19|#Level:Host|#hostname:ef6c7de9495d,timestamp:null
</pre>
<pre><font color="#8AE234"><b>dinger@dinger-ubuntu</b></font>:<font color="#729FCF"><b>~/mine/dockers/serve/examples/image_classifier</b></font>$ curl -X POST http://127.0.0.1:8080/predictions/densenet161 -T kitten.jpg
{
  "tiger_cat": 0.4693357050418854,
  "tabby": 0.4633876085281372,
  "Egyptian_cat": 0.06456158310174942,
  "lynx": 0.001282821991480887,
  "plastic_bag": 0.00023323067580349743
}
</pre>
