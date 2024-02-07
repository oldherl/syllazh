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
幸运的是，现代汉语普通话大约只有400个不同的音节（忽略声调）。于是我针对每个音节，挑选了一个最常用的汉字来代表那最多上百个读音近似的汉字。
这样再加上96个可见的ASCII字符和几个符号，它们就正好装进512字符的限制内了！

## But why? / 它有什么用？
To be honest, it is not very pleasant to stare at those "wrong" characters and try to guess the meaning of the sentences. Thus, I don't expect anyone to use this as a daily driver.
It's 2024 now, you should be using your favorite Wayland or X desktop, not TTY. All major GUI toolkits support Chinese (and all languages in general) much better than this hack.

老实讲，盯着这些同音错字并通过句子来费劲猜测它是什么意思，并不是很愉快的体验。因此我也不期待任何人日常使用它。
现在都2024年了，你应该去用你喜欢的 Wayland 或 X 桌面，而不是TTY。所有主要的图形界面库对中文（以及所有其他语言）的支持都比我这奇技淫巧高到不知哪里去了。

I developed this as an exercise to understand better about the text rendering in Linux TTY, or a challenge to explore the limit of "obsolete" technology.

我开发这个项目是为了更好地理解 Linux TTY 的文字渲染，或把它看作一种对「老旧」技术的边界的探索。

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
- Prepare the Hanzi (Chinese characters) part of the font. 准备字体的汉字部分。
  - A PSF font can only contain up to 512 glyphs, but every glyph can be mapped to multiple Unicode codepoints.
  In Western fonts, this feature allows A (Latin A) and Α (Greek Alpha) to share one glyph to save spaces.
  - 一个 PSF 字体最多只能包含512个字符，但每个字符可以映射到多个不同的 Unicode 码位。在西方字体中，这可以把 A (拉丁字母A) 和 Α (希腊字母阿尔法) 映射到同一个字符来节省空间。
  - In this project, I map all Hanzis with the same pinyin (ignoring tones) to one single "representative" in order to save spaces. For example, 妈麻马骂吗 (pinyin: mā má mǎ mà ma) are all mapped to 马.
  The Hanzi-Pinyin mapping is extracted from the pinyin data of [fcitx/libime](https://github.com/fcitx/libime) by a script.
  - 在本项目中，我把所有拼音相同的汉字（忽略声调）都映射到一个「代表」汉字来节省空间。例如，妈麻马骂吗 (拼音: mā má mǎ mà ma) 全都映射到了 马。
  这个映射是由 [fcitx/libime](https://github.com/fcitx/libime) 的数据经过脚本提取得到的。
  - The bitmaps of each glyph come from an old public free font `gb24st.bdf`. It is one of the permissive licensed Chinese bitmap fonts, but it only covers GB2312 characters.
  - 每个字符的点阵数据来自一个古老的自由字体 `gb24st.bdf`。它是几个宽松授权的中文点阵字体之一，但它只覆盖了 GB2312 字符。
  - So some pinyin syllables aren't included in this project, such as rua(挼), fiao(覅), because there are no bitmaps in `gb24st.bdf` for any Hanzi with such pinyin. But anyway they are rarely used and freeing those spaces up to include some symbols might be a good thing.
  - 所以有些拼音音节没有包含在本项目的字体中，比如 rua(挼), fiao(覅) 等，因为`gb24st.bdf`字体里没有任何此读音的汉字的点阵数据。不过反正它们也很少用到，节省几个位置来装些符号或许还是好事情。
  - The representatives are basically assigned to the most frequently used ones of that pinyin syllable. However, I handpicked some of them in order to avoid confusion or to use a [phonetic component](https://en.wikipedia.org/wiki/Chinese_character_classification#Phonetic_loan_characters) (that can form many Phono-semantic compound characters).
  - 代表汉字基本上是挑选的该读音的最常见的汉字。不过有少数几个是我手工挑选的，目的是避免混淆或使用一个能组成许多形声字的[声旁](https://zh.wikipedia.org/wiki/%E5%85%AD%E6%9B%B8#%E5%BD%A2%E8%81%B2)。
  - The list of all pinyin and hanzi used in this font can be found in the [pinyin_hanzi](./pinyin_hanzi) file.
  - 具体的拼音和汉字列表可以在 [pinyin_hanzi](./pinyin_hanzi) 文件中找到。
  - The script `readbdf.py` then reads this list and extract the bitmap of the representatives from `gb24st.bdf`. Output format is the "txt" format used by PSF Tools.
  - 脚本`readbdf.py`随后就读取这个列表，并将代表汉字的位图从`gb24st.bdf`中提取出来。输出格式为 PSF Tools 中使用的 "txt" 格式。
- Prepare the ASCII part and some other symbols. 准备字体的 ASCII 和其他几个符号的部分。
  - They come from the "Libertinus Mono" font. That's a vector font and I converted it to bitmap (bdf) using FontForge.
  - 它们来自 Libertinus Mono 字体。该字体为矢量字体，我使用 FontForge 将其转换到了 bdf 格式的位图字体。
  - Then it is converted to psf by `bdf2psf` tool and converted to txt by `psf2txt` in PSF Tools.
  - 然后通过`bdf2psf`把它转换到 psf 格式，再用 PSF Tools 中的 `psf2txt` 转换到 txt 格式。
- Combine them two manually and convert to psf format by `txt2psf`. 手工把它们合并起来并使用 `txt2psf` 转换为 psf 格式。
  - Linux TTY assumes the 32nd glyph is U+20 (the space character), or that glyph would be used to clear the background. So I repositioned U+20 to the 32rd place.
  - Linux TTY 预设第32个字符为 U+20 (空格)，否则它将被用来填充背景中没有字符的位置。所以我手工把它调整到了第32个位置。

## Installation / 安装
### Arch Linux (AUR)
(WIP)
### Manually for other Linux distros / 其他 Linux 发行版，手动安装
Copy the [output/syllazh.psfu.gz](./output/syllazh.psfu.gz) file to `/usr/share/kbd/consolefonts/`. Then run `setfont syllazh` from a TTY. Enjoy!

将 [output/syllazh.psfu.gz](./output/syllazh.psfu.gz) 文件复制到 `/usr/share/kbd/consolefonts/` 目录中。然后在TTY里运行 `setfont syllazh`。请尽情享用！

## License / 许可
The generated font is released under the [SIL OFL](./output/OFL.txt).
Files in the root folder (currently only `readbdf.py` and `pinyin_hanzi` files) are released under GNU Lesser General Public License (LGPL) 2.1.
Files in sub-folders are released under different license. You can find the details in those folders.

生成的字体以 [SIL OFL 协议](./output/OFL.txt) 发布。
根目录中的文件（目前只有`readbdf.py`和`pinyin_hanzi`文件）以 GNU Lesser General Public License (LGPL) 2.1 协议发布。
各个子目录中的文件以其他协议发布，你可以在对应目录中查看它们的协议。

## Acknowledgement / 致谢
- [PSF Tools](https://www.seasip.info/Unix/PSF/) for the tool dumping psf fonts to a custom text format and converting back.
- [bdf2psf](https://packages.debian.org/unstable/bdf2psf) for bdf-to-psf converting tool.
- [Libertinus Fonts](https://github.com/alerque/libertinus) for the "Libertinus Mono" font, which I use for the ASCII range.
- The Institute of Software, Academia Sinica (中国科学院软件研究所) for making the `gb24st.bdf` 24-pixel Song Ti bitmap font free for everyone as early as the year 1988.
- [Andries Brouwer](https://www.win.tue.nl/~aeb/linux/kbd/font-formats.html) and [OSDev Wiki](https://wiki.osdev.org/PC_Screen_Font) for great documentation of PC Screen Font (psf) file format.
- [fcitx/libime](https://github.com/fcitx/libime) for pinyin data
- [bdflib](https://bdflib.readthedocs.io/en/stable/index.html), a Python library for working with BDF fonts.
