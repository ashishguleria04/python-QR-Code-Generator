import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50,border=1)

qr.add_data("<your link/text/anything you want to convert into qr code here>")

qr.make(fit=True)

img = qr.make_image(fill_color = "Black" , back_color="White")

img.save("advanced.png")
