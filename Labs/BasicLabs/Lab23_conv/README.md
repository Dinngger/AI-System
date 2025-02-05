# Lab 2 & 3 - 定制一个新的张量运算及其CUDA实现和优化

## 实验目的

1.	理解DNN框架中的张量算子和在GPU加速器上加速的原理
2.	基于不同方法实现新的张量运算，并比较性能差异

## 实验环境

* PyTorch==1.5.0
* CUDA 10.0

## 实验原理

1. 深度神经网络中的张量运算原理
2. PyTorch中基于Function和Module构造张量的方法
3. 通过C++扩展编写Python函数模块
4. 矩阵运算与计算机体系结构
5. GPU加速器的加速原理

## 实验内容

### 实验流程图

![](/imgs/Lab2-flow.png "Lab2 flow chat")
![](/imgs/Lab3-flow.png "Lab3 flow chat")

### 具体步骤

1.	在MNIST的模型样例中，选择线性层（Linear）张量运算进行定制化实现

2.	理解PyTorch中Linear张量运算的计算过程，推导计算公式

3.	理解PyTorch构造张量运算的基本单位：Function和Module

4.	基于Function和Module的Python API重新实现Linear张量运算

    1. 修改MNIST样例代码
    2. 基于PyTorch  Module编写自定义的Linear 类模块
    3. 基于PyTorch Function实现前向计算和反向传播函数
    4. 使用自定义Linear替换网络中nn.Linear() 类
    5. 运行程序，验证网络正确性
   
5.	理解PyTorch张量运算在后端执行原理

6.	实现C++版本的定制化张量运算

    1. 基于C++，实现自定义Linear层前向计算和反向传播函数，并绑定为Python模型
    2. 将代码生成python的C++扩展
    3. 使用基于C++的函数扩展，实现自定义Linear类模块的前向计算和反向传播函数
    4. 运行程序，验证网络正确性

7.	实现CUDA版本的定制化张量运算

    1. 编写.cu文件，实现矩阵相乘的kernel
    2. 在上述.cu文件中，编写使用cuda进行前向计算和反向传播的函数
    3. 基于C++ API，编写.cpp文件，调用上述函数，实现Linear张量运算的前向计算和反向传播。
    4. 将代码生成python的C++扩展
    5. 使用基于C++的函数扩展，实现自定义Linear类模块的前向计算和反向传播函数
    6. 运行程序，验证网络正确性

8.	使用profiler比较网络性能：比较原有张量运算和两种自定义张量运算的性能，基于C++API，比较有无CUDA对张量运算性能的影响

9.	【可选实验，加分】实现卷积层（Convolutional）的自定义张量运算


## 实验报告

### 实验环境

||||
|--------|--------------|--------------------------|
|硬件环境|CPU（vCPU数目）|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
||GPU(型号，数目)||
|软件环境|OS版本||
||深度学习框架<br>python包名称及版本||
||CUDA版本||
||||

### 实验结果

|||
|---------------|---------------------------|
| 实现方式（Linear层为例）| &nbsp; &nbsp; &nbsp; &nbsp; 性能评测 |
|<br/> <br/>PyTorch原有张量运算<br/> <br/>&nbsp;|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
|<br/> <br/>基于Python API的定制化张量运算<br/> <br/>&nbsp;||
|<br/> <br/>基于C++的定制化张量运算<br/> <br/>&nbsp;||
|<br/> <br/>With CUDA<br/> <br/>&nbsp;||
||||

## 参考代码

1.	基于Python API实现定制化张量运算Linear

    代码位置：`Lab2/mnist_custom_linear.py`

    运行命令：`python mnist_custom_linear.py`

2.	基于C++ API实现定制化张量运算Linear

    代码位置：`Lab2/mnist_custom_linear_cpp.py`

    运行命令：
    ```
    cd mylinear_cpp_extension
    python setup install --user
    cd ..
    python mnist_custom_linear_cpp.py
    ```

## 参考资料

* EXTENDING PYTORCH: https://pytorch.org/docs/master/notes/extending.html
* CUDA Programming model: https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html 
* An Even Easier Introduction to CUDA: https://devblogs.nvidia.com/even-easier-introduction-cuda/ 
* CUSTOM C++ AND CUDA EXTENSIONS: https://pytorch.org/tutorials/advanced/cpp_extension.html
