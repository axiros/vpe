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


python3 << EOL
import os, sys
D=vim.eval("s:script_path")
dbg=vim.eval("s:vpe_reload")
if not D in sys.path:
    sys.path.insert(0, D)
    import vim_python_eval as vpe 
if int(dbg):
    m = vpe.ctx.state
    sys.modules.pop('vim_python_eval')
    import vim_python_eval as vpe
    vpe.ctx.state = m

vpe.ctx.L1 = int(vim.eval("a:l1"))
vpe.ctx.L2 = int(vim.eval("a:l2"))

getattr(vpe, vim.eval("a:func_name"))()
EOL
endfunction

command! -range PythonEval <line1>,<line2> call s:VPE('ExecuteSelectedRange', <line1>, <line2>)
command! EvalInto silent call s:EvalInto()

