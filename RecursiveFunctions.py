#Есть список, внутри которого есть как значения, так и другие списки со значениями.
#Необходимо вывести список со всеми значения, в том числе со значениями вложенных списков
def linear(nested_lists: list [any]) -> list[any]:
    b = []
    for i in nested_lists:
        if not isinstance(i, list):
            b.append(i)
        else:
            b.extend(linear(i))
    return (b)

#For example:
# my_list = [3, [4], [5, [6, [7, 8]]]]
# print(linear(my_list))
#Answer:
    #[3, 4, 5, 6, 7, 8]


#Есть словарь, внутри которого как пары ключ-значение, так и другие словари с произвольной вложенностью.
# Необходимо вывести значение по указанному ключу (key). Гарантируется, что такой ключ лишь один.
def get_value(nested_dicts: dict[str|int, any],key: str|int) -> any:
    if key in nested_dicts:
        return nested_dicts[key]
    for i in nested_dicts.values():
            if isinstance(i,dict):
                value = get_value(i, key)
                if value:
                    return value
# For example:
# data = {'firstName': 'Тимур', 'address': {'streetAddress': 'Часовая 25',
#                                           'city': {'type': 'город', 'cityName': 'Москва'}, 'Code': '125315'}}
# print(get_value(data, 'cityName'))
# Answer:
#     Москва

#Есть словарь, внутри которого пары ключ-значени и другие словари с произвольной вложенностью.
# Необходимо вернуть список со всеми значеними по указанному ключу (key).
def get_values(nested_dicts: dict[str|int, any], key: str|int) -> list[any]:
    result = []
    if key in nested_dicts:
        result.append(nested_dicts[key])
    for i in nested_dicts.values():
            if isinstance(i,dict):
                result.extend(get_values(i, key))
    return result

#For example:
# data = {'firstName': 'Тимур', 'birthDate': {'day': 10, 'month': 'October'},
#         'address': {'streetAddress': 'Часовая 25, кв. 127',
#                     'city': {'cityName': 'Москва', 'дополнительно':{'cityName':'МОСКВА'}}}}
# print(get_values(data, 'cityName'))
#Answer:
    #['Москва', 'МОСКВА']

#Есть словарь, внутри которого пары ключ-значени и другие словари с произвольной вложенностью.
# Необходимо вернуть ключ, значение которого = value. Гарантируется, что он один.
def get_key(nested_dicts: dict[str|int, any],value: any) -> str|int:
    for i,j in nested_dicts.items():
        if value == j:
            return i
        if isinstance(j,dict):
             return get_key(j,value)

#For example:
# data = {'address': {'Address': 'Часовая 25', 'city': {'cityName': 'Москва'}, 'Code': '125315'}}
# print(get_key(data, 'Москва'))
#Answer:
    #cityName

#Есть словарь, внутри которого пары ключ-значени и другие словари с произвольной вложенностью.
# Необходимо вернуть список со всеми ключами, значение которых = value.
def get_keys(nested_dicts: dict[str|int, any],value: any) -> list[str|int]:
    result = []
    for i,j in nested_dicts.items():
        if value == j:
            result.append(i)
        if isinstance(j,dict):
            result.extend(get_keys(j,value))
    return result

#ForExample:
    # data = {'firstName': 'Тимур', 'birthDate': {'day': 10, 'month': 'October',},
    #         'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Тимур'}}}
    # print (get_keys(data,'Тимур'))
#Answer:
    #['firstName', 'region']


#Есть список, внутри которого словари. В качестве значений словарей могут быть другие словари и так далее.
#Необходимо вывести значение по указанному ключу. Гарантируется, что такой ключ лишь один во всё списке.
def get_value_from_list(nested_lists: list[dict[str|int, any]], key: str|int) -> any:
    for i in nested_lists:
        a = get_value(i,key)
        if a:
            return a

#ForExample:
# data = [{1:{2:{3:'три', 4:'четыре'}}},{'пять':{6:'шесть'}},{7:{8:{9:'девять'}}}]
# print (get_value_from_list(data, 9))
#Answer:
    #восемь


#Есть список, внутри которого словари. В качестве значений словарей могут быть другие словари и так далее.
#Необходимо вывести список со всеми значениями по указанному ключу.
def get_values_from_list(nested_lists: list[dict[str|int, any]], key: str|int) -> list[any]:
    result = []
    for i in nested_lists:
        result.extend(get_values(i,key))
    return result

# ForExample:
# data = [{1:{2:{3:'три', 4:'четыре'}}},{'пять':{'шесть':6}},{7:{8:{'шесть':'шесть'}}}]
# print (get_values_from_list(data, 'шесть'))
# Answer:
#     [6, 'шесть']

#Есть список, внутри которого словари. В качестве значений словарей могут быть другие словари и так далее.
#Необходимо вывести ключ по указанному значения. Гарантируется, что такой ключ лишь один во всё списке.
def get_key_from_list(nested_lists: list[dict[str|int, any]], value: any) -> str|int:
    for i in nested_lists:
        a = get_key(i,value)
        if a:
            return a

#ForExample:
# data = [{1:{2:{3:'три', 4:'четыре'}}},{'пять':{6:'шесть'}},{7:{8:{9:'девять'}}}]
# print (get_key_from_list(data, 'шесть'))
#Answer:
    #6

#Есть список, внутри которого словари. В качестве значений словарей могут быть другие словари и так далее.
#Необходимо вывести список со всеми ключами по указанному значению.
def get_keys_from_list(nested_lists: list[dict[str|int, any]], value: any) -> list[str|int]:
    result = []
    for i in nested_lists:
        result.extend(get_keys(i,value))
    return result

#ForExample:
# data = [{1:{2:{3:'три', 4:'четыре'}}},{'пять':{6:'шесть'}},{7:{8:{'шесть':'шесть'}}}]
# print (get_keys_from_list(data, 'шесть'))
#Answer:
    #[6, 'шесть']


