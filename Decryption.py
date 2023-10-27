import math
def desubstitute(text):
    substitution_key = {
    'Q': 'A', 'W': 'B', 'E': 'C', 'R': 'D', 'T': 'E', 'Y': 'F', 'U': 'G', 'I': 'H',
    'O': 'I', 'P': 'J', 'A': 'K', 'S': 'L', 'D': 'M', 'F': 'N', 'G': 'O', 'H': 'P',
    'J': 'Q', 'K': 'R', 'L': 'S', 'Z': 'T', 'X': 'U', 'C': 'V', 'V': 'W', 'B': 'X',
    'N': 'Y', 'M': 'Z'
}
    plain_text = ''.join(substitution_key.get(c, c) for c in text)
    return plain_text

def columnar_detransposition(text,columnar_key):
    msg_len = len(text)
    col = len(columnar_key)
    
    row = int(math.ceil(msg_len / col))
    matrix = [['' for _ in range(col)] for _ in range(row)]

    k_indx = 0
    msg_indx = 0

    for i in range(col):
        curr_idx = columnar_key.index(i + 1)
        for j in range(row):
            matrix[j][curr_idx] = text[msg_indx]
            msg_indx += 1

    original_message = ''.join(''.join(row) for row in matrix)
    original_message = original_message.rstrip('_')

    return original_message

def row_detransposition(cipher, row_key):
    num_columns = len(row_key)
    num_rows = len(cipher) // num_columns
    rows = ['' for _ in range(num_rows)]
    sorted_key = sorted(range(num_columns), key=lambda k:row_key[k])
    for i in range(num_rows):
        row = cipher[i * num_columns:(i + 1) * num_columns]
        for j in range(num_columns):
            rows[i] += row[sorted_key[j]]
    message = ''.join(rows)
    
    return message

def decrypt(text, columnar_key, row_key):
    text = row_detransposition(text, row_key)
    text = columnar_detransposition(text,columnar_key)
    text = desubstitute(text)
    return text

text = input("Enter Your cipher text: ")
columnar_key = [3,1,2,4]
row_key = [2,1,3,4]
plaintext = decrypt(text, columnar_key, row_key)
print("Plain Text: ", plaintext)

