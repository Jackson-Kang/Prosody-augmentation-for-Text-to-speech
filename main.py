from utils import *
from configs import Arguments as args

import ffmpeg
import sys


def change_sampling_rate():


	save_dir = create_dir(args.save_dir)
	resampled_wav_dir = create_dir(save_dir, "resampled_wavs")

	dataset_name_list = [ wav_path.split("/")[-1] for wav_path in args.wav_paths ]
	resampled_dataset_paths = [ create_dir(get_path(resampled_wav_dir, dataset_name)) for dataset_name in dataset_name_list ]	

	all_in_wav_paths = [get_speech_path(path) for path in args.wav_paths]
	all_out_wav_paths = [list(map( lambda path: get_path(resampled_dataset_paths[idx], path.split("/")[-1]), wav_paths )) for idx, wav_paths in enumerate(all_in_wav_paths)]	
	


	for idx, in_wav_paths in enumerate(all_in_wav_paths):

		print("\t[LOG] {} / {} processed...".format(idx, len(all_in_wav_paths)))

		do_multiprocessing(resample_wav, list(zip(in_wav_paths, all_out_wav_paths[idx], [args.sampling_rate for _ in range(len(in_wav_paths))])), num_jobs=args.num_jobs)	





def augment_data():
	pass




if __name__ == "__main__":

	if sys.argv[1] in ["True", True, 1, "1"]:
		print("\n[LOG] start to change sampling rate of wav-signal")
		change_sampling_rate()
	if sys.argv[2] in ["True", True, 1, "1"]:
		print("\n[LOG] start to augment prosodies of speech dataset")
		augment_data()
