from flask import Flask, jsonify, render_template

import pymongo

DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('pyecharts.html')


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/consumption', methods=['GET'])
def cons():


    # define the client, the database, and the collection
    # the database and the collection are created at first insert
    # if needed
    client = pymongo.MongoClient('localhost', 27017)
    mydb = client["test2"]
    sinfun = mydb["sin2"]



    # Enable Access-Control-Allow-Origin


    output = []
    for c in sinfun.find():
        output.append({'ADCO': c['ADCO'], 'OPTARIF': c['OPTARIF'], 'ISOUSC': c['ISOUSC'], 'BASE': c['BASE'],
                       'PTEC': c['PTEC'], 'INST': c['INST'], 'MAX': c['MAX'], 'PAPP': c['PAPP'],
                       'HHPHC': c['HHPHC'], 'MOTDETAT': c['MOTDETAT']})
    response = jsonify({'result': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run()
