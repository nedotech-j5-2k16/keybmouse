try:
    import os
    from platform import system, release
    if system() == "Windows": # Windows, no need to explain what is this
        clearcmd = "cls" # ok, very memorable
    elif system() == "Linux": # Linux, very customizable core
        clearcmd = "clear" # also memorable
    elif system() == "Darwin": # MacOS, OS on all iMac and MacBook
        clearcmd = "/usr/bin/osascript -e 'tell application \"System Events\" to tell process \"Terminal\" to keystroke \"k\" using command down'" # WHAT IS THIS S##T
    else: # any other system
        exit("You are using unsupported system. Please, use Windows, Linux or MacOS")
    os.system(clearcmd) # clear screen
    print() # some cool Y-axis indentation
    print(" Welcome to keybmouse! Select any mode")
    print()
    print(" 1. DualShock2->PC")
    print(" 2. Exit")
    print()
    select = input(" Select mode: ")
    if select == "1":
        print("unrealised")
    else:
        os.system("clearcmd")  # clear screen
        exit("Bye!")  # say bye to user and exit:(
except EOFError:
    os.system(clearcmd) # clear screen
    exit("Bye!") # say bye to user and exit:(
except KeyboardInterrupt:
    os.system(clearcmd)  # clear screen
    exit("Bye!")  # say bye to user and exit:(
