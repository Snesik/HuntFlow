import json


class Hf_urls:
    base_url = 'https://dev-100-api.huntflow.dev'
    me = base_url + '/me'
    upload = base_url + '/account/2/upload'
    upload_bd = base_url + '/account/2/applicants'
    new_vacansi = base_url + '/account/2/vacancies'
    take_all_vacansis = base_url + '/account/2/vacancies'

def add_man_in_vanaci(id_vacansi):
    return f'{Hf_urls.base_url}/account/2/applicants/{id_vacansi}/vacancy'


def headers_base(key):
    base = {
        'User-Agent': 'App/1.0 test@huntflow.ru',
        'Authorization': f'Bearer {key}'
    }
    return base


def headers_upload(key):
    base = {
        'User-Agent': 'App/1.0 test@huntflow.ru',
        'X-File-Parse': 'true',
        'Authorization': f'Bearer {key}'

    }
    return base


def creat_kandidat(kondidat, excel):
    text = kondidat['text'].splitlines()
    text = list(dict.fromkeys(text))
    kondidat['text'] = '\n\n'.join(text)

    data = {
        "last_name": kondidat['fields']['name']['last'],
        "first_name": kondidat['fields']['name']['first'],
        "middle_name": kondidat['fields']['name']['middle'],
        "phone": kondidat['fields']['phones'][0],
        "email": kondidat['fields']['email'],
        "position": kondidat['fields']['position'],
        "money": excel['Ожидания по ЗП'],
        "company": kondidat['fields']['experience'][0]['position'],
        "photo": kondidat['photo']['id'],
        "externals": [
            {
                "data": {
                    "body": f"{kondidat['text']}"
                },
                "auth_type": "NATIVE",
                "files": [
                    {
                        "id": kondidat['id']
                    }
                ],

            }
        ]
    }
    if kondidat['fields']['birthdate'] != None:
        data["birthday_day"] = kondidat['fields']['birthdate']['day']
        data["birthday_month"] = kondidat['fields']['birthdate']['month']
        data["birthday_year"] = kondidat['fields']['birthdate']['year']

    return json.dumps(data)


def creat_vakansi(vakansi, how_match):
    data = {"position": vakansi,
            "fill_quotas": [
                {

                    "applicants_to_hire": how_match,
                }
            ]
            }

    return json.dumps(data)


def add_to_vacansi(post_id, excel):
    data = {
        "vacancy": post_id,
        "status": status[excel['Статус']],
        "comment": excel['Комментарий'],
    }
    return json.dumps(data)


status = {
    'Новые': 1,
    'Отправлено письмо': 2,
    'Оценка заказчиком': 3,
    'Интервью с HR': 4,
    'Интервью с заказчиком': 5,
    'Принятие решения': 6,
    'Выставлен оффер': 7,
    'Оффер принят': 8,
    'Исп. срок пройден': 9,
    'Отказ': 10
}
