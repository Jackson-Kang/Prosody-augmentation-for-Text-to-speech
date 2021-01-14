
import os

class Arguments():
	

	wav_paths = [	"/home/minsu/dataset/kss/kss",		# kss dataset path
			"/home/minsu/dataset/LJSpeech-1.1"]	# LJSpeech dataset	


	# save dir configurations
	save_dir = "preprocessed"
	savepath_to_resampled_wavs = os.path.join(save_dir, "resampled_wavs") 
	augment_repeat_numb = 3		# the number of augementation per one utterance.

	# audio(wav) configurations
	sampling_rate = 22050	# target sampling rate
	max_wav_value = 32768.0

	# # of threads
	num_jobs = 10		# how many thread will you use
