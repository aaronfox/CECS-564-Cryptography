function y = EncryptShift(x, k)
y = mod(x - 97 + k, 26) + 65;
