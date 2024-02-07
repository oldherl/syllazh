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
The list of all pinyin and hanzi used in this font can be found in the [pinyin_hanzi](./pinyin_hanzi) file.
Together with 96 visible ASCII characters and some symbols, they fit in the 512 glyphs' space perfectly!

Linux TTY 上的字体可以由一般位于`kbd`软件包里的`setfont`工具更换。它最多支持512个字形(glyph)，但每个字形可以被映射到多个 Unicode 码位。
所以为了支持显示中文，我必须把成千上万个汉字挤进这个狭小的空间。
幸运的是，现代汉语普通话大约只有400个不同的音节（忽略声调）。于是我针对每个音节，挑选了一个最常用的汉字来代表那最多上百个读音近似的汉字。
具体的拼音和汉字列表可以在[pinyin_hanzi](./pinyin_hanzi)文件中找到。
这样再加上96个可见的ASCII字符和几个符号，它们就正好装进512字符的限制内了！

## But why? / 它有什么用？
To be honest, it is not very pleasant to stare at those "wrong" characters and try to guess the meaning of the sentences. Thus, I don't expect anyone to use this as a daily driver.
It's 2024 now, you should be using your favorite Wayland or X desktop, not TTY. All major GUI toolkits support Chinese (and all languages in general) much better than this hack.

老实讲，盯着这些同音错字并通过句子来费劲猜测它是什么意思，并不是很愉快的体验。因此我也不期待任何人日常使用它。
现在都2024年了，你应该去用你喜欢的 Wayland 或 X 桌面，而不是TTY。所有主要的图形界面库对中文（以及所有其他语言）的支持都比我这奇技淫巧高到不知哪里去了。

I developed this as an exercise to understand better about the text rendering in Linux TTY, or a challenge to explore the limit of "obsolete" technology.

我把这个项目是为了更好地理解 Linux TTY 的文字渲染，或看作一种对「老旧」技术的边界的探索。

One possible use case might be performing some maintenance tasks in a Live environment (such as ArchISO).
You don't have access to graphical desktop or patched kernels and are stuck in the TTY, but need to check the filenames that are in Chinese.
You need something better than just some [Tofu](https://fonts.google.com/knowledge/glossary/tofu), but would avoid installing and configuring TTY replacements.
Now you can install just one tiny font and get some "hint" of those filesnames, which might be helpful.

我能想到的一种使用场景是在某种 Live 环境（如 ArchISO）中执行维护任务。
你没有办法使用图形界面或打过补丁的内核，只能用TTY，但是需要检查一些含中文的文件名。
你也不想安装和配置TTY的代用品，只希望把中文显示得比纯粹的 [豆腐](https://blog.justfont.com/2017/06/font-chat-room-1-noto-serif-cjk/) 好一些即可。
这时你只需要安装一个小小的字体就能猜测那些文件名了，这大概能或多或少地帮助到你。

Another interesting thought is that it gives a hint about how Chinese would look like if the [2nd Simp. Chinese Scheme](https://en.wikipedia.org/wiki/Second_round_of_simplified_Chinese_characters) succeeded.
(Note: this project is not using the exact characters as the 2nd Simp. Chinese)
In that scheme, many Chinese characters got merged just based on similar sounds or shapes, despite having distinct meanings and sources. It was considerd a step towards the romanization of the Chinese language.

另一个有意思的想法是，你可以感受到如果 [二简字](https://zh.wikipedia.org/zh-cn/%E4%BA%8C%E7%AE%80%E5%AD%97) 运动成功了，中文大概会变得怎样。（注：本项目与二简字简化方案不同）
在该方案中，许多汉字仅仅因为读音或形状相似就被合并，完全无视了它们的字义和字源。它被认为是朝着汉字拉丁化的一种试验。

Fortunately, it failed. That's why we can still use Chinese with elegant Hanzis today.

万幸的是，二简字烂尾了。我们才得以在今天继续使用优美的汉字。

## How was it made? / 它是怎么做出来的？
(WIP)

## Installation / 安装
(WIP)

## License / 许可
The generated font is released under the [SIL OFL](./output/OFL.txt).
Files in the root folder (currently only `readbdf.py` and `pinyin_hanzi` files) are released under GNU Lesser General Public License (LGPL) 2.1.
Files in sub-folders are released under different license. You can find the details in those folders.

生成的字体以 [SIL OFL 协议](./output/OFL.txt) 发布。
根目录中的文件（目前只有`readbdf.py`和`pinyin_hanzi`文件）以 GNU Lesser General Public License (LGPL) 2.1 协议发布。
各个子目录中的文件以其他协议发布，你可以在对应目录中查看它们的协议。

## Acknowledgement / 致谢
(WIP)
