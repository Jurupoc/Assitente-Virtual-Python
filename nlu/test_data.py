import yaml

data = yaml.safe_load(open('nlu//train.yml', 'r', encoding='utf-8').read())

for comands in data['comandos']:
    print(comands)
