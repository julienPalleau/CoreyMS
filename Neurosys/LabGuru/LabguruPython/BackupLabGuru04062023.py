#-----------------------------------------------------------------------------------------------------------------------
#-------------- 27/09/2023 ---------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
# 04-Dev-03.1-List of material used in a given project-for dev trigger
#-----------------------------------------------------------------------------------------------------------------------
import requests
import sys
import csv
import os

# Creating a csv file
import pandas as pd

experiment_ids = []

experiment = variable("trigger_experiment")
experiment_id = experiment["id"]

experiment = requests.get(f'{base()}/api/v1/experiments/{experiment_id}', json={"token": token()}).json()

##################################################################
# TRIGGER on section name = Material list #
##################################################################

# #-------- ITERATE OVER SECTION NAME AND TEST SECTION NAME VALUE FOR "Material list" ------------------------
experiment_procedure = experiment["experiment_procedures"]

for Each_experiment_procedure in experiment_procedure:
    # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
    # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
    print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

    if Each_experiment_procedure['experiment_procedure']['name'] == "Material list":
        print("RUN THE SCRIPT")

project_id = experiment["project_id"]
print(f'project_id: {isinstance(project_id, int)}')

# ESSAI SUR PROJECT 15---------------??????????????????????????????????????NE MARCHE PAS-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# project_data = requests.get('https://eu.labguru.com/api/v1/experiments?&filter={"project_id": "15"}',
#                          json={"token": token()}).json()

project_data = requests.get('https://eu.labguru.com/api/v1/experiments?&filter={"project_id"= project_id}',
                            json={"token": token()}).json()

print(f'project_data: {project_data}')

# CREATE LIST OF EXPERIMENT IDS FOR THE PROJECT - MARCHE AVEC PROJECT 15 ECRIT DANS REQUEST.GET ----------------------------------------------------------
for exp in project_data:
    print(exp["id"])
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
        print(f'DEBUG {stocks_ids}, {sample_el_name}')
        # dict_stock_id_samle_name [stocks_ids[0]] = sample_el_original_name
        stock_id_list.extend(stocks_ids)
print(f'stock_id_list:{stock_id_list}')

# FOR EACH Stock ID in stock_id_list, create liste with stock_ID, name, lot, content URL, manufacturer, catalog number

list_stock_data = []

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

    print(
        f'stock_id:{id}, sample_type: {sample_type},sample_url:{sample_url}, sample_url_root:{sample_url_root}, sample_id: {sample_id}')
    sample_id_data = requests.get(f'https://eu.labguru.com/api/v1{sample_url_root}{sample_id}',
                                  json={"token": token()}).json()
    # print(sample_id_data)

    built_line = f"stock_id: {stock_id_data['id']}, collection: {stock_id_data['content_type_for_display']}, sample_id: {stock_id_data['sample_id']}, name: {stock_id_data['name']}, lot: {stock_id_data['lot']}, manufacturer: {sample_id_data['manufacturer']}, catalog_number: {sample_id_data['catalog_number']}"

    list_stock_data.append(built_line)
for line in list_stock_data:
    print(line)

# Create a CSV file from list_stock_data
data = list_stock_data
df = pd.DataFrame(data)
file_name = "material_list.csv"
df.to_csv(file_name, index=False)

tr = sys.argv[1]
store_variable("file", {'tmp_path': f'{tr}/rendered_files/{file_name}'})

# CREATE a CSV file from stock_id_data and sample_id_data------------------------
# with open('material_list.csv', mode='w') as csv_file:
#  fieldnames=['stock_id','collection','sample_id','name','lot','manufacturer','catalog_number']
#  writer=csv.DictWriter(csv_file,fieldnames=fieldnames)

#  writer.writeheader()
#  writer.writerow({'stock_id': stock_id_data['id'], 'collection': stock_id_data['content_type_for_display'], 'sample_id': stock_id_data['sample_id'], 'name': stock_id_data['name'], 'lot': stock_id_data['lot'], 'manufacturer': sample_id_data['manufacturer'], 'catalog_number': sample_id_data['catalog_number']})


# print(f'pwd={os.getcwd()}')
# print(os.environ.get('HOME'))
# result = os.listdir()
# print(result)

# --------------------------------------------------------------------------------------
# Posting the created csv to Labguru, EXPERIEMENT 378  ----EN COURS DE DEV


experiment_uuid = 'd3624f1d-2ecb-4050-a16d-dfdf79c7516a'
section_id = "1577"
file_name = "material_list.csv"

with open(file_name, 'rb') as csv_file:
    attachment = csv_file.read()

attachment_response = requests.post(f'https://eu.labguru.com/api/v1/attachments',
                                    data={
                                        'item[title]': file_name,
                                        'item[attachable_type]': 'Knowledgebase::AbstractDocument',
                                        'item[attach_to_uuid]': experiment_uuid,
                                        'token': token()
                                    },
                                    files={'item[attachment]': (file_name, attachment)},
                                    )

attachment_id = attachment_response.json()['id']
print(f'attachment_id:{attachment_id}')

# --------------------------------------
# Adding a new attachment element to the target experiment
section_id = "1575"
response = requests.post(f'{base()}/api/v1/elements', json={
    "item": {
        "container_id": section_id,
        "container_type": "ExperimentProcedure",
        "element_type": "attachments",
        "data": None
    },
    "token": token()
})

# --------------- Debug ---------------
# response = requests.get('https://eu.labguru.com/api/v1/elements',
#                           json={"token": token()}).json()
# print(response)
# --------------------------------------

print('Add attachment element', response.status_code)
element_id = response.json()['id']
print(f'element_id:{element_id}')

# Associate the created attachment with the element:
response = requests.put(
    f'{base()}/api/v1/attachments/{attachment_id}/?token={token()}',
    json={'item': {'element_id': element_id}},
)




#-----------------------------------------------------------------------------------------------------------------------
#-------------- 23/08/2023 ---------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
# Test-Julien1
#-----------------------------------------------------------------------------------------------------------------------
import requests
import sys


# Get the path all the path to each stock
stock_data = requests.get('https://eu.labguru.com/api/v1/stocks', json={"token": token()}).json()
list_content_path = []
list_content_path_nums = []
list_path_temp=[]
list_path=[]
for line in stock_data:
  #print(line)
  if isinstance(line, dict):
    for key, value in line.items():
      # print(f'key --> {key}, value --> {value}')
      if key == 'api_url':
        list_content_path.append(value)
        list_content_path_nums.append(int(value.split("/")[-1]))
  # if isinstance(line, list):

indices = sorted(set(list_content_path_nums))

for line in sorted(set(list_content_path)):
  result = line.split("/")
  list_path_temp.append(result[0:-1])

# i = 0
# for line in list_path_temp:
#   url = f"/{line[1]}/{line[2]}/stocks/{i}"
#   list_path.append((f"/{line[1]}/{line[2]}/stocks/{i}"))
#   i+=1

list_stocks = requests.get('https://eu.labguru.com/api/v1/stocks', json={"token": token()}).json()

# print(list_stocks)

list_stocks_volume = []
for line in list_stocks:
  if isinstance(line, dict):
    if line['volume_to_display'] and not (line['volume_to_display'].isspace()):
      built_line = f"name: {line['name']:<80} volume: {line['volume_to_display']}"
      list_stocks_volume.append(built_line)
    else:
      built_line = f"name: {line['name']:<80} volume: null"
      list_stocks_volume.append(built_line)

for line in set(list_stocks_volume):
  print(line)


#-----------------------------------------------------------------------------------------------------------------------
#-------------- 23/08/2023 ---------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
# Test-Lucie
#-----------------------------------------------------------------------------------------------------------------------
import requests
import sys

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

def get_id(value, keyword: str):
    id_list = []
    if isinstance(value, dict):
        # get id if exist from dict
        if id := value.get(keyword):
            id_list += [id]

        # get id's from nested list or dicts
        for val in value.values():
            if isinstance(val, list) or isinstance(val, dict):
                id_list += get_id(val, keyword)

    if isinstance(value, list):
        for val in value:
            if isinstance(val, list) or isinstance(val, dict):
                id_list += get_id(val, keyword)

    return id_list


print(get_id(project_data, "id"))
print("done")

# CREATE LIST OF EXPERIMENT IDS FOR THE PROJECT----------------------------------------------------------
for exp in project_data:
    # print(exp["id"])
    experiment_ids.append(exp["id"])

print(f'experiment_ids:{experiment_ids}')

# For EACH EXPERIMENT ID, CREATE LIST OF SAMPLE IDS------------------------------------------------------

sample_list = []

for exp_id in experiment_ids:
    print(f'exp_id:{exp_id}')
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
                        # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                        if Element_key == 'elements':
                            # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                            # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                            # print(f"Element_key: {Element_key}")

                            for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                                if sample["element_type"] == "samples":
                                    # print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                                    sample_list.append(sample["id"])
                                    print(f'sample_list:{sample_list}')

print(f'sample_list:{sample_list}')

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
        print(f'DEBUG {stocks_ids}, {sample_el_name}')
        # dict_stock_id_samle_name [stocks_ids[0]] = sample_el_original_name
        stock_id_list.extend(stocks_ids)
        print(f'stock_id_list:{stock_id_list}')

# FOR EACH Stock ID in stock_id_list, create liste with stock_ID, name, lot, content URL, manufacturer, catalog number



#-----------------------------------------------------------------------------------------------------------------------
#-------------- 06/06/2023 ---------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
# 01-Dev-2.1-ExperimentDuplication-Without timer #
#-----------------------------------------------------------------------------------------------------------------------
import requests

duplicated_exp = variable("trigger_experiment")
original_exp_id = duplicated_exp["duplicate_of"]

original_exp = requests.get(f'{base()}/api/v1/experiments/{original_exp_id}', json={"token": token()}).json()
duplicated_exp_id = duplicated_exp["id"]
duplicated_exp = requests.get(f'{base()}/api/v1/experiments/{duplicated_exp_id}', json={"token": token()}).json()

store_variable('duplicated_exp', duplicated_exp)
store_variable('original_exp', original_exp)

print(
    f'DEBUG ------------------duplicated_exp: {duplicated_exp["id"]} \n -------------original_exp_id: {original_exp_id}')
# print(f'DEBUG----------------duplicated_exp: {duplicated_exp}\n DEBUG------------- original_exp: {original_exp}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR ORIGINAL EXP-----------------\n')
experiment_procedure = original_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_original:{experiment_procedure}')

sample_list_original = []
for Each_experiment_procedure in experiment_procedure:
    # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
    for Each_section_type in Each_experiment_procedure:
        for Element_key in Each_experiment_procedure[Each_section_type]:
            # print(f'Element_key:{Element_key}')
            for Each_section_type in Each_experiment_procedure:
                if Each_experiment_procedure[Each_section_type][Element_key]:
                    # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                    if Element_key == 'elements':
                        # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                        # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                        # print(f"Element_key: {Element_key}")

                        for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                            if sample["element_type"] == "samples":
                                # print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                                sample_list_original.append(sample["id"])

print(f'sample_list_original: {sample_list_original}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR DUPLICATED EXP-----------------\n')
experiment_procedure = duplicated_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_duplicated:{experiment_procedure}')

sample_list_duplicated = []
for Each_experiment_procedure in experiment_procedure:
    # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
    for Each_section_type in Each_experiment_procedure:
        for Element_key in Each_experiment_procedure[Each_section_type]:
            # print(f'Element_key:{Element_key}')
            for Each_section_type in Each_experiment_procedure:
                if Each_experiment_procedure[Each_section_type][Element_key]:
                    # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                    if Element_key == 'elements':
                        # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                        # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                        # print(f"Element_key: {Element_key}")

                        for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                            if sample["element_type"] == "samples":
                                print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                                sample_list_duplicated.append(sample["id"])

print(f'sample_list_duplicated: {sample_list_duplicated}')

print(f'\n---------ITERATE THE POSITION IN THE SAMPLE LISTS, ASSIGN SAMPLE_ID AND SAMPLE_EL_DUPLICATED-------------\n')

for position in range(0, len(sample_list_original)):
    print(f'position: {position}')

    sample_el_original_id = sample_list_original[position]
    sample_el_duplicated_id = sample_list_duplicated[position]
    print(f'sample_el_original_id: {sample_el_original_id} and sample_el_duplicated_id: {sample_el_duplicated_id}')

    sample_el_original = requests.get(f'{base()}/api/v1/elements/{sample_el_original_id}',
                                      json={"token": token()}).json()

    # Les donnees retournees par requests sont au format string, ci-dessous nous les transformons pour etre au format json
    # puis on affiche les donnees.
    sample_el_data = json.loads(sample_el_original["data"])
    print(f'\nsample_el_original_id: {sample_el_original_id}\n')
    # print(f'sample_el_original:{sample_el_original}')

    stock_id_list = []
    for sample in sample_el_data["samples"]:
        sample_el_original_id = sample["id"]
        stocks_ids = sample["saved_stocks_ids"]
        stock_id_list.extend(stocks_ids)
        print(f'stock_id_list: {stock_id_list}\n')

    # Reset sample element data, necessary for updating the sample element
    print(f'sample_el_duplicated_id:{sample_el_duplicated_id}')
    response = requests.put(f'{base()}/api/v1/elements/{sample_el_duplicated_id}',
                            json={'token': token(), 'element': {'data': None}})
    print(f'Reset sample element data, return code:', response.status_code)

    # Add stocks to the duplicated experiment

    for stock_id in stock_id_list:
        print(f'stock_id: {stock_id}, Debug base: {base()} sample_el_duplicated_id: {sample_el_duplicated_id}')

        response = requests.get(
            f'{base()}/api/v1/sample_stocks/add_stock_by_barcode?token={token()}&element_id={sample_el_duplicated_id}&barcode={stock_id}',
            json={'token': token()})

        print(f'add stock {stock_id} to sample {sample_el_duplicated_id} return code:', response.status_code)


#-----------------------------------------------------------------------------------------------------------------------
# 01-Prod-1.0-ExperimentDuplication-With timer
#-----------------------------------------------------------------------------------------------------------------------
'''
Experiment
Create

Simple conditions for strings
Action              A                   Condition               B
        if variable                 
        {{trigger_experiment.title}}    contains                duplicate

When stooped archive?   When Stopped Archive
                        true
                        
For example: {{attachment_1.extension}} equals [xlsx]
{{experiment_1.name}} contains proliferation
{{stock.type}} equals bottle

Scripter
Scripter Version
current
Description
explanation
lang            Code Template
Python          none
'''
import requests
import time

duplicated_exp = variable("trigger_experiment")
original_exp_id = duplicated_exp["duplicate_of"]

time.sleep(5)

original_exp = requests.get(f'{base()}/api/v1/experiments/{original_exp_id}', json={"token": token()}).json()
duplicated_exp_id = duplicated_exp["id"]
duplicated_exp = requests.get(f'{base()}/api/v1/experiments/{duplicated_exp_id}', json={"token": token()}).json()

store_variable('duplicated_exp', duplicated_exp)
store_variable('original_exp', original_exp)

print(
    f'DEBUG ------------------duplicated_exp: {duplicated_exp["id"]} \n -------------original_exp_id: {original_exp_id}')
# print(f'DEBUG----------------duplicated_exp: {duplicated_exp}\n DEBUG------------- original_exp: {original_exp}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR ORIGINAL EXP-----------------\n')
experiment_procedure = original_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_original:{experiment_procedure}')

sample_list_original = []
for Each_experiment_procedure in experiment_procedure:
    # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
    for Each_section_type in Each_experiment_procedure:
        for Element_key in Each_experiment_procedure[Each_section_type]:
            # print(f'Element_key:{Element_key}')
            for Each_section_type in Each_experiment_procedure:
                if Each_experiment_procedure[Each_section_type][Element_key]:
                    # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                    if Element_key == 'elements':
                        # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                        # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                        # print(f"Element_key: {Element_key}")

                        for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                            if sample["element_type"] == "samples":
                                # print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                                sample_list_original.append(sample["id"])

print(f'sample_list_original: {sample_list_original}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR DUPLICATED EXP-----------------\n')
experiment_procedure = duplicated_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_duplicated:{experiment_procedure}')

sample_list_duplicated = []
for Each_experiment_procedure in experiment_procedure:
    # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
    for Each_section_type in Each_experiment_procedure:
        for Element_key in Each_experiment_procedure[Each_section_type]:
            # print(f'Element_key:{Element_key}')
            for Each_section_type in Each_experiment_procedure:
                if Each_experiment_procedure[Each_section_type][Element_key]:
                    # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                    if Element_key == 'elements':
                        # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                        # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                        # print(f"Element_key: {Element_key}")

                        for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                            if sample["element_type"] == "samples":
                                print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                                sample_list_duplicated.append(sample["id"])

print(f'sample_list_duplicated: {sample_list_duplicated}')

