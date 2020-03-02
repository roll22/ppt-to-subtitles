import os
import re

directory = 'D:\\Cantarile Evangheliei 16_9\\pptx\\txt'


def split_text(path):
    with open(path, mode="r", encoding="cp1250") as fp:
        text = fp.read()
        # print(text)
        strofe = text.split("\n\n")
        lines = []
        writable = ''
        for strofa in strofe:
            lines = strofa.split("\n")
            if len(lines) % 2 != 0:
                lines.append("")
            for i in range(0, len(lines), 2):
                writable += lines[i] + "\n" + lines[i + 1] + "\n\n"

        writable = re.sub(r'(\n\n\n)+', r'\n\n', writable)
        # print(writable)
        with open("new/" + path, mode="w", encoding="utf-16") as wp:
            wp.write(writable)


for filename in os.listdir(directory):
    if filename.endswith(".txt"):

        path = filename
        split_text(path)
        continue
    else:
        continue

# split_text("230.txt")
