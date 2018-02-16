import tensorflow as tf

with tf.Session() as sess:
  hello = tf.constant('Hello TF')
  print(sess.run(hello))