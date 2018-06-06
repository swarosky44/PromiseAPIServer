# encoding=UTF-8
import requests
from flask import current_app


class WxLogin(object):
    def __init__(self, args):
        self.app_id = current_app.config.get("APP_ID")
        self.app_secret = current_app.config.get("APP_SECRET")
        self.code = args.get("code")

    def mini_program_login(self):
        print("app_id: {app_id}; app_secret: {app_secret}; code: {code}".format(
            app_id=self.app_id, app_secret=self.app_secret, code=self.code
        ))
        pass
