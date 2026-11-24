"""The Funniest Out-of-Office — R1 entry: "The Car Park".

Writes one line of an out-of-office auto-reply to /output/entry.txt.
Gate: UTF-8, 1 to 140 characters, not only whitespace.
Stdlib only.
"""

import os

LINE = "I'm not on holiday. I'm in the car park, reading your email and choosing not to answer it."


def main() -> None:
    text = LINE
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, gate is 1-140"
    # Reversal test (keeper reasoning): the last beat, "choosing not to answer
    # it", redefines the earlier beats — "reading your email" becomes
    # surveillance, not diligence, and "I'm not on holiday" a confession of
    # intent, not a location correction.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    written = open("/output/entry.txt", "rb").read()
    assert written == text.encode("utf-8"), "entry.txt bytes differ from LINE"
    assert b"\n" not in written, "entry must be a single line"
    print(f"entry.txt: {len(written)} bytes, {len(text)} chars, gate OK")


if __name__ == "__main__":
    main()
