# Vim Python Eval

<!--toc:start-->
- [Vim Python Eval](#vim-python-eval)
  - [Usage](#usage)
  - [Features](#features)
    - [Simple Example](#simple-example)
    - [Macros](#macros)
    - [Interacting with Swagger APIs](#interacting-with-swagger-apis)
      - [Source Layout and Navigation](#source-layout-and-navigation)
      - [Pre-Parametrization](#pre-parametrization)
  - [Installation](#installation)
    - [Requirements](#requirements)
  - [Developing](#developing)
<!--toc:end-->

- Facilitates evaluation and display of python directly from vim.
- Offers built in support for interaction with swagger APIs




## Usage

- Hit the hotkey (e.g. `,r`) on a line or visually selected range, which you want evaluated.
- When the evaluated block contains assignments to `p` or `y`, their values are shown pretty printed
  or as yaml within a vertical split window. As are evaluation errors.
- If the evaluated line is part of a block (e.g. a line within a function), then the whole block is evaluated by default.
- Invocations of the `print` function result in print outs within vim's status window.
- Previously evaluated lines are remembered, i.e. state is kept between evaluations.
- Objects or classes within result structures are walked for their attributes, when printing them

Note: Evaluated code may even reside within docstrings or markdown code blocks - as long as you omit the comment delimiters from the evaluation, all assignements make it into the next evaluation state.

## Features

### Directives

Supported (usually in comment blocks) are:

- `:clear`: The previous result is removed
- `:cmt <comment>`: Show the given comment string
- `:doc`: Show the evaluated block in the result window
- `:eval file`: The whole source module is evaluated before the single line is
- `:exec single`: Only the line on the cursor is evaluated, even if within a bigger block (see swagger) 
- `:[no]autodoc`: The `:doc` directive is set/removed for all subsequent evaluations
- `:wrap <code>`: The line is wrapped into code, replacing the string '{}' (see swagger)


### Result Display

Assign the following variables and evaluate to influence who results are shown:

- `p = <result>` or `y = <result>`: Pretty print or yaml dump any object, incl. attributes 
- `filter="<list of match strings>": Recursively scans the result structure and only shows key OR
  values (substring-)matching any of the filter
- `hide="<list of match strings>": Recursively scans the result structure and "x-out" values, whose
  keys(!) match any of the hide strings. Intended to not show passwords and the like in demos.

```python
filter = 'bar'
hide = 'bar'
m = {'u': 23, 'a': [{'foo': {'bar': 23, 'baz': 23}}]}
p = m   # :doc

# result:
# 2 keys filtered, matching [bar,somethingelse]
p = {'a': [{'foo': {'bar': 'xxx'}}]}
```



### Simple Example

[![asciicast](https://asciinema.org/a/cEmG79nApjbKe6Mvohco7OfqU.svg)](https://asciinema.org/a/cEmG79nApjbKe6Mvohco7OfqU)


### Macros

If you hit the hotkey on an empty line we present a list of predefined code blocks, for quick adds
into the source code window.

You may extend that list by your own "macros" like so:


```python
~ ❯ cat .config/vpe/macros.py                                                                                    tools
d = """
'Demo user macro'
import time
print('Hello', time.time())
"""

macros = {'demo': d}
```

[![asciicast](https://asciinema.org/a/057ewOGytqJDGEL6DF9Ck1hDw.svg)](https://asciinema.org/a/057ewOGytqJDGEL6DF9Ck1hDw)


### Interacting with Swagger APIs

Note: Early phase. Manually tested against various swagger files, incl. the
[petstore](https://petstore.swagger.io/) demo API.

[![asciicast](https://asciinema.org/a/Ot2gPgtAu292UgZpFgTwLKAU1.svg)](https://asciinema.org/a/Ot2gPgtAu292UgZpFgTwLKAU1)

1. After potential pre-parametrization, hit the hotkey on a Swagger definition URL or filename =>
  - All RPCs are listed, incl. Parameter definitions.
  - Path parameters are extracted and configured globally on module level
  - Definitions are wrapped into a `class Defs`
  - API Methods as top level classes, referencing definitions.
  - Tools for actual sending the requests within `class Tools` at the end.
3. You can now parametrize and send requests to the endpoint by hitting the hotkey on the methods.
4. Set `show_all` to 1 or True in order to inspect all attributes of the `requests` result object. 
5. Configure any authentication within `class API`
6. Directives are at the end of the `methods` block, ready for change.
    - Default: `# :clear :doc :eval file :exec single :wrap p = Tools.send({})`
    - Remove the `:clear` to not loose output of previous runs
    - Set `:wrap p = ...` to `:wrap y= ...` to get output as yaml

If you have downloaded a swagger definition into a file, press the hotkey on the filename

<details><summary>demo</summary>
<a href="https://asciinema.org/a/KTvAtUqYCVkYclJKLDoz0mGOK" target="_blank"><img src="https://asciinema.org/a/KTvAtUqYCVkYclJKLDoz0mGOK.svg" /></a>
</details>


#### Source Layout and Navigation

- The source module is optimized for jumping around using `gd` (goto definition), which should be part of your editor python setup. Optimized means: Some
    refs may be wrapped into lambdas, when not resolvable at import time
- `<Ctrl-o>` to jump back in history (`:help jump`)

- The source module is also built for simple indent based folding, allowing to focus on specific
  methods also within bigger APIs

#### Pre-Parametrization

Before evaluating the link to a swagger definition file, resulting in source module build, you may
parametrize the build by evaluating some other conventional assignments.


These are understood, in addition to the always supported ones (e.g. `hide` or `filter`):

- `sep=<methods seperator>`: "Stretching the methods, with a sep only line between them, for
  readability
- `params={<dict of global params>}`: The key values given here will be added to the path
  parameters, i.e. get referenced globally.
- `hdrs={<dict of additional headers}`: Request headers may be given here, e.g. API-Keys. `$`
  notation is understood for values, referencing environ variables.
- `sh_req=[0|1|2]`: Shows result only for 0, request with 1, full dump of the request object at 2



Here a demo against a DynDNS provider's API, illustrating the use of those parameters. 
<a href="https://asciinema.org/a/QhCpFAsHjM5CELXzClXO67eVv" target="_blank"><img src="https://asciinema.org/a/QhCpFAsHjM5CELXzClXO67eVv.svg" /></a>

Note that the API server was a bit... slow at time of recording, we had to raise the request
timeout.

## Installation

Not (yet) a plugin.

1. Put the module into your file system
2. Add this into your vimrc:

```vim
function! s:VPE(func_name, l1, l2) range
" Executes functions from vim_python_eval.py
python3 << EOL
import os, sys
D = f'{os.environ["HOME"]}/.config/nvim.gk'  # <--- ADAPT TO WHERE YOU HAVE THE MODULE
if not D in sys.path:
    sys.path.insert(0, D)
    import vim_python_eval as vpe 
vpe.ctx.L1 = int(vim.eval("a:l1"))
vpe.ctx.L2 = int(vim.eval("a:l2"))
getattr(vpe, vim.eval("a:func_name"))()
EOL
endfunction

" Supports by line evals and also visual range eval:
command! -range Evl <line1>,<line2> call s:VPE('ExecuteSelectedRange', <line1>, <line2>)
nnoremap          ,r  :Evl<CR>
xnoremap <silent> ,r  :Evl<CR>
```

This lazy loads the module on first use.


### Requirements

Should work for vim and neovim with python3 support.

For filetype python we assume these requirements in your config:

1. `set foldmethod=indent` should be set, since we collapse classes after creating swagger support
   definitions.
1. The module relies on the presence of a `:Format` command, which you typically get by adding LSP
   support for python. If you have support for sth like `:Black` or `:Blue`, then add to your vimrc (for filetype python):  
   `command Format :Black` 


## Developing

If you want to play around / extend the module, you can have the module reloaded at every hotkey
invocation.

Add these lines into your vimrc, before the line `vpe.ctx.L1 = ...`:

```python
# For debugging (reload at code changes) you may want to uncomment:
m = vpe.ctx.state
sys.modules.pop('vim_python_eval')
import vim_python_eval as vpe
vpe.ctx.state = m
```

This takes care to not loose your evaluation state over reloads.

In order to run tests w/o vim, just touch an empty `vim.py` next to the module (or pip install it).



