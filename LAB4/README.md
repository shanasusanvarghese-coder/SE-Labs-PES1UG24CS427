# Lab 4 – High-Low Card Predictor

## Implemented changes
- Compares cards using numeric rank values (2 through Ace), not text strings.
- Adds a consecutive-win streak multiplier: the first consecutive win earns 1 point, the second earns 2, the third earns 3, and so on.
- Treats equal-rank cards as a **PUSH**; score and streak remain unchanged.
- Briefly displays the previous and newly drawn cards side-by-side after each guess.

## Run
```bash
python3 -m pip install -r requirements.txt
python3 main.py
```

## Controls
- Press **H** or **Up Arrow** to guess Higher.
- Press **L** or **Down Arrow** to guess Lower.

## Submission videos
Add your own recorded gameplay videos to this folder:
- `Lab4_Before.mov`
- `Lab4_After.mov`
