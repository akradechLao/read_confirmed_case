def read_data(file_name):
    with open(file_name, mode='r', encoding='utf-8-sig') as f:
        data = f.readlines()
    return data 

data = read_data('C:\Users\AkradechNTC\Downloads\confirmed-cases-since-120864.csv')
keys = data.pop(0).strip().split(',')
    
print(keys)
print(values)





