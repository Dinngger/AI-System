# Lab 8 - 自动机器学习系统练习

## 实验环境

||||
|--------|--------------|--------------------------|
|硬件环境|CPU（vCPU数目）|Intel® Core™ i7-9700K CPU @ 3.60GHz × 8  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
||GPU(型号，数目)|GeForce RTX 2070 SUPER|
|软件环境|OS版本|Ubuntu 18.04.5 LTS|
||深度学习框架<br>python包名称及版本|Python 3.7.6<br>PyTorch 1.5.0|
||CUDA版本|10.2|
||||

## 实验结果

1.	记录不同调参方式下，cifar10程序训练结果的准确率。所有epochs均设为10.

||||
|---------|-----------------|------------|
| 调参方式 | &nbsp; &nbsp; 超参名称和设置值 &nbsp; &nbsp; | &nbsp; &nbsp; 模型准确率 &nbsp; &nbsp; |
| &nbsp; <br /> &nbsp; 原始代码 &nbsp; <br /> &nbsp; |'batch_size': 128,<br />'cutout': 0,<br />'epochs': 10,<br />'grad_clip': 0.0,<br />'initial_lr': 0.1,<br />'log_frequency': 20,<br />'model': 'resnet18',<br />'momentum': 0.9,<br />'num_workers': 2,<br />'optimizer': 'sgd',<br />'seed': 42,<br />'weight_decay': 0.0005|0.746400|
| &nbsp; <br /> &nbsp; 手动调参 &nbsp; <br /> &nbsp; |'batch_size': 32,<br />'cutout': 0,<br />'epochs': 10,<br />'grad_clip': 0.0,<br />'initial_lr': 0.01,<br />'log_frequency': 20,<br />'model': 'vgg16_bn',<br />'momentum': 0.9,<br />'num_workers': 2,<br />'optimizer': 'sgd',<br />'seed': 42,<br />'weight_decay': 0.0|0.815500|
| &nbsp; <br /> &nbsp; NNI自动调参 &nbsp; <br /> &nbsp; |'batch_size': 64,<br />'cutout': 8,<br />'epochs': 10,<br />'grad_clip': 0.0,<br />'initial_lr': 0.0007833215437439779,<br />'log_frequency': 20,<br />'model': 'resnet18',<br />'momentum': 0.9,<br />'num_workers': 2,<br />'optimizer': 'adam',<br />'seed': 42,<br />'weight_decay': 0.0007399797722863423|0.766900|
| &nbsp; <br /> &nbsp; 网络架构搜索 <br />&nbsp; &nbsp; （可选） <br /> &nbsp; |||
||||
2.	提交使用NNI自动调参方式，对 main.py、search_space.json、config.yml 改动的代码文件或截图。

3.	提交使用NNI自动调参方式，Web UI上的结果截图。
![](imgs/Screenshot%20from%202021-04-09%2011-06-54.png)
![](imgs/Screenshot%20from%202021-04-09%2011-07-46.png)
![](imgs/Screenshot%20from%202021-04-09%2011-08-15.png)
![](imgs/Screenshot%20from%202021-04-09%2011-09-54.png)
![](imgs/Screenshot%20from%202021-04-09%2011-10-11.png)

4.	（可选）提交 NAS 的搜索空间、搜索方法和搜索结果（得到的架构和最终准确率）。
