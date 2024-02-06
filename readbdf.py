#!/usr/bin/python
from bdflib import reader
import codecs
font = reader.read_bdf(open("songti/gb24st.bdf", "rb"))
height = 32
width = 24
v_offset = 27
count = 0
with open("pinyin_hanzi") as f:
    while True:
        line=f.readline()
        if not line:
            break
        s=line.split()
        if len(s)>=2:
            hanzis=s[1]
            zi=hanzis[0]
            try:
                gb=codecs.encode(zi, encoding="gb2312")
                glyph=font[(gb[0]-0x80)*0x100+(gb[1]-0x80)]
                print("%")
                print("// Zi", count, zi)
                count=count+1
                #print(glyph)
                print("Bitmap: ", end="")
                o_pixels=[[y for y in x] for x in glyph.iter_pixels()]
                [left, bottom, w, h]=glyph.get_bounding_box()
                #print([left, bottom, w, h])
                pixels=[["-" for j in range(0, width)] for i in range(0, height)]
                
                for i in range(0, h):
                    for j in range(0, w):
                        pixels[-bottom - h + i + v_offset][left + j] = ("#" if o_pixels[i][j] else "-")
                for l in range(0, height):
                    ll = "".join(pixels[l])
                    if l < height-1:
                        ll = ll+" \\"
                    print(ll)
                print("Unicode: ", end="")
                for h in hanzis:
                    print("[{0:08x}];".format(ord(h)), end="")
                print()
            except UnicodeError:
                pass
                #print(s[0], zi, " not found in gb2312")
                #print(hanzis)
