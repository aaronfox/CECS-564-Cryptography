function y = DecryptAffine(x, a, b)
x1=double(x);
z=ExtendedEuclidean(26,a);
y = mod(z(3)*(x1
- 65)
-b * z(3), 26) + 97;