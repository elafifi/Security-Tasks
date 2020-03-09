Assignment1 description:- implementation of [shift - affine - vigenere] ciphers
=========================


shift(Caesar) Cipher:-
======================
equations:
----------
  enc:
  ----
  E ( x ) = ( x + a ) mod m 
  dec:
  ----
  D ( y ) = ( y - a  ) mod m 
  
  a is key between 0 ==> 25
  m ===> mode  = 26
  x: plain text
  y: cihper text

how to use:
-----------
  cipher.py cipherType operationType inputFile outputFile a   
  ex:
    for enc: cipher.py shift enc inputFile.txt outputFile.txt 10
    for dec: cipher.py shift dec inputFile.txt outputFile.txt 10



Affine Cipher:-
===============
equation: 
---------
  enc:
  ----
  E ( x ) = ( a x + b ) mod m 
  modulus m: size of the alphabet
  a and b: key of the cipher.
  a must be chosen such that a and m are coprime.
  
  dec:
  ----
  D ( x ) = a^-1 ( x - b ) mod m
  a^-1 : modular multiplicative inverse of a modulo m. i.e., it satisfies the equation
  1 = a a^-1 mod m .
  
  how to use:
  -----------
    you can run this file from cmd as ex:
      cipher.py cipherType operationType inputFile outputFile a b 
      cipher.py affine enc inputFile outputFile 17 20 
      cipher.py affine dec inputFile outputFile 17 20 
 
 
Vigenere Cipher:-
===============
equations:
----------
  enc:
  ----
  The plaintext(P) and key(K) are added modulo 26.
  Ei = (Pi + Ki) mod 26
  dec:
  ----
  Di = (Ei - Ki + 26) mod 26
  example:
  --------
  Input : Plaintext :   GEEKSFORGEEKS
               Keyword :  AYUSH
  Output : Ciphertext :  GCYCZFMLYLEIM
  For generating key, the given keyword is repeated
  in a circular manner until it matches the length of 
  the plain text.
  The keyword "AYUSH" generates the key "AYUSHAYUSHAYU"
  The plain text is then encrypted using the process 
  explained below.

how to use:
-----------
  cipher.py cipherType operationType inputFile outputFile a   
  ex:
    for enc: cipher.py vigenere enc inputFile.txt outputFile.txt AYUSH
    for dec: cipher.py vigenere dec inputFile.txt outputFile.txt AYUSH

 
