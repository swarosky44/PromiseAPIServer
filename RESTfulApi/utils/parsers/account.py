# encoding=UTF-8
from flask_restful import reqparse


login_parser = reqparse.RequestParser()
login_parser.add_argument(
    'code', type=str,
    required=True, location="form",
    help="Not found code in request body"
)
