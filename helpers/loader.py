import csv
import numpy as np

def load_labels(cards_file_path):
  """
    Reads the labels of all cards from a CSV file.
    Each line in the file should start with the card name, followed by 57 binary [0/1] values to denote presence of each symbol in the card.

    :param cards_file_path: csv file path
    :returns: dictionnary mapping each card name to a numpy array of ints
  """
  labels_dict = {}
  with open(cards_file_path) as cardsfile:
    csvreader = csv.reader(cardsfile, delimiter=',')
    for row in csvreader:
      card_id, *labels = row
      labels_dict[card_id] = np.array(labels, np.int32)
  return labels_dict


def load_symbols(symbols_file_path):
  """
    Reads the name of the symbols from a CSV file.
    Each line should contain the symbol name in the second column.
    The symbols will be read and returned in the same order, ignoring the first column.

    :param symbols_file_path: csv file path
    :returns: array of 57 symbol names (indexed by their id-1)
  """
  symbols = []
  with open(symbols_file_path) as symbolsfile:
    csvreader = csv.reader(symbolsfile, delimiter=',')
    for row in csvreader:
      symbols.append(row[1])
  return symbols


def labels_to_symbols(labels, symbols_names):
  """
    Converts a labels hot array into a list of the symbol names it contains.

    :param labels: [0/1] array
    :param symbols_names: array of symbol names
    :returns: list of strings
  """
  def non_empty(str): return str != ''
  names = [symbols_names[idx] if hot == 1 else '' for idx,hot in enumerate(labels)]
  return list(filter(non_empty, names))