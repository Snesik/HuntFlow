import requests
import mimetypes
import os
import unicodedata
from flags_start import flags
from models import *
from excel_data import excel_data


class TD():
    def __init__(self, flag):
        self.excel = {}
        self.data = {}
        self.key = flag.key
        self.session = self.creat_session()
        self.take_files(flag.path)
        self.take_vacansi()
        for i in self.data:
            self.add_man_vacansi(i)

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
            fio = response['fields']['name']
            name = f"{fio['last']} {fio['first']}"
            name = unicodedata.normalize('NFC', name)
            self.data[name] = response

    def take_vacansi(self):
        all_vacansis = self.session.get(Hf_urls.take_all_vacansis).json()['items']
        for va in all_vacansis:
            for post in self.excel['post']:
                if va['position'] == post:
                    self.excel['post'][post] = va['id']

    def creat_vacansi(self):
        # Создание вакансий
        for vakanci in self.excel['post']:
            data = creat_vakansi(vakanci, self.excel['post'][vakanci])
            self.excel['post'][vakanci] = self.session.post(Hf_urls.new_vacansi, data=data).json()['id']
        # Удаление вакансий
        for i in range(5, 60):
            self.session.delete(f'https://dev-100-api.huntflow.dev/account/2/vacancies/{i}')

    def add_man_vacansi(self, i):
        kandidat = creat_kandidat(self.data[i], self.excel[i])
        self.data[i]['id_id'] = self.session.post(Hf_urls.upload_bd, data=kandidat).json()['id']
        post = self.excel['post'][self.excel[i]['Должность']]
        data = add_to_vacansi(post, self.excel[i])
        self.session.post(add_man_in_vanaci(self.data[i]['id_id']), data=data).json()


if __name__ == '__main__':
    TD(flags())
