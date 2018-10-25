import os

base_dir = r'/media/kry/K/RAN/nucleos_agrarios/nucleos_agrarios'
user = 'postgres'
password = 'postgres'
data_base = 'db'
server = 'localhost'

file_list =[]
for (path, dirs, files) in (os.walk(base_dir)): 
    print(path)
    for data in files:
        if '_.dbf' in data: 
            path = os.listdir(base_dir)
            target_path = os.path.join(path, data)           
            file_list.append(target_path)

for path in file_list: 
        pg_loader_txt = open("/home/kry/Documents/dbfs/pg_loader.txt", "w") 
        lines_text = ['LOAD DBF', ' FROM {}'.format(path), 
                      ' INTO {}://{}@localhost/{}'.format(user, password, data_base), 
                      ' WITH truncate, create table;']
        pg_loader_txt.writelines(lines_text)
        pg_loader_txt.close() 
