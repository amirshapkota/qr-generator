def get_data_input():
    data = input("Enter URL or text: ")
    return data

def get_filename_input(default="qrcode.png"):
    filename = input(f"Enter file name to save the QR code (default: '{default}'): ")
    return filename if filename else default
