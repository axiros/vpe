#!/usr/bin/env bash
# These tests require https://github.com/AXGKl/pds
#
set -o errexit
vpe_here="$(builtin cd $(dirname "$0") && pwd)"
verbose=true

. "$HOME/.config/pds/test/tools.sh"

function test-on-empty-show-macros { # ,r on empty line - >macro
    M1='
    
    intro

    '
    open 'm1.md' "$M1" intro ''
    ⌨️ 'gg' 0
    👁️ '1:1' 500
    ⌨️ ',r'            # ,r on empy line
    👁️ 'Reactive' 2000 # on of our "macros" offered
    👁️ 'intro'         # still shown, no new window but split
    vi_quit
}

function test-on-error-handler { # eval with exception leads to eval of first found:vpe_on_err line
    M1='
    xxx 
    :vpe /gg/foo/ # :vpe_on_err
    p = "foo" + "bar"
    p = "nope" + "bar"
    :vpe /gg/nope/ # :vpe_on_err
    '
    open 'm1.md' "$M1" vpe
    ⌨️ 'gg' 0
    👁️ '1:1' 500
    ⌨️ ',r'
    👁️ 'foobar' 2000
    📴 'nopebar'
    vi_quit
}

function test-mappings-md-to-lua { # our md to lua mapper
    cd "$(testdir)" && rm -f mappings.lua || exit 1
    open nd 'mappings.md' "$vpe_here/assets/mappings.md" ''
    ⌨️ ':10' Enter
    👁️ '10:1' 1000
    ⌨️ ',r'
    👁️ 'mappings.lua' 4000
    👁️ ', desc = "'
    vi_quit
    test -e "mappings.lua" || exit 1
    local s="$HOME/.local/share/nvim/mason/bin/stylua"
    # test -e "$s" && {
    "$s" mappings.lua || exit 1
    #}
}
return 2>/dev/null || test_in_tmux "$@"