print(f'\n---------ITERATE THE POSITION IN THE SAMPLE LISTS, ASSIGN SAMPLE_ID AND SAMPLE_EL_DUPLICATED-------------\n')

for position in range(0, len(sample_list_original)):
    print(f'position: {position}')

    sample_el_original_id = sample_list_original[position]
    sample_el_duplicated_id = sample_list_duplicated[position]
    print(f'sample_el_original_id: {sample_el_original_id} and sample_el_duplicated_id: {sample_el_duplicated_id}')

    sample_el_original = requests.get(f'{base()}/api/v1/elements/{sample_el_original_id}',
                                      json={"token": token()}).json()

    # Les donnees retournees par requests sont au format string, ci-dessous nous les transformons pour etre au format json
    # puis on affiche les donnees.
    sample_el_data = json.loads(sample_el_original["data"])
    print(f'\nsample_el_original_id: {sample_el_original_id}\n')
    # print(f'sample_el_original:{sample_el_original}')

    stock_id_list = []
    for sample in sample_el_data["samples"]:
        sample_el_original_id = sample["id"]
        stocks_ids = sample["saved_stocks_ids"]
        stock_id_list.extend(stocks_ids)
        print(f'stock_id_list: {stock_id_list}\n')

    # Reset sample element data, necessary for updating the sample element
    print(f'sample_el_duplicated_id:{sample_el_duplicated_id}')
    response = requests.put(f'{base()}/api/v1/elements/{sample_el_duplicated_id}',
                            json={'token': token(), 'element': {'data': None}})
    print(f'Reset sample element data, return code:', response.status_code)

    # Add stocks to the duplicated experiment

    for stock_id in stock_id_list:
        print(f'stock_id: {stock_id}, Debug base: {base()} sample_el_duplicated_id: {sample_el_duplicated_id}')

        response = requests.get(
            f'{base()}/api/v1/sample_stocks/add_stock_by_barcode?token={token()}&element_id={sample_el_duplicated_id}&barcode={stock_id}',
            json={'token': token()})

        print(f'add stock {stock_id} to sample {sample_el_duplicated_id} return code:', response.status_code)



#-----------------------------------------------------------------------------------------------------------------------
# 02-Dev-3.0- Lots and expiration date on SP exp-Update with -SP
#-----------------------------------------------------------------------------------------------------------------------
import requests
import datetime
import calendar
from dateutil.relativedelta import relativedelta

experiment = variable("trigger_experiment")
experiment_id = experiment["id"]
experiment = requests.get(f'{base()}/api/v1/experiments/{experiment_id}', json={"token": token()}).json()

########################################
# Get the lot and display it in labguru#
########################################


# #-------- GET SAMPLE NAME OF SECTION AND SAMPLE ID------------------------
experiment_procedure = experiment["experiment_procedures"]
sample_list = []
section_name_list = []
for Each_experiment_procedure in experiment_procedure:
    # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
    # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
    # print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

    for Each_section_type in Each_experiment_procedure:
        for Element_key in Each_experiment_procedure[Each_section_type]:
            for Each_section_type in Each_experiment_procedure:
                # print(f'Each_section_type: {Each_section_type}')
                if Each_experiment_procedure[Each_section_type][Element_key]:
                    # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                    # print(f'DEBUG1 dans elements {Element_key}')
                    if Element_key == 'elements':
                        # print(f'DEBUG2 dans elements -----------------------------------')
                        # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                        # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                        # print(f"Element_key: {Element_key}")
                        for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                            if sample["element_type"] == "samples":
                                section_nameANDsample_id = {}
                                section_nameANDsample_id[Each_experiment_procedure['experiment_procedure']['name']] = \
                                sample['id']
                                # section_nameANDsample_id_list.append(section_nameANDsample_id)

                                # print(Each_experiment_procedure['experiment_procedure']['name'])
                                # section_name_list.append(Each_experiment_procedure['experiment_procedure']['name'])
                                section_name_list.append(section_nameANDsample_id)

                                # print(f'DEBUG5 {section_name_list}')
                                # print(f"DEBUG6-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")
                                # sample_list.append(sample["id"])
                                # print(f'sample_list: {sample_list}')

# #-------- GET STOCK ID FOR THE COMPONENT SECTION------------------------
stock_id_list = []
dict_stock_id_samle_name = {}
stock_id_2 = []

for result in section_name_list:
    for key, value in result.items():
        if key != 'Add sample to stock':
            print(f'result final: {key, value}')
            sample_el_original = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()
            sample_el_data = json.loads(sample_el_original["data"])

            for sample in sample_el_data["samples"]:
                # sample_el_original_id = sample["id"]
                # sample_el_original_name = sample["name"]
                stocks_ids = sample["saved_stocks_ids"]
                # print(f'DEBUG {stocks_ids}, {sample_el_original_name}')
                # dict_stock_id_samle_name [stocks_ids[0]] = sample_el_original_name
                stock_id_list.extend(stocks_ids)

        if key == 'Add sample to stock':
            print(f'result final: {key, value}')
            sample_el_original_2 = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()
            sample_el_data_2 = json.loads(sample_el_original_2["data"])
            for sample in sample_el_data_2["samples"]:
                stock_id_2 = sample["saved_stocks_ids"]
                stock_id_2 = stock_id_2[0]

print(f'stock_id_list: {stock_id_list}\n')
# print(f'dictionary dict_stock_id_samle_name: {dict_stock_id_samle_name}')
print(f'stock_id_2: {stock_id_2}\n')

# #-------- CREATE A DICTIONARY {STOCK_ID[NAME,LOT]}------------------------
dict_id_list_name_lot = {}

for stock_id in stock_id_list:
    list_name_lot = []
    stock_data = requests.get(f'{base()}/api/v1/stocks/{stock_id}', json={"token": token()}).json()

    print(f'----------------stock_id: {stock_id}')

    stock_lot = stock_data["lot"]
    stock_name = stock_data["name"]
    list_name_lot.append((stock_name, stock_lot))
    print(f'list_name: {list_name_lot}')
    dict_id_list_name_lot[stock_id] = list_name_lot
print(f'----------------dict_id_list_name_lot: {dict_id_list_name_lot}')

# #--------  Update the lot in LabGuru: --------------------------------------
print("Reset lot, necessary for updating the lot")
# Reset lot, necessary for updating the lot
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'lot': None}})
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'lot': f'{dict_id_list_name_lot}'}})
print(f'requests.put response.url: {response.url}')
print(f'requests.put response.ok: {response.ok}')

# #--------  control de la valeur du lot pour savoir si l'update a reussi --------------------------------------
stock_2_data = requests.get(f'{base()}/api/v1/stocks/{stock_id_2}', json={"token": token()}).json()
print(f'stock_id_2_lot, have we changed the lot? if result is AAA we have not changed it: {stock_2_data["lot"]}')

##################################
# Expiry date: stored date+2weeks#
##################################


# #-------- Recuperation de la stored_date --------------------------------------
expiration_date = stock_2_data["expiration_date"]
print(f'stock_2_expiration date: {expiration_date}')
# print(f'stock_2_data{stock_2_data}')
Stored_on_date = stock_2_data["stored_on"]
print(f'Stored_on_date: {Stored_on_date}')

# Cut the date in year, month and day
# The cut of the date is necessary to use the object Stored_on_date
year, month, day = Stored_on_date.split("-")
Stored_on_date = datetime.datetime(int(year), int(month), int(day))
# print(Stored_on_date.year, Stored_on_date.month, Stored_on_date.day)

# Compute the expiration date
expiration_days = 14
expiration_month = 1
expdd = Stored_on_date + datetime.timedelta(days=expiration_days)
print(f'expiration date: {expdd.strftime("%Y-%m-%d")}')

expdm = Stored_on_date + relativedelta(months=expiration_month)
print(f'After Month: {expdm.strftime("%Y-%m-%d")}')

# #-------- Display the expiration date in LabGuru --------------------------------------
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'expiration_date': None}})
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'expiration_date': f'{expdd}.strftime("%Y-%m-%d")'}})

# #-------- Debug and Control stuff --------------------------------------
# # addition to check the content of stock data after the update - A supprimer une fois les tests complétés
stock_2_data = requests.get(f'{base()}/api/v1/stocks/{stock_id_2}', json={"token": token()}).json()
# stock_2_lot_after=stock_2_data["lot"]

# print(f'stock_id_2_lot_after: {stock_2_lot_after}')


expiration_date_after = stock_2_data["expiration_date"]
print(f'stock_2_expiration_date_after: {expiration_date_after}')




#-----------------------------------------------------------------------------------------------------------------------
# 02-Prod-1.0- Lots and expiration date on SP exp-Trigger on section-2 weeks shelf life
#-----------------------------------------------------------------------------------------------------------------------
'''
Experiment
Update

Scripter
Scripter Version
current
Description
explanation
lang            Code Template
Python          none
'''
import requests
import datetime
import calendar
from dateutil.relativedelta import relativedelta

experiment = variable("trigger_experiment")
experiment_id = experiment["id"]
experiment = requests.get(f'{base()}/api/v1/experiments/{experiment_id}', json={"token": token()}).json()

##################################################################
# TRIGGER on section name = Lot and expiry date added - 2 WEEKS #
##################################################################

# #-------- ITERATE OVER SECTION NAME AND TEST SECTION NAME VALUE FOR "Lot and expiry date added - 2 WEEKS" ------------------------
experiment_procedure = experiment["experiment_procedures"]

for Each_experiment_procedure in experiment_procedure:
    # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
    # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
    print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

    if Each_experiment_procedure['experiment_procedure']['name'] == "Lot and expiry date added - 2 WEEKS":
        print("RUN THE SCRIPT")

        ########################################
        # Get the lot and display it in labguru#
        ########################################

        # #-------- GET SECTION NAME AND SAMPLE ID------------------------
        experiment_procedure = experiment["experiment_procedures"]
        sample_list = []
        section_name_list = []
        for Each_experiment_procedure in experiment_procedure:
            # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
            # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
            # print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

            for Each_section_type in Each_experiment_procedure:
                for Element_key in Each_experiment_procedure[Each_section_type]:
                    for Each_section_type in Each_experiment_procedure:
                        # print(f'Each_section_type: {Each_section_type}')
                        if Each_experiment_procedure[Each_section_type][Element_key]:
                            # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                            # print(f'DEBUG1 dans elements {Element_key}')
                            if Element_key == 'elements':
                                # print(f'DEBUG2 dans elements -----------------------------------')
                                # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                                # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                                # print(f"Element_key: {Element_key}")
                                for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                                    if sample["element_type"] == "samples":
                                        section_nameANDsample_id = {}
                                        section_nameANDsample_id[
                                            Each_experiment_procedure['experiment_procedure']['name']] = sample['id']
                                        # section_nameANDsample_id_list.append(section_nameANDsample_id)

                                        # print(Each_experiment_procedure['experiment_procedure']['name'])
                                        # section_name_list.append(Each_experiment_procedure['experiment_procedure']['name'])
                                        section_name_list.append(section_nameANDsample_id)

                                        # print(f'DEBUG5 {section_name_list}')
                                        # print(f"DEBUG6-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")
                                        # sample_list.append(sample["id"])
                                        # print(f'sample_list: {sample_list}')

        # #-------- GET STOCK ID FOR THE COMPONENT SECTIONS-----------------------------------------------
        stock_id_list = []
        dict_stock_id_samle_name = {}
        stock_id_2 = []

        for result in section_name_list:
            for key, value in result.items():
                if key != 'Add sample to stock':
                    print(f'result final: {key, value}')
                    sample_el_original = requests.get(f'{base()}/api/v1/elements/{value}',
                                                      json={"token": token()}).json()
                    sample_el_data = json.loads(sample_el_original["data"])

                    for sample in sample_el_data["samples"]:
                        # sample_el_original_id = sample["id"]
                        # sample_el_original_name = sample["name"]
                        stocks_ids = sample["saved_stocks_ids"]
                        # print(f'DEBUG {stocks_ids}, {sample_el_original_name}')
                        # dict_stock_id_samle_name [stocks_ids[0]] = sample_el_original_name
                        stock_id_list.extend(stocks_ids)

                if key == 'Add sample to stock':
                    print(f'result final: {key, value}')
                    sample_el_original_2 = requests.get(f'{base()}/api/v1/elements/{value}',
                                                        json={"token": token()}).json()
                    sample_el_data_2 = json.loads(sample_el_original_2["data"])
                    for sample in sample_el_data_2["samples"]:
                        stock_id_2 = sample["saved_stocks_ids"]
                        stock_id_2 = stock_id_2[0]

        print(f'stock_id_list: {stock_id_list}\n')
        # print(f'dictionary dict_stock_id_samle_name: {dict_stock_id_samle_name}')
        print(f'stock_id_2: {stock_id_2}\n')

        # #-------- CREATE A DICTIONARY {STOCK_ID[NAME,LOT]}-------------------------------------------------------
        dict_id_list_name_lot = {}

        for stock_id in stock_id_list:
            list_name_lot = []
            stock_data = requests.get(f'{base()}/api/v1/stocks/{stock_id}', json={"token": token()}).json()

            print(f'----------------stock_id: {stock_id}')

            stock_lot = stock_data["lot"]
            stock_name = stock_data["name"]
            list_name_lot.append((stock_name, stock_lot))
            print(f'list_name: {list_name_lot}')
            dict_id_list_name_lot[stock_id] = list_name_lot
        print(f'----------------dict_id_list_name_lot: {dict_id_list_name_lot}')

        # #--------  Update the lot in LabGuru: -------------------------------------------------------
        print("Reset lot, necessary for updating the lot")
        # Reset lot, necessary for updating the lot
        response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                                json={'token': token(), 'item': {'lot': None}})
        response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                                json={'token': token(), 'item': {'lot': f'{dict_id_list_name_lot}'}})
        print(f'requests.put response.url: {response.url}')
        print(f'requests.put response.ok: {response.ok}')

        # #--------  control de la valeur du lot pour savoir si l'update a reussi --------------------------------------
        stock_2_data = requests.get(f'{base()}/api/v1/stocks/{stock_id_2}', json={"token": token()}).json()
        print(
            f'stock_id_2_lot, have we changed the lot? if result is AAA we have not changed it: {stock_2_data["lot"]}')

        ##################################
        # Expiry date: stored date+2weeks#
        ##################################

        # #-------- GET stored on date for the created stock ------------------------------------------
        expiration_date = stock_2_data["expiration_date"]
        print(f'stock_2_expiration date: {expiration_date}')
        # print(f'stock_2_data{stock_2_data}')
        Stored_on_date = stock_2_data["stored_on"]
        print(f'Stored_on_date: {Stored_on_date}')

        # #---------CUT the date in year, month and day-----------------------------------------------
        # The cut of the date is necessary to use the object Stored_on_date
        year, month, day = Stored_on_date.split("-")
        Stored_on_date = datetime.datetime(int(year), int(month), int(day))
        # print(Stored_on_date.year, Stored_on_date.month, Stored_on_date.day)

        ##--------------- Compute the expiration date--------------------------------------------------
        expiration_days = 14
        expiration_month = 1
        expdd = Stored_on_date + datetime.timedelta(days=expiration_days)
        print(f'expiration date: {expdd.strftime("%Y-%m-%d")}')

        expdm = Stored_on_date + relativedelta(months=expiration_month)
        print(f'After Month: {expdm.strftime("%Y-%m-%d")}')

        # #-------- Display the expiration date in LabGuru --------------------------------------
        response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                                json={'token': token(), 'item': {'expiration_date': None}})
        response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                                json={'token': token(), 'item': {'expiration_date': f'{expdd}.strftime("%Y-%m-%d")'}})

        # #-------- Debug and Control stuff --------------------------------------
        # # addition to check the content of stock data after the update - A supprimer une fois les tests complétés
        stock_2_data = requests.get(f'{base()}/api/v1/stocks/{stock_id_2}', json={"token": token()}).json()
        # stock_2_lot_after=stock_2_data["lot"]

        # print(f'stock_id_2_lot_after: {stock_2_lot_after}')

        expiration_date_after = stock_2_data["expiration_date"]
        print(f'stock_2_expiration_date_after: {expiration_date_after}')

        break

print(f'toto')



#-----------------------------------------------------------------------------------------------------------------------
# 03-Prod-1.0- Lots and expiration date on SP exp-Trigger on section-4 weeks shelf life
#-----------------------------------------------------------------------------------------------------------------------
'''
Experiment
Update

Scripter
Scripter Version
current
Description
explanation
lang            Code Template
Python          none
'''
import requests
import datetime
import calendar
from dateutil.relativedelta import relativedelta

experiment = variable("trigger_experiment")
experiment_id = experiment["id"]
experiment = requests.get(f'{base()}/api/v1/experiments/{experiment_id}', json={"token": token()}).json()

##################################################################
# TRIGGER on section name = Lot and exprity date added - 4 WEEKS #
##################################################################

