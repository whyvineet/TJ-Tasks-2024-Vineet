def compress(chars):
    #write your code here
    write_index = 0
    i = 0
    
    while i < len(chars):
        char = chars[i]
        count = 0
        
        while i < len(chars) and chars[i] == char:
            count += 1
            i += 1
            
        chars[write_index] = char
        write_index += 1
        
        if count > 1:
            for digit in str(count):
                chars[write_index] = digit
                write_index += 1
    
    return write_index

if __name__ == "__main__":
    chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    newSize = compress(chars)
    print("New length:", newSize)
    print(chars[:newSize])