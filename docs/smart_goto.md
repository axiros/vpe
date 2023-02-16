# Smart Goto

This function evaluates current cursor position or selected range and tries to find out
what your intent is, when pressing the hotkey invoking the function:

- Under a markdown title: Google the title (so that you find out which link you want to
  reference in the link)
- Under a ref: Open it in the editor. If not present and a MD ref: Create the file, open
  it.
- Under a manpage link: Open it
- Under a normal word or selected range: Google it

If you marked a bunch of URLs, those will be opened in browser as well.

## Examples

<!-- inserted by running smart_goto.py -->
<!--@examples-->


|Word|Whole Line<BR>Valid Cursor Positions: ^<br>Open Action|Comment|
|-  |-           | - |
|`readme`|`[foo bar][hosts](, g bla)` <br> `...........^^^^` <br> ✔️`/etc/hosts`|Ref link to existing file is opened| 
|`x`|`[new]: /tmp/vpeso.gk/m1.md` <br> `.........^^^^^` <br> ✔️`/tmp/vpeso.gk/m1.md`|Ref link to existing file is opened| 
|`x`|`foo [xxx](x1/x1.md)` <br> `.........^^^^^` <br> ✔️`/tmp/vpeso.gk/x1/x1.md`|Linked non existing markdown files: Dir created, file unsaved opened in vi<BR>dir created<BR>content: `# xxx LS `| 
|`bashrc`|`foo ~/.bashrc` <br> `....^^^^^^` <br> ✔️`/home/gk/.bashrc`|tilde replaced, file open in vi| 
|`bashrc`|`foo $HOME/.bashrc` <br> `....^^^^^^^^^^^` <br> ✔️`/home/gk/.bashrc`|$HOME replaced| 
|`bashrc`|`'foo ~/.bashrc'` <br> `.....^^^^^` <br> ✔️`/home/gk/.bashrc`|tilde replaced, file open in vi| 
|`etc`|`foo some_func("/etc/hosts") bar` <br> `...............^^^^^^^^^^` <br> ✔️`/etc/hosts`|file name extracted| 
|`etc`|`foo some_func(^/etc/hosts^) bar` <br> `...............^^^^^^^^^^` <br> ✔️`/etc/hosts`|file name extracted in backticks| 
|`bla`|`foo [xxx](/tmp/vpeso.gk/m1.md.tst)` <br> `.........^^^^^` <br>  |No auto creation of non .md file| 
|`x`|`x b [a][foo bar] x` <br> `^` <br>  |< 3 letter words (x) are not googled| 
|`y`|`x b [a][foo bar] y` <br> `................^^` <br>  |y only: no action| 
|`testimg`|`x b ![](./testimg.png)` <br> `..........^^^^^^` <br> ⌨`$BROWSER "/tmp/vpeso.gk/testimg.png" >/dev/null 2>&1`|Must run the image open command| 
|`foobar`|`a foobar bar foo` <br> `.^^^^^` <br> 🌐search: `client=%s-b-d&q=foobar`| 
|`foobar`|`foobar bar foo` <br> `^^^^^^` <br> 🌐search: `client=%s-b-d&q=foobar`| 
|`a`|`b [a](http://foo/bar) x` <br> `.....^^^^^^^` <br> 🌐`http://foo/bar`| 
|`foo`|`[foo]: http://foo.bar` <br> `^^^^^^^^^^` <br> 🌐`http://foo.bar`| 
|`git`|`a "git/hub" foo` <br> `...^^^^^^` <br> 🌐`https://github.com/git/hub`|github default for 2 word slash sepped| 
|`foo`|`[foo]: http://foo.bar .` <br> `.^` <br> 🌐`http://foo.bar`|Splits off after the link by space| 
|`foo`|`[foo bar]: ` <br> `^^^^^` <br> 🌐search: `client=%s-b-d&q=foo bar`|No link -> google title| 
|`foo`|`x b [a][foo bar] x` <br> `.......^^^^^` <br> 🌐`http://foo.bar`|Find defined link in the file, open it| 
|`a`|`x b [a][foo bar] x` <br> `....^^` <br> 🌐search: `client=%s-b-d&q=a`|Google the title| 
|`barx`|`x b [barx bah][foo] x` <br> `....^^^^^^^^^` <br> 🌐search: `client=%s-b-d&q=barx bah`|Google ALL title| 
||Notes: <br> - backticks replaced with `^` <br> - Testfile contains markdown ref:<br>   `[foo bar]: http://foo.bar`|

<!--@examples-->
