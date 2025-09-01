import sys

def reinject_data(original_file, modified_file, offset_hex, output_file):
    offset = int(offset_hex, 16)

    with open(original_file, "rb") as f:
        original_data = bytearray(f.read())

 
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("❗ الاستخدام:")
        print("python reinject.py original.bin modified.zlib 0xOFFSET output.bin")
    else:
        reinject_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
