import random
import os
import color

def gen_password (data):
  user = str(data["user_name"])
  user = user.replace(" ","").lower().strip()
  char = "@#$_&-+<>%*!?"
  birth = str(data["user_birth"])
  number = "0123456789"
  phone = str(data["user_phone"])
  words = []
  
  file = open("words.txt","w")
  while len(words) < data["length"]:
    char_2 = random.choice(char)
    word_1 = user+random.choice(char)+birth
    word_2 = user+random.choice(char)+phone[-4:]
    word_3 = user+random.choice(char)+random.choice(number)+random.choice(number)+random.choice(number)
    word_4 = char_2+char_2+user+char_2+char_2
    word_5 = data["user_name"].strip().replace(" ",char_2).lower()
    
    if word_1 not in words:
        words.append(word_1)
        file.write(word_1+"\n")
    if word_2 not in words:
        words.append(word_2)
        file.write(word_2+"\n")
    if word_3 not in words:
        words.append(word_3)
        file.write(word_3+"\n")
    if word_4 not in words:
        words.append(word_4)
        file.write(word_4+"\n")
    if word_5 not in words:
        words.append(word_5)
        file.write(word_5+"\n")
  
  
  print(color.LIGHT_CYAN+color.BOLD+" _______________________________________________")
  print(color.LIGHT_GREEN+color.BOLD+" _______________________________________________")
  print("\n")
  for i in words:
      print(color.GREEN+color.BOLD+" [+] "+color.LIGHT_CYAN+color.BOLD+"Creating Passwords ----------------->  "+color.GREEN+color.BOLD+i,end="\r")
  print(color.GREEN+color.BOLD+"\n\n ✅  "+color.BOLD+color.YELLOW+color.BOLD+"Total "+color.GREEN+color.BOLD+str(data["length"])+color.BOLD+color.YELLOW+color.BOLD+" Password Has Created !\n")
  print(color.LIGHT_CYAN+color.BOLD+" _______________________________________________")
  print(color.LIGHT_GREEN+color.BOLD+" _______________________________________________\n")

os.system("clear")
print("\n\n")
os.system("figlet -f small ' Password'| lolcat")
print(color.LIGHT_GREEN+color.BOLD+"\n [Note] : "+color.LIGHT_WHITE+color.BOLD+"Create New Password Dictionary According \n To Your Words Prompt Enter Any Users Name \n Or Words To Generate Your Password Dictionary !")
print(color.LIGHT_CYAN+color.BOLD+" _______________________________________________")
print(color.LIGHT_GREEN+color.BOLD+" _______________________________________________")
user_name = input(color.GREEN+color.BOLD+"\n [+] "+color.LIGHT_CYAN+color.BOLD+"Enter User Name :  "+color.YELLOW+color.BOLD)
user_phone = input(color.GREEN+color.BOLD+"\n [+] "+color.LIGHT_CYAN+color.BOLD+"Enter User Phone IF Has :  "+color.YELLOW+color.BOLD)
user_birth = input(color.GREEN+color.BOLD+"\n [+] "+color.LIGHT_CYAN+color.BOLD+"Enter User Birth Year If Has :  "+color.YELLOW+color.BOLD)
pass_len = int(input(color.GREEN+color.BOLD+"\n [+] "+color.LIGHT_CYAN+color.BOLD+"How Many Password You Want To Create ?  "+color.YELLOW+color.BOLD))

data = {
  "user_name":user_name,
  "user_phone":user_phone,
  "user_birth":user_birth,
  "length":pass_len
}

gen_password(data)