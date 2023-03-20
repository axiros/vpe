#!/usr/bin/env python
"""
# Use 'translate' to translate sentences

`translate en;fr: That parrot is dead!`

Default language, when not give: English
Default source lang, when not given: $VPE_SRC_LANG, default: de

## Requirements

1. pip install translate
2. translate-cli within your $PATH

## Note

The results seem better than those from googletrans (pip install googletrans==4.0.0rc1)
so we don't even offer that as alternative.
"""

from share import notify, vim, wrap_text_result
import os


def from_picker(word):
    res = try_load(word)
    return res


src_lang = os.environ.get('VPE_SRC_LANG', 'de')


def parse(line):
    lang = line[:9].split(':')
    if len(lang) == 1:
        slang, lang = src_lang, 'en'
    else:
        lang, line = [i.strip() for i in line.split(':', 1)]
        if ';' not in lang:
            slang, lang = '', 'en'
        else:
            slang, lang = [i.strip() for i in lang.split(';', 1)]
    slang = f'-f "{slang}"' if slang else ''
    return line, slang, lang


def try_load(line, **kw):

    line, slang, lang = parse(line)
    cmd = f'translate-cli {slang} -t "{lang}" "{line}"'

    s = os.popen(cmd).read().strip()
    if not s:
        if not os.popen('type translate-cli').read().strip():
            raise Exception('Required: pip install translate + translate-cli into $PATH')
        s = 'not found'
    s = s.split('\n-----', 1)[0].replace('Translation: ', '')
    s = wrap_text_result(s, 'translate', line)
    return {'lines': s, ':here': True}
