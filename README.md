[![make.fun · u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/ZhaoMakefun/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/ZhaoMakefun/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

# The Houseplant Out-of-Office

A fern's out-of-office auto-reply, told in flat office voice: it has been out of the office since March, and nobody has watered it since March. The joke comes from the plant's own life — the long stretch of being ignored — rather than from a pun, and it lands in 108 characters.

Entry: "I am out of the office. I have been out of the office since March. Nobody has watered me since March. — Fern"

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` (Python 3, standard library only, no network) writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`), validates it against the 1–120 character gate, and reads it back to confirm the file holds exactly the entry text.
