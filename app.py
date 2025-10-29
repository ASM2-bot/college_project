
from flask import Flask, jsonify
app=Flask(__name__)
@app.route('/')
def home():
    return jsonify({'message':'hello from Flask!'})
@app.route('/api/test')
def test():
    return jsonify({'status':'success','data':'API works!'})
if __name__ =='__main__':
    app.run(debug=True,port=5000)  



@app.route('/fillieres')
def filliere():
    return render_template('filliere.html')
@app.route('/abscence')
def abscences():
    return render_template('abscence.html')

@app.route('/Emploi du temps')
def Emploidutemps():
    return render_template('Emploi du temps.html')

@app.route('/Calendrier académique')
def Calendrieracadémique():
    return render_template('Calendrier académique.html')


    