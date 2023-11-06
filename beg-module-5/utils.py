import numpy as np
from scipy.io.wavfile import write, read
import matplotlib.pyplot as plt

samplerate = 44100

def plot_fft(data, title='FFT', save=False):
	"""
	Plots the fast Fourier transform of a standard WAV-form (44.1 KHz sample rate).

	Parameters:
		data: 	waveform as array
		title: 	title of plot
		save: 	if true, saves the plot as fft.png

	Returns: None
	"""
	n = len(data)
	ft = np.abs(np.fft.fft(data))
	f = np.fft.fftfreq(n)*samplerate
	
	f = f[:int(n/2)]
	ft = ft[:int(n/2)]
	
	fig, ax = plt.subplots(figsize=(8, 3))
	ax.plot(f, ft)
	ax.set_xlabel('Frequency (Hz)')
	ax.set_ylabel('Fourier Coefficient (arb. unit)')
	ax.set_title(title)
	ax.set_xlim(0, 220*16)
	ax.set_xticks([220*i for i in range(16)])
	plt.show()    
	fig.savefig('fft.png', dpi=300, bbox_inches='tight')
	
def fft(data):
	"""
	Calculates fast Fourier transform.

	Parameters:
		data: 	waveform as array

	Returns:
		f, fft: the frequencies and Fourier transform values
	"""
	n = len(data)
	ft = np.abs(np.fft.fft(data))
	f = np.fft.fftfreq(n)*samplerate
	
	f = f[:int(n/2)]
	ft = ft[:int(n/2)]

	return f, ft

def save(data, filename='out/tone.wav'):
	"""
	Saves waveform as out/tone.wav (default)

	Parameters:
		data: 		waveform as array
		filename: 	file location

	Returns: None
	"""
	write(filename, samplerate, data.astype(np.int16))


def input(filename):
	"""
	Reads in WAV file as array.

	Parameters:
		filename: file location

	Returns: list
	"""
	samplerate, data = read(filename)
	return data

equal_temp = {
	'C': 16.35160,
	'C#': 17.32391, 'Db': 17.32391,
	'D': 18.35405,
	'D#': 19.44544, 'Eb': 19.44544,
	'E': 20.60172,
	'F': 21.82676,
	'F#': 23.12465, 'Gb': 23.12465,
	'G': 24.49971,
	'G#': 25.95654, 'Ab': 25.95654,
	'A': 27.50000,
	'A#': 29.13524, 'Bb': 29.13524,
	'B': 30.86771
}

def f(note):
	"""
	Returns the equal-tempermant frequency of a given note.

	Parameters:
		note: in "scientific notation"

	Returns: frequency

	>>> f('A4')
	440.0
	"""
	if note=='':
		return 0
	tone = equal_temp[note[:-1]]
	tone *= 2**int(note[-1:])
	return tone

def pachelbel_canon_D(tvetone, timbre, mono=False):
	"""
	Generates the first 14 bars of Pachelbels Canon in D with the user specified tone-generating function

	Parameters:
		tvetone: tone-generating function in the module 5, 3a exercise
		timbre: timbre profile determined in the module 5, 1c exercise
		mono: toggles mono/stereo audio. With headphones, the music sounds better in stereo

	Returns: None
	"""
	def add_instrument(notes, times, tempo=60, amp=1, data=[]):
	    """
	    Parameters:
	        notes: notes in "scientific notation"
	        times: duration of each note in 1/8 beats
	        tempo: in beats per min
	        data: existing score to add on
	        
	    """
	    notes = np.array(notes)
	    times = np.array(times)
	    # time of 32nd note in secs
	    t32 = 60/(tempo*8) 
	    n32 = int(t32*samplerate)
	        
	    if len(data)==0:
	        n = n32*np.sum(times)
	        data = np.zeros(n)

	    n = n32*times
	    index = np.cumsum(n)
	    index = np.insert(index, 0, 0)
	        
	    for i in range(len(notes)):
	        data[index[i]:index[i+1]] += amp*tvetone(n[i], f(notes[i]), timbre, 6, 0.5, 0.05, 0.15)
	    return data

	print('Canon in D for 4 cellos (15 bars)')
	if mono:
		print("***MONO AUDIO: if you're listening WITH headhones, set mono=False")
		amps = 1.6*np.array([0.15, 0.35, 0.15, 0.1])
	else:
		print("***STEREO AUDIO: if you're listening WITHOUT headhones, set mono=True\n")
		amps = 1.6*np.array([0.3, 0.35, 0.3, 0.3])
	
	print('Generating cello 1 part...', end='')
	notes = np.array(['D3', 'A2', 'B2', 'F#2', 'G2', 'D2', 'G2', 'A2']*7) # much excite
	times = np.array([8, 8, 8, 8, 8, 8, 8, 8]*7)

	left = add_instrument(notes, times, 60, amp=amps[0])
	print('done')

	print('Generating cello 2 part...', end='')
	notes = ['',
	        'F#4', 'E4', 'D4', 'C#4',
	        'B3', 'A3', 'B3', 'C#4', 
	        'D4', 'C#4', 'B3', 'A3',
	        'G3', 'F#3', 'G3', 'E3',
	        'D3', 'F#3', 'A3', 'G3', 'F#3', 'D3', 'F#3', 'E3',
	        'D3', 'B2', 'D3', 'A3', 'G3', 'B3', 'A3', 'G3',
	        'F#3', 'D3', 'E3', 'C#4', 'D4', 'F#4', 'A4', 'A3',
	        'B3', 'G3', 'A3', 'F#3', 'D3', 'D4', 'D4', 'C#4',
	        'D4', 'C#4', 'D4', 'D3', 'C#3', 'A3', 'E3', 'F#3', 'D3', 'D4', 'C#4', 'B3', 'C#4', 'F#4', 'A4', 'C#5',
	        'G4', 'F#4', 'E4', 'G4', 'F#4', 'E4', 'D4', 'C#4', 'B3', 'A3', 'G3', 'F#3', 'E3', 'G3', 'F#3', 'E3',
	        'D3', 'E3', 'F#3', 'G3', 'A3', 'E3', 'A3', 'G3', 'F#3', 'B3', 'A3', 'G3', 'A3', 'G3', 'F#3', 'E3',
	        'D3', 'B2', 'B3', 'C#4', 'D4', 'C#4', 'B3', 'A3', 'G3', 'F#3', 'E3', 'B3', 'A3', 'B3', 'A3', 'G3']
	times = [64, 
	        8, 8, 8, 8,
	        8, 8, 8, 8, 
	        8, 8, 8, 8,
	        8, 8, 8, 8,
	        4, 4, 4, 4, 4, 4, 4, 4,
	        4, 4, 4, 4, 4, 4, 4, 4,
	        4, 4, 4, 4, 4, 4, 4, 4,
	        4, 4, 4, 4, 4, 4, 6, 2,
	        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
	        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
	        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
	        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
	right = add_instrument(notes, times, 60, amp=amps[1])
	print('done')

	print('Generating cello 3 part...', end='')
	notes = notes[:81] # it is a canon after all...
	times = times[:81]
	times[0] = 128
	left = add_instrument(notes, times, 60, amp=amps[2], data=left)
	print('done')

	print('Generating cello 4 part...', end='')
	notes = notes[:49]
	times = times[:49]
	times[0] = 192
	right = add_instrument(notes, times, 60, amp=amps[3], data=right)
	print('done')

	if mono:
		save(left+right, filename='out/Pachelbel_Canon_D.wav') 
	else:
		save(np.column_stack((left, right)), filename='out/Pachelbel_Canon_D.wav')


