import hashlib
i = 0
while True:
    md5input = "ckczppom"+str(i) 
    md5input = md5input.encode('utf-8')
    hashobj = hashlib.md5(md5input)
    if hashobj.hexdigest()[:6] == "000000":
        print(hashobj.hexdigest())
        print(i)
        break
    i += 1




