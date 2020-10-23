# TensorFlow笔记

## 第一讲 神经网络计算

张量（tensor）：多维数组（列表） 阶：张量的维数

![张量](/Users/apple/Documents/TF/images/张量.png)

判断一个张量是几阶的，就看一开始有几个中括号。

![创建一个张量](/Users/apple/Documents/TF/images/创建一个张量.png)

创建一个张量，用

```python
tf.constant(张量内容, dtype = 数据类型(可选))
```

![类似matlab语法生成特定张量](/Users/apple/Documents/TF/images/类似matlab语法生成特定张量.png)

生成特定格式的张量 如全0 全1 张量内所有元素都是特定数字的张量

```
tf.zeros(维度)
tf.ones(维度)
tf.fill(维度, 指定值)
```

![生成符合标准正态分布的张量](/Users/apple/Documents/TF/images/生成符合标准正态分布的张量.png)

生成符合标准正态分布的张量

```python
tf.random.normal(维度, mean = 均值, stddev = 标准差)
tf.random.truncated_normal(维度, mean = 均值, stddev = 标准差)
```

![符合均匀分布的张量](/Users/apple/Documents/TF/images/符合均匀分布的张量.png)

生成均匀分布的张量 minval和maxval指定最大最小值，前闭后开区间

```python
tf.random.uniform(维度, minval = 最小值, maxval = 最大值)
```

![常用函数1](/Users/apple/Documents/TF/images/常用函数1.png)

```
tf.cast(张量名, dtype = 数据类型) //强制类型转换
tf.reduce_min(张量名) //求一个张量里面的最小值
tf.reduce_max(张量名) //求一个张量里面的最大值
```

![常用函数2](/Users/apple/Documents/TF/images/常用函数2.png)


```
tf.reduce_mean(张量名, axis = 操作轴) //求某一方向上的均值
tf.reduce_sum(张量名, axis = 操作轴) //求某一方向上的和
```

axis = 0表示沿纵轴，axis = 1表示沿横轴

![常用函数3](/Users/apple/Documents/TF/images/常用函数3.png)

```
tf.Variable(初始值)
```

产生一个变量，常用该函数标记训练参数



```
张量四则运算
tf.add()
tf.divide()
tf.substract()
tf.multiply()
```

维度相同的张量才可以四则运算

```
tf.square()
tf.pow()
tf.sqrt()
```

平方 n次方 开方操作

```
tf.matmul()
```

两个矩阵相乘

```
tf.data.Dataset.from_tensor_slices(features, labels)
```

将数据和对应的标签配对

![对函数中某个变量求导](/Users/apple/Documents/TF/images/对函数中某个变量求导.png)

```
tf.GradientTape()

with tf.GradientTape() as tape:
	若干计算过程

grad = tf.GradientTape(函数, 求导对象)
```

对某个函数的参数求导

![独热码](/Users/apple/Documents/TF/images/独热码.png)

在分类问题中，常常用独热码做标签，1表示是，0表示非。



```
tf.nn.softmax(x)
```

使张量x符合概率分布

```
tf.argmax(张量名, axis = 操作轴)
```

返回张量沿指定维度最大值的索引