# #-------- ITERATE OVER SECTION NAME AND TEST SECTION NAME VALUE FOR "Lot and expiry date added - 4 WEEKS" ------------------------
experiment_procedure = experiment["experiment_procedures"]

for Each_experiment_procedure in experiment_procedure:
    # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
    # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
    print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

    if Each_experiment_procedure['experiment_procedure']['name'] == "Lot and expiry date added - 4 WEEKS":
        print("RUN THE SCRIPT")

        ########################################
        # Get the lot and display it in labguru#
        ########################################

        # #-------- GET SECTION NAME AND SAMPLE ID------------------------
        experiment_procedure = experiment["experiment_procedures"]
        sample_list = []
        section_name_list = []
        for Each_experiment_procedure in experiment_procedure:
            # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
            # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
            # print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

            for Each_section_type in Each_experiment_procedure:
                for Element_key in Each_experiment_procedure[Each_section_type]:
                    for Each_section_type in Each_experiment_procedure:
                        # print(f'Each_section_type: {Each_section_type}')
                        if Each_experiment_procedure[Each_section_type][Element_key]:
                            # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                            # print(f'DEBUG1 dans elements {Element_key}')
                            if Element_key == 'elements':
                                # print(f'DEBUG2 dans elements -----------------------------------')
                                # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                                # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                                # print(f"Element_key: {Element_key}")
                                for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                                    if sample["element_type"] == "samples":
                                        section_nameANDsample_id = {}
                                        section_nameANDsample_id[
                                            Each_experiment_procedure['experiment_procedure']['name']] = sample['id']
                                        # section_nameANDsample_id_list.append(section_nameANDsample_id)

                                        # print(Each_experiment_procedure['experiment_procedure']['name'])
                                        # section_name_list.append(Each_experiment_procedure['experiment_procedure']['name'])
                                        section_name_list.append(section_nameANDsample_id)

                                        # print(f'DEBUG5 {section_name_list}')
                                        # print(f"DEBUG6-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")
                                        # sample_list.append(sample["id"])
                                        # print(f'sample_list: {sample_list}')

        # #-------- GET STOCK ID FOR THE COMPONENT SECTIONS-----------------------------------------------
        stock_id_list = []
        dict_stock_id_samle_name = {}
        stock_id_2 = []

        for result in section_name_list:
            for key, value in result.items():
                if key != 'Add sample to stock':
                    print(f'result final: {key, value}')
                    sample_el_original = requests.get(f'{base()}/api/v1/elements/{value}',
                                                      json={"token": token()}).json()
                    sample_el_data = json.loads(sample_el_original["data"])

                    for sample in sample_el_data["samples"]:
                        # sample_el_original_id = sample["id"]
                        # sample_el_original_name = sample["name"]
                        stocks_ids = sample["saved_stocks_ids"]
                        # print(f'DEBUG {stocks_ids}, {sample_el_original_name}')
                        # dict_stock_id_samle_name [stocks_ids[0]] = sample_el_original_name
                        stock_id_list.extend(stocks_ids)

                if key == 'Add sample to stock':
                    print(f'result final: {key, value}')
                    sample_el_original_2 = requests.get(f'{base()}/api/v1/elements/{value}',
                                                        json={"token": token()}).json()
                    sample_el_data_2 = json.loads(sample_el_original_2["data"])
                    for sample in sample_el_data_2["samples"]:
                        stock_id_2 = sample["saved_stocks_ids"]
                        stock_id_2 = stock_id_2[0]

        print(f'stock_id_list: {stock_id_list}\n')
        # print(f'dictionary dict_stock_id_samle_name: {dict_stock_id_samle_name}')
        print(f'stock_id_2: {stock_id_2}\n')

        # #-------- CREATE A DICTIONARY {STOCK_ID[NAME,LOT]}-------------------------------------------------------
        dict_id_list_name_lot = {}

        for stock_id in stock_id_list:
            list_name_lot = []
            stock_data = requests.get(f'{base()}/api/v1/stocks/{stock_id}', json={"token": token()}).json()

            print(f'----------------stock_id: {stock_id}')

            stock_lot = stock_data["lot"]
            stock_name = stock_data["name"]
            list_name_lot.append((stock_name, stock_lot))
            print(f'list_name: {list_name_lot}')
            dict_id_list_name_lot[stock_id] = list_name_lot
        print(f'----------------dict_id_list_name_lot: {dict_id_list_name_lot}')

        # #--------  Update the lot in LabGuru: -------------------------------------------------------
        print("Reset lot, necessary for updating the lot")
        # Reset lot, necessary for updating the lot
        response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                                json={'token': token(), 'item': {'lot': None}})
        response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                                json={'token': token(), 'item': {'lot': f'{dict_id_list_name_lot}'}})
        print(f'requests.put response.url: {response.url}')
        print(f'requests.put response.ok: {response.ok}')

        # #--------  control de la valeur du lot pour savoir si l'update a reussi --------------------------------------
        stock_2_data = requests.get(f'{base()}/api/v1/stocks/{stock_id_2}', json={"token": token()}).json()
        print(
            f'stock_id_2_lot, have we changed the lot? if result is AAA we have not changed it: {stock_2_data["lot"]}')

        ####################################
        # Expiry date: stored date+28 days #
        ####################################
        expiration_days = 28

        # #-------- GET stored on date for the created stock ------------------------------------------
        expiration_date = stock_2_data["expiration_date"]
        print(f'stock_2_expiration date: {expiration_date}')
        # print(f'stock_2_data{stock_2_data}')
        Stored_on_date = stock_2_data["stored_on"]
        print(f'Stored_on_date: {Stored_on_date}')

        # #---------CUT the date in year, month and day-----------------------------------------------
        # The cut of the date is necessary to use the object Stored_on_date
        year, month, day = Stored_on_date.split("-")
        Stored_on_date = datetime.datetime(int(year), int(month), int(day))
        # print(Stored_on_date.year, Stored_on_date.month, Stored_on_date.day)

        ##--------------- Compute the expiration date--------------------------------------------------
        expiration_month = 1
        expdd = Stored_on_date + datetime.timedelta(days=expiration_days)
        print(f'expiration date: {expdd.strftime("%Y-%m-%d")}')

        expdm = Stored_on_date + relativedelta(months=expiration_month)
        print(f'After Month: {expdm.strftime("%Y-%m-%d")}')

        # #-------- Display the expiration date in LabGuru --------------------------------------
        response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                                json={'token': token(), 'item': {'expiration_date': None}})
        response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                                json={'token': token(), 'item': {'expiration_date': f'{expdd}.strftime("%Y-%m-%d")'}})

        # #-------- Debug and Control stuff --------------------------------------
        # # addition to check the content of stock data after the update - A supprimer une fois les tests complétés
        stock_2_data = requests.get(f'{base()}/api/v1/stocks/{stock_id_2}', json={"token": token()}).json()
        # stock_2_lot_after=stock_2_data["lot"]

        # print(f'stock_id_2_lot_after: {stock_2_lot_after}')

        expiration_date_after = stock_2_data["expiration_date"]
        print(f'stock_2_expiration_date_after: {expiration_date_after}')

        break

print(f'toto')



#-----------------------------------------------------------------------------------------------------------------------
# Test-Julien
#-----------------------------------------------------------------------------------------------------------------------
'''
Scripter
Scripter Version
current
Description
explanation
lang            Code Template
Python          none
'''
# import datetime
# import calendar
# import requests
# import csv
# import os, sys
# import platform
#
# my_os = platform.system()
# print("OS in my system : ", my_os)
#
# print(help(lab))
#
# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['spam', 'Lovely Spam', 'Wonderful Spam'])
#
# path = '/srv/scripter/tmp/brid1dpbstsh1xbkezden7r1u/rendered_files'
# print({os.getcwd()})
# print(os.environ.get('HOME'))
# result = os.listdir()
# print(result)

# # response = requests.get(f'{base()}/api/v1/elements/1862', json={"token": token()}).json()
# response = requests.get(f'{base()}/api/v1/elements/1862', json={"token": token()})
# print(response.status_code)

# # Date calculations
# today = datetime.date.today()
# days_in_current_month = calendar.monthrange(today.year, today.month)[1]
# days_till_end_month = days_in_current_month - today.day
# start_date = today + datetime.timedelta(days=days_till_end_month + 1)
# print(start_date)


# response = requests.get(f'{base()}/api/v1/knowledge/experiments/177', json={"token": token()}).json()
# response = requests.get(f'{base()}/api/v1/experiments/177', json={"token": token()})
# print(f'status_code: {response.status_code}\n')
# data=response.json()
# for line in data:
#   print(f'key: {line}, value: {data[line]}')

# response = requests.get(f'{base()}/api/v1/storage/storages?id=533')
# print(f'status_code: {response.status_code}\n')

# ##################################
# # List all the modules installed #
# ##################################
# help('modules')

# #-------------------------------------------------------------------------------------
# # List folders id and then print each folder by its id: OK
# for index, value in enumerate(lab.list_folders(project_id=None, page_num=1)):
#   print(value)
#   # print(value.project_id)
#   # print(lab.get_folder(folder_id = value.project_id).title)


# #-------------------------------------------------------------------------------------

# # List Inventory items name and id: OK
# for index, value in enumerate(lab.list_inventory_items(item_type='cell_lines', page_num=1)):
#   print(f"item name: {lab.list_inventory_items(item_type='cell_lines', page_num=1)[index].name}")
#   print(f"item id: {lab.list_inventory_items(item_type='cell_lines', page_num=1)[index].id}")


# #-------------------------------------------------------------------------------------

# # Number of Inventory items: OK

# print(f"number items in inventory: {len(lab.list_inventory_items(item_type='cell_lines', page_num=1))}")

# #-------------------------------------------------------------------------------------

# # List all projects id, projects name and for each one, all folders title: OK
# for proj in lab.list_projects(page_num=1):
#     print(f'PROJECT - project id: {proj.id}, project name: {proj.name}')

#     for folder in lab.list_folders(project_id=proj.id, page_num=1):
#       print(f'Folder title: {folder.title}')


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


# for exp in lab.list_experiments(page_num=1):
#   print(exp.id)
#   for index, value in enumerate(lab.get_elements_by_type(experiment_id=exp.id, element_type=None)):
#     print(index, value)


# #-------------------------------------------------------------------------------------

# # List all sections: NOK

# # The script doesn't return anything. Is there any section created?

# sections = lab.list_experiment_procedures(experiment_id=None, page_num=1)

# print(sections)

# #-------------------------------------------------------------------------------------

# # List all projects: OK

# print out project info
# for project in lab.list_projects(page_num=1):
#     print(f'Project id: {project.id}, Project title: {project.title}, Project owner: {project.owner}')

# #-------------------------------------------------------------------------------------

# # Download project information

# project = lab.get_project(project_id='1')
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
##########
# # Update a project
# # for project in lab.list_projects(page_num=1):
# #     print(f'Project id: {project.id}, Project title: {project.title}, Project owner: {project.owner}')

# project_update = lab.update_project(project_id='7', title="Update my new test project - JP")

# print(project_update.id, project_update.title)

# #-------------------------------------------------------------------------------------

# # List all experiments: OK
# for exp in lab.list_experiments(page_num=1):
#   print(f'experiment id: {exp.id}, experiment name: {exp.title}, experiment description: {exp.description}')


# #-------------------------------------------------------------------------------------

# # Firt test with usual "hello world!": OK

# log("Hello world this is a log!")
# print("Hello World this is a print!")



#-----------------------------------------------------------------------------------------------------------------------
# Test-Lucie
#-----------------------------------------------------------------------------------------------------------------------
'''
Find Element By Section
            Variable Name                               element of type
Find in     trigger_experiment      element of type     text

                        Section Name
In a section named      Lot and expiry date added - 2 WEEKS

                        Element
And store it as         element_1


Scripter
Scripter Version
current
Description
explanation
lang            Code Template
Python          none
'''



#-----------------------------------------------------------------------------------------------------------------------
# Tool-Get list of sample element ids-V1.0
#-----------------------------------------------------------------------------------------------------------------------
import requests

experiment_1 = variable("experiment_1")
# print(f'experiment DEBUG11 {experiment_1}')
experiment_procedure = experiment_1["experiment_procedures"]
# print(f'experiment DEBUG12: {experiment_1["experiment_procedures"]}')
print(f'experiment_procedure DEBUG13:{experiment_procedure}\n\n')

