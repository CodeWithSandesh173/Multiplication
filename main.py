import os

os.makedirs("mal", exist_ok=True)

def mul():
    for i in range(1, 100000):
        with open(f"mal/{i}.txt", "w") as f:
            for k in range(1, 11):
                f.write(f"{i} x {k} = {i*k}\n")

mul()
