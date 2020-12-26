from emojis.db.db import EMOJI_DB


def main():
    completions = []
    for emoji in EMOJI_DB:
        for alias in emoji.aliases:
            completions.append({"word": alias, "kind": emoji.emoji})

    print(f"EMOJI_LIST={completions}")


if __name__ == "__main__":
    main()
