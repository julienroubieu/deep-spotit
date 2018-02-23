import tensorflow as tf
import numpy as np
import cv2
from keras.optimizers import SGD
from models.model1 import CNN_1
from helpers.loader import load_labels, load_symbols, labels_to_symbols

card_labels = load_labels('data/cards.csv')
symbol_names = load_symbols('data/symbols.csv')
for card_id, labels in card_labels.items():
  print(f"Card {card_id}: {labels_to_symbols(labels, symbol_names)}")

model = CNN_1(input_shape=(300,200,3))
print(model.summary())