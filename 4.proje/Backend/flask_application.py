# ---------- Bu dosya ucus_log.json içinden filtreleme yapacaktır. ----------
from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, 'ucus_log.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/ucus/<int:ucus_id>', methods=['GET'])
def get_ucus(ucus_id):
    try:
        data = load_data()
        ucus_rotasi = []
        
        for zaman_dilimi in data:
            for iha in zaman_dilimi.get("konumBilgileri", []):
                if iha.get("takim_numarasi") == ucus_id:
                    ucus_rotasi.append({
                        "enlem": iha["iha_enlem"],
                        "boylam": iha["iha_boylam"],
                        "irtifa": iha["iha_irtifa"]
                    })
        
        if ucus_rotasi:
            return jsonify({"id": ucus_id, "noktalar": ucus_rotasi}), 200
        else:
            return jsonify({"hata": "Uçuş (Takım) bulunamadı"}), 404
            
    except Exception as e:
        return jsonify({"hata": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)