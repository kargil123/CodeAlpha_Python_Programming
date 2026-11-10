import re
from pathlib import Path

INPUT_FILE = Path("sample_text.txt")
OUTPUT_FILE = Path("extracted_emails.txt")

EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+"
)


def extract_emails():
    if not INPUT_FILE.exists():
        print(f"Input file '{INPUT_FILE}' was not found.")
        print("Create it and add some text containing email addresses, then run again.")
        return

    text = INPUT_FILE.read_text(encoding="utf-8")
    emails = sorted(set(EMAIL_PATTERN.findall(text)), key=str.lower)

    OUTPUT_FILE.write_text(
        "\n".join(emails) + ("\n" if emails else ""),
        encoding="utf-8"
    )

    print(f"Found {len(emails)} unique email address(es).")
    print(f"Results saved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    extract_emails()
