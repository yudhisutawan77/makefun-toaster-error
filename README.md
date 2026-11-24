# The Funniest Toaster Error Message

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/yudhisutawan77/makefun-toaster-error/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/yudhisutawan77/makefun-toaster-error/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

Entry for the [make.fun bounty "The Funniest Toaster Error Message"](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd): one line, at most 120 characters — the error message a kitchen toaster shows its owner when something goes wrong.

## The entry

> ERROR: Toast ejected early. It saw what you spread on it yesterday.

**67 characters** — well inside the 120-character limit.

## Why this line

Deadpan appliance voice, one clear twist at the end: the toast didn't burn, it *left* — and the reason is something the owner did yesterday. No tired "burnt toast" pun; the surprise comes from the toast having an opinion about the spread. It reads like a real appliance error on first read, and every word earns its place.

## How it works

`main.py` writes the single line to `/output/entry.txt` and validates it first: 1–120 characters, one line, no leading/trailing whitespace. It exits non-zero if the line is ever out of bounds.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
