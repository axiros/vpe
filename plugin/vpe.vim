let s:script_path = fnamemodify(resolve(expand('<sfile>:p')), ':h')

function! s:EvalInto()
  " Just an add on, for eval any into buffer, using vim funcs "only":
  " Opens new window with eval result in it

  "  if a:cmd =~ '^!'
  "     execute "let output = system('" . substitute(a:cmd, '^!', '', '') . "')"
  let cmd = getline('.')
  let ft=&filetype
  redir => output
  execute cmd
  redir END
  if output ==# '' 
    put! = 'no output'
    return
  endif
 
  let filename = 'result_eval_into'
  rightbelow vsplit eval_into_res
  execute 'file ' . cmd
  setlocal nobuflisted buftype=nofile bufhidden=wipe noswapfile nospell ft=ft
  " call setline(1, split(output, "\n"))
  " put! = 'Result: ' .  cmd
  " put = '----'
  " :bwipeout
  :%d
  put=output
endfunction

function! s:VPE(func_name, l1, l2) range
"" Executes functions from py_api.py

if exists('vpe_reload')
  let s:vpe_reload = 1
else
  let s:vpe_reload = 0
endif
let s:vpe_word = expand("<cword>")
let s:vpe_pth = expand("%:p")
"let s:vpe_foo = getpos("'<")[1:2]
" just indent all python
python3 << EOL
if 'python':
    import os, sys
    D=vim.eval("s:script_path")
    reload_=vim.eval("s:vpe_reload")
    line = vim.eval("getline('.')")
    if not D in sys.path:
        sys.path.insert(0, D)
        import vim_python_eval
    if int(reload_) or ':reload' in  line:
        m = vim_python_eval.ctx.state
        for k in  list(sys.modules.keys()):
          v = sys.modules[k]
          if '/vpe/' in str(v):
            sys.modules.pop(k)
        import vim_python_eval
        vim_python_eval.ctx.state = m
    # make a lot of stuff accessible via ctx, for the module:
    # 2: actual col, not bytes. like in python
    ccp = vim.eval('getcursorcharpos()')
    #os.system(f'notify-send ccp  "{ccp}"')
    _ = vim_python_eval
    _.ctx.L1  = int(ccp[1]) # like vim, from 1
    _.ctx.COL  = int(ccp[2]) # like vim, from 1
    _.ctx.L2  = int(vim.eval("a:l2"))
    _.ctx.W   = vim.eval("s:vpe_word")
    _.ctx.PTH = vim.eval("s:vpe_pth")
    _.ctx.L   = line
    _.ctx.executed_lines = []
    # funcname: 'ExecuteSelectedRange' or 'SmartGoto'
    getattr(vim_python_eval, vim.eval("a:func_name"))()
EOL
endfunction

command! PythonEval silent  call s:VPE('ExecuteSelectedRange', -1, -1) 
command! PythonGoto silent  call s:VPE('SmartGoto', -1, -1) 
command! -range PythonEvalRange silent <line1>,<line2> call s:VPE('ExecuteSelectedRange', <line1>, <line2>)
command! -range PythonGotoRange silent <line1>,<line2> call s:VPE('SmartGoto', <line1>, <line2>)
command! EvalInto silent call s:EvalInto()

