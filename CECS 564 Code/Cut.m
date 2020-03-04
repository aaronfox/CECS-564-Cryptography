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
