from flask import Flask, jsonify
from flask_restful import Resource, Api
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
#import json
import obpdata

app = Flask(__name__)  # Flask app instance initiated
api = Api(app)  # Flask restful wraps Flask app around it.
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='current account Api',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)


class LoanDataResponseSchema(Schema):
    account_id = fields.String()
    amount = fields.Float()
    bank_id = fields.String()
    end_date = fields.String()
    loan_name = fields.String()
    monthly_repayment = fields.Number()
    num_of_payments = fields.Number()
    start_date = fields.String()
    usury = fields.Number()

class ExpensesResponseSchema(Schema):
        name = fields.String()
        amount = fields.Float()
        categoryId = fields.Number()

class BalanceDataSchema(Schema):
    bank_id = fields.String()
    account_id = fields.String()
    balance = fields.Float()
    expenses = fields.Nested(ExpensesResponseSchema, many=True)





data = [{"bank_id": "Latlux", "account_id": "5430670", "start_date": "13/01/2021", "end_date": "13/09/2021", "loan_name":"Photojam", "ammount": "3640", "num_of_payments": 8, "monthly_repayment": 455, "usury": 2}, {"bank_id": "Pannier", "account_id": "51-8010051", "start_date": "11/01/2020", "end_date": "11/8/2020", "loan_name": "Skalith", "ammount": 4725, "num_of_payments": 7, "monthly_repayment": 675, "usury": 4}, {"bank_id": "Tampflex", "account_id": "20-5375546", "start_date": "08/7/2020", "end_date": "08/07/2022", "loan_name": "Bluezoom", "ammount": 6384, "num_of_payments": 24, "monthly_repayment": 266, "usury": 1}, {"bank_id": "Tres-Zap", "account_id": "04-3114529", "start_date": "15/04/2020", "end_date": "15/08/2020", "loan_name": "Yodel", "ammount": 6168, "num_of_payments": 4, "monthly_repayment": 1542, "usury": 3}, {"bank_id": "Greenlam", "account_id": "58-6993977", "start_date": "15/06/2020", "end_date": "15/09/2021", "loan_name": "Quire", "ammount": 9150, "num_of_payments": 15, "monthly_repayment": 610, "usury": 8}, {"bank_id": "It", "account_id": "09-6877184", "start_date": "21/01/2020", "end_date": "21/03/2020", "loan_name": "Npath", "ammount": 3164, "num_of_payments":2,"monthly_repayment":1582,"usury":5},{"bank_id":"Latlux","account_id":"37-1906857","start_date":"26/03/2020","end_date":"26/11/2021","loan_name":"Devify","ammount":7000,"num_of_payments":20,"monthly_repayment":350,"usury":1},{"bank_id":"Home Ing","account_id":"59-7476513","start_date":"31/03/2021","end_date":"31/07/2021","loan_name":"Ozu","ammount":560,"num_of_payments":4,"monthly_repayment":140,"usury":2},{"bank_id":"Job","account_id":"97-0957797","start_date":"24/04/2021","end_date":"24/11/2021","loan_name":"Mydeo","ammount":7000,"num_of_payments":7,"monthly_repayment":1000,"usury":10}]



@app.route("/")
def home():
    return "shoval"


# @app.route("/loans/bank/<string:bank_id>/account/<string:account_id>")
# def get_loans(bank_id, account_id):
#     loans = []
#     for loan in data:
#         print(loan)
#         if loan["account_id"] == account_id and loan["bank_id"] == bank_id:
#             loans.append("{}: {}".format(loan["loan_name"], loan["ammount"]))
#     if len(loans) == 0:
#         return "There is no loans for this account & bank"
#     return_string = ""
#     for l in loans:
#         print(type(l))
#         return_string += "{}{}".format(l, "\n")
#     return return_string


class LoansEP(MethodResource, Resource):
    @doc(description='User loans data', tags=['Loans'])
    @marshal_with(LoanDataResponseSchema)  # marshalling
    def get(self,bank_id,account_id):
        loans = []
        for loan in data:
            print(loan)
            if loan["account_id"] == account_id and loan["bank_id"] == bank_id:
               # loans.append("{}: {}".format(loan["loan_name"], loan["ammount"]))
               loans.append(loan)
        if len(loans) == 0:
            return "There is no loans for this account & bank"
        return_value = ""
        for l in loans:
            print(l)
            #return_string += "{}{}".format(l, "\n")
            return_value = jsonify(l)
            print(return_value)
        return return_value


# @app.route("/balances/bank/<string:bank_id>/account/<string:account_id>")
# def get_balances(bank_id, account_id):
#     b_data = obpdata.get_obp_balances(bank_id, account_id)
#     return b_data

class BalancesEP (MethodResource, Resource):
    @doc(description='User balance and expenses data', tags=['balances'])
    @marshal_with(BalanceDataSchema)  # marshalling
    def get(self, bank_id, account_id):
        b_data = obpdata.get_obp_balances(bank_id, account_id)
        return jsonify(b_data)


api.add_resource(LoansEP, '/loans/bank/<string:bank_id>/account/<string:account_id>')
api.add_resource(BalancesEP, '/balances/bank/<string:bank_id>/account/<string:account_id>')
docs.register(LoansEP)
docs.register(BalancesEP)

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True, port=8080)
