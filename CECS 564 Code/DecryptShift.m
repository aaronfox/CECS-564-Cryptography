function y = DecryptShift(x, k)
y = mod(x- 65 - k, 26) + 97;
end