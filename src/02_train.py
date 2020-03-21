import os
import tensorflow as tf
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator
from models.model1 import CNN_1

training_datagen = ImageDataGenerator(
  rescale=1./255,
  rotation_range=40,
  horizontal_flip=True,
  fill_mode='nearest'
)

training_generator = training_datagen.flow_from_directory(
  TRAINING_DIR,
  target_size=(200, 200),
  classes=57
)

#model = CNN_1(input_shape=(300,200,3))
#print(model.summary())