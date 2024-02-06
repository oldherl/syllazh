# syllazh
Linux TTY font for Chinese, but treat it as a syllabic writing / 中文 Linux TTY 字体，但是表音文字
![image](https://github.com/oldherl/syllazh/assets/172495/9b7509ba-86ab-446f-ac61-b19711796110)

## WTF is this? / 这是什么××玩意？
This is [Linux console](https://wiki.archlinux.org/title/Linux_console), aka TTY, displaying Chinese text (in a sense).
- It is unmodified kernel, without applying patches such as [cjktty](https://github.com/zhmars/cjktty-patches).
- It is good old TTY (in-kernel VT), not running [kmscon](http://www.freedesktop.org/wiki/Software/kmscon), [fbterm](https://salsa.debian.org/debian/fbterm), or [zhcon](https://zhcon.sourceforge.net/).
  
这是 [Linux 控制台](https://wiki.archlinux.org/title/Linux_console)，也叫 TTY，在显示中文（某种意义上）。
- 原版内核，没有打 [cjktty](https://github.com/zhmars/cjktty-patches) 之类的内核补丁。
- 它就是老式TTY（内核控制台），没有运行 [kmscon](http://www.freedesktop.org/wiki/Software/kmscon)、 [fbterm](https://salsa.debian.org/debian/fbterm) 或是 [zhcon](https://zhcon.sourceforge.net/) 之类的第三方软件。

Fonts on Linux TTY can be changed by the `setfont` utility, usually in the `kbd` package. It supports only up to 512 glyphs, but each glyph can be mapped to multiple Unicode code points.
So in order to support Chinese, I need to squeeze thousands of Chinese characters into this tiny space.
Luckily, Modern Chinese Mandarin has only around 400 different syllables (ignoring tones).
One of the most frequently used character for each syllable is picked to represent all those hundreds characters with the similar pronounciation.
Together with 96 visible ASCII characters and some symbols, they fit in the 512 glyphs' space perfectly!

Linux TTY 上的字体可以由一般位于`kbd`软件包里的`setfont`工具更换。它最多支持512个字形(glyph)，但每个字形可以被映射到多个 Unicode 码位。
所以为了支持显示中文，我必须把成千上万个汉字挤进这个狭小的空间。
幸运的是，现代汉语普通话大约只有400个不同的音节（忽略声调）。于是我针对每个音节，我挑选了一个最常用的汉字来代表那上百个读音近似的汉字。
这样再加上96个可见的ASCII字符和几个符号，它们就正好装进512字符的限制内了！
