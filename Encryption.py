import math

def substitution(text):
    substitution_dict = {
        'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T', 'F': 'Y', 'G': 'U', 'H': 'I',
        'I': 'O', 'J': 'P', 'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F', 'O': 'G', 'P': 'H',
        'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'Z', 'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B',
        'Y': 'N', 'Z': 'M'
    }
    encrypted_text = ''.join(substitution_dict.get(c, c) for c in text)
    return encrypted_text

def columnar_transposition(msg, key):
    cipher = ""
    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher

def row_transposition(msg, key):
    cipher = ""
    key_len = len(key)
    msg_len = len(msg)

    num_rows = -(-msg_len // key_len)
    matrix = [['' for _ in range(key_len)] for _ in range(num_rows)]
    index = 0
    for row in range(num_rows):
        for col in range(key_len):
            if index < msg_len:
                matrix[row][col] = msg[index]
                index += 1
    key_order = sorted(range(key_len), key=lambda k: key[k])
    for row in matrix:
        cipher += ''.join(row[i] for i in key_order)

    return cipher




def encrypt(text, substitution, columnar_key, row_key):
    text = substitution(text)
    text = columnar_transposition(text, columnar_key)
    text = row_transposition(text, row_key)
    return text



plain_text = input("Enter Your plain text: ")
columnar_key = [3,1,2,4]
row_key = [2,1,3,4]

cipher_text = encrypt(plain_text, substitution, columnar_key, row_key)
print("Cipher Text:", cipher_text)

