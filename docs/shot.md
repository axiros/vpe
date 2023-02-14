# Making Screenshots

Example: `,r` on the line

`shot img/foo`

Will let you

- select a rectangle or window (double click) on the screen
- shoot it, using `scrot --freeze -s img/foo.png`
- delete `img/foo.png` if existing
- save the shot as at `img/foo.png`
- replace the line with `![](img/foo.png)`

This assumes you have the [scrot](https://github.com/resurrecting-open-source-projects/scrot) utility installed on the system.
If you use another screenshot tool, you have to provide a wrapper named "scrot" within your `$PATH`.

![cast](https://github.com/AXGKl/large_assets/blob/master/vpe/make_shot.mp4.gif?raw=true)

- In the screencast the area selection cursor after hitting `,r` was not recorded unfortunatelly
- Browser preview via [MarkdownPreviewNvim](https://github.com/iamcco/markdown-preview.nvim)
