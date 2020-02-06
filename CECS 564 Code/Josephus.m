function y = Josephus(n,k)
kk = k;
if k > n
 kk = mod(kk,n);
end;
y(1) = kk;
j = kk;
d=dec2bin(0,n);
d(kk)='1';
for i = 2 : n
 kk = 0;
 while kk < k
 j = mod(j,n)+1;
 if d(j) == '0'
 kk = mod(kk,k)+1;
 end;
 end;
 d(j) = '1';
 y(i) = j;
end;