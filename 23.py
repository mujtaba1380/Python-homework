class Configur_file:
    def read_file(self,file_path):
        self.file_path = file_path
        with open(file_path,'r') as file:
            self.data = file.read()
    def setting(self,content,k,new_value):
        content = self.data

        analyze = content.split(maxsplit=12)
        for equal in analyze:
            if equal == "=":
                analyze.remove("=")
        even_number = 0
        keys = []
        for key in analyze:
            if even_number % 2 == 0:
                keys.append(key)
            even_number += 1
        odd_number = 0
        values = []
        for value in analyze:
            if odd_number % 2 != 0:
                values.append(value)
            odd_number += 1
        zipped = zip(keys, values)
        dictionary = dict(zipped)
        dictionary[k] = new_value
        # print(dictionary)
        with open(self.file_path,"w") as file:
            for ke,val in dictionary.items():
                file.write(f"{ke} = {val}\n")

confi = Configur_file()
confi.read_file("C:\\Users\\Mujtaba\\Desktop\\programming homework\\Mujtaba.txt")
confi.setting("C:\\Users\\Mujtaba\\Desktop\\programming homework\\Mujtaba.txt","username","emal")
confi.setting("C:\\Users\\Mujtaba\\Desktop\\programming homework\\Mujtaba.txt","host","guest")