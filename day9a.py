import re

def decompress(compressed_string):
    """ Returns the length of decompressed string. 
    """
    decompressed_len = 0
    data_count = 0
    repeat = 0

    i = 0
    while i < len(compressed_string):

        # read the data sequence?
        if data_count > 0:
            decompressed_len += decompress(compressed_string[i:i+data_count]) * repeat
            i += data_count
            data_count, repeat = 0, 0
            continue

        # start of marker
        regex = re.compile(r'^\(([0-9]+)x([0-9]+)\)')
        if regex.match(compressed_string[i:]):
            data_count, repeat = regex.search(compressed_string[i:]).groups()
            i += len(data_count) + len(repeat) + 3
            data_count, repeat = int(data_count), int(repeat)
            continue
        
        # read normal character 
        decompressed_len += 1
        i += 1

    return decompressed_len



if __name__ == "__main__":


    compressed_string = open("input9.txt").read().strip()
    print(decompress(compressed_string)) # 10780403063

    
    

        
