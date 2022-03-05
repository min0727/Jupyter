import pickle

with open('./data.pickle', 'rb') as f:
    x: [int] = pickle.load(f)

print(x)