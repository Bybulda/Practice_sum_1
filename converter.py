import librosa
import numpy as np
import matplotlib.pyplot as plt
import os


def read_audio_from_filename(filename):
    audio, sr = librosa.load(filename)
    D = np.abs(librosa.stft(audio))**2
    audio = librosa.feature.melspectrogram(y=audio, sr=sr, S=D)
    return audio


def make_spectro(path):
    S = read_audio_from_filename(path)
    *dr, name = path.split('/')
    S_dB = librosa.power_to_db(S, ref=np.max)
    name = name[:-4]
    if not os.path.isdir(f'{dr}/spectr/{name}'):
        os.mkdir(f'{dr}/spectr/{name}')
    plt.imsave(fname=f'{dr}/spectr/{name}/{name}.png', arr=S_dB, cmap='inferno', format='png')
