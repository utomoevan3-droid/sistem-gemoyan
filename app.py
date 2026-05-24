from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Agar HP bisa "ngobrol" dengan laptop

# Data statistik simulasi
@app.route('/api/stats', methods=['GET'])
def get_stats():
    # Ini angka yang akan muncul di dashboard HP kamu
    return jsonify({"stok_drive": 28})

# Endpoint untuk menerima perintah dari tombol di HP
@app.route('/run-automation', methods=['POST'])
def run_automation():
    data = request.json
    print(f"Menerima perintah dari HP: {data}")
    # Nanti di sini kita isi logika otomatisasinya
    return jsonify({"status": "success", "message": "Perintah diterima laptop!"})

if __name__ == '__main__':
    # host='0.0.0.0' agar bisa diakses dari HP
    app.run(host='0.0.0.0', port=5000)