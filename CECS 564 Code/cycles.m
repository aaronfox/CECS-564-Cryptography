function [z, l, k] = cycles(x)
%Cycles computes the cycle decomposition of input permutation x, lengths
%of cycles, and the order of x.
n=size(x,2);
y=zeros(n,n);
mx=0;
for k=1:n
for i=1:n
 if (x(i) > 0)
 s=i;
 break;
 end;
end;
y(k,1)=s;
for i=2:n
 t=y(k,i-1);
 if x(t) == y(k,1)
 x(t)=0;
 if i-1 > mx
 mx=i-1;
 end;
 break;
 end;
 y(k,i)=x(t);
 x(t)=0;
end;
if sum(x) == 0
 break;
end;
end;
for i=1:k
 if y(i,1)>0
 z(i,1:mx)=y(i,1:mx);
 end;
end;
[m,n]=size(z);
k=1;
for i = 1 : m
 l(i) = 0;
 for j = 1 : n
 if z(i,j) > 0
 l(i) = l(i) + 1;
 end;
 end;
 k=lcm(k,l(i));
end;
end
