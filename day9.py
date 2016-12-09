import re


def decompress(compressed_string):
    decompressed_string = ""
    marker = False
    marker_string = ""
    data_sequence = ""
    data_count = 0
    repeat = 0

    for c in compressed_string:

        if not marker:
            if data_count > 0:
                data_sequence += c
                data_count -= 1
                if data_count == 0:
                    decompressed_string += data_sequence * repeat
                    data_sequence = ""
                continue

            if c == '(':
                marker = True
                marker_string = ""
                continue
        
            decompressed_string += c
            
        else:
            #reading the marker
            if c == ')':
                marker = False
                data_count, repeat = map(int,
                                         re.search(r'([0-9]+)x([0-9]+)', marker_string).groups())
            else:
                marker_string += c

    return decompressed_string
                
def test(): 
    for compressed_string in ["ADVENT", "A(1x5)BC", "(3x3)XYZ",
                              "A(2x2)BCD(2x2)EFG", "(6x1)(1x3)A",
                              "X(8x2)(3x3)ABCY"]: 
        decompressed_string = decompress(compressed_string)
        
        print(decompressed_string)
        print(len(decompressed_string))
    

if __name__ == "__main__":
    compressed_string = open("input9.txt").read().strip()
    print(len(decompress(compressed_string)))
        
