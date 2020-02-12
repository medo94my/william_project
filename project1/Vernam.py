import math, random

class Vernamencryption(object):
    def __init__(self, message):
        message = self.message
        
    def encrypt(self,message, KEY):
        cipher = ''
        count = 0
        for char in message:
            cipher += chr(ord(char) * ord(KEY[count]))
            count += 1
            if count == len(message):
                count = 0
        print("Your encrypted message:" + cipher)
        return cipher

    def getmessage(self):
        message = self.message
        digits = "0123456789"
        KEY = ''
        for x in range(len(self.message)):
            KEY += digits[math.floor(random.random()*10)]
        a = encrypt(self.message, KEY)
        return a, KEY

class Decipher(Vernamencryption):
    def __init__(self, KEY, encryptedmessage):
        encryptedmessage = self.encryptedmessage
        super().__init__(KEY)

    def decrypt(encryptedmessage, KEY):
        deciphered = ''
        pointer = 0
        for char in encryptedmessage:
            deciphered += chr(ord(char) // ord(KEY[pointer]))
            pointer += 1
            if pointer == len(encryptedmessage):
                pointer = 0
            print("Your original message: " + deciphered)
            return deciphered

    def getdecryptmessage(self,KEY):
        encryptedmessage = self.encryptedmessage
        b = decrypt(encryptedmessage, KEY)
        return b
