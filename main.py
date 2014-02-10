import pydub
import random

drums = pydub.AudioSegment.from_wav("amen.wav")
#half = drums[:len(drums)/2]
#half.export("test.wav", format="wav")

fast = pydub.effects.speedup(drums, chunk_size=50)
chopped = []
slice_length = len(fast) /16
for n in range(1,16):
    chopped.append(fast[(n-1) * slice_length:n * slice_length])
random.shuffle(chopped)
final_drums = chopped[random.randint(0,14)] + chopped[random.randint(0,14)] + chopped[random.randint(0,14)] + chopped[random.randint(0,14)] + chopped[random.randint(0,14)] + chopped[random.randint(0,14)] + chopped[random.randint(0,14)] + chopped[random.randint(0,14)] + chopped[random.randint(0,14)]
final_drums.export("test_random.wav", format="wav")