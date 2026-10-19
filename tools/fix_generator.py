# -*- coding: utf-8 -*-
import re

with open('E:/Sites/bambino-kids-fashion/generate_all_pages.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace `html = f"""` with `html = """`
# Replace `{header}` with `__HEADER__`
# Replace `{footer}` with `__FOOTER__`
# Replace `f.write(html)` with `f.write(html.replace('__HEADER__', header).replace('__FOOTER__', footer))`

text = text.replace('{header}', '__HEADER__').replace('{footer}', '__FOOTER__')
text = text.replace('html = f"""', 'html = """')
text = text.replace('f.write(html)', "f.write(html.replace('__HEADER__', header).replace('__FOOTER__', footer))")

with open('E:/Sites/bambino-kids-fashion/generate_all_pages.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("generate_all_pages.py fixed successfully!")
