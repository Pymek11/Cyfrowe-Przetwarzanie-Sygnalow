clear; clc; close all;

fpr = 100000; % 100 kHz
f_cut = 15000; % 15 kHz cutoff
N = 128; % długość filtru
Wn = f_cut / (fpr/2); % normalizacja

% Używamy okna Blackmana dla dobrego tłumienia
b_lpr = fir1(N-1, Wn, blackman(N));

% Analiza charakterystyki
[H, f] = freqz(b_lpr, 1, 1024, fpr);

figure;
plot(f, 20*log10(abs(H)));
title('Filtr dolnoprzepustowy dla L+R'); xlabel('Hz'); ylabel('|H(f)| [dB]');
grid on; xlim([0 50e3]);
fp1 = 18500;
fp2 = 19500;
Wn_pilot = [fp1 fp2]/(fpr/2);

b_bp = fir1(N-1, Wn_pilot, blackman(N));

[H, f] = freqz(b_bp, 1, 1024, fpr);
figure;
plot(f, 20*log10(abs(H)));
title('Filtr pasmowoprzepustowy dla pilota 19 kHz');
xlabel('Hz'); ylabel('|H(f)| [dB]');
grid on; xlim([0 40e3]);
delay = (N-1)/2;
fprintf('Opóźnienie wprowadzone przez filtr: %.1f próbek\n', delay);
