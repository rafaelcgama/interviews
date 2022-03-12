def encode_number(n):
    if n > 0xFFFF:
        raise "Number is too large to encode"
    return chr(n)

def decode_number(s):
    return ord(s)

def serialize(mylist):
    result = []
    for word in mylist:
        result.append(encode_number(len(word)))
        result.append(word)
    return ''.join(result)

def deserialize(mystring):
    result = []
    i = 0
    if len(mystring) < 2:
        return result

    while i < len(mystring):
        word_len = decode_number(mystring[i])
        if word_len + i >= len(mystring):
            raise "Bad encoding"

        i += 1
        word = mystring[i: i + word_len]
        result.append(word)
        i += word_len

    return result

