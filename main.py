import tensorflow as tf
import numpy as np
import cv2
from keras.optimizers import SGD
from models.model1 import CNN_1

model = CNN_1(input_shape=(300,200,3))
print(model.summary())