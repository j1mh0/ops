import common
import test_svc

task_name = 'test'
task_config_file = './task_config.yaml'


def search_task_config(config, name):
    for i in config:
        if i['name'] == name:
            return i['servers']
        return None


def search_service_name(task_name):
    # 此处做了简化，假设任务名和服务名是一样的
    return task_name


def do_task(service_name):
    task_config = common.read_config(task_config_file)

    servers = search_task_config(task_config, service_name)
    if servers == None:
        print('没有找到任务的配置')
        return

    service_name = search_service_name(task_name)

    for server in servers:
        test_svc.do_test_svc(service_name, server)


do_task(task_name)
