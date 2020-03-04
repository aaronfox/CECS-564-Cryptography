%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%This function implements Bayes' Theorem for the purpose of comp. probabilistic
%Security evaluation of a crypto system.
%Inputs are:
%(1) p: pdf of the plaintext characters or priori probabilities
%(2) pk: pdf of the keys
%(3) e: Encryption function "c = e(k, p); where c is the cipher character"
%Outputs using p and k.
%(1) q: pdf of the ciphetext characters
%(2) ppgivenc: conditional pdf of plaintext given ciphertext or posteriori
% probabilities
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [q,ppgivenc] = Bayes(p,pk,e)
m = size(pk,2);
n = size(p ,2);
q = zeros(1,n);
pcgivenp=zeros(n);
for i=1:m
 for j=1:n
 q(e(i,j))=q(e(i,j))+pk(i)*p(j);
 pcgivenp(e(i,j),j)=pcgivenp(e(i,j),j)+pk(i);
 end
end
for i=1:n
 for j=1:n
 ppgivenc(i,j)=pcgivenp(j,i)*p(i)/q(j);
 end
end
end