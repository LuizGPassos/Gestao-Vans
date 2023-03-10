from flask import Flask, request, jsonify
from flask_restx import Api, Resource, reqparse
import mysql.connector
from flask_cors import CORS, cross_origin
from sets import request_handler

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
            
@api.route('/tables/motoristas-cadastro/<string:func>')
class motoristas(Resource):
    def post(self,func):
        
        if func == 'save':

           if request.method == 'POST': 

                id = request.form.get('id', None)
                placa = request.form.get('placa', None)
                modelo_van = request.form.get('modelo_van', None)
                nome = request.form.get('nome', None)
                registro_prefeitura = request.form.get('registro_prefeitura', None)
                aptidao = request.form.get('aptidao', None)

                print(id)

                try:
                    query = '''insert into motoristas values (
                    :1,
                    :2,
                    :3,
                    :4,
                    :5,
                    :6
                    )'''
                    cursor.execute(query, [id,placa,modelo_van,nome,registro_prefeitura,aptidao])
                except:
                    return 'error'
                else:
                    mydb.commit()
                    return 'sucesso'
    

if __name__ == '__main__':
    app.run()
