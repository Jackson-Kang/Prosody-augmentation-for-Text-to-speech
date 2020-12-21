# Prosody-augmentation-for-Text-to-speech
Simple tool for speech dataset augmentation for modeling various prosodies.

# Introduction
Modeling various prosodies (such as pitch, speed and etc) is very important for natural and human-like speech generation. In the technological perspective, modeling various prosodies can be hard when we use dataset with little prosody variations. For example, the [LJSpeech dataset](https://keithito.com/LJ-Speech-Dataset/) which is popularly used to various TTS model has little prosody variations and this makes TTS-model (like [FastSpeech2](https://arxiv.org/pdf/2006.04558.pdf) or other prosody-controllable model) produce awkward speech.
To relieve seriousness of the problem, one may think prosody augmentation for utterances. Thus, I implemented simple prosody augmentation tool for Text-to-speech(TTS) model, using conventional signal-processing algorithms provided by [librosa](https://github.com/librosa/librosa) and others. **This tool currently offers following prosody augmentation methods**:
* **Pitch only**
* **Speed(duration of utterance) only**
* **Pitch and speed**

Other prosody augmentation method will be added later.

# Install dependencies
Install dependencies via following command:
```
# python 3.7

# install ffmpeg
sudo apt-get install ffmpeg

# install python packages
pip install -r requirements.txt
```

# How-to-use
(1) edit ```config.py```
- write your dataset paths in the list-variable ```wav_paths```.
- change ```augment_repeat_numb```, ```sampling_rate``` and ```num_jobs``` value

(2) run ```main.py``` via following command:
```
python main.py <argv[1]> <[argv]2>
# ex) python main.py 1 1
```
* If argv[1] is 1, convert sampling rate using ffmpeg. (By default, sampling rate of whole dataset will be converted to 22050.)
* If argv[2] is 1, run prosody-augmentation.

(3) check augmentation results
After running, you may see **two directories** in the ```preprocessed``` directory.
* resampled_wavs: contain the utterances resampled to ```sampling_rate``` if you activate argv[1]-option.
* **augmented_wavs**: contain the prosody-augmented dataset if you activate argv[2]-option. (You may want this directory.)

# References
* [Sound-augmentation-librosa](https://www.kaggle.com/huseinzol05/sound-augmentation-librosa)
