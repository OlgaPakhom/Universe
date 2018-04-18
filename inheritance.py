class spaceObjects():    
    #mass, ,orbiting objects ,radius
    def __init__(self, name, m, ro, o_o, r):
        if not str(name).isalnum():
            raise NameError('Name is not valid')
        
        self.name = str(name)
        self.m = float(m)
        self.ro = ro
        self.o_o = o_o 
        self.r = r
        self.population = 0
        
    def send_peeps_here(additional):
        self.population = self.population + additional    


class Car(spaceObjects):
    def send_peeps_here(additional):
        if self.population + additional <= 0:
            self.population = 0
        elif self.population + additional > 2:
            self.population = 2
        elif self.population + additional < 2:
            self.population = self.population + additional


class Star(spaceObjects):
    def send_peeps_here(additional):
        self.population = 0        


class Planet(spaceObjects):
    def __init__(self, name, m, ro, o_o, r, atm):
        super().__init__()
        self.atm = atm


        
