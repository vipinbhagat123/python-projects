import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=20, border =3,)
qr.add_data("https://www.linkedin.com/in/vipin-bhagat-b0433322b/")
qr.make(fit=True)
img=qr.make_image(fill_color="Black", back_color="white")
img.save("linkedinmy.png")