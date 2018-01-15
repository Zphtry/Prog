T   = 1
Tc  = 1
tau = 0.5
A   = 2
N   = 800
Wc  = 100

teta = 0:Tc/N:Tc
W    = 0:Wc/N:Wc
n    = 7

Fi = np.zeros(1, length(teta))
for i = 1:length(teta);
  if teta(i) == n*T 
      Fi(i) = 1;
  else
      Fi(i)= sin((pi/T)*(teta(i)-n*T))/((pi/T)*(teta(i)-n*T));
  end
end
figure(1); plot(teta, Fi);

Xjw = zeros(1, length(W));
for i = 1:length(W)
    Xjw(i) = trapz(teta, Fi.*cos(teta.*W(i))) - (1i)*trapz(teta, Fi.*sin(teta.*W(i)));
end
figure(2); plot(teta, Xjw);


x = zeros(1,length(teta)); 
for i=1:length(teta);
    if teta(i)>=0 && teta(i)<=Tc
        x(i) = A*exp(-teta(i)/tau);
    else
        x(i) = 0;
    end
end
figure(3); plot(teta, x);

Xw = zeros(1, length(W));
for i = 1:length(W)
    Xw(i) = sqrt((trapz(teta, x.*cos(teta.*W(i))))^2 + (trapz(teta, x.*sin(teta.*W(i))))^2);
end
figure(4); plot(W, Xw);

maxXw = 0.05*max(Xw);
for i = 1:length(Xw)  
   if Xw(i) <= maxXw
       Wv = W(i);
       return;
   end
end
disp(Wv);


T = (pi/Wv);
NN = fix(Tc/T);
teta1 = 0:T/900:Tc;

x1 = zeros(1,length(teta1)); 
for i=1:length(teta1);
    if teta1(i)>=0 && teta1(i)<=Tc
        x1(i) = A*exp(-teta1(i)/tau);
    else
        x1(i) = 0;
    end
end
%figure(5); plot(teta1, x1);


 x2 = zeros(1,length(teta1));
 Xn1 = zeros(1,length(teta1)); cdf = zeros(1, length(teta1));
 
for i=1:length(teta1)
    for nn=1:NN+1
        Xn1(i) = Xn1(i) + Func(T*(nn-1),Tc)*CDF(teta1(i),T,nn-1);
    end
end

% for i = 1:length(teta1)
%   for nn = 1:NN+1
%        
%        if Tc*(nn-1)>=0 && Tc*(nn-1)<=Tc 
%            x2(i) = (A*exp(-Tc*(nn-1)/tau));
%        else
%            x2(i) = 0;
%        end
%        
%         if teta1(i) == (nn-1)*T 
%             cdf(i) = 1;
%         else
%             cdf(i)= sin((pi/T)*(teta1(i)-(nn-1)*T))/((pi/T)*(teta1(i)-(nn-1)*T));
%         end       
%         Xn(i) = Xn(i) + x2(i)*cdf(i);
%    end
% end

figure(5);
subplot(1,2,1);
plot(teta1,x1);
subplot(1,2,2);
plot(teta1,Xn1);

err = abs(x1 - Xn1);
MaxEps = max(err);
disp(MaxEps);

figure(6);
plot(teta1,err);
