class Demo:
    a=10
    b=20
    def __init__(self,c,d):
        self.c=c
        self.d=d
    def display(self):
        print(self.c,self.d)
    def ch_c(self,new_c):
        self.c=new_c
    @classmethod
    def disp(cls):
      print(cls.a,cls.b)
    @staticmethod
    def msg():
      print("public acess specifier")
user=Demo(30,40)
user.display()
user.ch_c(50)
user.display()