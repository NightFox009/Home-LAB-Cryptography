from collections import Counter

data = open("aes.bmp.enc", "rb").read()

for start in (0, 54):
    chunk = data[start:]
    blocks = [chunk[i:i+16] for i in range(0, len(chunk) - 15, 16)]
    counts = Counter(blocks)
    print(f"--- starting at byte {start} ---")
    print("Total blocks:", len(blocks))
    print("Unique blocks:", len(counts))
    for block, n in counts.most_common(3):
        print(" ", block.hex(), n)
