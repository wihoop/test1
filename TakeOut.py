class Eat:
    def __init__(self,name,number,adress,eat,time):
        self.name=name
        self.number=number
        self.adress=adress
        self.eat=eat
        self.time=time

class Runner:
    def __init__(self,name):
        self.name=name
    def runner(self,a):
        print("%s先生(女士)，我是送外卖的,已经到了%s"%(a.name,a.adress))

class  DeliveryTime:
    def __init__(self,time):
        self.time=time
    def deliverytime(self,e):
        print("预计配送时间是:%s"%(e.time))

class Restaurant:
    def __init__(self,name,adress):
        self.name=name
        self.adress=adress
    def ss(self,people,rider):
        print("%s先生(女士),%s骑手已接单"%(people.name,rider.name))
if  __name__ == "__main__":
    s=Eat("小微",'123456','电子校','蛋炒面','')
    a=Runner("小张")
    b=Restaurant("xx",'xx')
    c=DeliveryTime("12：30")
    b.ss(s,a)  
    c.deliverytime(c)
    a.runner(s)
 
