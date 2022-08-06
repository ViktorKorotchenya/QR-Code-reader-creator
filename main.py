import cv2
import qrcode

# get link from qrcode
img = cv2.imread('img.png')
detect = cv2.QRCodeDetector()
res, _, _ = detect.detectAndDecode(img)
print(res)

# make qrcode from link
new_code = qrcode.make(res)
new_code.save('new_code.png')