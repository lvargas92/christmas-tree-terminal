import sys
import time
from os import system, name 
from termcolor import colored, cprint

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#Merry Christmas message
msg1 = colored('M E R R Y', 'green')
msg2 = colored('C H R I S T M A S', 'green')

#stars colors
star_temp = colored('*', 'blue')
star_colors = [
    colored('*', 'yellow'),
    colored('*', 'cyan'),
    colored('*', 'white')
]

star1 = star_colors[0]
star2 = star_colors[1]

# tree structure
bomb = colored('()', 'red')

tree_struct = []
tree_struct.insert(0, "                                        ")
tree_struct.insert(1, "           " + star2 + "             ,")
tree_struct.insert(2, colored("                       _/^\_", 'yellow'))
tree_struct.insert(3, colored("                      <     >", 'yellow'))
tree_struct.insert(4, "     " + star1 + colored("                 /.-.\\          ", 'yellow') + star2)
tree_struct.insert(5, "              " + star1 + colored("        `/&\`                   ", "green") + star1)
tree_struct.insert(6, colored("                      ,@","green") + bomb + colored(";,\\","green"))
tree_struct.insert(7, colored("                     /_o.I %_\\    ","green") + star1)
tree_struct.insert(8, "        " + star2 + "           " + colored("(`'--:o(", "yellow") + colored("_@;","green"))
tree_struct.insert(9, "                   " + colored("/`;", "green") + colored("--.,__ `')             ", "yellow") + star2)
tree_struct.insert(10, colored("                  ;@`o % O,*`'`&\\","green"))
tree_struct.insert(11, "            " + star1 + "    " + colored("(`'--)_","yellow") + colored("@ ;o %'", "green") + bomb + colored("\\      ", "green") +star1)
tree_struct.insert(12, colored("                 /`;--._`''--._", "yellow") + colored("O'@;","green"))
tree_struct.insert(13, colored("                /&*,", "green") + bomb + colored("~o`;", "green") + colored("-.,_ `""`)", "yellow"))
tree_struct.insert(14, "     " + star1 + "          " + colored("/`,@ ;+& ","green") + bomb + colored(" o*`;-';\\", "green"))
tree_struct.insert(15, "               "+ colored("(`""--.,_", "yellow")+ colored("0 +% @' &","green") + bomb + colored("+.\\", "green"))
tree_struct.insert(16, "               " + colored("/-", "green")+ colored(".,_    ``''--....-'`)  ", "yellow") + star2)
tree_struct.insert(17, "          " + star2 + "    " + colored("/@%;o", "green") + colored("`:;'--,.__   __.'","yellow") + colored("\\ ","green"))
tree_struct.insert(18, "              "+ colored(";*,&", "green") + bomb + colored("; @ % &^;~`\"`o;@", "green") + bomb + ";         " + star1)
tree_struct.insert(19, "              "+ colored("/", "green") + bomb + colored("; o^~; & ", "green") + bomb + colored(".o@*&`;&%O\\","green"))
tree_struct.insert(20, colored("              `\"=\"==\"\"==,,,.,=\"==\"===\"`\"","green"))
tree_struct.insert(21, "           "+ colored("__.----.","cyan")+"(\\"+ colored("-''","cyan") +colored("#####","green")+colored("---...___...-----._","cyan"))
tree_struct.insert(22, "         "+ colored("'`", "cyan") +"         \\)_" + colored("`\"\"\"\"\"`","green"))
tree_struct.insert(23, "                 .--\' \')")
tree_struct.insert(24, "               o(  )_-\\    " + msg1)
tree_struct.insert(25, "                 `\"\"\"` ` " + msg2)

#print tree on terminal
tree_body = ""
for parts in tree_struct:
    tree_body = tree_body + parts + "\n"

try:
    i = 0
    while True:
        clear()
        if i == 2 :
            i = 0
            
        tree_body = tree_body.replace(star_colors[i + 1], star_temp)
        tree_body = tree_body.replace(star_colors[i], star_colors[i + 1])
        tree_body = tree_body.replace(star_temp, star_colors[i])
        print(tree_body)
        
        i = i + 1
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass
