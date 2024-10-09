import requests
from pprint import pprint
import inspect

some_string = 'i am a string'
some_number = 42
some_list = [some_string, some_number]

def some_function(param, param_2='n/a'):
    print('my params is', param, param_2)

class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_metod(self, value):
        self.attribute_1 = value
        print(self.attribute_1)

some_object = SomeClass()



#print(dir(some_object))

# for attr_name in dir(requests):
#     attr = getattr(requests, attr_name)
#     print(attr_name, type(attr))

#print(getattr(some_object, 'attribute_2', 'Этого не может быть!'))
#print(help(getattr))
# attr_name = 'attribute_2'
# print(hasattr(some_object, attr_name))
#func = some_function

# print(func.__name__)
#
# print(type(some_number) is int)
#
# print(type(requests.post))

#pprint(dir(requests))
