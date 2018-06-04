clc;
clear all;
close all;
 
%начальные значения и переменные
 
l_left = 0.01;
l_right = 1;
delta_l = 0.05;
M = 10;
N = 10;
m = 0.9;
 
%1
X1 = factorial(M)/(factorial(N)*factorial(M-N));
k = 0;
X = l_left;
 
while(X < l_right)
    X2 = (X/m)^N;
    S = 0;
    Y = 0;
    while(Y <= N)
        Y2 = (X/m)^Y;
        Y1 = factorial(M)/(factorial(Y)*factorial(M-Y));
        S = S + Y1*Y2;
        Y = Y + 1;
    end
    P1_k(k+1) = X1*(X2/S);
    G1_k(k+1) = X*M*(1 - P1_k(k+1));
    E1_k(k+1) = (X*M/m)*(1-P1_k(k+1));
    XX_k = X;
    X = X+ delta_l;
    k = k + 1;
end
 

%2
k = 0;
X = l_left;
 
while(X < l_right)
    X2 = ((X*M/m)^N)/factorial(N);
    S = 0;
    Y = 0;
    while(Y <= (N+1))
        Y2 = ((X*M/m)^Y)/factorial(Y);
        S = S + Y2;
        Y = Y + 1;
    end
    P2_k(k+1) = X2/S;
    G2_k(k+1) = X*M*(1 - P2_k(k+1));
    E2_k(k+1) = (X*M/m)*(1-P2_k(k+1));
    X = X + delta_l;
    k = k + 1;
end
 
%3
X1 = factorial(M)/(factorial(N)*factorial(M-N));
k = 0;
X = l_left;
 
while(X < l_right)
    X2 = (X/(m+X))^N;
    Y2 = (1-(X/(m+X)))^(M-N);
    P3_k(k+1) = X1*X2*Y2;
    G3_k(k+1) = X*M*(1 - P3_k(k+1));
    E3_k(k+1) = (X*M/m)*(1-P3_k(k+1));
    X = X + delta_l;
    k = k + 1;
end
 
figure(1);
plot(l_left:delta_l:l_right, P1_k, l_left:delta_l:l_right, P2_k, l_left:delta_l:l_right, P3_k);
grid on;
ylabel('Вероятность потерь вызовов');
xlabel('Lambda');
legend('Эрланг', 'Энгсет', 'Биноминальное распределение')
 
figure(2);
plot(l_left:delta_l:l_right, G1_k, l_left:delta_l:l_right, G2_k, l_left:delta_l:l_right, G3_k);
grid on;
ylabel('Производительность');
xlabel('Lambda');
legend('Эрланг', 'Энгсет', 'Биноминальное распределение')
 
figure(3);
plot(l_left:delta_l:l_right, G1_k, l_left:delta_l:l_right, G2_k, l_left:delta_l:l_right, G3_k);
grid on;
ylabel('Среднее число соединений');
xlabel('Lambda');
legend('Эрланг', 'Энгсет', 'Биноминальное распределение')