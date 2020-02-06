%This procedure attacks shift cipher crypto system by comparing the
%histogram of the cipherext with the shifted histogram of the
%plainrtext. It performs three curve fitting techniques.
%Sum-Absolute-Difference, looking for the shift that gives a minimum.
%dot product; looking for maximum.
%Sum-squares of differences; looking for minimum.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%
function AttackShift(x)
h0
=[.082 .015 .028 .043 .127 .022 .020 .061 .070 .002 .008 .040 .024 .067 .075 .019 .001 .060 .063 .09
1 .028 .010 .023 .001 .020 .001];
h1=hist(uint8(x), 65:90) / size(x,2);
temp0 = 999999;
temp1 = 0;
temp2 = 999999;
for i = 2 : 26
 h0s = circshift(h0', i - 1);
 a = abs(h0s' - h1);
 b = h0s' .* h1;
 sad = sum(a);
 if sad < temp0
 c(1) = char(i + 96);
 temp0 = sad;
 end;
 dp = sum(b);
 if dp > temp1
 c(2) = char(i + 96);
 temp1 = dp;
 end;
 chi = sum(a .* a);
 if chi < temp2
 c(3) = char(i + 96);
 temp2 = chi;
 end;
end;
fprintf('Minimum sum-absolute-difference; sad, of the two histograms\n');
fprintf('corresponds to shift key equals\n');
fprintf(c(1));
fprintf('\n\nMaximum dot product ; d, of the two histograms\n');
fprintf('corresponds to shift key equals\n');
fprintf(c(2));
fprintf('\n\nMinimum sum-squares of differences; ss, of the two histograms\n');
fprintf('corresponds to shift key equals\n');
fprintf(c(3));
fprintf('\n\n');