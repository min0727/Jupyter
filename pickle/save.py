import pickle

x: [int] = [3, 1, 7]

with open('./data.pickle', 'wb') as f:
    pickle.dump(x, f)