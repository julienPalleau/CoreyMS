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