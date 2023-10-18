# list_essai = [{'experiment_procedure1': {'id': 1508, 'name': 'Description', 'section_type': 'description',
#                                          'collapsed': False, 'time_range': None, 'elements':
#                                              [{'id': 2442, 'uuid': '9cd64bc8-59de-4deb-9aa9-493f366a938e',
#                                                'element_type': 'text', 'rows': None, 'cols': None, 'name': None}],
#                                          'start_date': None, 'end_date': None,
#                                          'uuid': 'c2d0de73-8981-4bf6-9ded-07821d709654'}}, {
#                   'experiment_procedure2': {'id': 1509, 'name': 'Procedure', 'section_type': 'procedure',
#                                             'collapsed': False, 'time_range': None, 'elements':
#                                                 [{'id': 2443, 'uuid': '62aae41e-bd9f-4dd5-954b-14bf59183319',
#                                                   'element_type': 'form', 'rows': None, 'cols': None, 'name': 'Form'}],
#                                             'start_date': None, 'end_date': None,
#                                             'uuid': '32f1b8d6-b21d-463f-888f-3ee2ee694fb2'}}, {
#                   'experiment_procedure3': {'id': 1510, 'name': 'Medium', 'section_type': 'custom', 'collapsed': False,
#                                             'time_range': None, 'elements':
#                                                 [{'id': 2444, 'uuid': '5666e14e-15bf-49e9-895d-6c214e9eca19',
#                                                   'element_type': 'samples', 'rows': None, 'cols': None,
#                                                   'name': 'Samples & Reagents'}],
#                                             'start_date': None, 'end_date': None,
#                                             'uuid': '9e718e56-c420-43eb-9546-2efe6128611a'}}, {
#                   'experiment_procedure4': {'id': 1511, 'name': 'Results', 'section_type': 'results',
#                                             'collapsed': False,
#                                             'time_range': None, 'elements':
#                                                 [{'id': 2445, 'uuid': '1eadcd2f-7d17-422c-8103-dc2f18922753',
#                                                   'element_type': 'text', 'rows': None, 'cols': None, 'name': None}],
#                                             'start_date': None, 'end_date': None,
#                                             'uuid': 'd101a38b-2940-4d82-93f2-15cd7e175c30'}}]
# ##########################
# # Tom algo pour neurosys #
# ##########################
# result = []
#
#
# def get_id(value, keyword: str):
#     id_list = []
#     if isinstance(value, dict):
#         # get id if exist from dict
#         if id := value.get(keyword):
#             id_list += [id]
#
#         # get id's from nested list or dicts
#         for val in value.values():
#             if isinstance(val, list) or isinstance(val, dict):
#                 id_list += get_id(val, keyword)
#
#     if isinstance(value, list):
#         for val in value:
#             if isinstance(val, list) or isinstance(val, dict):
#                 id_list += get_id(val, keyword)
#
#     return id_list
#
#
# print(get_id(list_essai, "id"))
# print("done")


###############################################
# Démystification de la récursivité en Python #
###############################################
# https://code.tutsplus.com/fr/demystifying-python-recursion--cms-30418t


# Introduction aux fonctions recursive en Python
# def factoriel(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factoriel(n - 1)
#
#
# print(factoriel(5))


# Cas d'etude 1: Fibonaci

# def Fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)
#
#
# print(Fibonacci(9))

import storeapi.test
print(__name__)