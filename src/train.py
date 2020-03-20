import tensorflow as tf
from models.model1 import CNN_1
from helpers.loader import load_cards, load_symbols, card_content_to_symbol_names

cards = load_symbols('data/cards.csv')
symbol_names = load_symbols('data/symbols.csv')
for i in range(len(cards)):
  print(f'Card {i+1}: ', card_content_to_symbol_names(cards[i], symbol_names))

#model = CNN_1(input_shape=(300,200,3))
#print(model.summary())