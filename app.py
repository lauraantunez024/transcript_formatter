from flask import Flask, request, jsonify
import re
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def format_transcript(text):
    """
    Process transcripts downloaded from premiere that include line numbers and timestamps 
    """

    formatted_text = []
    for line in text.splitlines():
        text_part = re.sub(r'^\d+\s+|\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\s*', '', line).strip()
        if text_part:
            formatted_text.append(text_part) 
    return ' '.join(formatted_text).strip()

@app.route('/format', methods=['POST'])
def format_text():
    """
    Receieves transcript text and outputs formatted text
    """
    data = request.json
    if 'transcript' not in data:
        return jsonify({'error': 'No transcript provided'}), 400
    
    transcript = data['transcript']
    formatted_transcript = format_transcript(transcript)
    return jsonify({'formatted_transcript': formatted_transcript})



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))



















