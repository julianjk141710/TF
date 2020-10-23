import tensorflow as tf
tensorflow_version = tf.__version__

a = tf.constant([1.0, 2.0], name = "a")
b = tf.constant([1.0, 2.0], name = "b")

result = tf.add(a, b, name = "add")
print(result)
