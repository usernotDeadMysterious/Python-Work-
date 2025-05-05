from Crypto.Util.number import *
from math import isqrt

# Given values from your original code output
n = 66614934560492068343665127593916300530978784796249835584907684213759490951781614877135866053823007405318980069351215477719681366294014909046514536250469778613914552833859755410172435779340839398310782242608381513634860939447150844018960892182679484174537944021592563113759334851601004117147691848461831393601
e = 65537
ct = 22865351250840877894991032342431169756379399914395894906018517209341557919386994258278351331187056096163192146250728872367765433164861456134494228431775595244814424751703850131845593350834564712160973504418119637342106235426997072054783711481570743790196037474582338259944256376457865733801220800805877457100

# Step 1: Factor n to find p (since n = p^2, p is the square root of n)
p = isqrt(n)
q = p  # Since q = p in your code

# Step 2: Compute φ(n)
phi_n = (p - 1) * (q - 1)

# Step 3: Compute the private key d
d = inverse(e, phi_n)

# Step 4: Decrypt the ciphertext (ct) to get the original message (flag)
flag_long = pow(ct, d, n)
flag_bytes = long_to_bytes(flag_long)

# Step 5: Handle decoding the flag (use 'ignore' or 'replace' if needed)
try:
    # Try decoding normally
    flag = flag_bytes.decode('utf-8')
except UnicodeDecodeError:
    # If decoding fails, use 'replace' to handle invalid characters
    flag = flag_bytes.decode('utf-8', errors='replace')

print(f"Decrypted flag: {flag}")
