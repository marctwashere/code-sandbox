import os
from pydub import AudioSegment
from pydub.utils import which
import imageio_ffmpeg as ffmpeg

# Set the environment variable to the ffmpeg binary installed by imageio
ffmpeg_path = ffmpeg.get_ffmpeg_exe()
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)

# Explicitly set the ffmpeg path for pydub
AudioSegment.converter = ffmpeg_path

# Directory containing the audio files
directory = "output"

# Function to extract the numeric part of the filename for sorting
def extract_number(filename):
    return int(''.join(filter(str.isdigit, filename)))

# Get a list of audio files in the directory, ordered numerically
audio_files = sorted(
    [f for f in os.listdir(directory) if f.endswith('.mp3')],
    key=extract_number
)

print(audio_files)

# Initialize an empty AudioSegment
combined = AudioSegment.empty()

# Loop through each audio file and append it to the combined AudioSegment
for file in audio_files:
    audio_path = os.path.join(directory, file)
    audio = AudioSegment.from_file(audio_path)
    combined += audio

# Export the combined audio file
combined.export("combined_audio.mp3", format="mp3")

print("Combined audio saved as combined_audio.mp3")