import json

import cv2
from flask import Flask
from flask import request, send_file

from device_classifier import classify
from hotspot import find_hotspot
from irimage import find_irimage

app = Flask(__name__)


@app.route('/api/simple-image', methods=['GET', 'POST'])
def process_simple_image():
    if request.method == 'POST':
        r = request
        temp = request.files['uploadFile']
        temp.save('simple.jpg')

        # nparr = np.fromstring(r.data, np.uint8)
        #
        # # decode image
        # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        #
        # file = request.files['file']
        # extension = os.path.splitext(file.filename)[1]
        # f_name = str(uuid.uuid4()) + extension
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))

        return app.response_class(
            response=json.dumps({'data': classify('simple.jpg')}),
            status=200,
            mimetype='application/json'
        )


@app.route('/api/heat-hot-image', methods=['GET', 'POST'])
def process_heat_hot_image():
    if request.method == 'POST':
        # first type
        temp = request.files['uploadFile']
        temp.save('hot.jpg')
        out_image = find_hotspot('hot.jpg')
        cv2.imwrite('hot_out.jpg', out_image)
        return send_file('hot_out.jpg', mimetype='image/jpg')


@app.route('/api/heat-ir-image', methods=['GET', 'POST'])
def process_heat_ir_image():
    if request.method == 'POST':
        # second type
        temp = request.files['uploadFile']
        temp.save('ir.jpg')
        find_irimage('ir.jpg')
        return send_file('ir_out.jpg', mimetype='image/jpg')


def create_app():
    return app


if __name__ == '__main__':
    app.run()
