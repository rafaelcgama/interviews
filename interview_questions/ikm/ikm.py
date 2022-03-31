# class Subject:
#     count = 0
#     def __init__(self, name):
#         self.name = name
#
#     def set(self, name):
#         self._name = name
#
#     def get(self):
#         return self._name
#
#     name = property(get, set)
#
# test = Subject('name')
# test.name = 'porra'
# print(test.name)

config = '$CONFIG_ROOT/tables/${DICTIONARY}/${LANGUAGE}.json'

import re
import os

def substitute_enviroment_variables(path):
    variables = find_variables(path)
    # this generates a list of paris
    for i in range(len(variables)):
        variables[i] = [x for x in variables[i] if x != '']

    for pattern, value in variables:
        # need to backslash the $ otherwise no match
        path = re.sub('\\' + pattern, os.getenv(value, '.'), path)

    return path