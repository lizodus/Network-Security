import hashlib, os
import hmac,binascii
import uuid

# initializing string
print("Kindly type the password")
password = input()
salt = os.urandom(16)

result = hashlib.md5(password.encode())
result1=hashlib.sha1(password.encode())
result2=hashlib.sha224(password.encode())
result3=hashlib.sha512(password.encode())

# printing the equivalent haexadecimal value.

print("MD5 hash is : ", end="")
print(result.hexdigest())
print("\n")
print("sha1 hash is : ", end="")
print(result1.hexdigest())
print("\n")
print("sha224 hash is : ", end="")
print(result2.hexdigest())
print("\n")
print("sha512 hash is : ", end="")
print(result3.hexdigest())


# md5 functions
def print_str_md5_salted(plainStr, saltStr):
    print("md5:")

    print("\tNo salt:", end="")
    for i in range(16):
        print(end=" ")
    print(string_md5(plainStr))

    print("\tLightly Salted:", end=" ")
    print(string_md5_salted(plainStr, saltStr))


# sha1 functions
def print_str_sha1_salted(plainStr, saltStr):
    print("sha1:")

    print("\tNo salt:", end="")
    for i in range(8):
        print(end=" ")
    print(string_sha1(plainStr))

    print("\tSalted:", end=" ")
    print(string_sha1_salted(plainStr, saltStr))


# sha224 functions
def print_str_sha224_salted(plainStr, saltStr):
    print("sha224:")

    print("\tNo salt:", end="")
    for i in range(8):
        print(end=" ")
    print(string_sha224(plainStr))

    print("\tSalted:", end=" ")
    print(string_sha224_salted(plainStr, saltStr))


# sha512 functions
def print_str_sha512_salted(plainStr, saltStr):
    print("sha512:")

    print("\tNo salt:", end="")
    for i in range(8):
        print(end=" ")
    print(string_sha512(plainStr))

    print("\tSalted:", end=" ")
    print(string_sha512_salted(plainStr, saltStr))
