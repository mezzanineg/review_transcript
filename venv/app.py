from flask import Flask, request, jsonify, send_from_directory, render_template
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

AUDIO_FOLDER = os.path.join('static', 'audio')
TEXT_FOLDER = os.path.join('static', 'transcripts')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcripts/<filename>')
def get_transcript(filename):
    try:
        return send_from_directory(TEXT_FOLDER, filename, as_attachment=True)
    except FileNotFoundError:
        return "File non trovato", 404

@app.route('/audio/<filename>')
def get_audio(filename):
    try:
        return send_from_directory(AUDIO_FOLDER, filename, as_attachment=True)
    except FileNotFoundError:
        return "File audio non trovato", 404
    
@app.route('/list-files')
def list_files():
    audio_files = [os.path.splitext(f)[0] for f in os.listdir(AUDIO_FOLDER) if f.endswith('.mp3')]
    transcript_files = [os.path.splitext(f)[0] for f in os.listdir(TEXT_FOLDER) if f.endswith('.txt')]

    # Intersezione dei nomi presenti in entrambe le cartelle
    common_files = list(set(audio_files) & set(transcript_files))

    return jsonify({"files": common_files})

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
