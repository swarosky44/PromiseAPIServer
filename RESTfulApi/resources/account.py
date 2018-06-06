# encoding=UTF-8
from flask_restful import Resource, marshal_with
from RESTfulApi.handlers.account import WxLogin
from RESTfulApi.utils.parsers.account import login_parser
from RESTfulApi.utils.fields.account import account_fields


class Account(Resource):
    @marshal_with(account_fields)
    def post(self):
        login_args = login_parser.parse_args()
        wx_login = WxLogin(login_args)
        user = wx_login.mini_program_login()
        return user
