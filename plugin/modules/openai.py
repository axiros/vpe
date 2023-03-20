#!/usr/bin/env python

"""
# Use 'openai' to generate python code

## Usage

openai models: Fetches current models and updates local cached file
openai [params:] prompt: Complete

## Alias: oai

## Params

T=0.6 t=400 dt=10 m=davinci [p=]py

or long forms.

### Defaults

{defaults}

m: First match of in models list, sorted by time
e.g. m=03 -> 'text-davinci-003'


## Requirements

1. `{openai_key_cmd}` must deliver a valid token`
If you don't use pass, generate a wrapper

## Examples

openai models
openai account
openai py dt=10: Say hello, use main and reactivex
openai Show all unicode emoticons for love
openai Say "What's your name?" in Spanish.

## Links

Bypass policies: https://gist.github.com/coolaj86/6f4f7b30129b0251f61fa7baaa881516
https://gpt3demo.com/
https://promptbase.com/

### AI Use Cases

https://www.techvantagesystems.com/telecom/
https://www.avanseus.com/

### AI Tech
https://github.com/ggerganov/llama.cpp
https://lambdalabs.com/ buy modelling time on GPUs
"""

from json import dumps, loads
import time
from share import notify, vim, wrap_text_result, cast, write_file, here, read_file
import os
import requests
from functools import partial

openai_key_cmd = 'pass show OPENAI_API_KEY'
dflt_model = '003'


def try_help():
    d = '\n'.join(
        [f'- {v.ljust(16)} {k.ljust(3)} = {defaults[k]}' for k, v in shorts.items()]
    )
    return __doc__.format(openai_key_cmd=openai_key_cmd, defaults=d)


def from_picker(word):
    res = try_load(word)
    return res


tmpls = {
    'py': 'Write python script to {prompt}. Provide only code, no text',
    'dflt': '{prompt}',
}

defaults = {'m': '003', 'T': 0.5, 't': 500, 'p': tmpls['dflt'], 'dt': 10}

shorts = {
    'm': 'model',
    'T': 'temperature',
    't': 'max_tokens',
    'dt': 'timeout',
    'p': 'prompt_template',
}

for k, v in shorts.items():
    defaults[v] = defaults[k]


def req(endpoint, data=None, timeout=5, **kw):

    api_endpoint = f'https://api.openai.com/v1/{endpoint}'
    api_key = os.getenv('OPENAI_API_KEY')

    request_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key,
    }
    r = requests.get if not data else requests.post
    r = partial(r, api_endpoint, headers=request_headers, timeout=timeout)
    if not data:
        response = r()
    else:
        try:
            response = r(json=data)
        except Exception as ex:
            return f'{ex} [dt={timeout}s]', 0
    if response.status_code == 200:
        return 0, response.json()
    return (
        f'Request for {api_endpoint} {data} failed, status code: {str(response.status_code)} {response.text}',
        0,
    )


models_ = []


def parse(line):
    kw, pre, prompt = dict(defaults), '', line
    if ':' in prompt:
        pre, prompt = prompt.split(':', 1)
    pre = ' ' + pre
    for t in tmpls:
        if t in pre:
            kw['prompt_template'] = tmpls[t]
    for k, v in defaults.items():
        if f' {k}=' not in pre:
            continue
        l = pre.split(f' {k}=', 1)[1].split(' ', 1)[0].strip()
        kw[k] = cast(l)
        if k in shorts:
            kw[shorts[k]] = kw[k]
    m = all_models()
    if isinstance(kw['model'], float):
        kw['model'] = str(int(kw['model']))
    l = [i for i in m if str(kw['model']) in i[0]]
    if not l:
        raise Exception(f'Model no match - {kw["model"]} - {l}')
    kw['model'] = l[0][0]

    return prompt.strip(), kw


def load_token():
    if os.environ.get('OPENAI_API_KEY'):
        return
    _ = os.environ['OPENAI_API_KEY'] = os.popen(openai_key_cmd).read().strip()
    if not _:
        raise Exception(f'Returned nothing: {openai_key_cmd}')


def complete(prompt, model, temperature, max_tokens, prompt_template, timeout, **kw):
    prompt = prompt_template.format(prompt=prompt)
    request_data = {
        'model': model,
        'prompt': prompt,
        'max_tokens': int(max_tokens),
        'temperature': temperature,
    }
    err, response = req('completions', data=request_data, timeout=timeout)
    if err:
        return err
    h = f'{response["usage"]["total_tokens"]} total tokens. Model: {model}, Temp: {temperature}, Max Tokens: {max_tokens}, Prompt: {prompt}\n'
    return h + response['choices'][0]['text']


fn_models = here + '/modules/assets/openaimodels.json'


def all_models():
    if models_:
        return models_
    m = loads(read_file(fn_models))
    models_.extend(m)
    return models_


def models():
    err, r = req('models')
    if err:
        return err
    r = reversed(sorted(r['data'], key=lambda d: d['created']))
    r = [
        [k['id'], time.ctime(k['created']), k['created']]
        for k in r
        if 'gpt' not in str(k)
    ][:20]
    write_file(fn_models, dumps(r))
    return dumps(r, indent=4)


def try_load(line, **kw):
    line = line.strip()
    load_token()
    if line == 'models':
        return {'lines': models(), ':here': True}
    if line == 'account':
        return {'lines': 'https://platform.openai.com/account/usage', ':here': True}
    prompt, kwargs = parse(line)
    res = complete(prompt, **kwargs)
    return {'lines': res, ':here': True}
