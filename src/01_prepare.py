import os
from data import preparator

TRAINING_DIR = 'data/pics/4 train'
VALIDATION_DIR = 'data/pics/5 dev'
TESTING_DIR = 'data/pics/6 test'

train_file = os.path.join('data/generated/train_files.csv')
preparator.write_cards_files_csv(os.path.join(TRAINING_DIR), train_file)
print(f"> Generated {train_file}");

validation_file = os.path.join('data/generated/dev_files.csv')
preparator.write_cards_files_csv(os.path.join(VALIDATION_DIR), validation_file)
print(f"> Generated {validation_file}");

test_file = os.path.join('data/generated/test_files.csv')
preparator.write_cards_files_csv(os.path.join(TESTING_DIR), test_file)
print(f"> Generated {test_file}");