import sys

def reinject_data(original_file, modified_file, offset_hex, output_file):
    offset = int(offset_hex, 16)

    with open(original_file, "rb") as f:
        original_data = bytearray(f.read())

 
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("❗ الاستخدام:")
    
