with open("歌词.txt", encoding="utf-8") as song :
    f = song.readline()
    while f != '' :
        print(f)
        f = song.readline()