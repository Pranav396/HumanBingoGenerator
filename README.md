# Human Bingo Generator

A Python tool that generates randomized Human Bingo cards as a PDF for use at Rutgers University Japanese Conversation Club events. Built to replace an external website that lacked the customization needed for JCC's specific prompts and bilingual (Japanese/English) format.

## How It Works

Each card is a 5×5 grid of randomized prompts in both Japanese and English. The "今日作った友達!" free space is always placed in the center. Cards are generated as individual PDFs, merged into a single file, and the intermediates are cleaned up automatically.

Running `makeSet(50)` at the bottom of the script generates 50 unique cards into `Bingo Cards.pdf`.

## Usage

```bash
pip install -r requirements.txt
python Bingo.py
```

## Note

The prompts and layout are tailored specifically for JCC events and are not intended as a general-purpose tool.
