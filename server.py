from flask import Flask, send_from_directory, request, jsonify
import base64, io
from PIL import Image
import numpy as np
from geometrize.bitmap import Bitmap
from geometrize.core import Geometrizer

app = Flask(__name__, static_folder='frontend/bin')

@app.route('/')
def index():
    return send_from_directory('frontend/bin', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('frontend/bin', path)

@app.route('/api/geometrize', methods=['POST'])
def api():
    data = request.json
    img_data = base64.b64decode(data['image'].split(',')[1])
    img = Image.open(io.BytesIO(img_data)).convert('RGB')
    bmp = Bitmap(img)
    geom = Geometrizer(bmp,
                       shape_type=data.get('shapeType','triangle'),
                       alpha=data.get('alpha',0.5),
                       trials=data.get('trials',50))
    result = geom.run(data.get('iterations',100))
    img_out = Image.fromarray(np.uint8(result.clip(0,255)))
    buf = io.BytesIO()
    img_out.save(buf, format='PNG')
    enc = base64.b64encode(buf.getvalue()).decode()
    return jsonify({'result':'data:image/png;base64,'+enc})

if __name__=='__main__':
    app.run(debug=True)
