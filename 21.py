class FileManager:
    def Read_file(self,file_path):
        with open(file_path,"r") as file:
            data = file.read()
            print(data)
    def Write_file(self,file_path,content):
        with open(file_path,"w") as file:
            data = file.write(content)
            print(data)

fir = FileManager()
fir.Read_file("C:\\Users\\Mujtaba\\Desktop\\programming homework\\honai.txt")
fir.Write_file("C:\\Users\\Mujtaba\\Desktop\\programming homework\\Mujtaba.text","assalamo alikom Mujtaba Sarwari  welcome to our program")