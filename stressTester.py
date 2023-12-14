import requests, os, time, shutil
from threading import Thread


class Get:
    path = os.path.dirname(os.path.abspath(__file__))
    url = ""
    lastFile = 0

    def __init__(self):
        temp = os.path.join(self.path, "downloades")
        try:
            os.makedirs(temp)
        except:
            shutil.rmtree(temp)
            os.makedirs(temp)

    def getFile(self, url, destination):
        flag = time.time()
        temp = self.lastFile

        response = requests.get(url)
        with open(destination, "wb") as file:
            file.write(response.content)

        print(f"\nDownload {temp} took: {str(time.time() - flag)}")

    def appointFile(self):
        dest = os.path.join(self.path, "downloades", str(self.lastFile))
        self.lastFile += 1
        self.getFile(self.url, dest)


class Ui:
    get = Get()
    url = ""
    type = ""
    value = ""

    def __init__(self):
        # select URL
        self.url = self.selectUrl()

        while True:
            # select attack type
            self.type = self.attackType()

            # select attack value
            self.value = self.selectValue()

            # generate url
            self.get.url = f"{self.url}/{self.type}/{self.value}"

            # ask for threads
            handle = input("\nHow many threads: ")
            threads = []

            # add threads
            for _ in range(int(handle)):
                thread = Thread(target=self.get.appointFile)
                threads.append(thread)

            # start threads
            for thread in threads:
                thread.start()

            # wait for threads to finish
            for thread in threads:
                thread.join()

    def selectUrl(self):
        while True:
            print(
                "\nEnter your URL or 0 for default: ( default is: http://localhost/ )"
            )

            temp = input()
            if temp == "0":
                return "http://localhost"
            elif temp[:4] == "http" and temp[4:7] == "://":
                return temp[:-1] if temp[-1] == "/" else temp
            else:
                continue

    def attackType(self):
        while True:
            print("\nSelect one of the options below:")
            if self.type != "":
                print(f"- 0: default (default is {self.type})")
            print("- 1: Bandwidth")
            print("- 2: CPU")
            print("- 3: RAM")
            temp = input()

            if temp == "0" and self.type != "":
                return self.type
            elif temp == "1":
                return "bw"
            elif temp == "2":
                return "cpu"
            elif temp == "3":
                return "ram"
            else:
                continue

    def selectValue(self):
        while True:
            print("\nEnter some value to use in your attack: ")
            temp = input()
            return temp


Ui()
