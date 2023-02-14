# EvalInto

Config: Map `,E` in normal and visual mode to `EvalInto<CR>`.

[![asciicast](https://asciinema.org/a/EkeLpbjEBbqH34PegKGda0TqG.svg)](https://asciinema.org/a/EkeLpbjEBbqH34PegKGda0TqG)

The function is using only built in vim mechanics: Basically `put=execute(getline('.'))` plus a few
lines of buffername handling. No directives evaluated.

Tip: For repeated evals, you want to close the result buffers, using `:bw` (wipe)

