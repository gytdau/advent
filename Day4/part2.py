import hashlib

i = 0

code = ""

with open("inputData.txt", "r") as infile:
    for line in infile:
        code = line

md5_hash_string = ""

# The only change needed was to add an extra 0
while not md5_hash_string.startswith('000000'):
    i += 1
    to_hash = code + str(i)
    to_hash.encode('utf-8')
    md5_hash = hashlib.md5()
    md5_hash.update(to_hash.encode('utf-8'))
    md5_hash_string = md5_hash.hexdigest()
    

print(i)