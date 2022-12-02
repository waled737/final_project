def intro():  # تقوم هذه الوظيفة بطباعة قائمة المستخدم وادخال اختياره

    print()
    print()
    print("Supermarket Management System\n" + "=" * 35)
    print("1. Print items info\n" + "2. Search for an item\n" + "3. Add new item")
    print("4. Remove an item\n" + "5. Sell an item\n" + "6. Update an item")
    print("7. Exit\n" + "=" * 35)

    # الطلب من المستخدم ادخال اختياره والتحقق منه اذا كان محصور بين 1 و 7
    choice = input("Enter your choice: ")
    while (choice.isdigit() == False) or (choice == "0") or (int(choice) > 8):
        print("Wrong enter,Please try again")
        choice = input("Enter your choice: ")
    return choice


def choice_1or2():  # تقوم هذه الوظيفة بادخال الاختيار وقبول "1" او "2" فقط

    choice2 = input("Enter your choice:")
    while choice2 != "1" and choice2 != "2":
        print("Wrong enter,Please try again")
        choice2 = input("Enter your choice: ")
    return choice2


def _format():  # تقوم هذه الوظيفة بطباعة راس الجدول

    print("%-15s" % "SN", "%-23s" % "Item Name", "%-10s" % "Price", "%-20s" % "Available Items", "%-10s" % "Sold Items")


def _format1(pos, SNL, INL, PRL, AIL, SIL):  # تقوم هذه الوظيفة بطباعة محتويات القوائم منسقة

    print("%-15s" % SNL[pos], "%-23s" % INL[pos], "%5s" % PRL[pos], "%20s" % AIL[pos], "%15s" % SIL[pos])


def creat_list():  # itemsInfo تقوم هذه الوظيفة بانشاء مجموعة من القوائم حسب محتويات ملف
    try:

        # انشاء القوائم
        SNL = []
        # Serial Number List
        INL = []
        # Item Name List
        PRL = []
        # PRice List
        AIL = []
        # Available Items List
        SIL = []
        # Sold Items List

        # فتح الملف و وضع محتوياته في القوائم
        infile = open("itemsInfo.txt", "r")
        for line in infile:
            wordlist = line.split(",")
            SNL.append(wordlist[0])
            INL.append(wordlist[1])
            PRL.append(wordlist[2])
            AIL.append(wordlist[3])
            SIL.append(wordlist[4].rstrip())

        infile.close()  # اغلق الملف
        return SNL, INL, PRL, AIL, SIL  # استرجاع القوائم

    except FileNotFoundError:
        print("File does not exist")
    except Exception as ex:
        print("Eror: " + str(ex))


def creat_list1():  # soldItems تقوم هذه الوظيفة بانشاء مجموعة من القوائم حسب محتويات ملف
    try:

        S_SNL = []
        # Soled_SN List
        S_NL = []
        # Siled_Name List

        # فتح الملف و وضع محتوياته في القوائم
        infile = open("soldItems.txt", "r")
        for line in infile:
            wordlist = line.split(",")
            S_SNL.append(wordlist[0])
            S_NL.append(wordlist[1].rstrip())

        infile.close()  # اغلق الملف
        return S_SNL, S_NL  # استرجاع القوائم

    except FileNotFoundError:
        print("File does not exist")
    except Exception as ex:
        print("Eror: " + str(ex))


def add_to_file(SNL, INL, PRL, AIL, SIL):  # itemsInfo تقوم هذه الوظيفة بكتابة محتويات القوائم داخل الملف
    try:
        outfile = open("itemsInfo.txt", "w")
        for i in range(len(SNL)):
            outfile.write(SNL[i] + "," + INL[i] + "," + PRL[i] + "," + str(AIL[i]) + "," + str(SIL[i]) + "\n")
        outfile.close()

    except Exception as ex:
        print("Eror: " + str(ex))


