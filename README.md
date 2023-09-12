## The Diana Cryptosytem

The Diana cryptosystem is a symetric key-sharing system that uses a one-time pad to encode a message using a trigraph table which converts two given ascii characters into a third letter. The table can be generated using the following:
```
Given characters p1 and p2 in the set A-Z, character p3 is given by (25 - p1 - p2) mod 26
```
The starting position of the encoding process in the one-time pad is randomized, which creates an n-letter fragment that will be the key during the decoding process. For simplicity, the key itself is returned and the message decoded to demonstrate the symetric principle at work. 

### References
- Diana Cryptosystem: https://dodona.be/en/activities/2088793301/