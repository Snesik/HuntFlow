import requests
import mimetypes
from flags_start import flags
from models import *
from excel_data import excel_data
import os
import unicodedata


class TD():
    def __init__(self, flag):
        self.excel = {}
        self.data = {}
        self.key = flag.key
        self.session = self.creat_session()
        self.take_files(flag.path)
        self.creat_vacansi()
        for i in self.data:
            a = creat_kandidat(self.data[i], self.excel[i])
            """Загружаем в базу, полуачем id"""
            self.data[i]['id_id'] = self.session.post(Hf_urls.upload_bd, data=a).json()['id']
            """Создаем вакансию если нету"""
            post = self.excel['post'][self.excel[i]['Должность']]
            data = add_to_vacansi(post, self.excel[i])
            self.session.post(add_man_in_vanaci(self.data[i]['id_id']), data=data).json()



    def take_files(self, path):
        paths_data = {}
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.xlsx'):
                    self.excel = excel_data(root + '/' + file)

                if file.endswith('.pdf') or file.endswith('.doc'):
                    paths_data[root.split('/')[-1]] = [root + '/' + i for i in files]
                    break

        for i in paths_data:
            for one in paths_data[i]:
                self.creat_data_upload(one)

    def creat_session(self):
        session = requests.session()
        session.headers.update(headers_base(self.key))
        return session

    def creat_data_upload(self, path):
        with open(path, 'rb') as content:
            self.session.headers.update(headers_upload(self.key))
            ext_data = os.path.splitext(path)
            if len(ext_data) > 1:
                mime_type = mimetypes.types_map.get(ext_data[len(ext_data) - 1]) or 'application/zip'
            else:
                mime_type = 'application/zip'
            name = 'file'
            data = {"file": (name, content, mime_type)}
            response = requests.post(Hf_urls.upload, headers=headers_upload(self.key), files=data).json()
            name = os.path.splitext(response['name'])[0]
            name = unicodedata.normalize('NFC', name)
            self.data[name] = response

    def creat_vacansi(self):
        for vakanci in self.excel['post']:
            data = creat_vakansi(vakanci, self.excel['post'][vakanci])
            self.excel['post'][vakanci] = self.session.post(Hf_urls.new_vacansi, data=data).json()['id']


if __name__ == '__main__':
    TD(flags())
