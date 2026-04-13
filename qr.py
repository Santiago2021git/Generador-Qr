import qrcode #Instalar libreria en consola pip install qrcode

url = "https://moto-tech.vercel.app/" #link o url para generar el codigo QR
qr = qrcode.QRCode(
    version=1,
    box_size=25,
    border=5
)

qr.add_data(url)
qr.make(fit=True)

imagen= qr.make_image()
imagen.save("Moto-Tech.jpg") # Nombre que llevara el codigo QR

