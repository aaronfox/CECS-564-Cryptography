function y = EncryptAffine(x, a, b)
x1=double(x);
y = mod(a*(x1
- 97) + b, 26) + 65;