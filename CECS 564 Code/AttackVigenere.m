function AttackVigenere(y,length)
n=length*floor(size(y,2)/length);
y=y(1:n);
w=reshape(char(y'),length,n / length);
for i = 1 : length
 AttackShift(w(i,:))
end;