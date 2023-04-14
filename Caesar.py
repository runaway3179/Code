import os

key = int(input("시프트시킬 숫자를 입력해주세요.\n권장 범위는 1~25입니다. : "))

def encrypt_caesar(input_file, output_file, key):
    
    #Encrypts an input file using the Caesar cipher algorithm and writes the result to an output file.
    
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        while True:
            byte_s = f_in.read(1)
            if not byte_s:
                break
            byte = byte_s[0]
            encrypted_byte = (byte + key) % 256
            f_out.write(bytes([encrypted_byte]))


def decrypt_caesar(input_file, output_file, key):
    
    #Decrypts an input file encrypted with the Caesar cipher algorithm and writes the result to an output file.
    
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        while True:
            byte_s = f_in.read(1)
            if not byte_s:
                break
            byte = byte_s[0]
            decrypted_byte = (byte - key) % 256
            f_out.write(bytes([decrypted_byte]))

#print("encrypt / decrypt complete.")

# Example usage:
input_file = 'input.txt'
encrypted_file = 'encrypted.txt'
decrypted_file = 'decrypted.txt'


encrypt_caesar(input_file, encrypted_file, key)
decrypt_caesar(encrypted_file, decrypted_file, key)
