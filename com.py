import marshal, zlib, base64

file = input("file: ")

content = open(file, encoding='utf-8').read()

comp = compile(content, 'MasAyip', 'exec')

print(marshal.dumps(comp))
