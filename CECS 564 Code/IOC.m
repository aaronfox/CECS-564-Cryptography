function y = IOC(x)
%This function computes the average AUTO_IOC of input string x and
%the shifted
%x with shifts = 1, 2,3, ...., 64
n = size(x, 2);
for i = 1 : 64
 t = 0;
 n1 = n - i;
 for j = 1 : n1
 if x(j) == x(j + i)
 t = t + 1;
 end;
 end;
 y(i) = t / n1;
end;