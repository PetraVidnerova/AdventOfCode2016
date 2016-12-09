import re

def decompress(compressed_string):
    """ Returns the length of decompressed string. 
    """
    decompressed_len = 0
    marker = False
    marker_string = ""
    data_sequence = ""
    data_count = 0
    repeat = 0

    for c in compressed_string:

        if not marker:
            # reading the data sequence 
            if data_count > 0:
                data_sequence += c
                data_count -= 1
                if data_count == 0:
                    decompressed_len += decompress(data_sequence) * repeat
                    data_sequence = ""
                continue

            if c == '(':
                marker = True
                marker_string = ""
                continue
        
            decompressed_len += 1
            
        else:
            #reading the marker
            if c == ')':
                marker = False
                data_count, repeat = map(int,
                                         re.search(r'([0-9]+)x([0-9]+)', marker_string).groups())
            else:
                marker_string += c

    return decompressed_len


def test(): 
    for compressed_string in ["ADVENT",
                              "(3x3)XYZ",
                              "X(8x2)(3x3)ABCY",
                              "(27x12)(20x12)(13x14)(7x10)(1x12)A",
                              "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"]: 
        print(decompress(compressed_string))

    

if __name__ == "__main__":

    compressed_string = open("input9.txt").read().strip()
    print(decompress(compressed_string))
    
    

        
