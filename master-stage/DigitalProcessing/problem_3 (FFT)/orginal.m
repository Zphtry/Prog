N  = 128
Tc = 1.5
Wc = 200
Q  = 0:Tc/N:Tc - 0.00001
F  = 0:Wc/N:Wc - 0.00001

y = zeros(1,length(Q)); 
for i=1:length(Q);
    y(i) = MyFunc(Q(i));
end

Sw = zeros(1,length(F));

for k=1:length(F)
    for n = 1:length(F)
    Sw(k) = Sw(k) + y(n)*W(k-1,n-1,N);
    end
end
figure(1);
plot(Q,y);

figure(3);
plot3(F, real(Sw),imag(Sw));

Sdft = DFT(y);
% if length(Sdft)>N
%     addN = length(Sdft) - N;
%     y = [y, zeros(1,addN)];
%     F = 0:Wc/length(Sdft):Wc - 0.00001;
% 
%     Sw = zeros(1,length(F));
% 
%     for k=1:length(F)
%         for n = 1:length(F)
%         Sw(k) = Sw(k) + y(n)*W(k-1,n-1,N);
%         end
%     end
% end
F1 = 0:Wc/length(Sdft):Wc - 0.00001;
figure(2);
subplot(1,2,1);
plot(F, abs(Sw));
subplot(1,2,2);
figure(2);
plot(F, abs(Sdft));

Err = abs(Sw - Sdft);
P = max(Err);
MaxErr = max(Err)/max(abs(Sw));
disp(MaxErr);