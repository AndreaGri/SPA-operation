from flask import Flask, jsonify , render_template, request
app=Flask(__name__)

#codice per restituire l'homepage

@app.route('/')
def homepage():
    return render_template('index.html')
#serevr API
@app.route('/calcola', Methods=['POST'])
def calcola():
    dati=request.get_json()





if __name__=='__main__':
    app.run(host='0.0.0.0', port=3245,debug=True)