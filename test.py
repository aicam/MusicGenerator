import pygame
from midiutil import MIDIFile

def generate_happy_song():
    # Set the parameters for the MIDI file
    num_tracks = 1
    tempo = 120
    time_signature = 4/4

    # Set the pitches for the happy melody
    happy_pitches = [
        60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79,
        81, 83, 84, 83, 81, 79, 77, 76, 74, 72, 71, 69
    ]

    # Create a MIDIFile object with the specified parameters
    midi = MIDIFile(num_tracks)
    midi.addTempo(track=0, time=0, tempo=tempo)
    midi.addTimeSignature(track=0, time=0, numerator=4, denominator=4,clocks_per_tick=2)

    # Generate the melody with the happy pitches
    note_duration = 1  # Duration of each note in beats
    for i, pitch in enumerate(happy_pitches):
        velocity = 80  # Velocity of each note
        start_time = i * note_duration
        end_time = start_time + note_duration
        midi.addNote(track=0, channel=0, pitch=pitch, time=start_time, duration=note_duration, volume=velocity)

    # Save the MIDI file
    filename = "happy_song.mid"
    with open(filename, "wb") as output_file:
        midi.writeFile(output_file)

    return filename

# Generate a happy song and get the filename
filename = generate_happy_song()

# Initialize Pygame and set up the MIDI output
pygame.init()
pygame.mixer.init()

# Load the MIDI file
pygame.mixer.music.load(filename)

# Play the MIDI file
pygame.mixer.music.play()

# Wait until the playback finishes
while pygame.mixer.music.get_busy():
    continue

# Clean up and exit
pygame.mixer.music.stop()
pygame.quit()
