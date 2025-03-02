from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('./data.pkl', 'rb') as p_f:
    n_tuple: list[Animal] = pickle.load(p_f)

    for tup in n_tuple:
        for field, value in zip(tup._fields, tup):

            print(f'{field}: {value}')

        print()
