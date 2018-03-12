#!/usr/bin/env python
# coding=utf-8


from getdb import GetDB
from confighttp import ConfigHttp
from configrunmode import ConfigRumMode


class Global:
    def __init__(self):
            #读取并配置接口服务器IP，端口等信息
        self.http = ConfigHttp('../http_config.ini')
            #读取并配置数据库服务器IP，端口等信息
        self.db =GetDB('../db_config.ini', 'DATABASE')
            # 读取运行模式配置
        self.run_mode_config = ConfigRumMode('../run_case_config.ini')

    def get_http(self):
        return self.http

        # 返回测试数据库连接
    def get_db_conn(self):
        return self.get_db_conn()

    def get_run_mode(self):
        return self.run_mode_config.get_run_mode()

    def get_run_case_list(self):
        return self.run_mode_config.get_run_case_list()

        # 释放资源
    def clear(self):
        # 关闭数据库连接
        self.db.get_conn().close()
