import pandas as pd
import re

def excel_data(path):
    s = pd.read_excel(path)

    s = pd.DataFrame(s)
    data = {}
    data['post'] = {}
    for index, i in s.iterrows():
        i[2] = re.sub(' ', '', str(i[2]))
        i[2] = str(int(re.findall('\d+', str(i[2]))[0]))
        name = i['ФИО'].strip()
        post = i['Должность']
        if i['Должность'] in data['post']:
            data['post'][post] = data['post'][post] + 1
        else:
            data['post'][post] = 1

        data[name] = dict(i)

    return data