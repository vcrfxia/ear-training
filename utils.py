import random

import mingus.core.intervals as intervals
import mingus.core.keys as keys
import mingus.core.notes as notes


def learn(option_names, play_func):
	assert len(option_names) <= len(ANSWER_INPUTS)
	prompt = _get_prompt(option_names)

	input_to_choice = _get_intput_to_choice(len(option_names))
	while True:
		choice = None
		while choice is None:
			choice = input_to_choice(raw_input(prompt))

		key = random_key()
		print key

		play_func(choice, key)

def quiz(option_names, play_func):
	assert len(option_names) <= len(ANSWER_INPUTS)
	prompt = _get_prompt(option_names)

	while True:
		key = random_key()
		print key
		choice = random.randrange(len(option_names))

		play_func(choice, key)
		answer = raw_input(prompt)

		if answer == ANSWER_INPUTS[choice]:
			print 'Correct!'
		else:
			print 'Whoops, ' + option_names[choice]

ANSWER_INPUTS = ['p', '[', ']', ';', '\'', '.', '/']
def _get_intput_to_choice(num_answers):
	lookup = {v:k for k,v in enumerate(ANSWER_INPUTS[:num_answers])}
	def _input_to_choice(answer_input):
		if answer_input in lookup:
			return lookup[answer_input]
		print 'Invalid input.'
		return None
	return _input_to_choice

def _get_prompt(option_names):
	return ' / '.join([option_names[i] + ' (' + ANSWER_INPUTS[i] + ')' for i in range(len(option_names))]) + ' ?'


def random_key():
	return random.choice(keys.major_keys)

def make_ascending(chord, octave=4):
	reduced_chord = [notes.reduce_accidentals(n) for n in chord]

	new_chord = [_add_octave_to_name(reduced_chord[0], octave)]
	for i in range(1, len(chord)):
		if reduced_chord[i-1] == 'C' and reduced_chord[i] != 'C':
			pass
		elif intervals.measure(chord[i-1], chord[i]) == intervals.measure(chord[i-1], 'C') + intervals.measure('C', chord[i]):
			octave += 1
		new_chord.append(_add_octave_to_name(reduced_chord[i], octave))

	return _rewrite_names(new_chord, chord)

def _add_octave_to_name(note, octave):
	return note + '-' + str(octave)

## notes_with_octaves: notes have octaves
## note_names: notes do not have octaves, but are the same as those in <notes_with_octaves>
## returns chord where notes have octaves, and note names are those in <note_names> 
def _rewrite_names(notes_with_octaves, note_names):
	assert len(notes_with_octaves) == len(note_names)
	return [_rewrite_name(notes_with_octaves[i], note_names[i]) for i in xrange(len(notes_with_octaves))]
def _rewrite_name(note_with_octave, note_name):
	current_note, octave = note_with_octave.split('-')
	octave = int(octave)

	assert current_note == notes.reduce_accidentals(current_note), 'current_note: ' + current_note
	assert notes.is_enharmonic(current_note, note_name)

	## assuming sharps, flats, double sharps, and double flats are the only accidentals
	## <note_name> could have, then these are the only edges cases of interest:
	if current_note[0] == 'B' and note_name[0] == 'C':
		return _add_octave_to_name(note_name, octave + 1)
	elif current_note[0] == 'C' and note_name[0] == 'B':
		return _add_octave_to_name(note_name, octave - 1)
	else:
		return _add_octave_to_name(note_name, octave)
