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
command! EvalInto silent call s:EvalInto()

function! PyEvalSelection(func_name, mode)
    if a:mode == 'picker'
        let l = ['last']
    else
      if a:mode == ''
          let l = [['']]
      else
          let l = [s:get_selected_lines(a:mode)]
      endif
      call add(l, expand("<cword>"))
      call add(l, expand("%:p"))
      call add(l, getline('.'))
      call add(l, getcursorcharpos())
      call add(l, s:script_path)
      " must be last!
      if exists('vpe_reload')
        call add(l, 'rel')
      else
        call add(l, '')
      endif
    endif

    let s:nfos = l
    python3 << EOL

if 'python':
    import os, sys
    l = vim.eval('s:nfos')
    if not l[0] == 'last':
        d = {
            'last_sel': l,
            'SEL': l[0],
            'W':   l[1],
            'PTH': l[2],
            'L':   l[3],
            'CCP': l[4],
            'D':   l[5],
            'rld': l[6],
            }
        lines = len(l[0])
        d['L1'] = l1 = int(d['CCP'][1])
        d['L2'] = -1 if lines < 2 else (l1 + lines -1)
        d['COL'] = int(d['CCP'][2])
        d['executed_lines'] = []

        if not d['D'] in sys.path:
            sys.path.insert(0, d['D'])
            import vim_python_eval

        if d['rld'] or ':reload' in  d['L']:
            m = vim_python_eval.ctx.state
            for k in  list(sys.modules.keys()):
              v = sys.modules[k]
              if '/vpe/' in str(v):
                sys.modules.pop(k)
            import vim_python_eval
            vim_python_eval.ctx.state = m

        m = vim_python_eval.ctx
        [setattr(m, k, v) for k, v in d.items()]
        # funcname: 'Eval' or 'SmartGoto'
    getattr(vim_python_eval, vim.eval("a:func_name"))()
    # with open('/tmp/b1', 'w') as fd:
    #     fd.write(str(d))
    # os.system(f'notify-send -t 10 "foo"  "{d["SEL"]}"')
EOL
endfunction
   
function s:get_selected_lines(mode)
    " Returns selected text. Call with visualmode() as the argument
    let [line_start, column_start] = getpos("'<")[1:2]
    let [line_end, column_end]     = getpos("'>")[1:2]
    let lines = getline(line_start, line_end)
    if a:mode ==# 'v'
        " Must trim the end before the start, the beginning will shift left.
        let lines[-1] = lines[-1][: column_end - (&selection == 'inclusive' ? 1 : 2)]
        let lines[0] = lines[0][column_start - 1:]
    elseif  a:mode ==# 'V'
        " Line mode no need to trim start or end
    elseif  a:mode == "\<c-v>"
        " Block mode, trim every line
        let new_lines = []
        let i = 0
        for line in lines
            let lines[i] = line[column_start - 1: column_end - (&selection == 'inclusive' ? 1 : 2)]
            let i = i + 1
        endfor
    endif
    return lines
endfunction
command! PyEvalFromPicker silent call PyEvalSelection('Eval', 'picker')
" for your config, e.g.:
" xnoremap ,r :<C-U> call PyEvalSelection(visualmode())<Cr>
" nnoremap ,r :call PyEvalSelection('')<Cr>

