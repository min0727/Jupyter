import pickle


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print(f'{self.name} / {self.age}')


omo: User = User('omo', 100)
if __name__ == '__main__':
    omo.print_age()

'''
with open('./data.pickle', 'rb') as f:
    x: [int] = pickle.load(f)

print(x)
'''


with open('./class_data.pickle', 'wb') as f:
    pickle.dump(omo, f)