sample_list = []
for Each_experiment_procedure in experiment_procedure:
    # print(f'DEBUG:{Each_experiment_procedure}\n')
    for Each_section_type in Each_experiment_procedure:
        # print(f'Each_section_type:{Each_experiment_procedure[Each_section_type]}')

        # for keys, value in Each_experiment_procedure.items():
        #   print("DEBUG")
        #   print(f'key: {keys}\nvalue: {value}')

        for Element_key in Each_experiment_procedure[Each_section_type]:
            # print(f'Element_key:{Element_key}')
            for Each_section_type in Each_experiment_procedure:
                if Each_experiment_procedure[Each_section_type][Element_key]:
                    # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                    if Element_key == 'elements':
                        print(
                            f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                        print("")
                        # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                        print(f"Element_key: {Element_key}")

                        for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                            if sample["element_type"] == "samples":
                                print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                                sample_list.append(sample["id"])

print(f'sample_list: {sample_list}')

# stock_id_list=[]
# for samples in experiment_1["id"]:
#   stocks_ids=sample["saved_stocks_ids"]
#   stock_id_list.extend(stocks_ids)
# print(stock_id_list)




#-----------------------------------------------------------------------------------------------------------------------
# Tool-Get stock name and lot from stock ID
#-----------------------------------------------------------------------------------------------------------------------
'''
Triggerless 
manual

Get Stock
                    ID                      Stock
Get Stock by ID     1034    and store in    stock_1

                Act
if not found    stop

Scripter
Scripter Version
current
Description
explanation
lang            Code Template
Python          none
'''
import requests

stock=variable("stock_1")

stock_id=stock["id"] #A modifier lors de l'intégration----------------------------
stock_data = requests.get(f'{base()}/api/v1/stocks/{stock_id}', json={"token": token()}).json()
print(f'stock_id{stock_id}')
# print(f'DEBUG------stock_data:{stock_data}')

stock_lot=stock_data["lot"]
print(f'stock_lot{stock_lot}')

stock_name=stock_data["name"]
print(f'stock_name:{stock_name}')

dict_stock_name_lot={}
dict_stock_name_lot[stock_name]=stock_lot
print(f'dict_stock_name_lot: {dict_stock_name_lot}')

exp_id=stock_data["id"]
print(f'exp_id:{exp_id}')




#-----------------------------------------------------------------------------------------------------------------------
# Tool-Lucie- Trigger on section name
#-----------------------------------------------------------------------------------------------------------------------
'''
Experiment
Update

Scripter
Scripter Version
current
Description
explanation
lang            Code Template
Python          none
'''
import requests

experiment = variable("trigger_experiment")
experiment_id = experiment["id"]
experiment = requests.get(f'{base()}/api/v1/experiments/{experiment_id}', json={"token": token()}).json()

################################################################
# TRIGGER on section name = ADD lot and 14 day expiration date #
################################################################

# #-------- ITERATE OVER SECTION NAME AND BREAK IF LIST OF COMPONENT LOTS DOES NOT EXIST------------------------
experiment_procedure = experiment["experiment_procedures"]

for Each_experiment_procedure in experiment_procedure:
    # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
    # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
    print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

    if Each_experiment_procedure['experiment_procedure']['name'] == "ADD lot and 14 day expiration date":
        print("RUN THE SCRIPT")
        break

print(f'toto')




#-----------------------------------------------------------------------------------------------------------------------
#-------------- 04/06/2023 ---------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------
# Test-Julien Trigerless
#-----------------------------------------------------------------------------------------------------------------------

import datetime
import calendar
import requests

# # response = requests.get(f'{base()}/api/v1/elements/1862', json={"token": token()}).json()
# response = requests.get(f'{base()}/api/v1/elements/1862', json={"token": token()})
# print(response.status_code)

# # Date calculations
# today = datetime.date.today()
# days_in_current_month = calendar.monthrange(today.year, today.month)[1]
# days_till_end_month = days_in_current_month - today.day
# start_date = today + datetime.timedelta(days=days_till_end_month + 1)
# print(start_date)


# response = requests.get(f'{base()}/api/v1/knowledge/experiments/177', json={"token": token()}).json()
response = requests.get(f'{base()}/api/v1/experiments/177', json={"token": token()})
print(f'status_code: {response.status_code}\n')
# data=response.json()
# for line in data:
#   print(f'key: {line}, value: {data[line]}')

response = requests.get(f'{base()}/api/v1/storage/storages?id=533')
print(f'status_code: {response.status_code}\n')

# ##################################
# # List all the modules installed #
# ##################################
# help('modules')

# #-------------------------------------------------------------------------------------
# # List folders id and then print each folder by its id: OK
# for index, value in enumerate(lab.list_folders(project_id=None, page_num=1)):
#   print(value)
#   # print(value.project_id)
#   # print(lab.get_folder(folder_id = value.project_id).title)


# #-------------------------------------------------------------------------------------

# # List Inventory items name and id: OK
# for index, value in enumerate(lab.list_inventory_items(item_type='cell_lines', page_num=1)):
#   print(f"item name: {lab.list_inventory_items(item_type='cell_lines', page_num=1)[index].name}")
#   print(f"item id: {lab.list_inventory_items(item_type='cell_lines', page_num=1)[index].id}")


# #-------------------------------------------------------------------------------------

# # Number of Inventory items: OK

# print(f"number items in inventory: {len(lab.list_inventory_items(item_type='cell_lines', page_num=1))}")

# #-------------------------------------------------------------------------------------

# # List all projects id, projects name and for each one, all folders title: OK
# for proj in lab.list_projects(page_num=1):
#     print(f'PROJECT - project id: {proj.id}, project name: {proj.name}')

#     for folder in lab.list_folders(project_id=proj.id, page_num=1):
#       print(f'Folder title: {folder.title}')


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


# for exp in lab.list_experiments(page_num=1):
#   print(exp.id)
#   for index, value in enumerate(lab.get_elements_by_type(experiment_id=exp.id, element_type=None)):
#     print(index, value)


# #-------------------------------------------------------------------------------------

# # List all sections: NOK

# # The script doesn't return anything. Is there any section created?

# sections = lab.list_experiment_procedures(experiment_id=None, page_num=1)

# print(sections)

# #-------------------------------------------------------------------------------------

# # List all projects: OK

# print out project info
# for project in lab.list_projects(page_num=1):
#     print(f'Project id: {project.id}, Project title: {project.title}, Project owner: {project.owner}')

# #-------------------------------------------------------------------------------------

# # Download project information

# project = lab.get_project(project_id='1')
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
##########
# # Update a project
# # for project in lab.list_projects(page_num=1):
# #     print(f'Project id: {project.id}, Project title: {project.title}, Project owner: {project.owner}')

# project_update = lab.update_project(project_id='7', title="Update my new test project - JP")

# print(project_update.id, project_update.title)

# #-------------------------------------------------------------------------------------

# # List all experiments: OK
# for exp in lab.list_experiments(page_num=1):
#   print(f'experiment id: {exp.id}, experiment name: {exp.title}, experiment description: {exp.description}')


# #-------------------------------------------------------------------------------------

# # Firt test with usual "hello world!": OK

# log("Hello world this is a log!")
# print("Hello World this is a print!")



#-----------------------------------------------------------------------------------------------------------------------
# Test-Julien
#-----------------------------------------------------------------------------------------------------------------------
'''
Trigerless
'''
import datetime
import calendar
import requests

# # response = requests.get(f'{base()}/api/v1/elements/1862', json={"token": token()}).json()
# response = requests.get(f'{base()}/api/v1/elements/1862', json={"token": token()})
# print(response.status_code)

# # Date calculations
# today = datetime.date.today()
# days_in_current_month = calendar.monthrange(today.year, today.month)[1]
# days_till_end_month = days_in_current_month - today.day
# start_date = today + datetime.timedelta(days=days_till_end_month + 1)
# print(start_date)


# response = requests.get(f'{base()}/api/v1/knowledge/experiments/177', json={"token": token()}).json()
response = requests.get(f'{base()}/api/v1/experiments/177', json={"token": token()})
print(f'status_code: {response.status_code}\n')
# data=response.json()
# for line in data:
#   print(f'key: {line}, value: {data[line]}')

response = requests.get(f'{base()}/api/v1/storage/storages?id=533')
print(f'status_code: {response.status_code}\n')

# ##################################
# # List all the modules installed #
# ##################################
# help('modules')

# #-------------------------------------------------------------------------------------
# # List folders id and then print each folder by its id: OK
# for index, value in enumerate(lab.list_folders(project_id=None, page_num=1)):
#   print(value)
#   # print(value.project_id)
#   # print(lab.get_folder(folder_id = value.project_id).title)


# #-------------------------------------------------------------------------------------

# # List Inventory items name and id: OK
# for index, value in enumerate(lab.list_inventory_items(item_type='cell_lines', page_num=1)):
#   print(f"item name: {lab.list_inventory_items(item_type='cell_lines', page_num=1)[index].name}")
#   print(f"item id: {lab.list_inventory_items(item_type='cell_lines', page_num=1)[index].id}")


# #-------------------------------------------------------------------------------------

# # Number of Inventory items: OK

# print(f"number items in inventory: {len(lab.list_inventory_items(item_type='cell_lines', page_num=1))}")

# #-------------------------------------------------------------------------------------

# # List all projects id, projects name and for each one, all folders title: OK
# for proj in lab.list_projects(page_num=1):
#     print(f'PROJECT - project id: {proj.id}, project name: {proj.name}')

#     for folder in lab.list_folders(project_id=proj.id, page_num=1):
#       print(f'Folder title: {folder.title}')


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


# for exp in lab.list_experiments(page_num=1):
#   print(exp.id)
#   for index, value in enumerate(lab.get_elements_by_type(experiment_id=exp.id, element_type=None)):
#     print(index, value)


# #-------------------------------------------------------------------------------------

# # List all sections: NOK

# # The script doesn't return anything. Is there any section created?

# sections = lab.list_experiment_procedures(experiment_id=None, page_num=1)

# print(sections)

# #-------------------------------------------------------------------------------------

# # List all projects: OK

# print out project info
# for project in lab.list_projects(page_num=1):
#     print(f'Project id: {project.id}, Project title: {project.title}, Project owner: {project.owner}')

# #-------------------------------------------------------------------------------------

# # Download project information

# project = lab.get_project(project_id='1')
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
##########
# # Update a project
# # for project in lab.list_projects(page_num=1):
# #     print(f'Project id: {project.id}, Project title: {project.title}, Project owner: {project.owner}')

# project_update = lab.update_project(project_id='7', title="Update my new test project - JP")

# print(project_update.id, project_update.title)

# #-------------------------------------------------------------------------------------

# # List all experiments: OK
# for exp in lab.list_experiments(page_num=1):
#   print(f'experiment id: {exp.id}, experiment name: {exp.title}, experiment description: {exp.description}')


# #-------------------------------------------------------------------------------------

# # Firt test with usual "hello world!": OK

# log("Hello world this is a log!")
# print("Hello World this is a print!")




#-----------------------------------------------------------------------------------------------------------------------
# Tool-Get list of sample element ids-V1.0
#-----------------------------------------------------------------------------------------------------------------------
'''
Get Experiment
Get experiment by id    234
and store in Experiment experiment_1
If not found Act stop

Scripter
Scripter Version
current
Description
Get list of element ids
lang            Code Template
Python          none
'''
import requests

experiment_1 = variable("experiment_1")
# print(f'experiment DEBUG11 {experiment_1}')
experiment_procedure = experiment_1["experiment_procedures"]
# print(f'experiment DEBUG12: {experiment_1["experiment_procedures"]}')
print(f'experiment_procedure DEBUG13:{experiment_procedure}\n\n')

sample_list = []
for Each_experiment_procedure in experiment_procedure:
    # print(f'DEBUG:{Each_experiment_procedure}\n')
    for Each_section_type in Each_experiment_procedure:
        # print(f'Each_section_type:{Each_experiment_procedure[Each_section_type]}')

        # for keys, value in Each_experiment_procedure.items():
        #   print("DEBUG")
        #   print(f'key: {keys}\nvalue: {value}')

        for Element_key in Each_experiment_procedure[Each_section_type]:
            # print(f'Element_key:{Element_key}')
            for Each_section_type in Each_experiment_procedure:
                if Each_experiment_procedure[Each_section_type][Element_key]:
                    # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                    if Element_key == 'elements':
                        print(
                            f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                        print("")
                        # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                        print(f"Element_key: {Element_key}")

                        for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                            if sample["element_type"] == "samples":
                                print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                                sample_list.append(sample["id"])

print(f'sample_list: {sample_list}')

# stock_id_list=[]
# for samples in experiment_1["id"]:
#   stocks_ids=sample["saved_stocks_ids"]
#   stock_id_list.extend(stocks_ids)
# print(stock_id_list)




#-----------------------------------------------------------------------------------------------------------------------
# Test-Lucie-developpement trigger for stock
#-----------------------------------------------------------------------------------------------------------------------
'''
Simple condition for strings
Action                                  if variableA            Condition   B
continue                                {{trigger_item.name}}   contains    stock

When stopped archive?
True

For example: {{attachment_1.extension}} equals [xlsx]
{{experiment_1.name}} contains proliferation
{{stock.type}} equals bottle 
Scripter
current
Description
explanation
'''
import requests

trigger_stock=variable("trigger_experiment")
experiment_id=trigger_experiment["id"]

print(f'toto')
print(f'trigger_experiment_id{trigger_experiment}')
print(f'stock_id:{stock_id}')




#-----------------------------------------------------------------------------------------------------------------------
# Tool-Get stock name and lot from stock ID
#-----------------------------------------------------------------------------------------------------------------------
'''
Get Stock
Get stock by idId       and store inStock
1034                    stock_1

If not found Act
stop

Scripter
Scripter Version
Current

Description
explanation

Lang    Code Template
Python  none
'''
import requests

stock=variable("stock_1")

stock_id=stock["id"] #A modifier lors de l'intégration----------------------------
stock_data = requests.get(f'{base()}/api/v1/stocks/{stock_id}', json={"token": token()}).json()
print(f'stock_id{stock_id}')
# print(f'DEBUG------stock_data:{stock_data}')

stock_lot=stock_data["lot"]
print(f'stock_lot{stock_lot}')

stock_name=stock_data["name"]
print(f'stock_name:{stock_name}')

dict_stock_name_lot={}
dict_stock_name_lot[stock_name]=stock_lot
print(f'dict_stock_name_lot: {dict_stock_name_lot}')

exp_id=stock_data["id"]
print(f'exp_id:{exp_id}')




#-----------------------------------------------------------------------------------------------------------------------
# 02-DevV3.0- Lots and expiration date on SP exp-Update with -SP
#-----------------------------------------------------------------------------------------------------------------------
'''
Simple condition for strings
Action      if variableA                    Condition       B
continue    {{trigger_experiment.title}}    contains        -SP

When stopped archive?When Stopped Archive
                        True

For example: {{attachment_1.extension}} equals [xlsx]
{{experiment_1.name}} contains proliferation
{{stock.type}} equals bottle

Scripter
Scripter Version
current

Description
explanation

Lang        Code Template
Python      none
'''
import requests
import datetime
import calendar
from dateutil.relativedelta import relativedelta

experiment = variable("trigger_experiment")
experiment_id = experiment["id"]
experiment = requests.get(f'{base()}/api/v1/experiments/{experiment_id}', json={"token": token()}).json()

########################################
# Get the lot and display it in labguru#
########################################


# #-------- GET SAMPLE NAME OF SECTION AND SAMPLE ID------------------------
experiment_procedure = experiment["experiment_procedures"]
sample_list = []
section_name_list = []
for Each_experiment_procedure in experiment_procedure:
    # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
    # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
    # print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

    for Each_section_type in Each_experiment_procedure:
        for Element_key in Each_experiment_procedure[Each_section_type]:
            for Each_section_type in Each_experiment_procedure:
                # print(f'Each_section_type: {Each_section_type}')
                if Each_experiment_procedure[Each_section_type][Element_key]:
                    # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                    # print(f'DEBUG1 dans elements {Element_key}')
                    if Element_key == 'elements':
                        # print(f'DEBUG2 dans elements -----------------------------------')
                        # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                        # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                        # print(f"Element_key: {Element_key}")
                        for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                            if sample["element_type"] == "samples":
                                section_nameANDsample_id = {}
                                section_nameANDsample_id[Each_experiment_procedure['experiment_procedure']['name']] = \
                                sample['id']
                                # section_nameANDsample_id_list.append(section_nameANDsample_id)

                                # print(Each_experiment_procedure['experiment_procedure']['name'])
                                # section_name_list.append(Each_experiment_procedure['experiment_procedure']['name'])
                                section_name_list.append(section_nameANDsample_id)

                                # print(f'DEBUG5 {section_name_list}')
                                # print(f"DEBUG6-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")
                                # sample_list.append(sample["id"])
                                # print(f'sample_list: {sample_list}')

# #-------- GET STOCK ID FOR THE COMPONENT SECTION------------------------
stock_id_list = []
dict_stock_id_samle_name = {}
stock_id_2 = []

for result in section_name_list:
    for key, value in result.items():
        if key != 'Add sample to stock':
            print(f'result final: {key, value}')
            sample_el_original = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()
            sample_el_data = json.loads(sample_el_original["data"])

            for sample in sample_el_data["samples"]:
                # sample_el_original_id = sample["id"]
                # sample_el_original_name = sample["name"]
                stocks_ids = sample["saved_stocks_ids"]
                # print(f'DEBUG {stocks_ids}, {sample_el_original_name}')
                # dict_stock_id_samle_name [stocks_ids[0]] = sample_el_original_name
                stock_id_list.extend(stocks_ids)

        if key == 'Add sample to stock':
            print(f'result final: {key, value}')
            sample_el_original_2 = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()
            sample_el_data_2 = json.loads(sample_el_original_2["data"])
            for sample in sample_el_data_2["samples"]:
                stock_id_2 = sample["saved_stocks_ids"]
                stock_id_2 = stock_id_2[0]

print(f'stock_id_list: {stock_id_list}\n')
# print(f'dictionary dict_stock_id_samle_name: {dict_stock_id_samle_name}')
print(f'stock_id_2: {stock_id_2}\n')

# #-------- CREATE A DICTIONARY {STOCK_ID[NAME,LOT]}------------------------
dict_id_list_name_lot = {}

for stock_id in stock_id_list:
    list_name_lot = []
    stock_data = requests.get(f'{base()}/api/v1/stocks/{stock_id}', json={"token": token()}).json()

    print(f'----------------stock_id: {stock_id}')

    stock_lot = stock_data["lot"]
    stock_name = stock_data["name"]
    list_name_lot.append((stock_name, stock_lot))
    print(f'list_name: {list_name_lot}')
    dict_id_list_name_lot[stock_id] = list_name_lot
print(f'----------------dict_id_list_name_lot: {dict_id_list_name_lot}')

# #--------  Update the lot in LabGuru: --------------------------------------
print("Reset lot, necessary for updating the lot")
# Reset lot, necessary for updating the lot
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'lot': None}})
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'lot': f'{dict_id_list_name_lot}'}})
print(f'requests.put response.url: {response.url}')
print(f'requests.put response.ok: {response.ok}')

# #--------  control de la valeur du lot pour savoir si l'update a reussi --------------------------------------
stock_2_data = requests.get(f'{base()}/api/v1/stocks/{stock_id_2}', json={"token": token()}).json()
print(f'stock_id_2_lot, have we changed the lot? if result is AAA we have not changed it: {stock_2_data["lot"]}')

##################################
# Expiry date: stored date+2weeks#
##################################


# #-------- Recuperation de la stored_date --------------------------------------
expiration_date = stock_2_data["expiration_date"]
print(f'stock_2_expiration date: {expiration_date}')
# print(f'stock_2_data{stock_2_data}')
Stored_on_date = stock_2_data["stored_on"]
print(f'Stored_on_date: {Stored_on_date}')

# Cut the date in year, month and day
# The cut of the date is necessary to use the object Stored_on_date
year, month, day = Stored_on_date.split("-")
Stored_on_date = datetime.datetime(int(year), int(month), int(day))
# print(Stored_on_date.year, Stored_on_date.month, Stored_on_date.day)

# Compute the expiration date
expiration_days = 14
expiration_month = 1
expdd = Stored_on_date + datetime.timedelta(days=expiration_days)
print(f'expiration date: {expdd.strftime("%Y-%m-%d")}')

expdm = Stored_on_date + relativedelta(months=expiration_month)
print(f'After Month: {expdm.strftime("%Y-%m-%d")}')

# #-------- Display the expiration date in LabGuru --------------------------------------
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'expiration_date': None}})
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'expiration_date': f'{expdd}.strftime("%Y-%m-%d")'}})

# #-------- Debug and Control stuff --------------------------------------
# # addition to check the content of stock data after the update - A supprimer une fois les tests complétés
stock_2_data = requests.get(f'{base()}/api/v1/stocks/{stock_id_2}', json={"token": token()}).json()
# stock_2_lot_after=stock_2_data["lot"]

# print(f'stock_id_2_lot_after: {stock_2_lot_after}')


expiration_date_after = stock_2_data["expiration_date"]
print(f'stock_2_expiration_date_after: {expiration_date_after}')




