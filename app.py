from flask import Flask, request, make_response, jsonify

app = Flask (__name__)

@app.route('/calcularMonto/', methods=['post'])
def calcularMonto():
     payload = request.get_json()
     total = 0.0
     try:
          total = total + float(payload['monto1'])
          total = total + float(payload['monto2'])
          return make_response(jsonify({"resultado": total}), 200)
     except:
          return make_response(jsonify({"error": "Ocurrió un error inesperado con los parámetros enviados", "parámetros": payload}), 400)

@app.route('/calcularMontosVarios/', methods=['post'])
def calcularMontosVarios():
     payload = request.get_json()
     total = 0.0
     try:
          for monto in payload['montos']:
               total += float(monto)
          return make_response(jsonify({"resultado": total}), 200)
     except:
          return make_response(jsonify({"error": "Ocurrió un error inesperado con los parámetros enviados", "parámetros": payload}), 400)
     
@app.route('/concatenar/', methods=['post'])
def concatenar():
     payload = request.get_json()
     palabras = ''
     try:
          for palabra in payload['palabras']:
               palabras += palabra + ' '
          return make_response(jsonify({"palabras concatenadas": palabras}),200)
     except:
          return make_response(jsonify({"error": "Ocurrió un error inesperado con los parámetros enviados", "parámetros": payload}), 400)


#Agrega otro endpoint post que concatene una serie de palabras y lo regrese en el parámetro resultado: {palabras concatenadas}"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)