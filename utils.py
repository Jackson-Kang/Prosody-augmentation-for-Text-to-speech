from multiprocessing import Pool
from tqdm import tqdm

import os, glob
import ffmpeg

def get_path(*args):
	return os.path.join('', *args)

def create_dir(*args):
	path = get_path(*args)
	if not os.path.exists(path):
		os.mkdir(path)
	return path

def get_speech_path(root_dir):
	paths = glob.glob(get_path(root_dir, "**/*.wav"), recursive=True)
	return paths

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


def save_wav(savepath):
	pass


def do_multiprocessing(job, tasklist, num_jobs=8):
	p = Pool(num_jobs)
	with tqdm(total=len(tasklist)) as pbar:
		for _ in tqdm(p.imap_unordered(job, tasklist)):
			pbar.update()	
