import base64

# Vraag de gebruiker om de base64-gecodeerde string
encoded_string = input("Voer de base64-gecodeerde string in: ")

# Proberen te decoderen van de base64-string
try:
    decoded_bytes = base64.b64decode(encoded_string)
except ValueError:
    print("Ongeldige base64-string. Probeer ASCII te gebruiken.")
    exit()

# Proberen te decoderen met verschillende tekensets
charsets = ['utf-8', 'ascii', 'windows-1252', 'ISO-8859-1', 'utf-16', 'ISO-8859-15', 'gb2312', 'gbk', 'big5', 'shift_jis', 'cp850', 'ISO-8859-2', 'ISO-8859-6', 'ISO-8859-15', 'EUC-CN', 'HZ' ]

decoded_strings = []
decode_success = False
for charset in charsets:
    try:
        decoded_string = decoded_bytes.decode(charset)
        if decoded_string not in decoded_strings:
            decoded_strings.append(decoded_string)
            print(f'Gedecodeerde string met {charset}: {decoded_string}')
            decode_success = True
    except UnicodeDecodeError:
        continue

if not decode_success:
    print('Het decoderen is niet gelukt met geen enkele tekenset.')