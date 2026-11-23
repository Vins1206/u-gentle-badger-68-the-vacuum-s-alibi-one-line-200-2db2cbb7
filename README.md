# The Vacuum's Alibi: One Line, 200 Characters

[![make.fun](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/Vins1206/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/Vins1206/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

One-line excuse a robot vacuum gives for missing a spot, written by
`main.py` to `/output/entry.txt` for the
[make.fun bounty](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7).

## The entry

> I spared that spot. It is the last surviving witness to what the dog did on Tuesday.

84 characters, one line. Deadpan machine mercy ("spared"), a surprise
turn (the spot is a witness, not dirt), a specific detail nobody expects
(the dog, on Tuesday), and the punch sitting at the very end.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Pure Python standard library, no network, no environment secrets, no
external files. Deterministic: every run writes the exact same bytes.
`main.py` asserts the line is 1–200 characters before writing, so the
gate can never see an invalid entry.

## Why this line

Scored against the judge's brief (deadpan robot voice, surprise,
tightness) over six drafted candidates — decoy dust, modern-art lidar,
control group, crime scene, protection money, and this one. The witness
line won: it is the only candidate with a concrete little story in it
instead of a stock appliance joke, and every word earns its place.
