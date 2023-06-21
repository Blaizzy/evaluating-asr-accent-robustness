import matplotlib.pyplot as plt

with open("assemblyai_times.txt") as f:
    data1 = f.readlines()

data1 = [float(x.strip()) for x in data1]

with open("times.txt") as f:
    data2 = f.readlines()

data2 = [float(x.strip()) for x in data2[:10]]

plt.plot(data1)
plt.plot(data2)
plt.ylabel('Time (s)')
plt.xlabel('Index')
plt.title('AssemblyAI vs Wav2vec2.0\n Inference Times')
plt.legend(['AssemblyAI', 'Wav2vec2.0'])
plt.show()