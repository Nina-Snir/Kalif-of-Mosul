#TODO - program, ktory vyhodnoti mat vyraz
#TODO  = +-/*()

#TODO Stack(zasobnik)= FILO, Queue(rad) = FIFO, Heap(Holder), všetky mozu byť cyklicke

#TODO- DOKONCIT KALIFA

people = int(input("Zadaj počet ľudí okolo Kalifa: "))
kill = int(input("Zadaj, koľkatého Kalif zabije: "))

class People:
    def __init__(self,people,kill):
        self.people = people
        self.kill = kill

    def list(self):
        self.all = []
        for i in range(1,self.people+1):
            self.all.append(i)
        print(self.all)
    def kill_func(self):
        count = 0 #rata na kolkom cloveku sme pre zabitie
        current= 0 #rata na ktorom cloveku sme celkovo
        so_far = 0 #rata kolko sme zabili
        while len(self.all)>1:
            while current-so_far<=len(self.all): #pokial sme neprisli na koniec listu
                if count<self.kill:
                    current+=1
                    count+=1
                elif count == self.kill:
                    so_far+=1
                    #print(self.all)
                    #print(current-so_far)
                    self.all.pop(current-so_far)
                    #print(self.all)
                    count = 0
            else:
                #print(count)
                current = 1 #nemožeme ist zasa od nuly, lebo by daloprec zleho cloveka
                so_far = 0
        return(f"Šťastná pozícia je {self.all[0]}")




p1 = People(people,kill)
print(p1.list())
print(p1.kill_func())



