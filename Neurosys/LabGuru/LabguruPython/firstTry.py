import json

import pandas
import requests
import re

from labguru import Labguru

lab = Labguru(login='jpalleau@gmail.com', password='LabG0urou')


########################################################################################################################
# Get the user token
########################################################################################################################
def base():
    return f'https://eu.labguru.com'


def get_token():
    lab = Labguru(login='jpalleau@gmail.com', password='LabG0urou')
    return lab


def main():
    # lab = get_token()
    # print(f'debug1 token: {lab.session.token}')
    print(f'debug3 get_token(): {get_token().session.token}')


def token():
    return get_token().session.token


########################################################################################################################

# ##################################
# # List all the modules installed #
# ##################################
# help('modules')

# #-------------------------------------------------------------------------------------
# # List folders id and then print each folder by its id: OK
# for index, value in enumerate(lab.list_folders(project_id=None, page_num=1)):
#     print(f'value project_id: {value.project_id}')
#     print(f'value: {value}')
#     print(f'folder: {value.title}')

# #-------------------------------------------------------------------------------------

# # List Inventory items name and id: OK
# for index, value in enumerate(lab.list_inventory_items(item_type='cell_lines', page_num=1)):
#     print(f"item name: {lab.list_inventory_items(item_type='cell_lines', page_num=1)[index].name}")
#     print(f"item id: {lab.list_inventory_items(item_type='cell_lines', page_num=1)[index].id}")

# #-------------------------------------------------------------------------------------

# # Number of Inventory items: OK

# print(f"number items in inventory: {len(lab.list_inventory_items(item_type='cell_lines', page_num=1))}")

# #-------------------------------------------------------------------------------------

# # List all projects id, projects name and for each one, all folders title: OK
# for proj in lab.list_projects(page_num=1):
#     print(f'PROJECT - project id: {proj.id}, project name: {proj.name}')
#     for folder in lab.list_folders(project_id=proj.id, page_num=1):
#         print(f'Folder title: {folder.title}')

# Look for what is get_future_folders() and what is get_past_folders() ???
#     if proj.id:
#         print(f'project members: {proj.member}')
#         # # print(proj.register('New Folder 2'))
# for f in proj.get_folder(folder_id)
#         # print('current folders')
#         # for f in proj.get_current_folders():
#         #     print(f)
#         # print('future folders')
#         # for f in proj.get_future_folders():
#         #     print(f)
#         # print('pass folders')
#         # for f in proj.get_past_folders():
#         #     print(f)

# #-------------------------------------------------------------------------------------

# # List in all experiments all elements: OK

# i = 0
# for exp in lab.list_experiments(page_num=1):
#     # print(i)
#     if 'duplicate' in exp.title:
#         # print("Ok")
#         i += 1
#         original_exp_id = exp.to_dict()["duplicate_of"]
#         original_exp_title = exp.title.replace(" (duplicate)", "")
#         # print(f'debug1: {exp_title, original_exp_id, token()}')
#         original_exp = requests.get(
#             f'{base()}/api/v1/experiments/{original_exp_id}',
#             json={"token": token()}).json()
#         # print(f'debug1: original_exp: {original_exp}')
#         # print(f'\n"----------------------------------------------------------"\n')
#         # print(f'original exp: {original_exp}')
#         if str(original_exp).find('Samples & Reagents'):
#             print(original_exp_title, original_exp_id)

# print(f'debug2: exp: {exp}')
# #
# #

#     break

# for index, value in enumerate(lab.get_elements_by_type(experiment_id=exp.id, element_type=None)):
#     print(f'debug {value.id}')

# # Find Element By Name the one use in labguru but here it is not able to get data
# test = lab.find_elements('Sample & Reagents')
# print(test)

#

# for experiment_id in lab.list_experiments(page_num=1):
#     sample_element = lab.get_elements_by_type(experiment_id=220, element_type='samples')[0]
#     sample_element_data = sample_element.get_data()
#     sample_id = sample_element_data[0].get('id')
#     stock_id = sample_element_data[0].get('stocks')[0]['id']
#     print(f"debug4: {stock_id}")

# #-------------------------------------------------------------------------------------

# # List experiment 220 and try to get JP-Item03-pour essai stock
#
# experiment_id_list = []
# for experiment in lab.list_experiments(page_num=4):
#     experiment_id_list.append(experiment.id)
#     # print(experiment.milestone_id)
#
# print(f'project_id: {lab.get_experiment(220).project_id}')
# print(f'experiment_id_list: {experiment_id_list}\n')
#
# for stock in lab.list_stocks(page_num=1):
#     print(f'inventaire: {stock.id}')


# Sotck item
# for stock in lab.list_stocks(page_num=None):
#     print(f'stock_name: {stock.name}, stock_id: {stock.id}')


