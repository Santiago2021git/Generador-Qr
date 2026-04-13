import qrcode #Instalar libreria en consola pip install qrcode

url = "" #link o url para generar el codigo QR
qr = qrcode.QRCode(
    version=1,
    box_size=25,
    border=5
)

qr.add_data(url)
qr.make(fit=True)

imagen= qr.make_image()
imagen.save("") # Nombre que llevara el codigo QR

