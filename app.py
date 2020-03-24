from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/wa", methods=['POST'])
def sms_reply():

    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    op = ['Selamat datang di toko Agung widhiatmojo', 'order: Cara Order Barang', 'list: List Produk Barang', 'askme: Tanya Status Pemilik Toko','','Ketik order , list , atau askme  kami bisa menjawab pertanyaan mu. ']
    listp = ['1. Makanan', '2. Minuman', '3. Baju', '4. dll', 'silakan kunjungi agungw.net untuk barang yang lain ']
    if 'order' in incoming_msg:
        msg.body('tinggal order aja.')
        responded = True
    if 'list' in incoming_msg:
        msg.body("\n".join(listp))
        responded = True
    if 'askme' in incoming_msg:
        msg.body(':)')
        responded = True
    if 'pacar' in incoming_msg:
        msg.body('Belum')
        responded = True
    if 'ngapain' in incoming_msg:
        msg.body('Lagi WHF sambil iseng bikin bot wa')
        responded = True
    if not responded:
        msg.body("\n".join(op))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