# #-------------------------------------------------------------------------------------

# # List all projects: OK

# print out project info
# for project in lab.list_projects(page_num=1):
#     print(f'Project id: {project.id}, Project title: {project.title}, Project owner: {project.owner}')

# #-------------------------------------------------------------------------------------

# # Download project information

# project = lab.get_project(project_id='7')
# print(f'Project id: {project.id}, Project title: {project.title}')

# #-------------------------------------------------------------------------------------

# # Find a project by name: NOK it returns an empty string ??? Must be investigated

# for project in lab.list_projects(page_num=1):
#   projects = lab.find_projects(name=project.title)
#   print(projects)

# #-------------------------------------------------------------------------------------

# # Start new project

# project_new = lab.add_project(title="My new test project - JP", description="Dev test project")

# print(project_new)

# #-------------------------------------------------------------------------------------

# # Update a project
# # for project in lab.list_projects(page_num=1):
# #     print(f'Project id: {project.id}, Project title: {project.title}, Project owner: {project.owner}')

# project_update = lab.update_project(project_id='7', title="Update my new test project - JP")

# print(project_update.id, project_update.title)


# #-------------------------------------------------------------------------------------
# List details about experiment id=220, 2023-05-16 - Julien Palleau's Experiment 001


# #-------------------------------------------------------------------------------------

# # Firt test with usual "hello world!": OK

# #log("Hello world this is a log!")
# print("Hello World this is a print!")

# #-------------------------------------------------------------------------------------
# Get all storages of a particular parent_id
# storages = requests.get('https://my.labguru.com/api/v1/storages', json={"token": token()}).json()
# storages_by_parent = []
# print(storages)

# #-------------------------------------------------------------------------------------
# data = requests.get('https://eu.labguru.com/api/v1/elements/1497', json={"token": token()}).json()
#
# for key, value in data.items():
#     if key == 'data':
#         print(value)
#
#         x = re.findall('saved_stocks_ids":\[.+?\]', value)
#         print(x)
#
#         list_right_numbers = []
#         for line in x:
#             numbers_only = line.split('[')[1].split(']')[0]
#             list_of_number_strings = numbers_only.split(',')
#             list_of_numbers = [int(number) for number in list_of_number_strings]
#             # print(f'list of numbers: {list_of_numbers}')
#             list_right_numbers.extend(list_of_numbers)
#         print(list_right_numbers)
#
#         # result1 = value.split("[")
#         # for result2 in result1:
#         #     if ']' in result2:
#         #         # print(result2)
#         #         result3 = result2.split("]")
#         #         print(result3)
#
#         # valeur = value.split(",")
#         # for v in valeur:
#         #     if "saved_stocks_ids" in v:
#         #         print(v)
#
# if __name__ == '__main__':
#     main()

# #-------------------------------------------------------------------------------------
import requests
import sys
import csv
import os

# Creating a csv file
import pandas as pd



experiment_ids = []

# ESSAI SUR PROJECT 15
project_data = requests.get('https://eu.labguru.com/api/v1/experiments?&filter={"project_id":"15"}',
                            json={"token": token()}).json()

# TESTS
# from sys import getrecursionlimit
# from sys import setrecursionlimit
# setrecursionlimit(10)
# print(f'Recursion limit: {getrecursionlimit()}')

# print(f"{project_data} \n")

# GET ALL IDs---------------------------------------------------------------


# CREATE LIST OF EXPERIMENT IDS FOR THE PROJECT----------------------------------------------------------
for exp in project_data:
    # print(exp["id"])
    experiment_ids.append(exp["id"])

print(f'experiment_ids:{experiment_ids}')

# For EACH EXPERIMENT ID, CREATE LIST OF SAMPLE IDS------------------------------------------------------

sample_list = []
list_exp_id = []
sample_exp_id_list = {}

for exp_id in experiment_ids:
    # print(f'exp_id:{exp_id}')
    list_exp_id.append(exp_id)
    exp_data = requests.get(f'https://eu.labguru.com/api/v1/experiments/{exp_id}', json={"token": token()}).json()
    # print(f'exp_data:{exp_data}')
    experiment_procedure = exp_data["experiment_procedures"]
    # print(f'experiment_procedure:{experiment_procedure}')

    for Each_experiment_procedure in experiment_procedure:
        # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
        for Each_section_type in Each_experiment_procedure:
            for Element_key in Each_experiment_procedure[Each_section_type]:
                # print(f'Element_key:{Element_key}')
                for Each_section_type in Each_experiment_procedure:
                    if Each_experiment_procedure[Each_section_type][Element_key]:
                        if Element_key == 'elements':
                            for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                                if sample["element_type"] == "samples":
                                    # print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                                    sample_list.append(sample["id"])
                                    # print(f'sample_list:{sample_list}')

