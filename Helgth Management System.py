Client_List = {1: "Harry", 2: "Rohan", 3: "Satyajit", 4: "Rai",}
Log_List = {1: "Exercise", 2: "Diet"}


def getdate():
    import datetime
    return datetime.datetime.now()


k = 'y'
while k == "y":
    try:
        print("Select Client Name: ")
        for key, value in Client_List.items():
            print("Press ", key, "for", value, "\n", end="")
        Client_Name = int(input())
        print("Selected client: ", Client_List[Client_Name], "\n", end="")

        print("Press 1 for Log")
        print("Press 2 for Retrieve")
        op = int(input())

        if op == 1:
            for key, value in Log_List.items():
                print("Press ", key, "for Log", value, "\n", end="")
            Log_Name = int(input())
            print("Selected Job: ", Log_List[Log_Name])
            file = open(Client_List[Client_Name] + "_" + Log_List[Log_Name] + ".txt", "a")
            Key = 'y'
            while Key != "n":
                print("Please enter ", Log_List[Log_Name], "\n", end="")
                Mydata = input()
                file.write("[" + str(getdate()) + "]:" + Mydata + "\n")
                Key = input("Do you want to add more data?y/n:")
                continue
            file.close()
        elif op == 2:
            for key, value in Log_List.items():
                print("Press ", key, "for Retrive", value, "\n", end="")
            Log_Name = int(input())
            print(Client_List[Client_Name], "-", Log_List[Log_Name], "Report:"",\n", end="")
            file = open(Client_List[Client_Name] + "_" + Log_List[Log_Name] + ".txt")
            context = file.readlines()
            for item in context:
                print(item, end=" ")
            file.close()
        else:
            print("Please enter valid input..")
    except Exception as e:
        print(e)

    k = input("Do you want to continu ..?y/n")
    continue
