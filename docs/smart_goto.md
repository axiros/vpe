# Smart Goto

This function evaluates current cursor position or selected range and tries to find out
what your intent is, when pressing the hotkey invoking the function:

- Under a markdown title: Google the title (so that you find out which link you want to
  reference in the link)
- Under a ref: Open it in the editor. If not present and a MD ref: Create the file, open
  it.
- Under a manpage link: Open it
- Under a normal word or selected range: Google it
