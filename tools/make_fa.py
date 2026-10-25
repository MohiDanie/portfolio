"""Regenerate fa/index.html (Persian entry page) from index.html."""
import re, os
s = open('index.html', encoding='utf-8').read()
fa = s.replace('<html lang="en" dir="ltr">', '<html lang="fa" dir="rtl">', 1)
fa = fa.replace('<link rel="canonical" href="https://mdanaie.ir/">', '<link rel="canonical" href="https://mdanaie.ir/fa/">', 1)
fa = fa.replace('<meta property="og:url" content="https://mdanaie.ir/">', '<meta property="og:url" content="https://mdanaie.ir/fa/">\n<meta property="og:locale" content="fa_IR">', 1)
fa = re.sub(r'<title>[^<]*</title>', '<title>محدثه دانائی · طراح محصول</title>', fa, 1)
fa = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="محدثه دانائی، طراح محصول در تهران با سابقه مدیریت محصول. کیس‌استادی‌هایی در حوزه استخدام، تحلیل داده با هوش مصنوعی و آموزش.">', fa, 1)
fa = fa.replace('<!doctype html>', '<!doctype html>\n<!-- Generated from /index.html (Persian entry). Regenerate when index.html changes: python3 tools/make_fa.py -->', 1)
os.makedirs('fa', exist_ok=True)
open('fa/index.html', 'w', encoding='utf-8').write(fa)
