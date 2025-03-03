import json


def find_best_service_type(file_name: str):

    type_dicts: dict[str, tuple] = {}
    with open(file_name, 'r', encoding='utf-8') as f:

        jsoned_value = json.load(f)


        for value in jsoned_value:
            if type_dicts.get(value['TypeObject'], (0, 0))[1] < value['SeatsCount']:
                type_dicts[value['TypeObject']] = (value['Name'], value['SeatsCount'])


        for k, v in sorted(type_dicts.items(), key=lambda x: x[0]):
            print(f'{k}: {v[0]}, {v[1]}')


find_best_service_type('food_services.json')
