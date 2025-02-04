class Student :
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.grades = {'语文' : 0 , '数学' : 0 , '英语' : 0}
    def setgrades(self,course,grade):
        if course in self.grades :
            self.grades[course] = grade
            print('设置完毕')
        else :
            print(f"{course}成绩暂时未收录.")
    def printgrade(self):
        i = self.grades['语文']+self.grades['数学']+self.grades['英语']
        print(f"{self.name}({self.number})成绩为：")
        for course in self.grades:
            print(f"{course}: {self.grades[course]}")
        print(f'总分为：{i}')


feng = Student(input("请输入学生姓名："),input('请输入学号：'))
feng.setgrades(input('科目：'),int(input('分数：')))
feng.setgrades('数学',120)
feng.setgrades('语文',119)
feng.printgrade()