# -*- coding: utf-8 -*-
"""
@title: implementation of ciphers[shift - affine - vigenere]
@author: Elafifi
@date:3/9/2020

"""
#[“shift”,”affine”,”vigenere”].

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
def mod_inv(a):
    for i in range(26):
        if (a * i)%26 == 1:
            return i
    return -1
        
        
def f(cipherType, operationType, inputFile, outputFile, sa, b=-1):
    with open(inputFile, 'r') as rf:
        with open(outputFile,'w') as wf:
            
            if cipherType == "shift":
                
                if operationType == "enc":
                    
                    for line in rf:
                        text = "";
                        for i in line:
                            if i.isalpha():
                                if i.islower():
                                    c = ord(i)-ord('a')
                                    y = (c + sa)%26 +ord('a')
                                    text = text + chr(y)
                                elif i.isupper():
                                    c = ord(i)-ord('A')
                                    y = (c + sa)%26 +ord('A')
                                    text = text + chr(y)
                            
                            else:
                                    #print("Error: all inputFile must contain letters only!")
                                    text = text + i
                        wf.write(text)
                elif operationType == "dec":
                    for line in rf:
                        text = "";
                        for i in line:
                            if i.isalpha():
                                if i.islower():
                                    c = ord(i)-ord('a')
                                    y = (c - sa)%26 +ord('a')
                                    text = text + chr(y)
                                elif i.isupper():
                                    c = ord(i)-ord('A')
                                    y = (c - sa)%26 +ord('A')
                                    text = text + chr(y)
                            
                            else:
                                    #print("Error: all inputFile must contain letters only!")
                                    text = text + i
                        wf.write(text)
                else:
                    print("Error: operationType is invalid.")
                    return
            elif cipherType == "affine":
                if(gcd(sa, b) != 1):
                    print("Error: a key doesn't have mod_inv in Z26")
                    return
                if sa < 0 | b < 0 | b > 25| sa > 25:
                    print("Error: invalid keys in affine cipher")
                    return
                if operationType == "enc":
                    
                    for line in rf:
                        text = "";
                        for i in line:
                            if i.isalpha():
                                if i.islower():
                                    c = ord(i)-ord('a')
                                    y = (sa*c + b)%26 +ord('a')
                                    text = text + chr(y)
                                elif i.isupper():
                                    c = ord(i)-ord('A')
                                    y =  (sa*c + b)%26 + ord('A')
                                    text = text + chr(y)
                            
                            else:
                                    #print("Error: all inputFile must contain letters only!")
                                    text = text + i
                        wf.write(text)
                elif operationType == "dec":
                    for line in rf:
                        text = "";
                        for i in line:
                            if i.isalpha():
                                if i.islower():
                                    c = ord(i)-ord('a')
                                    y =  (mod_inv(sa) * (c - b) ) % 26 + ord('a')
                                    text = text + chr(y)
                                elif i.isupper():
                                    c = ord(i)-ord('A')
                                    y =  (mod_inv(sa) * (c - b) ) % 26 +ord('A')
                                    text = text + chr(y)
                            
                            else:
                                    #print("Error: all inputFile must contain letters only!")
                                    text = text + i
                        wf.write(text)
            elif cipherType == "vigenere":
                key_size = len(sa)
                cnt = -1
                if operationType == "enc":
                    for line in rf:
                        text = "";
                        for i in line:
                            if i.isalpha():
                                cnt = (cnt + 1) % key_size
                                if i.islower():
                                    c = ord(i)-ord('a')
                                    y = (c + ord(sa[cnt].lower()) - ord('a'))%26 +ord('a')
                                    text = text + chr(y)
                                elif i.isupper():
                                    c = ord(i)-ord('A')
                                    y = (c + ord(sa[cnt].lower()) - ord('a'))%26 +ord('A')
                                    text = text + chr(y)
                            
                            else:
                                    #print("Error: all inputFile must contain letters only!")
                                    text = text + i
                        wf.write(text)
                elif operationType == "dec":
                    for line in rf:
                        text = "";
                        for i in line:
                            if i.isalpha():
                                cnt = (cnt + 1) % key_size
                                if i.islower():
                                    c = ord(i)-ord('a')
                                    y = (c - (ord(sa[cnt].lower()) - ord('a')) + 26)%26 +ord('a')
                                    text = text + chr(y)
                                elif i.isupper():
                                    c = ord(i)-ord('A')
                                    y = (c - (ord(sa[cnt].lower()) - ord('a')) + 26)%26 +ord('A')
                                    text = text + chr(y)
                            
                            else:
                                    #print("Error: all inputFile must contain letters only!")
                                    text = text + i
                        wf.write(text)
                else:
                    print("Error: operationType is invalid.")
                
                
            else:
                print("Error: cipherType is invalid.")



if __name__ == "__main__":
    import sys
    print ("This is the name of the script= ", sys.argv[0])
    print("Number of arguments= ", len(sys.argv))
    print("all args= ", str(sys.argv))
    print("arg1= ", sys.argv[1])
    print("arg2= ", sys.argv[2])
    print("arg1= ", sys.argv[3])
    print("arg2= ", sys.argv[4])
    print("arg1= ", int(sys.argv[5]))
    print("arg1= ", int(sys.argv[6]))
    
    cipherType = sys.argv[1]
    operationType = sys.argv[2]
    inputFile = sys.argv[3]
    outputFile = sys.argv[4]
    a = sys.argv[5]
    b = sys.argv[6]

    if cipherType == "shift":
        a = int(a)
    elif cipherType == "affine":
        a = int(a)
        b = int(b)
    elif cipherType == "vigenere":
        pass
    f(cipherType, operationType, inputFile, outputFile, a, b)
                
