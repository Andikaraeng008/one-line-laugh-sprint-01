import os

TEXT = "I told my plants I'm going on holiday. The cactus didn't care. The fern has already started dying out of spite."

os.makedirs("/output", exist_ok=True)
assert 1 <= len(TEXT) <= 200
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
