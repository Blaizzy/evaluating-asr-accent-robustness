import os

# Loading percetange with tqdm
from tqdm import tqdm

import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.ASRModel.from_pretrained("nvidia/stt_en_conformer_transducer_xlarge")

transcriptions = asr_model.transcribe(["data/american/speaker_01/american_s01_001.wav"])

print(transcriptions)