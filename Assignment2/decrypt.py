from struct import pack, unpack

def F(w):
    return ((w * 31337) ^ (w * 1337 >> 16)) % 2**32

def decrypt(block):
    a, b, c, d = unpack("<4I", block)
    for i in xrange(32):
        # decrypting the second step in encrypt
        old_a = a
        d = d ^ 1337
        a = c ^ (F(d | F(d) ^ d))
        b = b ^ (F(d ^ F(a) ^ (d | a)))
        c = old_a ^ (F(d | F(b ^ F(a)) ^ F(d | b) ^ a))
        # decrypting the frist step in encrypt
        old_a = a
        a = d ^ 31337
        d = c ^ (F(a | F(a) ^ a))
        c = b ^ (F(a ^ F(d) ^ (a | d)))
        b = old_a ^ (F(a | F(c ^ F(d)) ^ F(a | c) ^ d))
    return pack("<4I", a, b, c, d)

ct = open("flag.enc").read()
pt = "".join(decrypt(ct[i:i+16]) for i in xrange(0,len(ct), 16))
print(pt);
