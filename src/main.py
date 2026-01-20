import argparse
from datetime import datetime


def build_message(name: str, lang: str) -> str:
    hour = datetime.now().hour

    if hour < 12:
        time_greeting = "Good morning"
    elif hour < 18:
        time_greeting = "Good afternoon"
    else:
        time_greeting = "Good evening"

    lang = (lang or "en").lower()

    if lang == "bs":
        return f"{time_greeting}! Ja sam {name}."
    if lang == "es":
        return f"¡{time_greeting}! Me llamo {name}."
    return f"{time_greeting}! My name is {name}."


def main() -> None:
    parser = argparse.ArgumentParser(description="A simple greeting CLI.")
    parser.add_argument("--name", default="Vedad", help="Your name")
    parser.add_argument("--lang", default="en", help="Language: en, bs, es")
    args = parser.parse_args()

    print(build_message(args.name, args.lang))


if __name__ == "__main__":
    main()
