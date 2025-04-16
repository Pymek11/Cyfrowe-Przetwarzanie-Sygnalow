[s, fs] = audioread('s0.wav');  % zmień nazwę na odpowiedni plik, np. s3.wav
t = (0:length(s)-1)/fs;

% Wizualizacja sygnału
figure;
plot(t, s);
xlabel('Czas [s]');
ylabel('Amplituda');
title('Sygnał DTMF');
% Parametry do spektrogramu
window = 4096;
noverlap = 4096 - 512;
nfft = 4096;

figure;
spectrogram(s, window, noverlap, nfft, fs, 'yaxis');
title('Spektrogram sygnału DTMF');
% Załóżmy, że chcesz przefiltrować pasmo wokół 770 Hz i 1336 Hz (cyfra "5")
bpFilt1 = designfilt('bandpassiir','FilterOrder',8, ...
         'HalfPowerFrequency1',750,'HalfPowerFrequency2',790, ...
         'SampleRate',fs);
bpFilt2 = designfilt('bandpassiir','FilterOrder',8, ...
         'HalfPowerFrequency1',1300,'HalfPowerFrequency2',1370, ...
         'SampleRate',fs);

filtSignal1 = filter(bpFilt1, s);
filtSignal2 = filter(bpFilt2, s);

figure;
subplot(2,1,1);
spectrogram(filtSignal1, window, noverlap, nfft, fs, 'yaxis');
title('Sygnał po filtracji pasmowej (770 Hz)');

subplot(2,1,2);
spectrogram(filtSignal2, window, noverlap, nfft, fs, 'yaxis');
title('Sygnał po filtracji pasmowej (1336 Hz)');
