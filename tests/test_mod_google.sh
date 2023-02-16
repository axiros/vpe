#!/usr/bin/env bash
#

here="$(builtin cd "$(dirname "$0")" && pwd)"
vpe="$here/../plugin/vim_python_eval.py"

function die { echo -e "${esc}1;38;5;124mErr: $cur_test ${esc}0m"; }
function test_cli {
    "$vpe" google cnn news | grep 'https://us.cnn.com/' || die
}
function test_help {
    "$vpe" google | grep '@gh' || die
}

function main {
    for k in cli help; do
        cur_test="test_$k"
        eval "$cur_test"
    done
    echo "All good."
}
esc="\x1b["
main "$@"
