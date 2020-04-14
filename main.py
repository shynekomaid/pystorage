import getpass
import requests
import json
from os import system, name


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def promt():
    promt = input("> ")
    if promt == "exit":
        exit(0)
    elif promt[0] == "l" and promt[1] == "s":
        ls(promt[1:])


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ls(data):
    req = json.loads(get("documents", TOKEN).content.decode())
    indent = 3
    folders = []
    for i in req["entries"]:
        try:
            if i["folder"]:
                folders.append(i)
        except:
            pass
    longestFolderName = 4
    longestIDName = 2
    for folder in folders:
        folderNameLen = len(folder["name"])
        folderIDLen = len(str(folder["id"]))
        if folderNameLen > longestFolderName:
            longestFolderName = folderNameLen
        if folderIDLen > longestIDName:
            longestIDName = folderIDLen
    print(bcolors.WARNING + "Name" + bcolors.ENDC, end="")
    for i in range(0, longestFolderName):
        print(" ", end="")
    print(bcolors.WARNING + "id" + bcolors.ENDC, end="")
    for i in range(0, longestIDName):
        print(" ", end="")
    print(bcolors.WARNING + "share" + bcolors.ENDC)
    for folder in folders:
        folderNameLen = len(folder["name"])
        folderIDLen = len(str(folder["id"]))
        print(bcolors.OKGREEN + folder["name"] + bcolors.ENDC, end="")
        for i in range(0 - indent, longestFolderName - folderNameLen):
            print(" ", end="")
        print(folder["id"], end="")
        for i in range(0 - indent, longestIDName - folderIDLen):
            print(" ", end="")
        if folder["shared"]:
            print(bcolors.OKGREEN + "  +" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "  -" + bcolors.ENDC)


def get(adr, TOKEN):
    try:
        req = requests.get('https://www.xran.ru/' + adr,
                           headers={'Accept': 'application/json',
                                    'Authorization': TOKEN}, )
    except:
        return 1
    return req


if __name__ == '__main__':

    while True:
        login_data = getpass.getpass("Please enter you login@password from xran.ru or type 'exit' to exit:\n")
        if login_data == "exit":
            exit(0)
        try:
            login_data = login_data.split("@")
            auth_data = {'login': login_data[0], 'password': login_data[1]}
        except:
            continue
        break
    session = requests.Session()
    auth = session.post('https://www.xran.ru/users/telegram/authorize', {
        'username': auth_data['login'],
        'password': auth_data['password'],
        'remember': 1,
    })
    try:
        TOKEN = eval(auth.content.decode())["access_token"]
    except:
        print("Wrong login data!")
        exit(1)

    clear()
    print("You logged in.")
    while True:
        promt()