# FOR EACH SAMPLE ID IN SAMPLE LIST,CREATE LIST OF STOCK IDS------------------------------------

stock_id_list = []

for sample_list_id in sample_list:
    sample_el = requests.get(f'https://eu.labguru.com/api/v1/elements/{sample_list_id}', json={"token": token()}).json()
    sample_el_data = json.loads(sample_el["data"])
    # print(f'sample_el_data: {sample_el_data}')

    for sample in sample_el_data["samples"]:
        sample_el_id = sample["id"]
        sample_el_name = sample["name"]
        stocks_ids = sample["saved_stocks_ids"]
        # print(f'DEBUG {stocks_ids}, {sample_el_name}')
        # dict_stock_id_samle_name [stocks_ids[0]] = sample_el_original_name
        stock_id_list.extend(stocks_ids)
print(f'stock_id_list:{stock_id_list}')

# FOR EACH Stock ID in stock_id_list, create liste with stock_ID, name, lot, content URL, manufacturer, catalog number
test=[]
list_stock_data = []
array_1 = []
array_2 = []
array_3 = []
array_4 = []
array_5 = []
array_6 = []
array_7 = []
array = {}
global s1, s2
for id in stock_id_list:
    stock_id_data = requests.get(f'https://eu.labguru.com/api/v1/stocks/{id}', json={"token": token()}).json()

    sample_type = stock_id_data["sample_type"]
    sample_id = stock_id_data["sample_id"]

    if "Catalog" in sample_type:
        sample_url_root = "/catalogs/"
    else:
        sample_url = stock_id_data['stockable']['url']
        sample_url = sample_url.split("/")
        if "Generic" not in sample_type:
            sample_url_root = "/" + sample_url[2] + "/"
        else:
            sample_url_root = "/biocollections/" + sample_url[2] + "/"

    # print(f'stock_id:{id}, sample_type: {sample_type},sample_url:{sample_url}, sample_url_root:{sample_url_root}, sample_id: {sample_id}')
    print(sample_id)
    sample_id_data = requests.get(f'https://eu.labguru.com/api/v1{sample_url_root}{sample_id}',
                                  json={"token": token()}).json()

    print(sample_id_data)

    built_line = f"stock_id: {stock_id_data['id']}| collection: {stock_id_data['content_type_for_display']}| sample_id: {stock_id_data['sample_id']}| name: {stock_id_data['name']}| lot: {stock_id_data['lot']}| manufacturer: {sample_id_data['manufacturer']}| catalog_number: {sample_id_data['catalog_number']}"
    print(built_line)

    print("\n")
    # print(stock_id_data['id'])
    array_1.append(str(stock_id_data['id']))
    array_2.append(stock_id_data['content_type_for_display'])
    array_3.append(stock_id_data['sample_id'])
    array_4.append(stock_id_data['name'])
    array_5.append(stock_id_data['lot'])
    array_6.append(sample_id_data['manufacturer'])
    array_7.append(sample_id_data['catalog_number'])

    # print(array_7)

pd.options.display.width = 0
pd.options.display.max_colwidth = 200
pd.set_option('display.width', 1000)
pd.set_option('display.max_column', None)


df = pd.DataFrame({'stock_id': array_1, 'collection': array_2, 'sample_id': array_3, 'name': array_4, 'lot': array_5, 'manufacturer': array_6, 'catalog_number': array_7})
df_reset = df.set_index('stock_id')

# Ecriture du fichier csv
df = pd.DataFrame(df_reset)
file_name = "material_list.csv"
df.to_csv(file_name, index=True, sep=';', encoding='utf-8')

df.info()









#     list_stock_data.append(built_line)
# for line in list_stock_data:
#     print(line)

# # Create a CSV file from list_stock_data
# df = pd.read_csv('material_list.csv')
# # df.to_csv('material_list.csv', index=False)
# # pd.options.display.width = 0
# # pd.options.display.max_colwidth = 200
# # pd.set_option('display.width', 1000)
# pd.set_option('display.max_column', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_seq_items', None)
# pd.set_option('display.max_colwidth', 500)
# pd.set_option('expand_frame_repr', True)
#
# # pd.set_option('max_colwidth', 800) # working
# # pd.options.display.max_colwidth = 200 # working
#
# print(df.head(10))
# print(df.tail())
#
# # data = list_stock_data
# # df = pd.DataFrame(data)
# # file_name = "material_list.csv"
# # df.to_csv(file_name, index=False)
#
# # tr = sys.argv[1]
# # store_variable("file", {'tmp_path': f'{tr}/rendered_files/{file_name}'})
# print(sys.argv)
#
# # Read CSV file
# # test = pd.read_csv("material_list.csv")
# # print(test)