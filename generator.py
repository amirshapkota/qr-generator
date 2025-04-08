import qrcode

def generate_qr_code(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,  # Size 
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True) 

    img = qr.make_image(fill='black', back_color='white')

    # Save
    img.save(filename)
    print(f"QR code saved as {filename}")