def add_to_file1(S_SNL, S_NL):  # soldItems تقوم هذه الوظيفة بكتابة محتويات القوائم داخل الملف
    try:
        outfile = open("soldItems.txt", "w")
        for i in range(len(S_NL)):
            outfile.write(S_SNL[i] + "," + S_NL[i] + "\n")
        outfile.close()

    except Exception as ex:
        print("Eror: " + str(ex))


def item_info():  # itemsInfo تقوم هذه الوظيفة بعرض جميع محتويات العناصر داخل ملف
    try:

        # طباعة محتويات الملف منسقة
        infile = open("itemsInfo.txt", "r")
        print("%-15s" % "SN", "%-23s" % "Item Name", "%-10s" % "Price", "%-20s" % "Total Items")  # طباعة رأس الجدول
        for line in infile:
            wordlist = line.split(",")
            print("%-15s" % wordlist[0], "%-23s" % wordlist[1], "%5s" % wordlist[2],
                  "%16d" % (int(wordlist[3]) + int(wordlist[4])))
        infile.close()

    except FileNotFoundError:
        print("File does not exist")
    except Exception as ex:
        print("Eror: " + str(ex))


def search():  # تستخدم هذه الوظيفة للبحث عن عنصر داخل الملف
    try:
        SNL, INL, PRL, AIL, SIL = creat_list()
        Found = False
        print("1. By Serial Number\n" + "2. By Item Name")
        choice2 = choice_1or2()

        # SN البحث عن عنصر بادخال
        if choice2 == "1":
            SN = input("Enter serial number of the item: ")
            if SN in SNL:
                pos = SNL.index(SN)
                _format()
                _format1(pos, SNL, INL, PRL, AIL, SIL)
            else:
                print("The item you search is not found")

        # البحث عن عنصر بادخال اسمه او جزء منه
        else:
            IN = input("Enter item name or part of it: ")
            # Item Name

            for name in INL:
                if (IN.lower()) in (name.lower()):
                    pos = INL.index(name)
                    if Found:
                        _format1(pos, SNL, INL, PRL, AIL, SIL)
                    else:
                        _format()
                        _format1(pos, SNL, INL, PRL, AIL, SIL)
                        Found = True
            if not Found:
                print("The item you search is not found")

    except Exception as ex:
        print("Eror: " + str(ex))


def add():  # تقوم هذه الوظيفة باضافة عنصر للملف
    try:
        SNL, INL, PRL, AIL, SIL = creat_list()

        SN = input("Enter item SN: ")
        # Serial Number

        # التحقق اذا كان الرقم المدخل رقم صحيح موجب مكون من اربع خانات غير متواجد في الملف
        while len(SN) != 4 or SN in SNL or SN.isdigit() == False:
            if len(SN) != 4:
                print("The length of SN must be 4")
                SN = input("Enter item SN: ")
            elif SN in SNL:
                print("Serial Number already exists")
                SN = input("Enter item SN: ")
            else:
                print("SN must be a positive value")
                SN = input("Enter item SN: ")

        IN = input("Enter item name:")
        # Item Name

        # التحقق اذا كان الاسم المدحل غير فارغ
        while IN == "" or IN.isspace():
            print("Item name cannot be empty")
            IN = input("Enter item name:")

        PR = input("Enter item price: ")
        # PRice

        # التحقق من السعر إذا كان رقم نسبي موجب
        if "." in PR and PR[-1] != ".":
            pos = PR.find(".")
            npr = PR[0:pos] + PR[pos + 1:]
        else:
            npr = PR
        while npr.isdigit() == False:
            print("Price must be a positive value and non-empty")
            PR = input("Enter item price: ")
            if "." in PR and PR[-1] != ".":
                pos = PR.find(".")
                npr = PR[0:pos] + PR[pos + 1:]
            else:
                npr = PR

        AI = input("Enter number of available items: ")
        # Available Items

        # التحقق اذا كان رقم صحيح موجب
        while AI.isdigit() == False:
            print("Available Items must be positive and non-empty")
            AI = input("Enter number of available items: ")

        # اضافة المدخلات للقوائم
        SNL.append(SN)
        INL.append(IN)
        PRL.append(PR)
        AIL.append(AI)
        SIL.append("0")

        add_to_file(SNL, INL, PRL, AIL, SIL)

        print("Item has been added successfully !!!")

    except Exception as ex:
        print("Eror: " + str(ex))


