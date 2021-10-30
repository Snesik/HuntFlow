import re
import os
import requests
import json
import pandas as pd
import itertools
import mimetypes


ss = 1



headers = {
    'User-Agent': 'App/1.0 test@huntflow.ru',

     'X-File-Parse': 'true',
    'Authorization': 'Bearer 71e89e8af02206575b3b4ae80bf35b6386fe3085af3d4085cbc7b43505084482'
}
content = open('/home/snesik/Тестовое задание/Frontend-разработчик/Глибин Виталий Николаевич.doc', 'rb')
name = 'resume1.pdf'
ext_data = os.path.splitext(name)

if len(ext_data) > 1:
    mime_type = mimetypes.types_map.get(ext_data[len(ext_data) - 1]) or 'application/zip'
else:
    mime_type = 'application/zip'
files = {"file": (name, content, mime_type)}
response = requests.post('https://dev-100-api.huntflow.dev/account/2/upload', headers=headers, files=files).json()
print()


a = 'https://dev-100-store.huntflow.dev/uploads/named/m/8/3/m838nih76fmhdo4q2jei49a5p6wio7rv.doc/%25D0%2593%25D0%25BB%25D0%25B8%25D0%25B1%25D0%25B8%25D0%25BD%2B%25D0%2592%25D0%25B8%25D1%2582%25D0%25B0%25D0%25BB%25D0%25B8%25D0%25B9%2B%25D0%259D%25D0%25B8%25D0%25BA%25D0%25BE%25D0%25BB%25D0%25B0%25D0%25B5%25D0%25B2%25D0%25B8%25D1%2587.doc?s=4Fj2soxTa1n4eowlYPGs0w&e=1635638178'


b = {'name': 'Глибин Виталий Николаевич.doc', 'content_type': 'application/msword', 'id': 2, 'url': 'https://dev-100-store.huntflow.dev/uploads/named/m/8/3/m838nih76fmhdo4q2jei49a5p6wio7rv.doc/%25D0%2593%25D0%25BB%25D0%25B8%25D0%25B1%25D0%25B8%25D0%25BD%2B%25D0%2592%25D0%25B8%25D1%2582%25D0%25B0%25D0%25BB%25D0%25B8%25D0%25B9%2B%25D0%259D%25D0%25B8%25D0%25BA%25D0%25BE%25D0%25BB%25D0%25B0%25D0%25B5%25D0%25B2%25D0%25B8%25D1%2587.doc?s=226hgrDZYaq8XmCQ8p-AKw&e=1635642327'}




headers = {
    'User-Agent': 'App/1.0 test@huntflow.ru',

    'Authorization': 'Bearer 71e89e8af02206575b3b4ae80bf35b6386fe3085af3d4085cbc7b43505084482'
}






# data = {
#     "position": "Frontend-разработчик2",
#
# }
#
#
#
# data = json.dumps(data)
#
#
# #g = requests.get('https://dev-100-api.huntflow.dev/accounts', headers=headers).json()
#
# #r = requests.get('https://dev-100-api.huntflow.dev/account/2/vacancies', headers=headers).json()
#
#
# r = requests.post('https://dev-100-api.huntflow.dev/account/2/vacancies',
#                    headers=headers, data=data).json()
# #8
# print()




"""
ЗАГРУЗКА КАНДИДАТА В БАЗУ
data = {
    "last_name": "Глибин2",
    "first_name": "Виталий",
    "middle_name": "Николаевич",
    "position": "Frontend-разработчик",
    "money": "100000 руб",
    "externals": [
        {

            "auth_type": "NATIVE",
            "files": [
                {
                    "id": 2
                }
            ],

        }
    ]
}




# data = json.dumps(data)
# g = requests.post('https://dev-100-api.huntflow.dev/account/2/applicants', headers=headers, data=data).json()
# print()
# id = 1005
"""












#files1 = '/home/snesik/Тестовое задание/Тестовая база.xlsx'
# s = pd.read_excel(files1)
#
# s = pd.DataFrame(s)
# a = {}
# for index, i in s.iterrows():
#     i[2] = re.sub(' ', '', str(i[2]))
#     i[2] = str(int(re.findall('\d+', str(i[2]))[0]))
#     a[index] = dict(i)
#


