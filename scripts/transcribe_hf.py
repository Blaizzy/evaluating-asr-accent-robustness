import os
import time
from transformers import pipeline

# Loading percetange with tqdm
from tqdm import tqdm

# Create a transcriber object.
transcriber = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")

# Create a folder to store the transcripts
os.makedirs("./transcripts", exist_ok=True)

list_of_times = []

# Loop through all the files within subfolders in the data directory using tqdm
for root, dirs, files in tqdm(os.walk("data")):
    for i, file in tqdm(enumerate(files)):
        if i <= 10:
            # Check if the file is a wav file
            if file.endswith(".wav"):
                # Get root path
                abs_root = os.path.abspath(root)

                # Extract the file path
                file_path = os.path.join(abs_root, file)

                # Start timing
                start_time = time.time()

                # Transcribe the audio file
                transcript = transcriber(file_path)

                # Stop timing
                end_time = time.time()

                # Calculate the time taken
                time_taken = end_time - start_time

                # Print the time taken
                print(f"Time taken: {time_taken}")

                list_of_times.append(time_taken)
                
            
            # # Remove the absolute root path from the file path
            # file_path = file_path.replace(abs_root, root)

            # # remove the .wav suffix
            # file_path = file_path.replace(".wav", "")

            # # Create a folder to store the transcript
            # os.makedirs(f"./transcripts/{root}", exist_ok=True)

            # # save the transcription to a file with the same name as the audio file.
            # if "text" in transcript:
            #     with open(f"./transcripts/{file_path}.txt", "w") as f:
            #             f.write(transcript["text"])

# Save the list of times to a file
with open("times.txt", "w") as f:
    for time in list_of_times:
        f.write(f"{time}\n")