#-----------------------------------------------------------------------------------------------------------------------
# 01-Prod01.0-ExperimentDuplication-With timer
#-----------------------------------------------------------------------------------------------------------------------
'''
Simple condition for strings
Action          if variableA                    Condition       B
continue        {{trigger_experiment.title}     contains        duplicate

When stopped archive?   When Stopped Archive
                        True

For example: {{attachment_1.extension}} equals [xlsx]
{{experiment_1.name}} contains proliferation
{{stock.type}} equals bottle

Scripter
Scripter Version        Description         Lang        Code Template
current                 Tempo 5s            Python      none
'''
import requests
import time

duplicated_exp = variable("trigger_experiment")
original_exp_id = duplicated_exp["duplicate_of"]

time.sleep(5)

original_exp = requests.get(f'{base()}/api/v1/experiments/{original_exp_id}', json={"token": token()}).json()
duplicated_exp_id = duplicated_exp["id"]
duplicated_exp = requests.get(f'{base()}/api/v1/experiments/{duplicated_exp_id}', json={"token": token()}).json()

store_variable('duplicated_exp', duplicated_exp)
store_variable('original_exp', original_exp)

print(
    f'DEBUG ------------------duplicated_exp: {duplicated_exp["id"]} \n -------------original_exp_id: {original_exp_id}')
# print(f'DEBUG----------------duplicated_exp: {duplicated_exp}\n DEBUG------------- original_exp: {original_exp}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR ORIGINAL EXP-----------------\n')
experiment_procedure = original_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_original:{experiment_procedure}')

sample_list_original = []
for Each_experiment_procedure in experiment_procedure:
    # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
    for Each_section_type in Each_experiment_procedure:
        for Element_key in Each_experiment_procedure[Each_section_type]:
            # print(f'Element_key:{Element_key}')
            for Each_section_type in Each_experiment_procedure:
                if Each_experiment_procedure[Each_section_type][Element_key]:
                    # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                    if Element_key == 'elements':
                        # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                        # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                        # print(f"Element_key: {Element_key}")

                        for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                            if sample["element_type"] == "samples":
                                # print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                                sample_list_original.append(sample["id"])

print(f'sample_list_original: {sample_list_original}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR DUPLICATED EXP-----------------\n')
experiment_procedure = duplicated_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_duplicated:{experiment_procedure}')

sample_list_duplicated = []
for Each_experiment_procedure in experiment_procedure:
    # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
    for Each_section_type in Each_experiment_procedure:
        for Element_key in Each_experiment_procedure[Each_section_type]:
            # print(f'Element_key:{Element_key}')
            for Each_section_type in Each_experiment_procedure:
                if Each_experiment_procedure[Each_section_type][Element_key]:
                    # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                    if Element_key == 'elements':
                        # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                        # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                        # print(f"Element_key: {Element_key}")

                        for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                            if sample["element_type"] == "samples":
                                print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                                sample_list_duplicated.append(sample["id"])

print(f'sample_list_duplicated: {sample_list_duplicated}')

print(f'\n---------ITERATE THE POSITION IN THE SAMPLE LISTS, ASSIGN SAMPLE_ID AND SAMPLE_EL_DUPLICATED-------------\n')

for position in range(0, len(sample_list_original)):
    print(f'position: {position}')

    sample_el_original_id = sample_list_original[position]
    sample_el_duplicated_id = sample_list_duplicated[position]
    print(f'sample_el_original_id: {sample_el_original_id} and sample_el_duplicated_id: {sample_el_duplicated_id}')

    sample_el_original = requests.get(f'{base()}/api/v1/elements/{sample_el_original_id}',
                                      json={"token": token()}).json()

    # Les donnees retournees par requests sont au format string, ci-dessous nous les transformons pour etre au format json
    # puis on affiche les donnees.
    sample_el_data = json.loads(sample_el_original["data"])
    print(f'\nsample_el_original_id: {sample_el_original_id}\n')
    # print(f'sample_el_original:{sample_el_original}')

    stock_id_list = []
    for sample in sample_el_data["samples"]:
        sample_el_original_id = sample["id"]
        stocks_ids = sample["saved_stocks_ids"]
        stock_id_list.extend(stocks_ids)
        print(f'stock_id_list: {stock_id_list}\n')

    # Reset sample element data, necessary for updating the sample element
    print(f'sample_el_duplicated_id:{sample_el_duplicated_id}')
    response = requests.put(f'{base()}/api/v1/elements/{sample_el_duplicated_id}',
                            json={'token': token(), 'element': {'data': None}})
    print(f'Reset sample element data, return code:', response.status_code)

    # Add stocks to the duplicated experiment

    for stock_id in stock_id_list:
        print(f'stock_id: {stock_id}, Debug base: {base()} sample_el_duplicated_id: {sample_el_duplicated_id}')

        response = requests.get(
            f'{base()}/api/v1/sample_stocks/add_stock_by_barcode?token={token()}&element_id={sample_el_duplicated_id}&barcode={stock_id}',
            json={'token': token()})

        print(f'add stock {stock_id} to sample {sample_el_duplicated_id} return code:', response.status_code)

#-----------------------------------------------------------------------------------------------------------------------
#-------------- Old Backup ---------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

# Get list of element ids
import requests

experiment_1 = variable("experiment_1")
# print(f'experiment DEBUG11 {experiment_1}')
experiment_procedure = experiment_1["experiment_procedures"]
# print(f'experiment DEBUG12: {experiment_1["experiment_procedures"]}')
print(f'experiment_procedure DEBUG13:{experiment_procedure}\n\n')
# print(f'experiment_procedure_id DEBUG14: {experiment_1["experiment_procedures"][0]}')

# for toto in experiment_procedure:
#   print(f'toto:{toto}')
#   for tutu in toto:
#     print(f'tutu:{toto[tutu]}')
#     for tata in toto[tutu]:
#       print(f'tata:{tata}')

