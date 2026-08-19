import mistletoe

with open ('exemple.md', 'r') as fin:
    rendered = mistletoe.markdown(fin)
    print(rendered)