function [m s e] = SummaryStat(x)
%SummaryStat Computes m: mean, s: standard deviation, and e: entropy
%of input data x
sz=size(x);
x1=reshape(x,sz(1)*sz(2),1);
m=mean(double(x1));
s=std(double(x1));
p=hist(double(x1),256);p=p/sum(p);
e=0;l2=log(2);
for i=1:256
 if p(i) > 0
 e=e-p(i)*log(p(i))/l2;
 end;
end;
end