for Each_experiment_procedure in experiment_procedure:
  # print(f'DEBUG:{Each_experiment_procedure}\n')
  for Each_section_type in Each_experiment_procedure:
    # print(f'Each_section_type:{Each_experiment_procedure[Each_section_type]}')

    # for keys, value in Each_experiment_procedure.items():
    #   print("DEBUG")
    #   print(f'key: {keys}\nvalue: {value}')

    for Element_key in Each_experiment_procedure[Each_section_type]:
      # print(f'Element_key:{Element_key}')
      for Each_section_type in Each_experiment_procedure:
        if Each_experiment_procedure[Each_section_type][Element_key]:
          # if Element_key == 'elements' and Element_key == "Samples & Reagents":
          if Element_key == 'elements':
            print(
              f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
            print("")
            # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
            print(f"Element_key: {Element_key}")

            for toto in Each_experiment_procedure[Each_section_type][Element_key]:
              if toto["element_type"] == "samples":
                print(f'toto: {toto["id"]} {toto["element_type"]}')



#-----------------------------------------------------------------------------------------------------------------------

import requests

samples_el_original = variable("element_1")
samples_el_duplicated_id = variable("element_2")["id"]

print("--------------------------")
print("Debug:")
print(f"samples_el_original: {samples_el_original}\n\n")
print(f"samples_el_duplicated_id: {samples_el_duplicated_id}\n\n")
print("--------------------------\n")

# Iterate over the samples in the sample element of the original experiment to get stock ids
sample_el_data = json.loads(samples_el_original["data"])
print(f'sample_el_data: {sample_el_data}\n')
stock_id_list = []
for sample in sample_el_data["samples"]:
  #stocks_id = (sample["stocks"][0]["id"]) #Origil code. Do not give full list of IDs when multiple stocks
  sample_id = sample ["id"]
  stocks_ids = sample["saved_stocks_ids"] #From Malka's e-mail 11/05/2023. Give complete list of ids when multiple stocks allocated to one item but prevent allocation of stock.
  stock_id_list.extend(stocks_ids)
print(f'stock_id_list: {stock_id_list}\n')

# Reset sample element data, necessary for updating the sample element
response = requests.put(f'{base()}/api/v1/elements/{samples_el_duplicated_id}', json={'token': token(), 'element':{'data': None}})
print(f'Reset sample element data, return code:', response.status_code)

# Add stocks to the duplicated experiment
for stock_id in stock_id_list:
  print(f'stock_id: {stock_id}, Debug base: {base()} samples_el_duplicated_id: {samples_el_duplicated_id}')
  response = requests.get(f'{base()}/api/v1/sample_stocks/add_stock_by_barcode?token={token()}&element_id={samples_el_duplicated_id}&barcode={stock_id}\n', json={'token': token()})
  print(f'add stock {stock_id} to sample {samples_el_duplicated_id} return code:', response.status_code)



#-----------------------------------------------------------------------------------------------------------------------
# Julien-DuplicationTestWorkflow-V3.2-different names of Samples&Reagents-from ID174
import requests

duplicated_exp = variable("trigger_experiment")
original_exp_id = duplicated_exp["duplicate_of"]
original_exp = requests.get(f'{base()}/api/v1/experiments/{original_exp_id}', json={"token": token()}).json()

store_variable('duplicated_exp', duplicated_exp)
store_variable('original_exp', original_exp)

print(
  f'DEBUG ------------------duplicated_exp: {duplicated_exp["id"]} \n -------------original_exp_id: {original_exp_id}')
# print(f'DEBUG----------------duplicated_exp: {duplicated_exp}\n DEBUG------------- original_exp: {original_exp}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR ORIGINAL EXP-----------------\n')
experiment_procedure = original_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_original:{experiment_procedure}')

sample_list_original = []
for Each_experiment_procedure in experiment_procedure:
  # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
  for Each_section_type in Each_experiment_procedure:
    for Element_key in Each_experiment_procedure[Each_section_type]:
      # print(f'Element_key:{Element_key}')
      for Each_section_type in Each_experiment_procedure:
        if Each_experiment_procedure[Each_section_type][Element_key]:
          # if Element_key == 'elements' and Element_key == "Samples & Reagents":
          if Element_key == 'elements':
            # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
            # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
            # print(f"Element_key: {Element_key}")

            for sample in Each_experiment_procedure[Each_section_type][Element_key]:
              if sample["element_type"] == "samples":
                # print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                sample_list_original.append(sample["id"])

print(f'sample_list_original: {sample_list_original}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR DUPLICATED EXP-----------------\n')
experiment_procedure = duplicated_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_duplicated:{experiment_procedure}')

sample_list_duplicated = []
for Each_experiment_procedure in experiment_procedure:
  # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
  for Each_section_type in Each_experiment_procedure:
    for Element_key in Each_experiment_procedure[Each_section_type]:
      # print(f'Element_key:{Element_key}')
      for Each_section_type in Each_experiment_procedure:
        if Each_experiment_procedure[Each_section_type][Element_key]:
          # if Element_key == 'elements' and Element_key == "Samples & Reagents":
          if Element_key == 'elements':
            # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
            # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
            # print(f"Element_key: {Element_key}")

            for sample in Each_experiment_procedure[Each_section_type][Element_key]:
              if sample["element_type"] == "samples":
                # print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                sample_list_duplicated.append(sample["id"])

print(f'sample_list_duplicated: {sample_list_duplicated}')

print(f'\n---------ITERATE THE POSITION IN THE SAMPLE LISTS, ASSIGN SAMPLE_ID AND SAMPLE_EL_DUPLICATED-------------\n')

for position in range(0, len(sample_list_original)):
  print(f'position: {position}')

  sample_id = sample_list_original[position]
  sample_el_duplicated_id = sample_list_duplicated[position]
  print(f'sample_id: {sample_id} and sample_el_duplicated_id: {sample_el_duplicated_id}')

  sample_el_original = requests.get(f'{base()}/api/v1/elements/{sample_id}', json={"token": token()}).json()

  # Les donnees retournees par requests sont au format string, ci-dessous nous les transformons pour etre au format json
  # puis on affiche les donnees.
  sample_el_data = json.loads(sample_el_original["data"])
  print(f'\nsample_el_original_id: {sample_id}\n')
  # print(f'sample_el_original:{sample_el_original}')

  stock_id_list = []
  for sample in sample_el_data["samples"]:
    sample_id = sample["id"]
    stocks_ids = sample[
      "saved_stocks_ids"]  # From Malka's e-mail 11/05/2023. Give complete list of ids when multiple stocks allocated to one item but prevent allocation of stock.
    stock_id_list.extend(stocks_ids)
    print(f'stock_id_list: {stock_id_list}\n')

    # Reset sample element data, necessary for updating the sample element
    print(f'sample_el_duplicated_id:{sample_el_duplicated_id}')
    response = requests.put(f'{base()}/api/v1/elements/{sample_el_duplicated_id}',
                            json={'token': token(), 'element': {'data': None}})
    print(f'Reset sample element data, return code:', response.status_code)

    # Add stocks to the duplicated experiment

  for stock_id in stock_id_list:
    print(f'stock_id: {stock_id}, Debug base: {base()} sample_el_duplicated_id: {sample_el_duplicated_id}')
    response = requests.get(
      f'{base()}/api/v1/sample_stocks/add_stock_by_barcode?token={token()}&element_id={sample_el_duplicated_id}&barcode={stock_id}\n',
      json={'token': token()})
    print(f'add stock {stock_id} to sample {sample_el_duplicated_id} return code:', response.status_code)

#   FOR DEV
#     for position in range(0,len(sample_list_original)):
#   print(f'position: {position}')

#   sample_id = sample_list_original[position]
#   sample_el_duplicated_id=sample_list_duplicated[position]
#   print(f'sample_id: {sample_id} and sample_el_duplicated_id: {sample_el_duplicated_id}')

#   sample_el_original = requests.get(f'{base()}/api/v1/elements/{sample_id}', json={"token" : token()}).json()

# # Les donnees retournees par requests sont au format string, ci-dessous nous les transformons pour etre au format json
# # puis on affiche les donnees.
#   sample_el_data = json.loads(sample_el_original["data"])
#   print(f'\nsample_el_original_id: {sample_id}\n')
# # print(f'sample_el_original:{sample_el_original}')

#   stock_id_list = []
#   for sample in sample_el_data["samples"]:
#     sample_id = sample ["id"]
#     stocks_ids = sample["saved_stocks_ids"] #From Malka's e-mail 11/05/2023. Give complete list of ids when multiple stocks allocated to one item but prevent allocation of stock.
#     stock_id_list.extend(stocks_ids)
#     print(f'stock_id_list: {stock_id_list}\n')

#     # Reset sample element data, necessary for updating the sample element
#     print(f'sample_el_duplicated_id:{sample_el_duplicated_id}')
#     response = requests.put(f'{base()}/api/v1/elements/{sample_el_duplicated_id}', json={'token': token(), 'element':{'data': None}})
#     print(f'Reset sample element data, return code:', response.status_code)

#       # Add stocks to the duplicated experiment

#     for stock_id in stock_id_list:
#       print(f'stock_id: {stock_id}, Debug base: {base()} sample_el_duplicated_id: {sample_el_duplicated_id}')
#       response = requests.get(f'{base()}/api/v1/sample_stocks/add_stock_by_barcode?token={token()}&element_id={sample_el_duplicated_id}&barcode={stock_id}\n', json={'token': token()})
#       print(f'add stock {stock_id} to sample {sample_el_duplicated_id} return code:', response.status_code)


#-----------------------------------------------------------------------------------------------------------------------
#Julien-DuplicationTestWorkflow-V4.1

import requests

duplicated_exp = variable("trigger_experiment")
original_exp_id = duplicated_exp["duplicate_of"]
original_exp = requests.get(f'{base()}/api/v1/experiments/{original_exp_id}', json={"token": token()}).json()
duplicated_exp_id=duplicated_exp["id"]
duplicated_exp = requests.get(f'{base()}/api/v1/experiments/{duplicated_exp_id}', json={"token": token()}).json()

store_variable('duplicated_exp', duplicated_exp)
store_variable('original_exp', original_exp)

print(
  f'DEBUG ------------------duplicated_exp: {duplicated_exp["id"]} \n -------------original_exp_id: {original_exp_id}')
# print(f'DEBUG----------------duplicated_exp: {duplicated_exp}\n DEBUG------------- original_exp: {original_exp}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR ORIGINAL EXP-----------------\n')
experiment_procedure = original_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_original:{experiment_procedure}')

sample_list_original = []
for Each_experiment_procedure in experiment_procedure:
  # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
  for Each_section_type in Each_experiment_procedure:
    for Element_key in Each_experiment_procedure[Each_section_type]:
      # print(f'Element_key:{Element_key}')
      for Each_section_type in Each_experiment_procedure:
        if Each_experiment_procedure[Each_section_type][Element_key]:
          # if Element_key == 'elements' and Element_key == "Samples & Reagents":
          if Element_key == 'elements':
            # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
            # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
            # print(f"Element_key: {Element_key}")

            for sample in Each_experiment_procedure[Each_section_type][Element_key]:
              if sample["element_type"] == "samples":
                # print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                sample_list_original.append(sample["id"])

print(f'sample_list_original: {sample_list_original}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR DUPLICATED EXP-----------------\n')
experiment_procedure = duplicated_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_duplicated:{experiment_procedure}')

sample_list_duplicated = []
for Each_experiment_procedure in experiment_procedure:
  # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
  for Each_section_type in Each_experiment_procedure:
    for Element_key in Each_experiment_procedure[Each_section_type]:
      # print(f'Element_key:{Element_key}')
      for Each_section_type in Each_experiment_procedure:
        if Each_experiment_procedure[Each_section_type][Element_key]:
          # if Element_key == 'elements' and Element_key == "Samples & Reagents":
          if Element_key == 'elements':
            # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
            # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
            # print(f"Element_key: {Element_key}")

            for sample in Each_experiment_procedure[Each_section_type][Element_key]:
              if sample["element_type"] == "samples":
                print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                sample_list_duplicated.append(sample["id"])

print(f'sample_list_duplicated: {sample_list_duplicated}')

print(f'\n---------ITERATE THE POSITION IN THE SAMPLE LISTS, ASSIGN SAMPLE_ID AND SAMPLE_EL_DUPLICATED-------------\n')

for position in range(0, len(sample_list_original)):
  print(f'position: {position}')

  sample_el_original_id = sample_list_original[position]
  sample_el_duplicated_id = sample_list_duplicated[position]
  print(f'sample_el_original_id: {sample_el_original_id} and sample_el_duplicated_id: {sample_el_duplicated_id}')

  sample_el_original = requests.get(f'{base()}/api/v1/elements/{sample_el_original_id}', json={"token": token()}).json()

  # Les donnees retournees par requests sont au format string, ci-dessous nous les transformons pour etre au format json
  # puis on affiche les donnees.
  sample_el_data = json.loads(sample_el_original["data"])
  print(f'\nsample_el_original_id: {sample_el_original_id}\n')
  # print(f'sample_el_original:{sample_el_original}')

  stock_id_list = []
  for sample in sample_el_data["samples"]:
    sample_el_original_id = sample["id"]
    stocks_ids = sample["saved_stocks_ids"]
    stock_id_list.extend(stocks_ids)
    print(f'stock_id_list: {stock_id_list}\n')

  # Reset sample element data, necessary for updating the sample element
  print(f'sample_el_duplicated_id:{sample_el_duplicated_id}')
  response = requests.put(f'{base()}/api/v1/elements/{sample_el_duplicated_id}',
                          json={'token': token(), 'element': {'data': None}})
  print(f'Reset sample element data, return code:', response.status_code)

  # Add stocks to the duplicated experiment

  for stock_id in stock_id_list:
    print(f'stock_id: {stock_id}, Debug base: {base()} sample_el_duplicated_id: {sample_el_duplicated_id}')
    response = requests.get(
      f'{base()}/api/v1/sample_stocks/add_stock_by_barcode?token={token()}&element_id={sample_el_duplicated_id}&barcode={stock_id}\n',
      json={'token': token()})
    print(f'add stock {stock_id} to sample {sample_el_duplicated_id} return code:', response.status_code)


#-----------------------------------------------------------------------------------------------------------------------
BatchNumbersForPreparedSolution-V1.0
import requests

experiment = variable("experiment_1")
experiment_id = experiment["id"]
experiment = requests.get(f'{base()}/api/v1/experiments/{experiment_id}', json={"token": token()}).json()

# ------------------GET SAMPLE NAME OF SECTION AND SAMPLE ID------------------------
experiment_procedure = experiment["experiment_procedures"]
sample_list = []
section_name_list = []
for Each_experiment_procedure in experiment_procedure:
  # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
  # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
  # print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

  # section_nameANDsample_id_list=[]

  for Each_section_type in Each_experiment_procedure:
    for Element_key in Each_experiment_procedure[Each_section_type]:
      for Each_section_type in Each_experiment_procedure:
        # print(f'Each_section_type: {Each_section_type}')
        if Each_experiment_procedure[Each_section_type][Element_key]:
          # if Element_key == 'elements' and Element_key == "Samples & Reagents":
          # print(f'DEBUG1 dans elements {Element_key}')
          if Element_key == 'elements':
            # print(f'DEBUG2 dans elements -----------------------------------')
            # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
            # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
            # print(f"Element_key: {Element_key}")
            for sample in Each_experiment_procedure[Each_section_type][Element_key]:
              if sample["element_type"] == "samples":
                section_nameANDsample_id = {}
                section_nameANDsample_id[Each_experiment_procedure['experiment_procedure']['name']] = sample['id']
                # section_nameANDsample_id_list.append(section_nameANDsample_id)

                # print(Each_experiment_procedure['experiment_procedure']['name'])
                # section_name_list.append(Each_experiment_procedure['experiment_procedure']['name'])
                section_name_list.append(section_nameANDsample_id)

                # print(f'DEBUG5 {section_name_list}')
                # print(f"DEBUG6-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")
                # sample_list.append(sample["id"])
                # print(f'sample_list: {sample_list}')

# ------------------GET STOCK ID FOR THE COMPONENT SECTION------------------------


# -------------------UNDER DEVELOPMENT------------------------------------
for result in section_name_list:
  for key, value in result.items():
    if key != 'Add sample to stock':
      print(f'result final: {key, value}')
      sample_el_original = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()

      # Les donnees retournees par requests sont au format string, ci-dessous nous les transformons pour etre au format json
      # puis on affiche les donnees.
      sample_el_data = json.loads(sample_el_original["data"])

      # Affichage sous la forme d'un arbre
      # new_string = json.dumps(sample_el_data, indent=2)
      # print(f'\nsample_el_data: {new_string}\n')

      # Affichage sous form plate ou de string
      # print(f'sample_el_original:{sample_el_original}')

      # for sample_el_original_id in sample_list:
      #   print(sample_el_original_id)
      # sample_el_original = requests.get(f'{base()}/api/v1/elements/{sample_el_original_id}', json={"token": token()}).json()
      # sample_el_data = json.loads(sample_el_original["data"])

      dict_stock_id_samle_name = {}
      stock_id_list = []
      for sample in sample_el_data["samples"]:
        # print(sample)
        sample_el_original_id = sample["id"]
        sample_el_original_name = sample["name"]
        stocks_ids = sample["saved_stocks_ids"]
        print(f'DEBUG {stocks_ids}, {sample_el_original_name}')
        dict_stock_id_samle_name[sample_el_original_name] = stocks_ids[0]

        stock_id_list.extend(stocks_ids)
        print(f'stock_id_list: {stock_id_list}\n')

      print(f'dictionary dict_stock_id_samle_name: {dict_stock_id_samle_name}')


#-----------------------------------------------------------------------------------------------------------------------
-SP trigger and list of component lots-V1.0

'''
Simple condition for strings
Action            if variable A                                 Conditions    B
        continue                  {{trigger_experiment.title}}  contains      -SP

When stopped archive?  When Stopped Archive
                        True
'''
import requests

experiment = variable("trigger_experiment")
experiment_id = experiment["id"]
experiment = requests.get(f'{base()}/api/v1/experiments/{experiment_id}', json={"token": token()}).json()

# ------------------GET SAMPLE NAME OF SECTION AND SAMPLE ID------------------------
experiment_procedure = experiment["experiment_procedures"]
sample_list = []
section_name_list = []
for Each_experiment_procedure in experiment_procedure:
  # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
  # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
  # print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

  for Each_section_type in Each_experiment_procedure:
    for Element_key in Each_experiment_procedure[Each_section_type]:
      for Each_section_type in Each_experiment_procedure:
        # print(f'Each_section_type: {Each_section_type}')
        if Each_experiment_procedure[Each_section_type][Element_key]:
          # if Element_key == 'elements' and Element_key == "Samples & Reagents":
          # print(f'DEBUG1 dans elements {Element_key}')
          if Element_key == 'elements':
            # print(f'DEBUG2 dans elements -----------------------------------')
            # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
            # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
            # print(f"Element_key: {Element_key}")
            for sample in Each_experiment_procedure[Each_section_type][Element_key]:
              if sample["element_type"] == "samples":
                section_nameANDsample_id = {}
                section_nameANDsample_id[Each_experiment_procedure['experiment_procedure']['name']] = sample['id']
                # section_nameANDsample_id_list.append(section_nameANDsample_id)

                # print(Each_experiment_procedure['experiment_procedure']['name'])
                # section_name_list.append(Each_experiment_procedure['experiment_procedure']['name'])
                section_name_list.append(section_nameANDsample_id)

                # print(f'DEBUG5 {section_name_list}')
                # print(f"DEBUG6-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")
                # sample_list.append(sample["id"])
                # print(f'sample_list: {sample_list}')

# ------------------GET STOCK ID FOR THE COMPONENT SECTION------------------------
stock_id_list = []
dict_stock_id_samle_name = {}

for result in section_name_list:
  for key, value in result.items():
    if key != 'Add sample to stock':
      print(f'result final: {key, value}')
      sample_el_original = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()
      sample_el_data = json.loads(sample_el_original["data"])

      for sample in sample_el_data["samples"]:
        # sample_el_original_id = sample["id"]
        # sample_el_original_name = sample["name"]
        stocks_ids = sample["saved_stocks_ids"]
        # print(f'DEBUG {stocks_ids}, {sample_el_original_name}')
        # dict_stock_id_samle_name [stocks_ids[0]] = sample_el_original_name
        stock_id_list.extend(stocks_ids)

print(f'stock_id_list: {stock_id_list}\n')
# print(f'dictionary dict_stock_id_samle_name: {dict_stock_id_samle_name}')


dict_id_list_name_lot = {}

for stock_id in stock_id_list:
  list_name_lot = []
  stock_data = requests.get(f'{base()}/api/v1/stocks/{stock_id}', json={"token": token()}).json()
  print(f'----------------stock_id: {stock_id}')

  stock_lot = stock_data["lot"]
  stock_name = stock_data["name"]
  list_name_lot.append(stock_name)
  list_name_lot.append(stock_lot)
  print(f'list_name {list_name_lot}')
  dict_id_list_name_lot[stock_id] = list_name_lot
print(f'----------------dict_id_list_name_lot: {dict_id_list_name_lot}')














#-----------------------------------------------------------------------------------------------------------------------
-SP trigger and list of component lots-V1.x

import requests

experiment = variable("trigger_experiment")
experiment_id = experiment["id"]
experiment = requests.get(f'{base()}/api/v1/experiments/{experiment_id}', json={"token": token()}).json()

# ------------------GET SAMPLE NAME OF SECTION AND SAMPLE ID------------------------
experiment_procedure = experiment["experiment_procedures"]
sample_list = []
section_name_list = []
for Each_experiment_procedure in experiment_procedure:
  # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
  # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
  # print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

  for Each_section_type in Each_experiment_procedure:
    for Element_key in Each_experiment_procedure[Each_section_type]:
      for Each_section_type in Each_experiment_procedure:
        # print(f'Each_section_type: {Each_section_type}')
        if Each_experiment_procedure[Each_section_type][Element_key]:
          # if Element_key == 'elements' and Element_key == "Samples & Reagents":
          # print(f'DEBUG1 dans elements {Element_key}')
          if Element_key == 'elements':
            # print(f'DEBUG2 dans elements -----------------------------------')
            # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
            # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
            # print(f"Element_key: {Element_key}")
            for sample in Each_experiment_procedure[Each_section_type][Element_key]:
              if sample["element_type"] == "samples":
                section_nameANDsample_id = {}
                section_nameANDsample_id[Each_experiment_procedure['experiment_procedure']['name']] = sample['id']
                # section_nameANDsample_id_list.append(section_nameANDsample_id)

                # print(Each_experiment_procedure['experiment_procedure']['name'])
                # section_name_list.append(Each_experiment_procedure['experiment_procedure']['name'])
                section_name_list.append(section_nameANDsample_id)

                # print(f'DEBUG5 {section_name_list}')
                # print(f"DEBUG6-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")
                # sample_list.append(sample["id"])
                # print(f'sample_list: {sample_list}')

# ------------------GET STOCK ID FOR THE COMPONENT SECTION------------------------
stock_id_list = []
dict_stock_id_samle_name = {}
stock_id_2 = []

for result in section_name_list:
  for key, value in result.items():
    if key != 'Add sample to stock':
      print(f'result final: {key, value}')
      sample_el_original = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()
      sample_el_data = json.loads(sample_el_original["data"])

      for sample in sample_el_data["samples"]:
        # sample_el_original_id = sample["id"]
        # sample_el_original_name = sample["name"]
        stocks_ids = sample["saved_stocks_ids"]
        # print(f'DEBUG {stocks_ids}, {sample_el_original_name}')
        # dict_stock_id_samle_name [stocks_ids[0]] = sample_el_original_name
        stock_id_list.extend(stocks_ids)

    if key == 'Add sample to stock':
      print(f'result final: {key, value}')
      sample_el_original_2 = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()
      sample_el_data_2 = json.loads(sample_el_original_2["data"])
      for sample in sample_el_data_2["samples"]:
        stock_id_2 = sample["saved_stocks_ids"]

print(f'stock_id_list: {stock_id_list}\n')
# print(f'dictionary dict_stock_id_samle_name: {dict_stock_id_samle_name}')
print(f'stock_id_2: {stock_id_2}\n')

# ------------------CREATE A DICTIONARY {STOCK_ID[NAME,LOT]}------------------------

dict_id_list_name_lot = {}

for stock_id in stock_id_list:
  list_name_lot = []
  stock_data = requests.get(f'{base()}/api/v1/stocks/{stock_id}', json={"token": token()}).json()  # return aaa
  # stock_data = requests.get(f'{base()}/api/v1/stocks/1048', json={"token": token()}).json() # return AAA
  print(f'----------------stock_id: {stock_id}')

  stock_lot = stock_data["lot"]
  stock_name = stock_data["name"]
  list_name_lot.append((stock_name, stock_lot))
  print(f'list_name: {list_name_lot}')
  dict_id_list_name_lot[stock_id] = list_name_lot
print(f'----------------dict_id_list_name_lot: {dict_id_list_name_lot}')

# --------ADD {STOCK_ID[NAME,LOT]} TO LOT FIELD OF STOCK FOR PREPARED SOLUTION----------------

# Affiche le contenu de stock_2_data
stock_2_data = requests.get(f'{base()}/api/v1/stocks/1048', json={"token": token()}).json()
# print(f'stock_2_data: {stock_2_data}')

# @julien: ajouter le code qui permet d'aller écrire dans le champs stock le contenu de dic_id_list_name
# Reset sample element data, necessary for updating the sample element
# Reset sample element data, necessary for updating the sample element

# Les 2 blocs ci-dessous sont utilises pour remettre a 0 le lot, les memes seul l'url dans le request change:
# {base()}/storage/stocks/1048
# https://eu.labguru.com/storage/stocks/1048

response = requests.put(f'{base()}/storage/stocks/1048', json={'token': token(), 'item': {'lot': None}})
print(f'response: {response.status_code}')

# addition to check the content of stock data after the update - A supprimer une fois les tests complétés
stock_2_data = requests.get(f'{base()}/api/v1/stocks/1048', json={"token": token()}).json()
print(f'stock_id_2_lot after the first requests: {stock_2_data["lot"]}')

response = requests.put(f'https://eu.labguru.com/storage/stocks/1048', json={'token': token(), 'item': {'lot': None}})
print(f'response: {response.status_code}')
# addition to check the content of stock data after the update - A supprimer une fois les tests complétés
stock_2_data = requests.get(f'{base()}/api/v1/stocks/1048', json={"token": token()}).json()
print(f'stock_id_2_lot after the Second requests: {stock_2_data["lot"]}')

# change the lot:
response = requests.put(f'https://eu.labguru.com/storage/stocks/1048', json={'token': token(), 'item': {'lot': 'BBB'}})
print(f'response: {response.status_code}')
stock_2_data = requests.get(f'{base()}/api/v1/stocks/1048', json={"token": token()}).json()
print(f'stock_id_2_lot we changed the lot: {stock_2_data["lot"]}')

# --------stock expiry date is 2 weeks from today--------------------------------------
expiration_date = stock_2_data["expiration_date"]
print(f'stock_2_expiration: date{expiration_date}')
# @julien: ajouter le code qui permet d'aller écrire dans le champs expiration date la date du jour + 2 semaines

# addition to check the content of stock data after the update - A supprimer une fois les tests complétés
stock_2_data = requests.get(f'{base()}/api/v1/stocks/1048', json={"token": token()}).json()
stock_2_lot_after = stock_2_data["lot"]

print(f'stock_id_2_lot_after: {stock_2_lot_after}')
expiration_date_after = stock_2_data["expiration_date"]
print(f'stock_2_expiration_date_after: {expiration_date}')



#-----------------------------------------------------------------------------------------------------------------------


import requests
import json

experiment = variable("trigger_experiment")
experiment_id = experiment["id"]
experiment = requests.get(f'{base()}/api/v1/experiments/{experiment_id}', json={"token": token()}).json()

# ------------------GET SAMPLE NAME OF SECTION AND SAMPLE ID------------------------
experiment_procedure = experiment["experiment_procedures"]
sample_list = []
section_name_list = []
for Each_experiment_procedure in experiment_procedure:
  # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
  # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
  # print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

  for Each_section_type in Each_experiment_procedure:
    for Element_key in Each_experiment_procedure[Each_section_type]:
      for Each_section_type in Each_experiment_procedure:
        # print(f'Each_section_type: {Each_section_type}')
        if Each_experiment_procedure[Each_section_type][Element_key]:
          # if Element_key == 'elements' and Element_key == "Samples & Reagents":
          # print(f'DEBUG1 dans elements {Element_key}')
          if Element_key == 'elements':
            # print(f'DEBUG2 dans elements -----------------------------------')
            # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
            # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
            # print(f"Element_key: {Element_key}")
            for sample in Each_experiment_procedure[Each_section_type][Element_key]:
              if sample["element_type"] == "samples":
                section_nameANDsample_id = {}
                section_nameANDsample_id[Each_experiment_procedure['experiment_procedure']['name']] = sample['id']
                # section_nameANDsample_id_list.append(section_nameANDsample_id)

                # print(Each_experiment_procedure['experiment_procedure']['name'])
                # section_name_list.append(Each_experiment_procedure['experiment_procedure']['name'])
                section_name_list.append(section_nameANDsample_id)

                # print(f'DEBUG5 {section_name_list}')
                # print(f"DEBUG6-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")
                # sample_list.append(sample["id"])
                # print(f'sample_list: {sample_list}')

# ------------------GET STOCK ID FOR THE COMPONENT SECTION------------------------
stock_id_list = []
dict_stock_id_samle_name = {}
stock_id_2 = []

for result in section_name_list:
  for key, value in result.items():
    if key != 'Add sample to stock':
      print(f'result final: {key, value}')
      sample_el_original = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()
      sample_el_data = json.loads(sample_el_original["data"])

      for sample in sample_el_data["samples"]:
        # sample_el_original_id = sample["id"]
        # sample_el_original_name = sample["name"]
        stocks_ids = sample["saved_stocks_ids"]
        # print(f'DEBUG {stocks_ids}, {sample_el_original_name}')
        # dict_stock_id_samle_name [stocks_ids[0]] = sample_el_original_name
        stock_id_list.extend(stocks_ids)

    if key == 'Add sample to stock':
      print(f'result final: {key, value}')
      sample_el_original_2 = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()
      sample_el_data_2 = json.loads(sample_el_original_2["data"])
      for sample in sample_el_data_2["samples"]:
        stock_id_2 = sample["saved_stocks_ids"]

print(f'stock_id_list: {stock_id_list}\n')
# print(f'dictionary dict_stock_id_samle_name: {dict_stock_id_samle_name}')
print(f'stock_id_2: {stock_id_2}\n')

# ------------------CREATE A DICTIONARY {STOCK_ID[NAME,LOT]}------------------------

dict_id_list_name_lot = {}

for stock_id in stock_id_list:
  list_name_lot = []
  stock_data = requests.get(f'{base()}/api/v1/stocks/{stock_id}', json={"token": token()}).json()  # return aaa
  # stock_data = requests.get(f'{base()}/api/v1/stocks/1048', json={"token": token()}).json() # return AAA
  print(f'----------------stock_id: {stock_id}')

  stock_lot = stock_data["lot"]
  stock_name = stock_data["name"]
  list_name_lot.append((stock_name, stock_lot))
  print(f'list_name: {list_name_lot}')
  dict_id_list_name_lot[stock_id] = list_name_lot
print(f'----------------dict_id_list_name_lot: {dict_id_list_name_lot}')

# --------ADD {STOCK_ID[NAME,LOT]} TO LOT FIELD OF STOCK FOR PREPARED SOLUTION----------------

# Affiche le contenu de stock_2_data
stock_2_data = requests.get(f'{base()}/api/v1/stocks/1048', json={"token": token()}).json()
# print(f'stock_2_data: {stock_2_data}')

# @julien: ajouter le code qui permet d'aller écrire dans le champs stock le contenu de dic_id_list_name
# Reset sample element data, necessary for updating the sample element
# Reset sample element data, necessary for updating the sample element

# Les 2 blocs ci-dessous sont utilises pour remettre a 0 le lot, les memes seul l'url dans le request change:
# {base()}/storage/stocks/1048
# https://eu.labguru.com/storage/stocks/1048

response = requests.put(f'{base()}/storage/stocks/1048', json={'token': token(), 'item': {'lot': None}})
print(f'response: {response.status_code}')

# addition to check the content of stock data after the update - A supprimer une fois les tests complétés
stock_2_data = requests.get(f'{base()}/api/v1/stocks/1048', json={"token": token()}).json()
print(f'stock_id_2_lot after the first requests: {stock_2_data["lot"]}')

response = requests.put(f'https://eu.labguru.com/storage/stocks/1048', json={'token': token(), 'item': {'lot': None}})
print(f'response: {response.status_code}')
# addition to check the content of stock data after the update - A supprimer une fois les tests complétés
stock_2_data = requests.get(f'{base()}/api/v1/stocks/1048', json={"token": token()}).json()
print(f'stock_id_2_lot after the Second requests: {stock_2_data["lot"]}')

###################
# change the lot: #
###################

# Essais en vrac de differentes syntax -------------
# response = requests.get(
# f'{base()}/api/v1/sample_stocks/add_stock_by_barcode?token={token()}&element_id={sample_el_duplicated_id}&barcode={stock_id}', json={'token': token()})
response = requests.get(f'{base()}/api/v1/stocks/1048', json={'token': token()}).json()
# response = requests.get(f'https://eu.labguru.com/storage/stocks/1048', json={'token': token(), 'item': {'lot': 'BBB'}})


# Essai avec get -------------
payload = {'lot': 'BBB'}
response = requests.get(f'{base()}/api/v1/stocks/1048', json={'token': token()}, params=payload)  # fonctionne
# response = requests.get(f'{base()}/api/v1/stocks/1048', json={'token':token()}) # fonctionne
if response.ok:
  print(f'requests.get response.url: {response.url}')
  print(f'requests.get response.ok: {response.ok}')
  # print(f'response.texts requests.get: {response.text}')
events = response.json()
print(f"numero de lot avant la tentative de modification: {events['lot']}")

# Essai avec post -------------


# ################ Essai external code #############################################################
# payload = {'username': 'corey', 'password': 'testing'}
# r = requests.post('https://httpbin.org/post', data=payload)
# print(f'corey url: {r.url}')
# print(f'corey text: {r.text}')
# print(f'corey json: {r.json()}')

# r_dict = r.json()
# print(f"corey r_dict['form']: {r_dict['form']}")

# r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
# print(f'corey text: {r.text}')
# print(f'corey request result: {r}')
# print(f'corey request status: {r.ok}')
# ####################################################################################################
print("")
######################################################################################################
# Bout de code qui fonctionne pour ecrire le lot !!!!
print("Reset lot, necessary for updating the lot")
# Reset lot, necessary for updating the lot
response = requests.put(f'{base()}/api/v1/stocks/1048',
                        json={'token': token(), 'item': {'lot': None}})
response = requests.put(f'{base()}/api/v1/stocks/1048',
                        json={'token': token(), 'item': {'lot': '090909'}})
print(f'requests.put response.url: {response.url}')
print(f'requests.put response.ok: {response.ok}')
######################################################################################################

# Essai - 1
print("Resultat Essai - 1:")
payload = {"item": {'lot': 'BBB'}}
response = requests.post(f'{base()}/api/v1/stocks/1048', json={'token': token()}, data=payload)  # ne fonctionne pas
# response = requests.post(f'{base()}/api/v1/stocks/1048', json={'token':token()}, data=json.dumps(payload)) # ne fonctionne pas
# response = requests.post(f'{base()}/api/v1/stocks/1048?item:"lot"="BBB"', json={'token':token()}) # ne fonctionne pas

print(f'requests.post response.url: {response.url}')
print(f'requests.post response.ok: {response.ok}')
if response.ok:
  print(f'requests.post response.text: {response.text}')  # l'output format change completement et on obtient aucun text
  print(f'requests.post response.json: {reponse.json()}')  # fait planter
else:
  print("Essai-1 didn't work")

# control de la valeur du lot pour savoir si l'update a reussi
stock_2_data = requests.get(f'{base()}/api/v1/stocks/1048', json={"token": token()}).json()
print(f'stock_id_2_lot, have we changed the lot? if result is AAA we have not changed it: {stock_2_data["lot"]}')

print("Resultat Essai avec put fourni par Malka - 2:")
# Essai avec put fourni par Malka 1er juin-------------
response = requests.post(f'{base()}/api/v1/stocks/1048',
                         json={'token': token(), 'item': {'lot': '090909'}})  # ne fonctionne pas
if response.ok:
  print(
    f'Malka requests.post response.text: {response.text}')  # l'output format change completement et on obtient aucun text
  print(f'Malka requests.post response.json: {reponse.json()}')  # fait planter
else:
  print("Malka example didn't run")

# --------stock expiry date is 2 weeks from today--------------------------------------
expiration_date = stock_2_data["expiration_date"]
print(f'stock_2_expiration: date{expiration_date}')
# @julien: ajouter le code qui permet d'aller écrire dans le champs expiration date la date du jour + 2 semaines

# addition to check the content of stock data after the update - A supprimer une fois les tests complétés
stock_2_data = requests.get(f'{base()}/api/v1/stocks/1048', json={"token": token()}).json()
stock_2_lot_after = stock_2_data["lot"]

print(f'stock_id_2_lot_after: {stock_2_lot_after}')
expiration_date_after = stock_2_data["expiration_date"]
print(f'stock_2_expiration_date_after: {expiration_date}')




#-----------------------------------------------------------------------------------------------------------------------
# Julien-DuplicationTestWorkflow-V5.0-with 5s tempo

import requests
import time

duplicated_exp = variable("trigger_experiment")
original_exp_id = duplicated_exp["duplicate_of"]

time.sleep(5)

original_exp = requests.get(f'{base()}/api/v1/experiments/{original_exp_id}', json={"token": token()}).json()
duplicated_exp_id = duplicated_exp["id"]
duplicated_exp = requests.get(f'{base()}/api/v1/experiments/{duplicated_exp_id}', json={"token": token()}).json()

store_variable('duplicated_exp', duplicated_exp)
store_variable('original_exp', original_exp)

print(
  f'DEBUG ------------------duplicated_exp: {duplicated_exp["id"]} \n -------------original_exp_id: {original_exp_id}')
# print(f'DEBUG----------------duplicated_exp: {duplicated_exp}\n DEBUG------------- original_exp: {original_exp}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR ORIGINAL EXP-----------------\n')
experiment_procedure = original_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_original:{experiment_procedure}')

sample_list_original = []
for Each_experiment_procedure in experiment_procedure:
  # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
  for Each_section_type in Each_experiment_procedure:
    for Element_key in Each_experiment_procedure[Each_section_type]:
      # print(f'Element_key:{Element_key}')
      for Each_section_type in Each_experiment_procedure:
        if Each_experiment_procedure[Each_section_type][Element_key]:
          # if Element_key == 'elements' and Element_key == "Samples & Reagents":
          if Element_key == 'elements':
            # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
            # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
            # print(f"Element_key: {Element_key}")

            for sample in Each_experiment_procedure[Each_section_type][Element_key]:
              if sample["element_type"] == "samples":
                # print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                sample_list_original.append(sample["id"])

print(f'sample_list_original: {sample_list_original}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR DUPLICATED EXP-----------------\n')
experiment_procedure = duplicated_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_duplicated:{experiment_procedure}')

sample_list_duplicated = []
for Each_experiment_procedure in experiment_procedure:
  # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
  for Each_section_type in Each_experiment_procedure:
    for Element_key in Each_experiment_procedure[Each_section_type]:
      # print(f'Element_key:{Element_key}')
      for Each_section_type in Each_experiment_procedure:
        if Each_experiment_procedure[Each_section_type][Element_key]:
          # if Element_key == 'elements' and Element_key == "Samples & Reagents":
          if Element_key == 'elements':
            # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
            # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
            # print(f"Element_key: {Element_key}")

            for sample in Each_experiment_procedure[Each_section_type][Element_key]:
              if sample["element_type"] == "samples":
                print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                sample_list_duplicated.append(sample["id"])

print(f'sample_list_duplicated: {sample_list_duplicated}')

print(f'\n---------ITERATE THE POSITION IN THE SAMPLE LISTS, ASSIGN SAMPLE_ID AND SAMPLE_EL_DUPLICATED-------------\n')

for position in range(0, len(sample_list_original)):
  print(f'position: {position}')

  sample_el_original_id = sample_list_original[position]
  sample_el_duplicated_id = sample_list_duplicated[position]
  print(f'sample_el_original_id: {sample_el_original_id} and sample_el_duplicated_id: {sample_el_duplicated_id}')

  sample_el_original = requests.get(f'{base()}/api/v1/elements/{sample_el_original_id}', json={"token": token()}).json()

  # Les donnees retournees par requests sont au format string, ci-dessous nous les transformons pour etre au format json
  # puis on affiche les donnees.
  sample_el_data = json.loads(sample_el_original["data"])
  print(f'\nsample_el_original_id: {sample_el_original_id}\n')
  # print(f'sample_el_original:{sample_el_original}')

  stock_id_list = []
  for sample in sample_el_data["samples"]:
    sample_el_original_id = sample["id"]
    stocks_ids = sample["saved_stocks_ids"]
    stock_id_list.extend(stocks_ids)
    print(f'stock_id_list: {stock_id_list}\n')

  # Reset sample element data, necessary for updating the sample element
  print(f'sample_el_duplicated_id:{sample_el_duplicated_id}')
  response = requests.put(f'{base()}/api/v1/elements/{sample_el_duplicated_id}',
                          json={'token': token(), 'element': {'data': None}})
  print(f'Reset sample element data, return code:', response.status_code)

  # Add stocks to the duplicated experiment

  for stock_id in stock_id_list:
    print(f'stock_id: {stock_id}, Debug base: {base()} sample_el_duplicated_id: {sample_el_duplicated_id}')

    response = requests.get(
      f'{base()}/api/v1/sample_stocks/add_stock_by_barcode?token={token()}&element_id={sample_el_duplicated_id}&barcode={stock_id}',
      json={'token': token()})

    print(f'add stock {stock_id} to sample {sample_el_duplicated_id} return code:', response.status_code)

#-----------------------------------------------------------------------------------------------------------------------
# -SP trigger and list of component lots and expiration date-DevV3.0
import requests
import datetime
import calendar
from dateutil.relativedelta import relativedelta

experiment = variable("trigger_experiment")
experiment_id = experiment["id"]
experiment = requests.get(f'{base()}/api/v1/experiments/{experiment_id}', json={"token": token()}).json()

########################################
# Get the lot and display it in labguru#
########################################


# #-------- GET SAMPLE NAME OF SECTION AND SAMPLE ID------------------------
experiment_procedure = experiment["experiment_procedures"]
sample_list = []
section_name_list = []
for Each_experiment_procedure in experiment_procedure:
  # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
  # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
  # print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

  for Each_section_type in Each_experiment_procedure:
    for Element_key in Each_experiment_procedure[Each_section_type]:
      for Each_section_type in Each_experiment_procedure:
        # print(f'Each_section_type: {Each_section_type}')
        if Each_experiment_procedure[Each_section_type][Element_key]:
          # if Element_key == 'elements' and Element_key == "Samples & Reagents":
          # print(f'DEBUG1 dans elements {Element_key}')
          if Element_key == 'elements':
            # print(f'DEBUG2 dans elements -----------------------------------')
            # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
            # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
            # print(f"Element_key: {Element_key}")
            for sample in Each_experiment_procedure[Each_section_type][Element_key]:
              if sample["element_type"] == "samples":
                section_nameANDsample_id = {}
                section_nameANDsample_id[Each_experiment_procedure['experiment_procedure']['name']] = sample['id']
                # section_nameANDsample_id_list.append(section_nameANDsample_id)

                # print(Each_experiment_procedure['experiment_procedure']['name'])
                # section_name_list.append(Each_experiment_procedure['experiment_procedure']['name'])
                section_name_list.append(section_nameANDsample_id)

                # print(f'DEBUG5 {section_name_list}')
                # print(f"DEBUG6-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")
                # sample_list.append(sample["id"])
                # print(f'sample_list: {sample_list}')

# #-------- GET STOCK ID FOR THE COMPONENT SECTION------------------------
stock_id_list = []
dict_stock_id_samle_name = {}
stock_id_2 = []

for result in section_name_list:
  for key, value in result.items():
    if key != 'Add sample to stock':
      print(f'result final: {key, value}')
      sample_el_original = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()
      sample_el_data = json.loads(sample_el_original["data"])

      for sample in sample_el_data["samples"]:
        # sample_el_original_id = sample["id"]
        # sample_el_original_name = sample["name"]
        stocks_ids = sample["saved_stocks_ids"]
        # print(f'DEBUG {stocks_ids}, {sample_el_original_name}')
        # dict_stock_id_samle_name [stocks_ids[0]] = sample_el_original_name
        stock_id_list.extend(stocks_ids)

    if key == 'Add sample to stock':
      print(f'result final: {key, value}')
      sample_el_original_2 = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()
      sample_el_data_2 = json.loads(sample_el_original_2["data"])
      for sample in sample_el_data_2["samples"]:
        stock_id_2 = sample["saved_stocks_ids"]
        stock_id_2 = stock_id_2[0]

print(f'stock_id_list: {stock_id_list}\n')
# print(f'dictionary dict_stock_id_samle_name: {dict_stock_id_samle_name}')
print(f'stock_id_2: {stock_id_2}\n')

# #-------- CREATE A DICTIONARY {STOCK_ID[NAME,LOT]}------------------------
dict_id_list_name_lot = {}

for stock_id in stock_id_list:
  list_name_lot = []
  stock_data = requests.get(f'{base()}/api/v1/stocks/{stock_id}', json={"token": token()}).json()

  print(f'----------------stock_id: {stock_id}')

  stock_lot = stock_data["lot"]
  stock_name = stock_data["name"]
  list_name_lot.append((stock_name, stock_lot))
  print(f'list_name: {list_name_lot}')
  dict_id_list_name_lot[stock_id] = list_name_lot
print(f'----------------dict_id_list_name_lot: {dict_id_list_name_lot}')

# #--------  Update the lot in LabGuru: --------------------------------------
print("Reset lot, necessary for updating the lot")
# Reset lot, necessary for updating the lot
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'lot': None}})
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'lot': f'{dict_id_list_name_lot}'}})
print(f'requests.put response.url: {response.url}')
print(f'requests.put response.ok: {response.ok}')

