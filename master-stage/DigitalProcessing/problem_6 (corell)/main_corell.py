N = 2^11;
T = 0.02;
t = 0:T/N:T;
t = t(1:end-1);

%y = zeros(1,N);

A = 2;
fi = 2.09;
wi = 100;

y = zeros(1, length(t));
for i = 1:length(t)
    y(i) = A*sin(wi*t(i) + fi);
end

Y = fft(y);
YY = Y.*conj(Y)/N;

figure(1);
plot(t, YY);

teta = 1:1:N;
w1 = 81;
w2 = 14;
b = 5;

x = zeros(1, length(teta));
for i = 1:length(teta)
    x(i) = sin(w1*T*teta(i)) + cos(w2*T*teta(i));
end

r = zeros(1, length(teta));
for i = 1:length(teta)
    r(i) = b*rand;
end

y = x + (r - mean(r));

figure(2);
subplot(3,1,1); plot(teta, x);
subplot(3,1,2); plot(teta, r);
subplot(3,1,3); plot(teta, y);

r = zeros(1, fix(length(y)/10 - 1));
for i = 1:length(r)
    for j = 1:N - i
        r(i) = r(i) + (y(j))*(y(j + i));
    end
    r(i) = r(i)/(length(y) - i);
end

w = 0:(pi/T)/N:pi/T;
w = w(1:end-1);

y = zeros(1, length(w));
for n = 1:length(w)
    for m = 1:length(r)
        y(n) = y(n) + r(m)*cos(w(n)*T*m);
    end
    y(n) = 2*y(n);
end

figure(3); plot(w, y);
figure(4); plot(w, abs(y));


max_num = poisk(y);

ww1 = (pi*max_num(1))/(128*T); display(ww1);
ww2 = (pi*max_num(2))/(128*T); display(ww2);

bartletta_window = zeros(1, length(r));
ht = 1:1:length(r);
for i = 1:length(ht)
    if ht(i)>=0 && ht(i)<=length(ht)
%         bartletta_window(i) = 2*ht(i)/(length(ht));
%     else
%         bartletta_window(i) = 2 - (2*ht(i))/(length(ht));
%     end
       bartletta_window(i) = 0.42 - 0.5*cos((2*pi*ht(i))/length(ht)) + 0.08*cos((4*pi*ht(i))/length(ht));
        
       % bartletta_window(i) = 0.54 - 0.46 *cos(2*pi*ht(i)/((length(ht)-1)));
    end
end
figure(5); 
plot(ht, bartletta_window);

% bartletta_window = zeros(1, length(r));
% ht = 1:1:length(r);
% for i = 1:length(ht)
%     if ht(i)>=0 && ht(i)<=(length(ht))/2
%         bartletta_window(i) = 2*ht(i)/(length(ht));
%     else
%         bartletta_window(i) = 2 - (2*ht(i))/(length(ht));
%     end
% end
% figure(5); 
% plot(ht, bartletta_window);

y1 = zeros(1, length(w));
for n = 1:length(w)
    for m = 1:length(r)
        y1(n) = y1(n) + r(m)*bartletta_window(m)*cos(w(n)*T*m);
    end
    y1(n) = 2*y1(n);
end

figure(6); plot(w, y1);
figure(7); plot(w, abs(y1));

max_num = poisk(y1);
ww1_1 = (pi*max_num(1))/(128*T); display(ww1_1);
ww2_2 = (pi*max_num(2))/(128*T); display(ww2_2); 
