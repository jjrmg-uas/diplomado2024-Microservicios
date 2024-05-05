from flask import Flask

app = Flask (__name__)

@app.route('/helloWorld', methods=['get'])
def hello_world():
     return '¡Hola, mundo!'

#Agrega otro endpoint y retorna el texto que gustes!
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)