import qrcode

qr = qrcode.QRCode(
    version=15,
    box_size=5,
    border=5
)

data = "https://www.youtube.com/watch?v=I37kGX-nZEI"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")
