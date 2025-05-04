import qrcode

# Your link
link = "deeptech-three.vercel.app"

# Create QR code
qr = qrcode.make(link)

# Save as image
qr.save("my_qr.png")
