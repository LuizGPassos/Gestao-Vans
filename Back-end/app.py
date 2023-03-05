from flask import Flask, request, jsonify
from flask_restx import Api, Resource, reqparse
import mysql.connector
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
api = Api(app,version='1.0', title='Api de gestão de vans')


app.config['CORS_HEADERS'] = 'application/json'



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="gestao_vans",
    port="3306"
    )

cursor = mydb.cursor()


@api.route('/')
class helloworld(Resource):
    def get(self):
        return "api"
        
@api.route('/tables/motoristas/<string:func>')
class motoristas(Resource):
    def get(self,func):
        
        if func == 'list':
            try:
                query = '''select * from motoristas'''
                cursor.execute(query)
            except:
                return 'error'
            else:
                result = cursor.fetchall()
                data = []
                for row in result:
                    content = {
                        'id' : row[0],
                        'placa' : row[1],
                        'modelo_van' : row[2],
                        'nome' : row[3],
                        'registro_prefeitura' : row[4],
                        'aptidao' : row[5]
                    }
                    data.append(content)
                    content = {}
                resp = jsonify({
                    'data' : data
                })
                resp.headers.add('Access-Control-Allow-Origin', '*')
                return resp
    

if __name__ == '__main__':
    app.run()
