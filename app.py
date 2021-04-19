from flask import Flask
from flask_restful import Resource, Api
import json
import obpdata

data = [{"bank_id": "Latlux", "account_id": "5430670", "start_date": "13/01/2021", "end_date": "13/09/2021", "loan_name":"Photojam", "ammount": "3640", "num_of_payments": 8, "monthly_repayment": 455, "usury": 2}, {"bank_id": "Pannier", "account_id": "51-8010051", "start_date": "11/01/2020", "end_date": "11/8/2020", "loan_name": "Skalith", "ammount": 4725, "num_of_payments": 7, "monthly_repayment": 675, "usury": 4}, {"bank_id": "Tampflex", "account_id": "20-5375546", "start_date": "08/7/2020", "end_date": "08/07/2022", "loan_name": "Bluezoom", "ammount": 6384, "num_of_payments": 24, "monthly_repayment": 266, "usury": 1}, {"bank_id": "Tres-Zap", "account_id": "04-3114529", "start_date": "15/04/2020", "end_date": "15/08/2020", "loan_name": "Yodel", "ammount": 6168, "num_of_payments": 4, "monthly_repayment": 1542, "usury": 3}, {"bank_id": "Greenlam", "account_id": "58-6993977", "start_date": "15/06/2020", "end_date": "15/09/2021", "loan_name": "Quire", "ammount": 9150, "num_of_payments": 15, "monthly_repayment": 610, "usury": 8}, {"bank_id": "It", "account_id": "09-6877184", "start_date": "21/01/2020", "end_date": "21/03/2020", "loan_name": "Npath", "ammount": 3164, "num_of_payments":2,"monthly_repayment":1582,"usury":5},{"bank_id":"Latlux","account_id":"37-1906857","start_date":"26/03/2020","end_date":"26/11/2021","loan_name":"Devify","ammount":7000,"num_of_payments":20,"monthly_repayment":350,"usury":1},{"bank_id":"Home Ing","account_id":"59-7476513","start_date":"31/03/2021","end_date":"31/07/2021","loan_name":"Ozu","ammount":560,"num_of_payments":4,"monthly_repayment":140,"usury":2},{"bank_id":"Job","account_id":"97-0957797","start_date":"24/04/2021","end_date":"24/11/2021","loan_name":"Mydeo","ammount":7000,"num_of_payments":7,"monthly_repayment":1000,"usury":10}]

app = Flask(__name__)
api = Api(app)


@app.route("/")
def home():
    return "shoval"


@app.route("/loans/bank/<string:bank_id>/account/<string:account_id>")
def get_loans(bank_id, account_id):
    loans = []
    for loan in data:
        print(loan)
        if loan["account_id"] == account_id and loan["bank_id"] == bank_id:
            loans.append("{}: {}".format(loan["loan_name"], loan["ammount"]))
    if len(loans) == 0:
        return "There is no loans for this account & bank"
    return_string = ""
    for l in loans:
        print(type(l))
        return_string += "{}{}".format(l, "\n")
    return return_string


@app.route("/balances/bank/<string:bank_id>/account/<string:account_id>")
def get_balances(bank_id, account_id):
    b_data = obpdata.get_obp_balances(bank_id, account_id)
    return b_data


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True, port=8080)
