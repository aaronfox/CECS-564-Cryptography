function y = PreProcess(x)
n = size(x, 2);
j = 1;
for i = 1 : n
    xp = x(i);
    if (xp > 64 && xp < 91) 
        y(j) = xp + 32;
        j = j + 1;
    end;
    if (xp > 96 && xp < 123)
        y(j) = xp;
        j = j + 1;
    end;
end;