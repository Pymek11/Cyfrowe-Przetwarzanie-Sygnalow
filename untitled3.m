clear; clc; close all;

%% PARAMETRY
fs = 1e6;             % częstotliwość próbkowania: 1 MHz
N = 128;              % długość filtrów FIR
samples = 1e5;        % bezpieczna długość sygnału

%% Wczytanie sygnału
load stereo_samples_fs1000kHz_LR_IQ.mat
signal = I + 1j*Q;
x_full = real(signal);

%% Sprawdzenie długości
if length(x_full) < samples
    error('Za mało próbek w sygnale!');
end

x = x_full(1:samples).';  % kolumna
t = (0:samples-1).'/fs;

%% Filtry
b_pilot = fir1(N-1, [18500 19500]/(fs/2), blackman(N));
b_stereo = fir1(N-1, [37000 39000]/(fs/2), blackman(N));
b_aa = fir1(N-1, 15000/(fs/2), blackman(N));
b_lpr = fir1(N-1, 15000/(fs/2), blackman(N));

%% Filtrowanie
pilot = filter(b_pilot, 1, x);
lmr = filter(b_stereo, 1, x);
lpr = filter(b_lpr, 1, x);

%% Przesunięcie (38 kHz do 0 Hz) bez błędów
c = cos(2*pi*38000*t);  % kosinus w kolumnie
lmr_bb = lmr .* c;      % element-wise

%% Antyaliasing + downsampling
lmr_bb_filt = filter(b_aa, 1, lmr_bb);
lmr_ds = downsample(lmr_bb_filt, round(fs/30000));
lpr_ds = downsample(lpr, round(fs/30000));

%% Synchronizacja i rekonstrukcja
delay_stereo = (length(b_stereo)-1)/2 + (length(b_aa)-1)/2;
delay_mono = (length(b_lpr)-1)/2;
shift = round(delay_stereo - delay_mono);

lpr_sync = lpr_ds(shift+1:end);
lmr_sync = lmr_ds(1:end-shift);

yl = 0.5*(lpr_sync + lmr_sync);
yr = 0.5*(lpr_sync - lmr_sync);

soundsc([yl'; yr']', 30000);
fprintf('🎧 Sukces! Stereo zdekodowane z próbki %d\n', samples);
