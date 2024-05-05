from flask import Flask, request

app = Flask (__name__)

@app.route('/buscarPalabra/<palabra>', methods=['get'])
def buscarPalabra(palabra):
     return 'Estas buscando la palabra ' + palabra

@app.route('/buscarPalabraConArgumentos/<palabra1>/<palabra2>', methods=['get'])
def buscarPalabraConArgumentos(palabra1, palabra2):
     opciones = request.view_args
     fraseExtra = ''
     if(opciones['palabra1']):
          fraseExtra = ' con el argumento palabra1 = ' + opciones['palabra1']
     return 'Estas buscando la palabra ' + palabra1 + fraseExtra

@app.route('/suma/<num1>/<num2>', methods=['get'])
def suma(num1, num2):
     args = request.view_args
     n1 = float(args['num1'])
     n2 = float(args['num2'])
     res = n1 + n2
     return str(res)

#Agrega otro endpoint get que sume opcion1 + la opción 2 y retorne "La suma de los argumentos es: {total}"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)