clear; close all; clc;

fpr = 1200;
fc = 300;
df = 200;
fp1 = fc - df/2;
fp2 = fc + df/2;

N1 = 128; % parzyste
N2 = 129; % nieparzyste

Wn = [fp1 fp2]/(fpr/2); % normalizacja

okna = {
    rectwin(N1), 'Rectangular';
    hanning(N1), 'Hanning';
    hamming(N1), 'Hamming';
    blackman(N1), 'Blackman';
    blackmanharris(N1), 'Blackman-Harris'
};

figure;
for i = 1:size(okna,1)
    b = fir1(N1-1, Wn, 'bandpass', okna{i,1});
    [H, f] = freqz(b, 1, 1024, fpr);
    
    subplot(2,1,1);
    hold on; plot(f, abs(H), 'DisplayName', okna{i,2});
    title('Charakterystyki amplitudowe'); xlabel('Hz'); ylabel('|H(f)|'); grid on;

    subplot(2,1,2);
    hold on; plot(f, angle(H), 'DisplayName', okna{i,2});
    title('Charakterystyki fazowe'); xlabel('Hz'); ylabel('Faza [rad]'); grid on;
end
subplot(2,1,1); legend show;
subplot(2,1,2); legend show;
for i = 1:size(okna,1)
    b = fir1(N1-1, Wn, 'bandpass', okna{i,1});
    [H, f] = freqz(b, 1, 1024, fpr);
    idx_stop = (f < fp1 - 50 | f > fp2 + 50); % okolice pasma zaporowego
    attenuation = 20*log10(max(abs(H(idx_stop))));
    fprintf('%s window: Max stopband attenuation = %.2f dB\n', okna{i,2}, attenuation);
end

t = 0:1/fpr:1;
x = sin(2*pi*100*t) + sin(2*pi*300*t) + sin(2*pi*500*t); % testowy sygnał

figure;
pspectrum(x, fpr);
title('Widmo oryginalnego sygnału');

% Przykład filtracji:
b = fir1(N1-1, Wn, 'bandpass', blackman(N1));
y = filter(b, 1, x);

figure;
pspectrum(y, fpr);
title('Widmo po filtracji (Blackman)');
