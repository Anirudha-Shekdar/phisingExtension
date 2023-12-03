from flask import Flask ,jsonify,request
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route('/predict/url', methods=['GET'])
def get_data():
    data={
        "verdict":"predictin url",
        
    }
    return jsonify(data)


@app.route('/predict/dataURL', methods=['POST'])
def get_data_URL():
    data=request.form
    print(data)
    
    return('fom backend')
    

@app.route('/predict/email', methods=['GET'])
def get_data_email():
    data={
        "verdict_email":"predicting email"
    }
    return jsonify(data)


if __name__ =='__main__' :
    app.run(host='0.0.0.0', debug=True)