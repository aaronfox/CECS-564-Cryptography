function y = Riffle(n)
%This is a permutation of a sorted list by cutting the input list
%into two halves then do inside interleaving
x=1:n;
m=ceil(n/2);
y(1:2:n)=1:m;
y(2:2:n)=m+1:n;
end