# #--------  control de la valeur du lot pour savoir si l'update a reussi --------------------------------------
stock_2_data = requests.get(f'{base()}/api/v1/stocks/{stock_id_2}', json={"token": token()}).json()
print(f'stock_id_2_lot, have we changed the lot? if result is AAA we have not changed it: {stock_2_data["lot"]}')

##################################
# Expiry date: stored date+2weeks#
##################################


# #-------- Recuperation de la stored_date --------------------------------------
expiration_date = stock_2_data["expiration_date"]
print(f'stock_2_expiration date: {expiration_date}')
# print(f'stock_2_data{stock_2_data}')
Stored_on_date = stock_2_data["stored_on"]
print(f'Stored_on_date: {Stored_on_date}')

# Cut the date in year, month and day
# The cut of the date is necessary to use the object Stored_on_date
year, month, day = Stored_on_date.split("-")
Stored_on_date = datetime.datetime(int(year), int(month), int(day))
# print(Stored_on_date.year, Stored_on_date.month, Stored_on_date.day)

# Compute the expiration date
expiration_days = 14
expiration_month = 1
expdd = Stored_on_date + datetime.timedelta(days=expiration_days + 1)
print(f'expiration date: {expdd.strftime("%Y-%m-%d")}')

expdm = Stored_on_date + relativedelta(months=expiration_month)
print(f'After Month: {expdm.strftime("%Y-%m-%d")}')

