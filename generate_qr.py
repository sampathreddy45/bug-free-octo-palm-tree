import qrcode

data = input("Enter the text or URL to encode: ")
img = qrcode.make(data)
img.save("myqr.png")
print("QR code saved as myqr.png")
