import base64

# Vraag de gebruiker om de base64-gecodeerde string
encoded_string = input("Enter the base64-encoded string: ")

# Proberen te decoderen van de base64-string
try:
    decoded_bytes = base64.b64decode(encoded_string)
except ValueError:
    print("Invalid base64-string. Try using ASCII instead..")
    exit()

# Proberen te decoderen met verschillende tekensets
charsets = ['utf-8', 'ascii', 'windows-1252', 'ISO-8859-1', 'utf-16', 'ISO-8859-15', 'gb2312', 'gbk', 'big5', 'shift_jis', 'cp850', 'ISO-8859-2', 'ISO-8859-6', 'ISO-8859-15', 'EUC-CN', 'HZ' ]

for charset in charsets:
    try:
        decoded_string = decoded_bytes.decode(charset)
        print(f'Decoded string using {charset}: {decoded_string}')
    except UnicodeDecodeError:
        print(f'Unable to decode the string using {charset}')