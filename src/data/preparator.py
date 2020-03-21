import os

def write_cards_files_csv(cards_file_directory, files_csv_path):
  """
    Generates a CSV file at `files_csv_path`, containing the names of all card files in `cards_file_directory`,
    along with the index of the represented card (01 to 55).
    This file is useful when classifying the card itself, instead of the symbols on it.

    :params cards_file_directory: directory containing card images, named 'cardXX-YY.JPG'
    :params files_csv_path: path of the CSV file to write
  """
  files_names = os.listdir(cards_file_directory)
  files_names.sort()

  file_dir = os.path.dirname(files_csv_path)
  if not os.path.exists(file_dir): os.makedirs(file_dir)

  files_csv = open(files_csv_path, 'w')
  for file_name in files_names:
    if file_name[:4] != 'card': continue
    card_number = file_name[4:6]
    files_csv.write(file_name + "," + card_number + "\n")

  files_csv.close()
