mood_index = int(input("miku今天心情怎样（1-10）\n"))
if mood_index > 5 :
    print("太好了，来一起合奏吧")
else :
    if input("带了乐器吗？\n") == "带了":
        print("一起合奏把坏心情赶走吧")
    else :
        print("没事米库，我们出去走走")