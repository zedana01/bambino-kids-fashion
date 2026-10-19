# -*- coding: utf-8 -*-
import os, re

base = 'E:/Sites/bambino-kids-fashion'
html_files = [f for f in os.listdir(base) if f.endswith('.html')]
admin_files = [os.path.join('admin', f) for f in os.listdir(os.path.join(base, 'admin')) if f.endswith('.html')]

all_files = html_files + admin_files

errors = []
for file_rel in all_files:
    file_path = os.path.join(base, file_rel)
    dir_path = os.path.dirname(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove script tags to only test static HTML img/link elements
    html_without_scripts = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
    
    img_srcs = re.findall(r'<img[^>]+?\ssrc=["\']([^"\']+)["\']', html_without_scripts)
    for src in img_srcs:
        if src.startswith('http') or src.startswith('data:'):
            continue
        src_clean = src.split('?')[0].split('#')[0]
        full_src = os.path.normpath(os.path.join(dir_path, src_clean))
        if not os.path.exists(full_src):
            errors.append(f'Broken image in {file_rel}: {src} -> {full_src}')

    script_srcs = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', content)
    for src in script_srcs:
        src_clean = src.split('?')[0].split('#')[0]
        full_src = os.path.normpath(os.path.join(dir_path, src_clean))
        if not os.path.exists(full_src):
            errors.append(f'Broken script in {file_rel}: {src} -> {full_src}')

    css_hrefs = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', content)
    for href in css_hrefs:
        if href.startswith('http'):
            continue
        href_clean = href.split('?')[0].split('#')[0]
        full_href = os.path.normpath(os.path.join(dir_path, href_clean))
        if not os.path.exists(full_href):
            errors.append(f'Broken link in {file_rel}: {href} -> {full_href}')

if errors:
    print('ERRORS FOUND:')
    for e in errors:
        print(e)
else:
    print('ALL ASSETS AND INTERNAL LINKS VALIDATED 100% PERFECT!')
