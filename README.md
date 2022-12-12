# Vim Python Eval

<!--toc:start-->
- [Vim Python Eval](#vim-python-eval)
  - [Usage](#usage)
  - [Features](#features)
    - [Directives](#directives)
    - [Result Display](#result-display)
    - [Predefined Blocks (Macros)](#predefined-blocks-macros)
  - [Interacting with Swagger APIs](#interacting-with-swagger-apis)
  - [Installation](#installation)
    - [Requirements](#requirements)
  - [Developing](#developing)
  - [Credits, Alternatives, Interesting Links](#credits-alternatives-interesting-links)
<!--toc:end-->

vim/neovim [can](https://vim.fandom.com/wiki/Execute_Python_from_within_current_file) 'hot evaluate' code using e.g. `:py print("hello")`. 

This module adds

- Output handling 
    - within a split window (a buffer, incl. undo)
    - as valid python (lsp support, e.g. for re-formatting)
- Support for various [evaluation and output control directives](#directives)
- Loadable predefined python code blocks
- Hot reload of this module's code, w/o state loss
- More convience regarding evaluation of lines within code blocks

![](./docs/img/demo.gif)

The module also offers [built in support](./docs/swagger.md) for interaction with Swagger/OpenAPI APIs

![](./docs/img/swagger.png)


## Usage

- Hit the hotkey (e.g. `,r`) on a line or visually selected range, which you want evaluated.
- The line may be a filename or URL of a swagger definition, resulting in code generation for a
  python requests based API client (see [here](./swagger.md))
- When the evaluated block contains assignments to `p` or `y`, their values are shown pretty printed
  or as yaml within a vertical split window. As are evaluation errors.
- If the evaluated line is part of a block (e.g. a line within a function), then the whole block is evaluated by default.
- Invocations of the `print` function result in print outs within vim's status window.
- Previously evaluated lines are remembered, i.e. state is kept between evaluations.
- Objects or classes within result structures are walked for their attributes, when printing them

Notes:
- Evaluated code may even reside within docstrings or markdown code blocks - as long as you omit the
  comment delimiters from the evaluation, all assignements make it into the next evaluation state.
- vim calls the python code syncronously, blocking. You have to kill the python process to unblock
  it, should your code block forever, while executing.

## Features

### Directives

Supported (usually in comment blocks) are:

- `:all`: The whole source module is evaluated before the single line is
- `:clear`: The previous result is removed
- `:cmt <comment>`: Show the given comment string
- `:doc`: Show the evaluated block in the result window
- `:[no]autodoc`: The `:doc` directive is set/removed for all subsequent evaluations
- `:[no]always`: When set all directives of this eval run are remembered for future runs, until `:noalways` is set
- `:single`: Only the line on the cursor is evaluated, even if within a bigger block (see swagger) 
- `:state`: Add the evaluation state to result (shows all assigned variables)
- `:wrap <code>`: The line is wrapped into code, replacing the string '{}' (see swagger)


### Result Display

Assign the following variables and evaluate to influence how results are shown:

- `p = <result>` or `y = <result>`: Pretty print or yaml dump any object, incl. attributes 
- `filter="<list of match strings>"`: Recursively scans the result structure and only shows key OR
  values (substring-)matching any of the filter. 
  A filter value '1' results in all list reduced to their first item. 
- `hide="<list of match strings>"`: Recursively scans the result structure and "x-out" values, whose
  keys(!) match any of the hide strings. Intended to not show passwords and the like in demos.

```python
filter = 'bar,1'
hide = 'bar'
m = {'u': 23, 'a': [{'foo': {'bar': 23, 'baz': 23}}, {'other': 42}]}
p = m   # :doc

# result:
# 2 keys filtered, matching [bar,1]
p = {'a': [{'foo': {'bar': 'xxx'}}, '...[2 items]]}
```


### Predefined Blocks (Macros)

Note: At this time this feature does NOT offer anything more than a good snippets tool, i.e. you
probably do NOT need it. I was just adding it, in order to have those available on `cow style` machines
without a sophisticated vim setup.

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


## Interacting with Swagger APIs

See [here](./docs/swagger.md)


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


## Credits, Alternatives, Interesting Links

First of all: vim, with python support.

Inspiration from this: [vim-http-client](https://github.com/aquach/vim-http-client)

Powerful alternative: [jupyter-vim](https://github.com/jupyter-vim/jupyter-vim)

OpenAPI:

- Tools: https://openapi.tools/
- Generation UI, with import function: https://www.apibldr.com/
- Their default gen tool: https://github.com/OpenAPITools/openapi-generator
