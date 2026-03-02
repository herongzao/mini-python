from flask import Flask, jsonify, send_from_directory
import os
import requests

app = Flask(__name__)

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/api/first-record')
def first_record():
    try:
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/mini?select=*&limit=1",
            headers={
                'apikey': SUPABASE_KEY,
                'Authorization': f'Bearer {SUPABASE_KEY}'
            }
        )
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
