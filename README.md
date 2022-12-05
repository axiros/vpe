# Vim Python Eval

- Facilitates evaluation and display of python directly from vim.
- Offers built in support for interaction with swagger APIs



## Use Cases

### Rules

- Hit the hotkey (e.g. `,r`) on a line or visually selected range, which you want evaluated.
- If the line is part of a block (e.g. a line within a function), then the whole block is evaluated
  by default.
- When the evaluated block contains assignments to `p` or `y`, their values are shown pretty printed
  or as yaml within a vertical split window. As are evaluation errors.
- Invocations of the `print` function result in print outs within vim's status window.
- Previously evaluated lines are remembered, i.e. state is kept between evaluations.
- Directives understood (usually in comment blocks) are:
    - `:clear`: The previous result is removed
    - `:cmt <comment>`: Show the given comment string
    - `:doc`: Show the evaluated block in the result window
    - `:eval file`: The whole source module is evaluated before the single line is
    - `:exec single`: Only the line on the cursor is evaluated, even if within a bigger block (see
      swagger) 
    - `:[no]autodoc`: The `:doc` directive is set/removed for all subsequent evaluations
    - `:wrap <code>`: The line is wrapped into code, replacing the string '{}' (see swagger)
- Objects or classes within result structures are walked for their attributes, when printing them


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

Note: Early phase, only tested against the [petstore](https://petstore.swagger.io/) demo API.

1. Hit the hotkey on a Swagger definition URL or filename => All RPCs are listed, incl. Parameter
   definitions.
2. Path parameters are extracted and configured globally on module level
3. You can now parametrize and send requests to the endpoint by hitting the hotkey on the methods.
4. Set `show_all` to 1 or True in order to inspect all attributes of the `requests` result object. 
5. Configure any authentication within `class API`
6. Directives are at the end of the `methods` block, ready for change.
    - Remove the `:clear` to not loose output of previous runs
    - Set `:wrap p = ...` to `:wrap y= ...` to get output as yaml

[![asciicast](https://asciinema.org/a/Ot2gPgtAu292UgZpFgTwLKAU1.svg)](https://asciinema.org/a/Ot2gPgtAu292UgZpFgTwLKAU1)

- The source module is folded and optimized for jumping around using `gd` (goto definition), which
should be part of your editor python setup.

- If you have the swagger definition in a file, press the hotkey on the filename

<details><summary>demo</summary>
<a href="https://asciinema.org/a/KTvAtUqYCVkYclJKLDoz0mGOK" target="_blank"><img src="https://asciinema.org/a/KTvAtUqYCVkYclJKLDoz0mGOK.svg" /></a>
</details>

- You may define, in addition to automatically extracted path params, other parameters globally, by
  evaluating a `params={<param defs>}` assignment, before evaluating the file path or URL to the
  swagger definition.

<details><summary>demo</summary>
<a href="https://asciinema.org/a/12rsNrLd55oyjG1LlO93HcP4L" target="_blank"><img src="https://asciinema.org/a/12rsNrLd55oyjG1LlO93HcP4L.svg" /></a>
</details>



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

