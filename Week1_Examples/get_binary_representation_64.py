import struct


def float_to_64bit_binary(value):
    value = float(value)

    packed = struct.pack(">d", value)   # big-endian double precision
    integer = int.from_bytes(packed, byteorder="big")
    bits = f"{integer:064b}"

    sign = bits[0]
    exponent = bits[1:12]
    fraction = bits[12:]

    return sign, exponent, fraction, bits


if __name__ == "__main__":
    fp_num = input("Enter your floating point value:\n")

    sign, exponent, fraction, bits = float_to_64bit_binary(fp_num)

    print("\nIEEE-754 Double Precision (64-bit):")
    print(f"{sign} | {exponent} | {fraction}")

    print("\nFull 64-bit representation:")
    print(bits)

    print("\nHex representation:")
    print(hex(int(bits, 2)))