# #-------- Display the expiration date in LabGuru --------------------------------------
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'expiration_date': None}})
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'expiration_date': f'{expdd}.strftime("%Y-%m-%d")'}})

# #-------- Debug and Control stuff --------------------------------------
# # addition to check the content of stock data after the update - A supprimer une fois les tests complétés
stock_2_data = requests.get(f'{base()}/api/v1/stocks/{stock_id_2}', json={"token": token()}).json()
# stock_2_lot_after=stock_2_data["lot"]

# print(f'stock_id_2_lot_after: {stock_2_lot_after}')


expiration_date_after = stock_2_data["expiration_date"]
print(f'stock_2_expiration_date_after: {expiration_date_after}')



#-----------------------------------------------------------------------------------------------------------------------
# 02-DevV3.1- Lots and expiration date on SP exp-Trigger on section
#-----------------------------------------------------------------------------------------------------------------------
'''
Simple condition for strings
Action          if variableA                    Condition           B
continue        {{trigger_experiment.title}}    contains            -SP

When stopped archive?When Stopped Archive
                    true

For example: {{attachment_1.extension}} equals [xlsx]
{{experiment_1.name}} contains proliferation
{{stock.type}} equals bottle 

Scripter
Scripter Version        Description     Lang        Code Template
current                 explanation     Python      none
'''
import requests
import datetime
import calendar
from dateutil.relativedelta import relativedelta

experiment = variable("trigger_experiment")
experiment_id = experiment["id"]
experiment = requests.get(f'{base()}/api/v1/experiments/{experiment_id}', json={"token": token()}).json()

########################################
# Get the lot and display it in labguru#
########################################


# #-------- GET SAMPLE NAME OF SECTION AND SAMPLE ID------------------------
experiment_procedure = experiment["experiment_procedures"]
sample_list = []
section_name_list = []
for Each_experiment_procedure in experiment_procedure:
    # print(f"DEBUG1-----------:{Each_experiment_procedure}\n")
    # print(f"DEBUG2-----------:{Each_experiment_procedure.keys()}\n")
    # print(f"DEBUG3-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")

    for Each_section_type in Each_experiment_procedure:
        for Element_key in Each_experiment_procedure[Each_section_type]:
            for Each_section_type in Each_experiment_procedure:
                # print(f'Each_section_type: {Each_section_type}')
                if Each_experiment_procedure[Each_section_type][Element_key]:
                    # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                    # print(f'DEBUG1 dans elements {Element_key}')
                    if Element_key == 'elements':
                        # print(f'DEBUG2 dans elements -----------------------------------')
                        # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                        # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                        # print(f"Element_key: {Element_key}")
                        for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                            if sample["element_type"] == "samples":
                                section_nameANDsample_id = {}
                                section_nameANDsample_id[Each_experiment_procedure['experiment_procedure']['name']] = \
                                sample['id']
                                # section_nameANDsample_id_list.append(section_nameANDsample_id)

                                # print(Each_experiment_procedure['experiment_procedure']['name'])
                                # section_name_list.append(Each_experiment_procedure['experiment_procedure']['name'])
                                section_name_list.append(section_nameANDsample_id)

                                # print(f'DEBUG5 {section_name_list}')
                                # print(f"DEBUG6-----------:{Each_experiment_procedure['experiment_procedure']['name']}\n")
                                # sample_list.append(sample["id"])
                                # print(f'sample_list: {sample_list}')

# #-------- GET STOCK ID FOR THE COMPONENT SECTION------------------------
stock_id_list = []
dict_stock_id_samle_name = {}
stock_id_2 = []

for result in section_name_list:
    for key, value in result.items():
        if key != 'Add sample to stock':
            print(f'result final: {key, value}')
            sample_el_original = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()
            sample_el_data = json.loads(sample_el_original["data"])

            for sample in sample_el_data["samples"]:
                # sample_el_original_id = sample["id"]
                # sample_el_original_name = sample["name"]
                stocks_ids = sample["saved_stocks_ids"]
                # print(f'DEBUG {stocks_ids}, {sample_el_original_name}')
                # dict_stock_id_samle_name [stocks_ids[0]] = sample_el_original_name
                stock_id_list.extend(stocks_ids)

        if key == 'Add sample to stock':
            print(f'result final: {key, value}')
            sample_el_original_2 = requests.get(f'{base()}/api/v1/elements/{value}', json={"token": token()}).json()
            sample_el_data_2 = json.loads(sample_el_original_2["data"])
            for sample in sample_el_data_2["samples"]:
                stock_id_2 = sample["saved_stocks_ids"]
                stock_id_2 = stock_id_2[0]

print(f'stock_id_list: {stock_id_list}\n')
# print(f'dictionary dict_stock_id_samle_name: {dict_stock_id_samle_name}')
print(f'stock_id_2: {stock_id_2}\n')

# #-------- CREATE A DICTIONARY {STOCK_ID[NAME,LOT]}------------------------
dict_id_list_name_lot = {}

for stock_id in stock_id_list:
    list_name_lot = []
    stock_data = requests.get(f'{base()}/api/v1/stocks/{stock_id}', json={"token": token()}).json()

    print(f'----------------stock_id: {stock_id}')

    stock_lot = stock_data["lot"]
    stock_name = stock_data["name"]
    list_name_lot.append((stock_name, stock_lot))
    print(f'list_name: {list_name_lot}')
    dict_id_list_name_lot[stock_id] = list_name_lot
print(f'----------------dict_id_list_name_lot: {dict_id_list_name_lot}')

# #--------  Update the lot in LabGuru: --------------------------------------
print("Reset lot, necessary for updating the lot")
# Reset lot, necessary for updating the lot
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'lot': None}})
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'lot': f'{dict_id_list_name_lot}'}})
print(f'requests.put response.url: {response.url}')
print(f'requests.put response.ok: {response.ok}')

# #--------  control de la valeur du lot pour savoir si l'update a reussi --------------------------------------
stock_2_data = requests.get(f'{base()}/api/v1/stocks/{stock_id_2}', json={"token": token()}).json()
print(f'stock_id_2_lot, have we changed the lot? if result is AAA we have not changed it: {stock_2_data["lot"]}')

##################################
# Expiry date: stored date+2weeks#
##################################


# #-------- Recuperation de la stored_date --------------------------------------
expiration_date = stock_2_data["expiration_date"]
print(f'stock_2_expiration date: {expiration_date}')
# print(f'stock_2_data{stock_2_data}')
Stored_on_date = stock_2_data["stored_on"]
print(f'Stored_on_date: {Stored_on_date}')

# Cut the date in year, month and day
# The cut of the date is necessary to use the object Stored_on_date
year, month, day = Stored_on_date.split("-")
Stored_on_date = datetime.datetime(int(year), int(month), int(day))
# print(Stored_on_date.year, Stored_on_date.month, Stored_on_date.day)

# Compute the expiration date
expiration_days = 14
expiration_month = 1
expdd = Stored_on_date + datetime.timedelta(days=expiration_days)
print(f'expiration date: {expdd.strftime("%Y-%m-%d")}')

expdm = Stored_on_date + relativedelta(months=expiration_month)
print(f'After Month: {expdm.strftime("%Y-%m-%d")}')

# #-------- Display the expiration date in LabGuru --------------------------------------
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'expiration_date': None}})
response = requests.put(f'{base()}/api/v1/stocks/{stock_id_2}',
                        json={'token': token(), 'item': {'expiration_date': f'{expdd}.strftime("%Y-%m-%d")'}})

# #-------- Debug and Control stuff --------------------------------------
# # addition to check the content of stock data after the update - A supprimer une fois les tests complétés
stock_2_data = requests.get(f'{base()}/api/v1/stocks/{stock_id_2}', json={"token": token()}).json()
# stock_2_lot_after=stock_2_data["lot"]

# print(f'stock_id_2_lot_after: {stock_2_lot_after}')


expiration_date_after = stock_2_data["expiration_date"]
print(f'stock_2_expiration_date_after: {expiration_date_after}')



#-----------------------------------------------------------------------------------------------------------------------
# 01-Dev02.1-ExperimentDuplication-Without timer
#-----------------------------------------------------------------------------------------------------------------------
'''
Simple condition for strings
Action          if variableA                    Condition       B
continue        {{trigger_experiment.title}}    contains        duplicate

When stopped archive?When Stopped Archive
                        true
                        
For example: {{attachment_1.extension}} equals [xlsx]
{{experiment_1.name}} contains proliferation
{{stock.type}} equals bottle 

Scripter
Scripter Version    Description     Lang        Code Template
    current         explanation     Python      none     
'''
import requests

duplicated_exp = variable("trigger_experiment")
original_exp_id = duplicated_exp["duplicate_of"]

original_exp = requests.get(f'{base()}/api/v1/experiments/{original_exp_id}', json={"token": token()}).json()
duplicated_exp_id = duplicated_exp["id"]
duplicated_exp = requests.get(f'{base()}/api/v1/experiments/{duplicated_exp_id}', json={"token": token()}).json()

store_variable('duplicated_exp', duplicated_exp)
store_variable('original_exp', original_exp)

print(
    f'DEBUG ------------------duplicated_exp: {duplicated_exp["id"]} \n -------------original_exp_id: {original_exp_id}')
# print(f'DEBUG----------------duplicated_exp: {duplicated_exp}\n DEBUG------------- original_exp: {original_exp}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR ORIGINAL EXP-----------------\n')
experiment_procedure = original_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_original:{experiment_procedure}')

sample_list_original = []
for Each_experiment_procedure in experiment_procedure:
    # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
    for Each_section_type in Each_experiment_procedure:
        for Element_key in Each_experiment_procedure[Each_section_type]:
            # print(f'Element_key:{Element_key}')
            for Each_section_type in Each_experiment_procedure:
                if Each_experiment_procedure[Each_section_type][Element_key]:
                    # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                    if Element_key == 'elements':
                        # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                        # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                        # print(f"Element_key: {Element_key}")

                        for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                            if sample["element_type"] == "samples":
                                # print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                                sample_list_original.append(sample["id"])

print(f'sample_list_original: {sample_list_original}')

print(f'\n---------------------GET LIST OF ELEMENT IDS FOR DUPLICATED EXP-----------------\n')
experiment_procedure = duplicated_exp["experiment_procedures"]
# print(f'DEBUG-----------------experiment_procedure_duplicated:{experiment_procedure}')

sample_list_duplicated = []
for Each_experiment_procedure in experiment_procedure:
    # print(f'DEBUG-----------:{Each_experiment_procedure}\n')
    for Each_section_type in Each_experiment_procedure:
        for Element_key in Each_experiment_procedure[Each_section_type]:
            # print(f'Element_key:{Element_key}')
            for Each_section_type in Each_experiment_procedure:
                if Each_experiment_procedure[Each_section_type][Element_key]:
                    # if Element_key == 'elements' and Element_key == "Samples & Reagents":
                    if Element_key == 'elements':
                        # print(f'Element_key:{Element_key} Element_value:{Each_experiment_procedure[Each_section_type][Element_key]}')
                        # print(f'Debug {Each_experiment_procedure[Each_section_type][Element_key][0]}')
                        # print(f"Element_key: {Element_key}")

                        for sample in Each_experiment_procedure[Each_section_type][Element_key]:
                            if sample["element_type"] == "samples":
                                print(f'sample_id: {sample["id"]} element_type: {sample["element_type"]}')
                                sample_list_duplicated.append(sample["id"])

print(f'sample_list_duplicated: {sample_list_duplicated}')

print(f'\n---------ITERATE THE POSITION IN THE SAMPLE LISTS, ASSIGN SAMPLE_ID AND SAMPLE_EL_DUPLICATED-------------\n')

for position in range(0, len(sample_list_original)):
    print(f'position: {position}')

    sample_el_original_id = sample_list_original[position]
    sample_el_duplicated_id = sample_list_duplicated[position]
    print(f'sample_el_original_id: {sample_el_original_id} and sample_el_duplicated_id: {sample_el_duplicated_id}')

    sample_el_original = requests.get(f'{base()}/api/v1/elements/{sample_el_original_id}',
                                      json={"token": token()}).json()

    # Les donnees retournees par requests sont au format string, ci-dessous nous les transformons pour etre au format json
    # puis on affiche les donnees.
    sample_el_data = json.loads(sample_el_original["data"])
    print(f'\nsample_el_original_id: {sample_el_original_id}\n')
    # print(f'sample_el_original:{sample_el_original}')

    stock_id_list = []
    for sample in sample_el_data["samples"]:
        sample_el_original_id = sample["id"]
        stocks_ids = sample["saved_stocks_ids"]
        stock_id_list.extend(stocks_ids)
        print(f'stock_id_list: {stock_id_list}\n')

    # Reset sample element data, necessary for updating the sample element
    print(f'sample_el_duplicated_id:{sample_el_duplicated_id}')
    response = requests.put(f'{base()}/api/v1/elements/{sample_el_duplicated_id}',
                            json={'token': token(), 'element': {'data': None}})
    print(f'Reset sample element data, return code:', response.status_code)

    # Add stocks to the duplicated experiment

    for stock_id in stock_id_list:
        print(f'stock_id: {stock_id}, Debug base: {base()} sample_el_duplicated_id: {sample_el_duplicated_id}')

        response = requests.get(
            f'{base()}/api/v1/sample_stocks/add_stock_by_barcode?token={token()}&element_id={sample_el_duplicated_id}&barcode={stock_id}',
            json={'token': token()})

        print(f'add stock {stock_id} to sample {sample_el_duplicated_id} return code:', response.status_code)

