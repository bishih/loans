from flask import Flask, request
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:secretpassword@172.17.89.82:31004/operator_result"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

metrics = PrometheusMetrics(app)
by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'path': lambda: request.path}
)

class OperatorResult(db.Model):
    __tablename__ = 'opertorresult'
 
    num1 = db.Column(db.Integer())
    num2 = db.Column(db.Integer())
    operator = db.Column(db.String(1))
    result = db.Column(db.Integer())
    id=db.Column(db.Integer,primary_key=True)


    def __init__(self, num1, num2, operator, result):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
        self.result = result

    def __repr__(self):
        return f"<OperatorResult {self.name}>"

@app.route('/getTime')
@by_path_counter
def getTime():
   now = datetime.now()
   timestr = now.strftime("%A, %d %B, %Y at %X")
   
   return "the current date and time on server is :  " + timestr

@app.route('/doOperation',methods = ['POST'])
@by_path_counter
def doOperation():
   
   num1 = int(request.args.get('num1'))
   num2 = int(request.args.get('num2'))
   operator =request.args.get('operator')
   result = getResult(num1,num2,operator)

   operatorResult = OperatorResult(num1,num2,operator, result)
  
   db.session.add(operatorResult)
   db.session.commit()
   
   return "the result is : "  + str(result)

@metrics.do_not_track()
@app.route('/getAll',methods = ['GET'])
def getAllOperation():
   
   
   operatorResults=OperatorResult.query.all()
   results = [
            {
                "num1": operResult.num1,
                "num2": operResult.num2,
                "operator": operResult.operator,
                "result" : operResult.result,
                "id" : operResult.id

            } for operResult in operatorResults]

   return {"count": len(results), "operatorResults": results}

@app.route('/deleteOperation/<operator_id>',methods = ['DELETE'])
@by_path_counter
def deleteOperation(operator_id):

   OperatorResult.query.filter(OperatorResult.id == operator_id).delete()
   operatorResult=db.session.query(OperatorResult)
   db.session.commit()

   return "delete invoke"

def getResult(num1, num2, operator):

    if(operator == '-'):
     return int(num1)-int(num2)
    elif (operator == '*'):
        return num1*num2
    elif(operator == '/'):
        return num1/num2  
    elif(operator == '%'):
        return num1%num2 
    else:
        return num1+num2   

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=False, port=8083)