% ========================================================
% SquareAndMultiply algorithm is a fast modular exponetiation
% Input parameter are:
% x : base integer
% c : exponent integer
% n : modulus
% ========================================================
function z = SquareAndMultiply(x, c, n)
b=dec2bin(c);
m = size(b,2);
z = 1;
for i = 1 : m 
z = mod(z * z, n);
if (b(i) == '1')
z = mod( z * x, n);
end;
end;