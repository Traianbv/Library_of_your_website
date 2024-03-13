import webbrowser


websites = []

def read_file():
    with open('websites.txt', 'r') as file:
       data = file.readlines()
       for line in data:
           line = line.strip()
           if line:
            websites.append(line)
       return websites


def write_file(add):
    with open('websites.txt', 'a') as file:
        data = file.write('\n' + add)
        print("You site was added to the list !")
    return data

def remove_file(remove):
    try:
        with open('websites.txt', 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open('websites.txt', 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != remove:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! something error")


def remove_files():
    try:
        with open('websites.txt', 'r') as fr:
            lines = fr.readlines()

        with open('websites.txt', 'w') as fw:
            for line in lines:
                if line.strip():
                    fw.write(line)
    except:
        print("Oops! Something went wrong.")

print(f"The list of your websites : {read_file()} ")

while True:
    ask_websites = input('You want to add some websites in your library ? y or n , if you want to remove the website'
                         ' from the library type r : ')
    if ask_websites == 'y':
        add = input('Add a websites to your library (ex : https://www.google.ro/)  : ')
        if add.startswith(("https://")):
            write_file(add)
        else:
            print('Type the link correctly !')
    elif ask_websites == 'r':
        remove = int(input('What websites you want to remove choose the number from the list !'))
        remove_file(remove)
    elif ask_websites == 'n':
        print('Your list is finish')
        break
    else:
        print('Choose the right answer !')


while True:
    ask_user = input("You want to open the websites from your library ?(for open the websites type 'y', to exit type 'e': ")
    if ask_user == 'y':
        for site in websites:
            webbrowser.open(site)
        break
    elif ask_user == 'e':
        print('By By')
        break
    else:
        print('Choose the right answer !')


