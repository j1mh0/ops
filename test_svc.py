import requests
import json
import common


svc_config_file = './svc_config.yaml'


def test_svc(url, data):
    # print(json.dumps(data))
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    # print(r.status_code)
    # print(r.content)
    resp = json.loads(r.content)
    if resp['response'] == data['response']:
        print(url, ' OK')
    else:
        print(url, ' ERROR')


def search_svc_config(config, name):
    for i in config:
        if i['name'] == name:
            return i['data']
    return None


def do_test_svc(service_name, server):
    svc_config = common.read_config(svc_config_file)
    data = search_svc_config(svc_config, service_name)

    if data == None:
        print('没有找到服务的配置')
        return

    test_svc(server, data)
