import librosa
import numpy as np

def pitch_augment(audio, sample_rate, bins_per_octave=12, pitch_pm=2):
	y_pitch = audio.copy()
	pitch_change =  pitch_pm * 2*(np.random.uniform())   
	y_pitch = librosa.effects.pitch_shift(	y_pitch.astype('float64'), 
						sample_rate, n_steps=pitch_change, 
						bins_per_octave=bins_per_octave)
	return y_pitch, round(pitch_change, 2)


def speed_augment(audio, low=0.5, high=1.8):
	y_speed = audio.copy()
	speed_change = np.random.uniform(low=low,high=high)
	y_speed = librosa.effects.time_stretch(y_speed.astype('float64'), speed_change)

	return y_speed, round(speed_change, 2)


def pitch_and_speed_augment(audio, low=0.5, high=1.8):
	y_pitch_speed = audio.copy()
	length_change = np.random.uniform(low=low, high=high)
	speed_fac = 1.0  / length_change
	y_pitch_speed = np.interp(np.arange(0, len(y_pitch_speed), speed_fac), np.arange(0, len(y_pitch_speed)), y_pitch_speed)

	return y_pitch_speed, round(length_change, 2)
