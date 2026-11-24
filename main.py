import os

LETTER = "A"


def main():
    # Coffee or tea: the answer is one of the two offered letters.
    assert LETTER in ("A", "B"), LETTER
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
