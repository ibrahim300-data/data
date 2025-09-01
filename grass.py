import sys

def reinject_data(original_file, modified_file, offset_hex, output_file):
    offset = int(offset_hex, 16)

    with open(original_file, "rb") as f:
        original_data = bytearray(f.read())

    with open(modified_file, "rb") as f:
        new_data = f.read()

    # تحقق أن البيانات الجديدة لا تتجاوز حجم الملف
    if offset + len(new_data) > len(original_data):
        print("❌ البيانات الجديدة أكبر من المساحة الأصلية!")
        return

    # حقن البيانات المعدّلة
    original_data[offset:offset + len(new_data)] = new_data

    with open(output_file, "wb") as f:
        f.write(original_data)

    print(f"✅ تم الحقن عند الإزاحة {hex(offset)} بنجاح.")
    print(f"📁 الملف الناتج: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("❗ الاستخدام:")
        print("python reinject.py original.bin modified.zlib 0xOFFSET output.bin")
    else:
        reinject_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])