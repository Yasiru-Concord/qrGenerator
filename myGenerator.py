from flask import Flask, request, send_file
import qrcode
from io import BytesIO

#digital business card qr generator

app = Flask(__name__)

@app.route('/generate_qr', methods=['GET'])
def generate_qr():
    # Retrieve the vCard data from the query string 
    vcard_data = request.args.get('data')
    
    if not vcard_data:
        return "Missing data", 400
    
    # Generate QR code
    img = qrcode.make(vcard_data)
    buf = BytesIO()
    img.save(buf, 'PNG')
    buf.seek(0)
    
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