# itemsinfo تقوم هذه الوظيفة بحذف عنصر من ملف
def remove():
    try:
        SNL,INL,PRL,AIL,SIL=creat_list()
        SN=input("Enter serial number of the item: ")

        #التحقق من وجود الرقم المدخل في الملف وعدم وجود نسخ مباعة
        if SN in SNL:
            pos=SNL.index(SN)
            if SIL[pos]!="0":
                print("you can not remove this item, because the item has some sold copies.")

            else :
                _format()
                _format1(pos,SNL,INL,PRL,AIL,SIL)
                YON=input("you sure you want to remove this item ? [Y/N]")
                #Yes Or No

                #اذا تم تاكيد الحذف حذف العنصر
                if YON.lower()=="y" :
                    SNL.remove(SN)
                    INL.pop(pos)
                    PRL.pop(pos)
                    AIL.pop(pos)
                    SIL.pop(pos)
                    print("Item has been removed successfully :)")
                    add_to_file(SNL,INL,PRL,AIL,SIL)

                else :
                    print("ٌRemove has been cancelled")

        else :
            print("Item does not exist")

    except Exception as ex:
        print("Eror: "+str(ex))

def sell(): #itemsinfo  تقوم هذه الوظيفة ببيع عناصر من ملف
    try:
        SNL,INL,PRL,AIL,SIL=creat_list()
        S_SNL,S_NL=creat_list1()

        SN=input("Enter serial number of the item: ")
        if SN in SNL:
            pos=SNL.index(SN)

            # التحقق اذا كان عدد العناصر المتوفرة اكبر من الصفر
            if int(AIL[pos])>0:


                AIL[pos]=int(AIL[pos])-1
                SIL[pos]=int(SIL[pos])+1
                add_to_file(SNL,INL,PRL,AIL,SIL)

                NOP=input("Enter the name of the person who bought this item: ")
                #Name Of Person

                S_SNL.append(SN)
                S_NL.append(NOP)
                add_to_file1(S_SNL,S_NL)

                print("Item has been sold to",NOP,"Successfully")

            else :
                print ("All quantity of this item has been sold out")

        else :
            print("Item does not exist")

    except Exception as ex:
        print("Eror: "+str(ex))


def update(): #itemsinfo تقوم هذه الوظيفة بتحديث البيانات في ملف
    try:
        SNL,INL,PRL,AIL,SIL=creat_list()

        SN=input("Enter serial number of the item: ")

        if SN in SNL:
            pos=SNL.index(SN)
            print(" "*11,"1. Update Name\n"," "*10,"2. Update Available Items")
            choice2=choice_1or2()

            #تحديث اسم عنصر
            if choice2=="1":

                NIN=input("Enter the new name of items:")
                #New Item Name

                while NIN=="" or NIN.isspace():
                    print("Item name cannot be empty")
                    NIN=input("Enter item name:")
                INL[pos]=NIN

            # تحديث عدد العناصر المتوفرة من العنصر
            elif choice2=="2":

                NAI=input("Enter the new available number of items: ")
                #New Available Items

                while NAI.isdigit()==False :
                    print("Available Items must be positive and non-empty")
                    NAI=input("Enter number of available items: ")

                AIL[pos]=NAI

            add_to_file(SNL,INL,PRL,AIL,SIL)

        else :
            print("Item does not exist")

    except Exception as ex:
        print("Eror: "+str(ex))


def main():
    choice = intro()
    while int(choice) > 0 and int(choice) < 7:
        if choice == "1":
            item_info()
            choice = intro()

        elif choice == "2":
            search()
            choice = intro()

        elif choice == "3":
            add()
            choice = intro()

        elif choice == "4":
            remove()
            choice = intro()

        elif choice == "5":
            sell()
            choice = intro()

        elif choice == "6":
            update()
            choice = intro()

    print("Thank")


# run the program
main()

