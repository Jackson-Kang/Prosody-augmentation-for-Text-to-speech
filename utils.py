from multiprocessing import Pool
from tqdm import tqdm
from configs import Arguments as args

from scipy.io.wavfile import read, write

import os, glob
import ffmpeg


p = Pool(args.num_jobs)

def get_path(*args):
	return os.path.join('', *args)

def create_dir(*args):
	path = get_path(*args)
	if not os.path.exists(path):
		os.mkdir(path)
	return path

def get_speech_path(root_dir, file_extension=".wav"):
	return glob.glob(get_path(root_dir, "**/*{}".format(file_extension)), recursive=True)

def resample_wav(wav_names):
	in_wav_name, out_wav_name, sampling_rate  = wav_names
	if not os.path.exists(out_wav_name):
		try:
			out, err = (ffmpeg
					.input(in_wav_name)
					.output(out_wav_name, acodec='pcm_s16le', ac=1, ar=sampling_rate)
					.overwrite_output()
					.run(capture_stdout=True, capture_stderr=True))
		except ffmpeg.Error as err:
			print(err.stderr, file=sys.stderr)
			raise


def read_wav(path, args_sampling_rate):
	sampling_rate, audio = read(path)
	assert args_sampling_rate == sampling_rate, "[ERROR] args.sampling_rate({}) is different from audio sampling rate({}).".format(args_sampling_rate, sampling_rate)
	return audio

def write_wav(savepath, audio, sampling_rate):
	write(savepath, sampling_rate, audio)


def do_multiprocessing(job, tasklist, num_jobs):
	p = Pool(num_jobs)
	with tqdm(total=len(tasklist)) as pbar:
		for _ in tqdm(p.imap_unordered(job, tasklist)):
			pbar.update()	
