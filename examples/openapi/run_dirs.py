#!/usr/bin/env python
import sys
import os


def absp(d):
    return os.path.abspath(d)


here = os.path.dirname(absp(__file__))
d_tests = here + '/test_res'
os.environ['testmode'] = 'true'


def read_file(fn):
    try:
        with open(fn) as fd:
            s = fd.read()
    except:
        s = ''
    return s


def write_file(fn, s):
    with open(fn, 'w') as fd:
        fd.write(s)


def rm_d_tests():
    if not os.path.exists(d_tests):
        return
    [os.unlink(d_tests + '/' + i) for i in os.listdir(d_tests)]
    os.rmdir(d_tests)


def die(msg):
    print(f'🟥 {msg}')
    sys.exit(1)


def run(what, cmd):
    print(what)
    if os.system(cmd):
        die(f'Failed: {what}')


def run_dir(d, vpe, testmode):
    s = [f'{d}/{i}' for i in os.listdir(d) if i.endswith('.json') and not 'results' in i]
    s = [read_file(i) for i in s]
    s = [i for i in s if 'openapi' in i or 'swagger' in i]
    if not s:
        print('no json file found!!')
        return
    s = s[0]
    rm_d_tests()
    os.makedirs(d_tests, exist_ok=True)
    os.chdir(d_tests)
    write_file('openapi.json', s)
    run('Generating client', f'"{vpe}" swagger openapi.json')
    run('Running all API methods', './client_openapi.py > results.json')
    s = read_file('results.json')
    p = read_file('client_openapi.py')
    assert s and p
    pre = 'test_' if testmode else ''
    write_file(f'{d}/{pre}results.json', s)
    write_file(f'{d}/{pre}created_client.py', p)
    os.system(f'chmod +x "{d}/{pre}created_client.py"')
    if not testmode:
        return

    # ------------------------------------------------------------------- test mode
    cmd = f'diff --color "{d}/results.json" "{d}/{pre}results.json"'
    r = os.popen(cmd).read().strip()
    if r:
        print(r)
        die(f'Test result differs from original: {d}')
    else:
        print(f'🟩 Test success, no diff: {d}')


def main(match, testmode):
    os.chdir(here)
    vpe = os.path.dirname(os.path.dirname(here)) + '/plugin/vim_python_eval.py'
    for d in os.listdir(here):
        if match in d and os.path.isdir(d):
            run_dir(absp(d), vpe, testmode)
            os.chdir(here)


if __name__ == '__main__':
    testmode = 'test' in sys.argv
    a = sys.argv
    a.append('')
    rm_d_tests()
    main(match=a[1], testmode=testmode)
