"""Fortune in a Pot — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one kind, funny fortune for a houseplant, 120 characters or fewer.
"""
import os

LINE = "Your leaves will grow toward the sun, your owner will finally water you on time, and the cat will leave you alone."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
