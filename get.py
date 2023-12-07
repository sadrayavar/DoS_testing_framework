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

    def getUrl(self):
        if self.url != "":
            return

    def getFile(self, url, destination):
        flag = time.time()
        temp = self.lastFile

        response = requests.get(url)
        with open(destination, "wb") as file:
            file.write(response.content)

        print(f"\nDownload {temp} took: {str(time.time() - flag)}")

    def appointFile(self):
        if self.url != "":
            self.getUrl()

        dest = os.path.join(self.path, "downloades", str(self.lastFile))
        self.lastFile += 1
        self.getFile(self.url, dest)


class Ui:
    obj = Get()
    url = "http://localhost:8000"
    attackType = ["bw", "cpu", "ram"]

    def __init__(self):
        self.selectUrl()

        while True:
            self.attackType()
            obj.getUrl()

            handle = input("\Select: ")
            handle = input("\nHow many threads: ")
            threads = []

            # add threads
            for _ in range(int(handle)):
                thread = Thread(target=obj.appointFile)
                threads.append(thread)

            # start threads
            for thread in threads:
                thread.start()

            # wait for threads to finish
            for thread in threads:
                thread.join()

    def selectUrl(self):
        print("Enter your URL or nothing for default:")
        print("( default is: http://localhost:8000 )")
        temp = include()

        if temp == "":

            pass

    def attackType(self):
        pass
