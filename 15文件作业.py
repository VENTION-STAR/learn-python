#任务
with open("poem.txt", "w", encoding="utf-8") as f :
    f.write('''我欲乘风归去，\n又恐琼楼玉宇，\n高处不胜寒。\n''')
with open("poem.txt", "a+", encoding="utf-8") as ff:
    ff.write('''起舞弄清影,\n何时在人间。''')
    ff.seek(0)  # 将文件指针移动到文件开头
    print(ff.read())