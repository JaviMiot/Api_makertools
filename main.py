import os
from app import create_app

PORT = os.environ.get('PORT', 5000)

app = create_app()

@app.route('/')
def index():
    return 'hola'

@app.route('/logout')
def logout():
    return 'Salida'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)