from random import choice, randint
from string import ascii_uppercase as uppercase

class OTP:
    def __init__(self, rows=4, cols=5, size=5):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.otp = self.makeOTP(self.rows, self.cols, self.size)

    def makeOTP(self, rows, cols, size) -> list:
        otp = [choice(uppercase) for _ in range(rows * cols * size)]
        return ''.join(otp)
    
    def printOTP(self):
        formatted = self.group(self.otp, self.size)
        for i in range(self.rows):
            for j in range(self.cols):
                print(formatted[i*j + j], end=' ')
            print()

    def group(self, mylist: list, size: int) -> list:
        l = []
        for i in range(0, len(mylist), size):
            l.append(''.join(mylist[i:i+size]))
        return l

def getTrigraphPosition(p1: chr, p2: chr) -> chr:
    return uppercase[(25 - ord(p1) - ord(p2)) % 26]


def encode(message: chr, otp: OTP) -> tuple:
    formatted = message.replace(' ','').upper()

    start = randint(0, len(otp.otp))
    key = ""
    encoded = ""
    for i in range(len(formatted)):
        pos = (i + start) % len(otp.otp)
        key += otp.otp[pos]
        encoded += getTrigraphPosition(key[i], formatted[i])
    return encoded, key

def decode(message: chr, key: chr) ->str:
    decoded = ""
    for i in range(len(message)):
        decoded += getTrigraphPosition(key[i], message[i])
    return decoded


def main():
    otp = OTP()
    print("Using this one-time pad:")
    otp.printOTP()
    message = "Attack at dawn"
    print(f"Message to encode: {message}")
    enc, key = encode(message, otp)
    print(f"Encoded: {enc}")
    print(f"Portion of one-time pad that is key: {key}")
    print(f"Decoded: {decode(enc, key)}\n")
    otp = OTP()
    print("Using this one-time pad:")
    otp.printOTP()
    message = "Lemmy was here"
    print(f"Message to encode: {message}")
    enc, key = encode(message, otp)
    print(f"Encoded: {enc}")
    print(f"Portion of one-time pad that is key: {key}")
    print(f"Decoded: {decode(enc, key)}\n")

if __name__ == "__main__":
    main()