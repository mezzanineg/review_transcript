from flask import Flask, request, jsonify, send_file, render_template
import os
from urllib.parse import unquote

app = Flask(__name__)

AUDIO_FOLDER = os.path.join('static', 'audio')
TEXT_FOLDER = os.path.join('static', 'transcripts')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list-files')
def list_files():
    files = [f[:-4] for f in os.listdir(TEXT_FOLDER) if f.endswith('.txt')]
    return jsonify(files)

@app.route('/get-transcript/<path:filename>')
def get_transcript(filename):
    safe_filename = unquote(filename)
    file_path = os.path.join(TEXT_FOLDER, safe_filename + ".txt")
    if os.path.exists(file_path):
        try:
            return send_file(file_path, mimetype='text/plain')
        except Exception as e:
            return f"Errore nella lettura del file: {str(e)}", 500
    else:
        return "File non trovato", 404

@app.route('/save', methods=['POST'])
def save_transcript():
    data = request.get_json()
    filename = data.get("filename")
    text = data.get("text")

    if not filename or text is None:
        return jsonify({"error": "Dati mancanti"}), 400

    filepath = os.path.join(TEXT_FOLDER, f"{filename}.txt")
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
