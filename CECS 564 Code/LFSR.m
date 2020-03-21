%This function performs LFSR. Inputs are non-zero seed bits and FB
%tap points. Outputs are a pseudo random byte and new seed.
function [byt seed] = LFSR(seed, c)
m=size(c,2);
n=size(seed,2);
seed = uint8(seed) - 48;
 for k = 1 : 8
 bt(k)=seed(n);
 b = 0;
 for i = 1 : m
 b = bitxor(b, seed(c(i)));
 end;
 seed=circshift(seed,[0 1]);
 seed(1) = b;
 end;
 bt = char(bt + 48);
 byt = bin2dec(bt);
 seed = char(seed + 48);