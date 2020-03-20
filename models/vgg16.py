import tensorflow as tf
import numpy as np
import numpy as np

def VGG_16(input_shape=(300,200,3), weights_path=None):

  model = tf.keras.models.Sequential(
    tf.keras.layers.ZeroPadding2D((1,1), input_shape=input_shape),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.ZeroPadding2D((1,1)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2), strides=(2,2)),

    tf.keras.layers.ZeroPadding2D((1,1)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.ZeroPadding2D((1,1)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2), strides=(2,2)),

    tf.keras.layers.ZeroPadding2D((1,1)),
    tf.keras.layers.Conv2D(256, (3, 3), activation='relu'),
    tf.keras.layers.ZeroPadding2D((1,1)),
    tf.keras.layers.Conv2D(256, (3, 3), activation='relu'),
    tf.keras.layers.ZeroPadding2D((1,1)),
    tf.keras.layers.Conv2D(256, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2), strides=(2,2)),

    tf.keras.layers.ZeroPadding2D((1,1)),
    tf.keras.layers.Conv2D(512, (3, 3), activation='relu'),
    tf.keras.layers.ZeroPadding2D((1,1)),
    tf.keras.layers.Conv2D(512, (3, 3), activation='relu'),
    tf.keras.layers.ZeroPadding2D((1,1)),
    tf.keras.layers.Conv2D(512, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2), strides=(2,2)),

    tf.keras.layers.ZeroPadding2D((1,1)),
    tf.keras.layers.Conv2D(512, (3, 3), activation='relu'),
    tf.keras.layers.ZeroPadding2D((1,1)),
    tf.keras.layers.Conv2D(512, (3, 3), activation='relu'),
    tf.keras.layers.ZeroPadding2D((1,1)),
    tf.keras.layers.Conv2D(512, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2), strides=(2,2)),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(4096, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(4096, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1000, activation='softmax')
  )

  if weights_path:
      model.load_weights(weights_path)

  return model