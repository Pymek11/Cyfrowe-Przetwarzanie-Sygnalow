clear; clc; close all;

%% --- PARAMETRY SYGNAŁU ---
fs = 360;               % częstotliwość próbkowania EKG
load ECG100.mat         % wczytujemy zmienną "val"
x = val(1, :);          % pierwszy kanał
x = x(:)';              % upewniamy się, że wektor jest rzędem
N = length(x);
t = (0:N-1)/fs;


%% --- WIDMO SYGNAŁU ---
figure;
pspectrum(x, fs);
title('Widmo oryginalnego sygnału EKG');

%% --- PROJEKT FILTRU FIR LPF ---
M = 101;                    % długość filtru (nieparzysta)
Wn = 40/(fs/2);             % pasmo do 40 Hz
b_fir = fir1(M-1, Wn, blackman(M));   % filtr LPF

%% --- FILTRACJA SYGNAŁU ORYGINALNEGO ---
y_filt = filter(b_fir, 1, x);
P = (M-1)/2;                % opóźnienie filtru

x_sync = x(P+1:end);
y_sync = y_filt(2*P+1:end);

min_len = min(length(x_sync), length(y_sync));
x_sync = x_sync(1:min_len);
y_sync = y_sync(1:min_len);

figure;
plot(t(1:min_len), x_sync, 'k--'); hold on;
plot(t(1:min_len), y_sync, 'r');
legend('Oryginalny', 'Po filtracji');
title('Filtracja EKG'); xlabel('Czas [s]'); ylabel('Amplituda');

%% --- DODANIE SZUMU I FILTRACJA ---
noise = 0.5 * randn(1, N);      % szum Gaussowski
x_noisy = x + noise;            % zaszumiony sygnał
y_noisy_filt = filter(b_fir, 1, x_noisy);

x_noisy_sync = x_noisy(P+1:end);
y_noisy_sync = y_noisy_filt(2*P+1:end);

min_len2 = min(length(x_noisy_sync), length(y_noisy_sync));
x_noisy_sync = x_noisy_sync(1:min_len2);
y_noisy_sync = y_noisy_sync(1:min_len2);

figure;
plot(t(1:min_len2), x_noisy_sync, 'b--'); hold on;
plot(t(1:min_len2), y_noisy_sync, 'g');
legend('Zaszumiony', 'Odszumiony');
title('Odszumianie EKG'); xlabel('Czas [s]'); ylabel('Amplituda');

%% --- KONIEC ---
fprintf("✅ Zadanie 4 zakończone sukcesem – EKG odszumione.\n");
