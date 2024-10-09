**本项目是确定性快排与随机化快排算法的对比实验，具体实验参数设置如下：**

![](C:\Users\Jerry\AppData\Roaming\marktext\images\2024-10-09-12-42-12-image.png)



### 运行

进入code目录，运行exp.sh文件即可运行确定性快排与随机化快排的实验，并生成对应的结果文件（以txt形式保存）以及对比图（png格式）。

**注意：exp_type目前只支持random、ascend、descend三种，对于随机化快排还有额外一种：random_gaussin，请确保在选择random_gaussin进行实验时将命令行文件中的“vanilla QS”实验关闭。下面是几种exp_type的具体含义：**

1.random：数组元素随机生成

2.ascend: 数组元素升序排列，此时算法将自动进行降序操作（为测试最坏情况）

3.descend：数组元素降序排列，此时算法将自动进行升序操作（为测试最坏情况）

4.random_gaussin：对于随机化快排的枢轴元素选取，将从高斯分布中采样。（仅对随机化快排生效！）
