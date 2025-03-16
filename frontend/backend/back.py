from flask import Flask, request, jsonify

import os, json, shutil, sqlite3, datetime
from hashlib import sha256
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/home', methods=['POST'])
def deploy_function():
    return jsonify(succes=True, items=[[[221], [2], [5], [6], [245], [122] * 250],  [[56], [14], [24], [13], [45], [241] * 250]]), 200



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)


"""
// { - Как выглядят данные, которые отдаёт бэк
//   "success": true,
//   "items": {
//     "1": [1, 2, 3],  // Этаж 1
//     "2": [66, 42, 42, 24],  // Этаж 2
//     ...
//   }
// }
"""
"""
// { - Как выглядят данные, которые отдаёт бэк
//   "success": true,
//   "items": {
//     "1": [[false], [true], ...],  // Этаж 1
//     "2": [[true], [false], ...],  // Этаж 2
//     ...
//   }
// }
"""