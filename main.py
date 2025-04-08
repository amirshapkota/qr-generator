from generator import generate_qr_code
from utils import get_data_input, get_filename_input

def main():
    data = get_data_input()

    filename = get_filename_input()

    generate_qr_code(data, filename)

if __name__ == "__main__":
    main()
