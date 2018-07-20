def get_bytes_from_file(filename):  
    return open(filename, "rb").read()  

byte_arr = get_bytes_from_file("file.gz")


for byte in byte_arr:
    try:
        byte.encode("ascii")
    except UnicodeDecodeError as error:
        hex = byte.encode("hex")
        num = int(hex,16)
        print(hex, num)
        if(num < 127):
            print("LOW")
        else:
            print("HIGH")