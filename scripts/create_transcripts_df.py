import pandas as pd
import os
from tqdm import tqdm
import time

# Set the directory containing the audio files
audio_dir = './transcripts/data'

# Create an empty list to store the transcriptions and file paths
transcripts = []

# Time the execution
start = time.time()

# Loop through all the files in the directory
for j, (root, dirs, files) in tqdm(enumerate(os.walk(audio_dir))):
    for file in files:
        # Check if the file is a Text file
        if file.endswith('.txt'):
            # Get root path
            abs_root = os.path.abspath(root)
            # Get the file path
            file_path = os.path.join(abs_root, file)
            # Open text file with the same name as the audio file
            with open(file_path, "r") as f:
                # Read the transcription
                transcription = f.read()
            # Add the transcription and file path to the list
            transcripts.append({'transcription': transcription, 'file_path': file})

# Create a dataframe from the list of transcriptions
df = pd.DataFrame(transcripts)

# Save the dataframe to a csv file
df.to_csv('./transcripts/transcripts.csv', index=False)

# Print the time taken to execute the script
print(f"Time taken: {time.time() - start} seconds")