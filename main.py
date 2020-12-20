from utils import *
from tuners import *
from configs import Arguments as args

from random import randrange

import ffmpeg
import sys


# [TO DO]	rewrite metadata.csv to record metadata of augmented dataset


def change_sampling_rate():

	save_dir = create_dir(args.save_dir)
	resampled_wav_dir = create_dir(save_dir, "resampled_wavs")

	dataset_name_list = [ wav_path.split("/")[-1] for wav_path in args.wav_paths ]
	resampled_dataset_paths = [ create_dir(get_path(resampled_wav_dir, dataset_name)) for dataset_name in dataset_name_list ]	

	all_in_wav_paths = [get_speech_path(path) for path in args.wav_paths]
	all_out_wav_paths = [list(map( lambda path: get_path(resampled_dataset_paths[idx], path.split("/")[-1]), wav_paths )) for idx, wav_paths in enumerate(all_in_wav_paths)]		

	for idx, in_wav_paths in enumerate(all_in_wav_paths):

		print("\n\t[LOG] {} / {} processed...".format(idx+1, len(all_in_wav_paths)))
		do_multiprocessing(resample_wav, list(zip(in_wav_paths, all_out_wav_paths[idx], [args.sampling_rate for _ in range(len(in_wav_paths))])))

def augment_data():

	def job(path):
	
		in_wav_path, out_wav_path = path	
		audio = read_wav(in_wav_path, args.sampling_rate)

		for _ in range(args.augment_repeat_numb):	
			augmented_audios = [	pitch_augment(audio, bins_per_octave, pitch_pm), 
						speed_augment(audio, low=0.5, high=1.8),
						pitch_and_speed_augment(audio, low=0.5, high=1.8)]
			out_wav_paths = [ out_wav_path.replace(".wav", "") + postfix + augmented_audios[idx][1] + ".wav" for idx, postfix in enumerate(("_pitch_", "_speed_", "_pitch_and_speed_"))]
			[save_wav(out_wav_paths[idx], audio[0]) for idx, audio in enumerate(augmented_audios)]
	save_dir = create_dir(args.save_dir)
	augmented_wav_dir = create_dir(save_dir, "augmented_wavs")
	dataset_name_list = [ wav_path.split("/")[-1] for wav_path in args.wav_paths ]
	augmented_dataset_paths = [ create_dir(get_path(augmented_wav_dir, dataset_name)) for dataset_name in dataset_name_list ]

	all_in_wav_paths = [get_speech_path(get_path(args.save_dir, "resampled_wavs", dataset_name)) for dataset_name in dataset_name_list]
	all_out_wav_paths = [list(map( lambda path: get_path(augmented_dataset_paths[idx], path.split("/")[-1]), wav_paths )) for idx, wav_paths in enumerate(all_in_wav_paths)]

	for idx, in_wav_paths in enumerate(all_in_wav_paths):
		print("\n\t[LOG] {} / {} processed...".format(idx+1, len(all_in_wav_paths)))
		do_multiprocessing(job, list(zip(in_wav_paths, all_out_wav_paths[idx])))


if __name__ == "__main__":

	if sys.argv[1] in ["True", True, 1, "1"]:
		print("\n[LOG] start to change sampling rate of wav-signal")
		change_sampling_rate()
	if sys.argv[2] in ["True", True, 1, "1"]:
		print("\n[LOG] start to augment prosodies of speech dataset")
		augment_data()
