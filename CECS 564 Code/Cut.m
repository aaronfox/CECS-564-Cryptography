function y = Cut(n)
%Cut is a permutation of a sorted n objects by cutting the input list
%in two packets b1 and b2 then switch their order
x=1:n;
m=ceil(n/2);
b1=1:m;
b2=m+1:n;
y(1:n-m)=b2;
y(n-m+1:n)=b1;
end
function y = Riffle(n)
%This is a permutation of a sorted list by cutting the input list
%into two halves then do inside interleaving
x=1:n;
m=ceil(n/2);
y(1:2:n)=1:m;
y(2:2:n)=m+1:n;
end
