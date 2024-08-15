class person:
    def attributes(self,name,age):
        print("Name is:",name,"| Age is:",age)
        self.name = name
    def greeting(self):
        print("Welcome! ",self.name)
p = person()
p.attributes("Mujtaba",23)
p.greeting()