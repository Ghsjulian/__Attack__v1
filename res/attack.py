import os
import threading
import time
from res import color


"""
File: FILENAME:pass.py
Author: Ghs Julian 
Description: This is class of threading
"""

class __Attack__:
    def __init__(self):
        self.word_list = {}
        self.threads = []
        self.match = False
        self.message = ""
        self.thread_limit = 0
        self.user_name = ""
        self.password = ""
        self.total_password = 0
        self.found_password = ""
        self.file_over = ""
        self.trying = 0
        self.start = float()
        self.end = float()
    def __run__(self,thread_time=100):
        message = ""
        list_name = "list_"
        with open("words.txt", "r") as file:
            total_words = [word.strip() for word in file]
        total_len = len(total_words)
        thread_len = thread_time
        list_len = total_len//thread_len
        item = list_len
        add = 1
        count = 0
        thred_limit = 0
        while len(self.word_list)<thread_len:
            self.word_list[list_name+str(add)] = total_words[count:list_len]
            count = list_len
            list_len +=item
            add += 1
        self.total_password = len(self.word_list)*len(self.word_list["list_1"])
    def __start__(self,thread_time=100):
        self.__run__(thread_time)
        if self.match == False:
            self.start = time.perf_counter()
            for i in self.word_list:
                t = threading.Thread(target=self.__login__, args=(self.word_list[i], self.user_name,self.password))
                self.threads.append(t)
                t.start()
                self.thread_limit += 1
                print(color.LIGHT_CYAN+color.BOLD+"\n _______________________________________________",end="\r")
                print(color.LIGHT_CYAN+color.BOLD+color.BOLD+f"\n  [{self.trying}]"+color.YELLOW+color.BOLD+" Trying Password...  ",end="\r")
                print(color.LIGHT_CYAN+color.BOLD+"\n _______________________________________________",end="\r")
            for t in self.threads:
                t.join()
            self.end = time.perf_counter()
            self.file_over = "Password Not Found In This Dictionary.\n Please Use Another Password Dictionary\n To Find Your Exact Password !"
        if self.match:
            self.__success_()
        self.__file_over__()
    def __login__(self,words,user_name, password):
        for word in words:
            if word == password:
                self.end = time.perf_counter()
                self.found_password = word
                self.match = True 
                break
                exit()
            self.trying += 1
    def __success_(self):
        if self.match:
            os.system("clear")
            print("\n")
            os.system("figlet -f small ' Successful'| lolcat")
            print(color.LIGHT_CYAN+color.BOLD+" _______________________________________________")
            print(color.PURPLE+color.BOLD+" _______________________________________________\n")
            print(color.LIGHT_GREEN+color.BOLD+"\n [+] "+color.YELLOW+color.BOLD+" Password Found         :  "+color.LIGHT_GREEN+color.BOLD,"✅  Successfully")
            print(color.LIGHT_GREEN+color.BOLD+"\n [+] "+color.YELLOW+color.BOLD+" Total Password         :  "+color.LIGHT_GREEN+color.BOLD,self.total_password)
            print(color.LIGHT_GREEN+color.BOLD+"\n [+] "+color.YELLOW+color.BOLD+" Your Password          :  "+color.LIGHT_GREEN+color.BOLD,self.found_password)
            print(color.LIGHT_GREEN+color.BOLD+"\n [+] "+color.YELLOW+color.BOLD+" Total Threads          :  "+color.LIGHT_GREEN+color.BOLD,self.thread_limit)
            print(color.LIGHT_GREEN+color.BOLD+"\n [+] "+color.YELLOW+color.BOLD+" Total Trying Time      :  "+color.LIGHT_GREEN+color.BOLD,self.trying)
            print(color.LIGHT_GREEN+color.BOLD+"\n [+] "+color.YELLOW+color.BOLD+" Total Executing Time   :  "+color.LIGHT_GREEN+color.BOLD,str(self.end-self.start))
            print(color.PURPLE+color.BOLD+"\n _______________________________________________")
            print(color.LIGHT_CYAN+color.BOLD+" _______________________________________________")
    def __file_over__(self):
        if self.match == False:
            os.system("clear")
            print("\n")
            os.system("figlet -f small 'Not Found'| lolcat")
            print(color.LIGHT_CYAN+color.BOLD+" _______________________________________________")
            print(color.LIGHT_WHITE+color.BOLD+"\n Total Password         :  "+color.YELLOW+color.BOLD,self.total_password)
            print(color.LIGHT_WHITE+color.BOLD+"\n Total Trying Time      :  "+color.YELLOW+color.BOLD,self.trying)
            print(color.LIGHT_WHITE+color.BOLD+"\n Total Threads          :  "+color.YELLOW+color.BOLD,self.thread_limit)
            print(color.LIGHT_WHITE+color.BOLD+"\n Total Executing Time   :  "+color.YELLOW+color.BOLD,str(self.end-self.start))
            print(color.LIGHT_CYAN+color.BOLD+" _______________________________________________")
            print(color.LIGHT_CYAN+color.BOLD+" _______________________________________________")
            print(color.LIGHT_GREEN+color.BOLD+"\n [Note] : "+color.RED+color.BOLD+self.file_over)
    def __intro__(self):
        self.user_name = "YOUR_USER_NAME"
        os.system("clear")
        print("\n")
        os.system("figlet -f small '__Attack__'| lolcat")
        print(color.LIGHT_CYAN+color.BOLD+" _______________________________________________")
        print(color.LIGHT_GREEN+color.BOLD+" _______________________________________________")
        print(color.LIGHT_WHITE+color.BOLD+"\n Dictionary Attack     : "+color.YELLOW+color.BOLD,"For Testing Passwords")
        print(color.LIGHT_WHITE+color.BOLD+"\n Used Multiple Threads : "+color.YELLOW+color.BOLD,"It's Create For Educational")
        print(color.LIGHT_WHITE+color.BOLD+"\n My Personal Portfolio : "+color.YELLOW+color.BOLD,"https://ghsresume.netlify.app")
        print(color.LIGHT_WHITE+color.BOLD+"\n Github Profile Link   : "+color.YELLOW+color.BOLD,"https://github.com/Ghsjulian")
        print(color.LIGHT_WHITE+color.BOLD+"\n Follow Me On GitHub   : "+color.YELLOW+color.BOLD,"Ghs Julian")
        print(color.LIGHT_CYAN+color.BOLD+"\n _______________________________________________")
        print(color.LIGHT_GREEN+color.BOLD+" _______________________________________________\n")
        print(color.LIGHT_GREEN+color.BOLD+"\n [OPTIONS] : "+color.PURPLE+color.BOLD+"Select An Option ")
        # Select  Options 
        print(color.LIGHT_GREEN+color.BOLD+"\n [!] "+color.LIGHT_CYAN+color.BOLD+"Create New Password Dictionary   : "+color.YELLOW+color.BOLD,"[01]")
        print(color.LIGHT_GREEN+color.BOLD+"\n [!] "+color.LIGHT_CYAN+color.BOLD+"See Total Password In Dictionary : "+color.YELLOW+color.BOLD,"[02]")
        print(color.LIGHT_GREEN+color.BOLD+"\n [!] "+color.LIGHT_CYAN+color.BOLD+"Delete Password Dictionary       : "+color.YELLOW+color.BOLD,"[03]")
        print(color.LIGHT_GREEN+color.BOLD+"\n [!] "+color.LIGHT_CYAN+color.BOLD+"Start Your Dictionary Attack     : "+color.YELLOW+color.BOLD,"[04]")
                
        
        print(color.LIGHT_CYAN+color.BOLD+"\n _______________________________________________")
        print(color.LIGHT_GREEN+color.BOLD+" _______________________________________________")
        cmd = input(color.GREEN+color.BOLD+"\n [+] "+color.LIGHT_CYAN+color.BOLD+"What's Your Option ?  "+color.LIGHT_GREEN+color.BOLD+color.BOLD)
        
        #if thread == "":
        #return 100
        #return int(thread)
        if cmd == "01":
            os.system("python res/gen_pass.py")
        elif cmd == "04":
            self.password = input(color.GREEN+color.BOLD+"\n [+] "+color.LIGHT_CYAN+color.BOLD+"Enter Your Password For Testing  : "+color.LIGHT_GREEN+color.BOLD+color.BOLD)
            self.__start__()


# Example...
"""
data = {
    "user_name" : "Ghs Julian",
    "password" : "ghsjulian@291"
}
attack = __Attack__(data)
attack.__start__(500)
"""