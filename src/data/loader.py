import csv
import numpy as np

def load_cards(cards_file_path):
  """
    Reads the content of all cards from a CSV file.
    There are 55 cards in the game.
    The file should contain one line per card, containing 57 int [0/1] values to denote presence of each symbol in the card.

    :param cards_file_path: csv file path
    :returns: numpy 2D array of '0'|'1' strings, representing the content of each card. Shape: (55, 57).
  """
  return np.genfromtxt(cards_file_path, delimiter=',', dtype=np.str)


def load_symbols(symbols_file_path):
  """
    Reads the name of the symbols from a CSV file.
    Each line should contain the symbol name.
    The line index should be the same as the column index in the cards file.

    :param symbols_file_path: csv file path
    :returns: numpy array of 57 symbol names. Shape: (57,)
  """
  return np.genfromtxt(symbols_file_path, delimiter=',', dtype=np.str)


def card_content_to_symbol_names(card_content, symbol_names):
  """
    Converts a card's content hot array into a list of the symbol names it contains.

    :param card_content: [0/1] numpy array
    :param symbols_names: numpy array of symbol names using same indexes as card_content
    :returns: list of strings
  """
  return symbol_names[card_content == '1']