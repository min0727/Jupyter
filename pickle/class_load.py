import pickle
from class_save import User

with open('./class_data.pickle', 'rb') as f:
    omo: User = pickle.load(f)
omo.print_age()
