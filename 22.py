class Log:
    def write_error_messege(self,file_path,file_name,error_messege):
        with open(file_path + "\\" + file_name + ".txt","a") as file:
            file.write(error_messege)
            print("succesfully creat error file messege!")
error1 = Log()
error1.write_error_messege("C:\\Users\\Mujtaba\\Desktop","error messege","This is Error messege!\n")