import getpass
import requests
import json
from os import system, name
from datetime import datetime


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
    files = []
    for i in req["entries"]:
        try:
            if i["folder"]:
                folders.append(i)
        except:
            pass
        try:
            if i["@type"] == 'message':
                files.append(i)
        except:
            pass

    class Longest:
        class Directories:
            name = 4
            viewName = 5
            idName = 2
            permName = 2

        class Files:
            name = 4
            mime_type = 4
            id = 2
            size = 4
            views = 5
            date = 4

    class CurrentLen:
        class Directories:
            name = 0
            viewName = 0
            idName = 0
            permName = 0

        class Files:
            name = 0
            mime_type = 0
            id = 0
            size = 0
            views = 0
            date = 0

    print(bcolors.FAIL + "DIRECTORIES" + bcolors.ENDC)
    for folder in folders:
        CurrentLen.Directories.name = len(str(folder["name"]))
        CurrentLen.Directories.idName = len(str(folder["id"]))
        CurrentLen.Directories.viewName = len(str(folder["view_count"]))
        CurrentLen.Directories.permName = len(str(folder["permissions"]))
        if CurrentLen.Directories.name > Longest.Directories.name:
            Longest.Directories.name = CurrentLen.Directories.name
        if CurrentLen.Directories.idName > Longest.Directories.idName:
            Longest.Directories.idName = CurrentLen.Directories.idName
        if CurrentLen.Directories.viewName > Longest.Directories.viewName:
            Longest.Directories.viewName = CurrentLen.Directories.viewName
        if CurrentLen.Directories.permName > Longest.Directories.permName:
            Longest.Directories.permName = CurrentLen.Directories.permName
    print(bcolors.WARNING + "Name" + bcolors.ENDC, end="")
    for i in range(0, Longest.Directories.name):
        print(" ", end="")
    print(bcolors.WARNING + "ID" + bcolors.ENDC, end="")
    for i in range(-1, Longest.Directories.idName):
        print(" ", end="")
    print(bcolors.WARNING + "Share" + bcolors.ENDC, end="")
    for i in range(0, Longest.Directories.viewName):
        print(" ", end="")
    print(bcolors.WARNING + "Views" + bcolors.ENDC, end="")
    for i in range(0, Longest.Directories.permName):
        print(" ", end="")
    print(bcolors.WARNING + "Perm" + bcolors.ENDC)

    for folder in folders:
        CurrentLen.Directories.name = len(folder["name"])
        CurrentLen.Directories.idName = len(str(folder["id"]))
        CurrentLen.Directories.viewName = len(str(folder["view_count"]))
        CurrentLen.Directories.permName = len(str(folder["permissions"]))
        print(bcolors.OKGREEN + folder["name"] + bcolors.ENDC, end="")
        for i in range(-1 - indent, Longest.Directories.name - CurrentLen.Directories.name):
            print(" ", end="")
        print(folder["id"], end="")
        for i in range(0 - indent, Longest.Directories.idName - CurrentLen.Directories.idName):
            print(" ", end="")
        if folder["shared"]:
            print(bcolors.OKGREEN + "  +" + bcolors.ENDC, end='')
        else:
            print(bcolors.FAIL + "  -" + bcolors.ENDC, end='')
        for i in range(0 - indent, Longest.Directories.viewName - CurrentLen.Directories.viewName):
            print(" ", end="")
        print(folder["view_count"], end="")
        for i in range(-5 - indent, Longest.Directories.permName - CurrentLen.Directories.permName):
            print(" ", end="")
        if folder["permissions"] == "write":
            print(" ", end="")
        print(folder["permissions"])
    print()
    print(bcolors.FAIL + "FILES" + bcolors.ENDC)

    for file in files:
        human_size = file["content"]["document"]["document"]["size"]
        human_size_type = "B"
        if human_size > 1024:
            human_size = human_size / 1024
            human_size_type = "KB"
            if human_size > 1024:
                human_size = human_size / 1024
                human_size_type = "MB"
                if human_size > 1024:
                    human_size = human_size / 1024
                    human_size_type = "GB"
        human_size = round(human_size, 2)
        human_size = str(str(human_size) + " " + human_size_type)
        human_date = (datetime.utcfromtimestamp(file["date"]).strftime('%Y-%m-%d %H:%M:%S'))
        CurrentLen.Files.date = len(str(human_date))
        CurrentLen.Files.size = len(human_size)
        CurrentLen.Files.name = len(str(file["content"]["document"]["file_name"]))
        CurrentLen.Files.mime_type = len(str(file["content"]["document"]["mime_type"])) - 12
        CurrentLen.Files.id = len(str(file["content"]["document"]["document"]["id"]))
        CurrentLen.Files.views = len(str(file["views"]))

        if CurrentLen.Files.name > Longest.Files.name:
            Longest.Files.name = CurrentLen.Files.name
        if CurrentLen.Files.mime_type > Longest.Files.mime_type:
            Longest.Files.mime_type = CurrentLen.Files.mime_type
        if CurrentLen.Files.id > Longest.Files.id:
            Longest.Files.id = CurrentLen.Files.id
        if CurrentLen.Files.size > Longest.Files.size:
            Longest.Files.size = CurrentLen.Files.size
        if CurrentLen.Files.views > Longest.Files.views:
            Longest.Files.views = CurrentLen.Files.views
        if CurrentLen.Files.date > Longest.Files.date:
            Longest.Files.date = CurrentLen.Files.date

    print(bcolors.WARNING + "Name" + bcolors.ENDC, end="")
    for i in range(0, Longest.Files.name):
        print(" ", end="")
    print(bcolors.WARNING + "Type" + bcolors.ENDC, end="")
    for i in range(-1, Longest.Files.mime_type):
        print(" ", end="")
    print(bcolors.WARNING + "ID" + bcolors.ENDC, end="")
    for i in range(0, Longest.Files.id):
        print(" ", end="")
    print(bcolors.WARNING + "Size" + bcolors.ENDC, end="")
    for i in range(0, Longest.Files.size):
        print(" ", end="")
    print(bcolors.WARNING + "Views" + bcolors.ENDC, end="")
    for i in range(0, Longest.Files.views):
        print(" ", end="")
    print(bcolors.WARNING + "Date" + bcolors.ENDC)

    for file in files:
        human_size = file["content"]["document"]["document"]["size"]
        human_size_type = "B"
        if human_size > 1024:
            human_size = human_size / 1024
            human_size_type = "KB"
            if human_size > 1024:
                human_size = human_size / 1024
                human_size_type = "MB"
                if human_size > 1024:
                    human_size = human_size / 1024
                    human_size_type = "GB"
        human_size = round(human_size, 2)
        human_size = str(str(human_size) + " " + human_size_type)
        human_date = (datetime.utcfromtimestamp(file["date"]).strftime('%Y-%m-%d %H:%M:%S'))
        CurrentLen.Files.date = len(str(human_date))
        CurrentLen.Files.size = len(human_size)
        CurrentLen.Files.name = len(str(file["content"]["document"]["file_name"]))
        CurrentLen.Files.mime_type = len(str(file["content"]["document"]["mime_type"])) - 12
        CurrentLen.Files.id = len(str(file["content"]["document"]["document"]["id"]))
        CurrentLen.Files.views = len(str(file["views"]))
        print(bcolors.OKBLUE + file["content"]["document"]["file_name"] + bcolors.ENDC, end="")
        for i in range(-1 - indent, Longest.Files.name - CurrentLen.Files.name):
            print(" ", end="")
        print(file["content"]["document"]["mime_type"][file["content"]["document"]["mime_type"].find("/") + 1:], end="")
        for i in range(-2 - indent, Longest.Files.mime_type - CurrentLen.Files.mime_type):
            print(" ", end="")
        print(file["content"]["document"]["document"]["id"], end="")
        for i in range(1 - indent, Longest.Files.id - CurrentLen.Files.id):
            print(" ", end="")
        print(human_size, end="")
        for i in range(-1 - indent, Longest.Files.size - CurrentLen.Files.size):
            print(" ", end="")
        print(file["views"], end="")
        for i in range(-2 - indent, Longest.Files.views - CurrentLen.Files.views):
            print(" ", end="")
        print(human_date)


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
