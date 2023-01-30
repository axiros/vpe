# Hetzner

We are using the optimized one:

https://raw.githubusercontent.com/MaximilianKoestler/hcloud-openapi/master/openapi/hcloud.json

## Usage

Totally automated including Auth: From the commandline, not via eval on the URL in vim.

    vpe ./hcloud.json # vpe the vim_python_eval.py, e.g. aliased

This will respect `./mods.py` and set the authorization correctly in the module params.
