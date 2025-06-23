from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/crear-cancion', methods=['POST'])
def crear_cancion():
    data = request.get_json()

    prompt = data.get('prompt')
    genero = data.get('genre')

    if not prompt or not genero:
        return jsonify({'error': 'Faltan datos: prompt o genre'}), 400

    # Simular generación de canción
    url_falsa = f"https://mis-canciones.com/{prompt.replace(' ', '-')}-{genero}.mp3"

    return jsonify({
        'estado': 'generado',
        'url': url_falsa
    })

if __name__ == '__main__':
    app.run(debug=True)
