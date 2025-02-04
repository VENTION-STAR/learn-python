class VocaloidSinger :
    #定义属性
    def __init__(self,name,age,rank,sex):
        self.name = name
        self.age = age
        self.rank = rank
        self.sex = sex
singer_1 = VocaloidSinger('miku',16,1,'女生')
print(f"第{singer_1.rank}名是{singer_1.name},{singer_1.age}岁，{singer_1.sex}")