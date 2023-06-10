import os

if __name__ == '__main__':

    dirname = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(dirname, 'hex2dec_rom.bin'), 'wb') as f:
        for i in range(256):
            var = int(str(i), base=16)
            byte = var.to_bytes(length=2, byteorder='little');
            f.write(byte)
    f.close()
    print('completed!')
    