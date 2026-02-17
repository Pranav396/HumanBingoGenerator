from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from random import shuffle
from pypdf import PdfWriter
from os import remove

# Japanese Font
pdfmetrics.registerFont(TTFont("Noto Sans JP", "./NotoSansJP.ttf"))

WIDTH = 792
HEIGHT = 612
boxBottomY = 0.05 * HEIGHT
boxTopY = round(0.85 * HEIGHT, 1)
boxLeftX = 11
boxRightX = 781
boxWidth = (boxRightX - boxLeftX) / 5

prompts = {"ペットを飼っている!": "Has a pet!", "仕事がある!": "Employed!", "好きな歌手は同じ!": "Likes the same artists!",
           "楽器がやれる!": "Can play an instrument!", "スポーツをする!": "Plays a sport!", "二つ以上言語が話せる!": "Trilingual or better!",
           "海外に引っ越したことある!": "Has moved abroad!", "家族は5人以上!": "Family is larger than five!", "下の名前が二つある!": "Has two first names!",
           "好きな番組は同じ!": "Likes the same shows!", "演じたことがある!": "Has acted before!", "骨折したことがある!": "Has had a fracture!",
           "今日作った友達!": "A new friend!", "今サンリオ商品を持ってる!": "Has a Sanrio item on them!", "有名人に会ったことある!": "Has met a celebrity!",
           "タトゥーがある!": "Has tattoos!", "好きなポケモンは同じ!": "Likes the same Pokémon!", "好きな本か漫画は同じ!": "Likes the same books!",
           "好きなゲームは同じ!": "Likes the same games!", "料理ができる!": "Can cook!", "酒好きです!": "Likes to drink (alcohol)!",
           "趣味は同じ!": "Same hobbies!", "最近コンサートに行った!": "Went to a concert recently!", "先学期参加したメンバー!": "A Fall 2025 JCC regular!",
           "アレルギーがある!": "Has an allergy!"}

promptsKeys = list(prompts.keys())
mergerList = []

def makePage(iteration):
    c = canvas.Canvas(f"Test{iteration}.pdf", pagesize=(WIDTH, HEIGHT))
    mergerList.append(f"Test{iteration}")
    c.setFont('Noto Sans JP', 36)
    c.setAuthor('Pranav Kalingeri Rao')

    # Heading
    c.drawCentredString(0.5 * WIDTH, 0.90 * HEIGHT, "JCCの人間ビンゴ")
    c.setFontSize(12)

    # Lines
    vCounter = boxLeftX
    while (vCounter <= boxRightX):
        c.line(vCounter, boxBottomY, vCounter, boxTopY)
        vCounter += (boxRightX - boxLeftX) / 5
    hCounter = boxBottomY
    while (hCounter <= boxTopY):
        c.line(boxLeftX, hCounter, boxRightX, hCounter)
        hCounter += 0.16 * HEIGHT # From (0.85 - 0.05) / 5.

    # Text
    for i, prompt in enumerate(promptsKeys):
        xAdjustment = boxLeftX + boxWidth * (i % 5)
        yAdjustment = boxTopY - (0.16 * HEIGHT) * (i // 5)
        c.drawCentredString(xAdjustment + boxWidth / 2, yAdjustment - 18, prompt)
        c.drawCentredString(xAdjustment + boxWidth / 2, yAdjustment - 36, prompts[prompt])
        c.drawString(11, 0.02 * HEIGHT, f"Set {iteration + 1}")

    c.showPage()
    c.save()

def controlledShuffle():
    shuffle(promptsKeys)
    freeSpaceIndex = promptsKeys.index("今日作った友達!")
    promptsKeys[12], promptsKeys[freeSpaceIndex] = promptsKeys[freeSpaceIndex], promptsKeys[12]

def merge():
    m = PdfWriter()
    for file in mergerList:
        m.append(file + ".pdf")
    m.write("./Bingo Cards.pdf")

def clean():
    for file in mergerList:
        remove(file + ".pdf")

def makeSet(numPages):
    for i in range(numPages):
        controlledShuffle()
        makePage(i)
    merge()
    clean()

makeSet(50)