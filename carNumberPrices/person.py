class Person:
    def __init__(self, name, isAdmin):
        self.name = name
        self.isAdmin = isAdmin


class Admin(Person):
    __login = "akmal"
    __password = 2222

    def __init__(self, name, isAdmin):
        super().__init__(name, isAdmin)
        self.carNumbers = []
        self.userSalesNumber = []

    def checkPasswd(self):
        while True:
            if self.isAdmin == "admin":
                login = input("Enter login: ")
                parol = int(input("Enter password: "))
                if login == self.__login and parol == self.__password:
                    print("Dasturga xush kelibsiz!")
                    return True
                    break
                else:
                    print("Login yoki parol noto'g'ri!")
                    return False
            else:
                print("Siz admin emassiz!")
                return False

    def addNumber(self):
        newnumber = input("Sotuvga raqam qo'shing (masalan: 90A001AB): ")
        numberPrise = int(input("Narxini kiriting: "))
        carNum = {
            "id": len(self.carNumbers) + 1,
            "number": newnumber,
            "prise": numberPrise,
            "status": "mavjud"
        }
        self.carNumbers.append(carNum)
        print("Raqam qo'shildi")

    def upgradeNumber(self):
        idEdit = int(input("Tahrir qilmoqchi bo'lgan raqamning ID raqamini kiriting: "))
        for car in self.carNumbers:
            if car["id"] == idEdit:
                editNum = input("Raqamni tahrirlashingiz mumkin: ")
                price = int(input("Yangi narxni kiriting: "))
                newStatus = input("Yangi holatni kiriting (mavjud/sotilgan): ")
                car["number"] = editNum
                car["prise"] = price
                car["status"] = newStatus
                print(f"ID {idEdit} bo'lgan raqam muvaffaqiyatli tahrirlandi!")
                return
        print("Bunday raqam topilmadi")

    def removeNumber(self):
        removeId = int(input("Qaysi id dagi raqamni o'chirmoqchisiz: "))
        for car in self.carNumbers:
            if car["id"] == removeId:
                self.carNumbers.remove(car)
                print("Raqam o'chirildi")
                return
        print("Bunday raqam topilmadi")

    def allNumberShow(self):
        if not self.carNumbers:
            print("Hozircha raqamlar yo'q.")
            return
        for car in self.carNumbers:
            print(f"ID: {car['id']}, Raqam: {car['number']}, Narx: {car['prise']} sum, Holat: {car['status']}")

    def showUserInfo(self, users):
        if not users:
            print("Hozircha hech qanday foydalanuvchi yo'q.")
            return
        
        print("Foydalanuvchi ma'lumotlari:")
        for user_id, user_obj in users.items():
            print(f"ID: {user_id}, Ismi: {user_obj.name}, Manzili: {user_obj.addres}")
            if user_obj.userSalesNumber:
                print("  Sotib olgan raqamlar:")
                for sale in user_obj.userSalesNumber:
                    print(f"    Raqam ID: {sale['id']}, Raqam: {sale['number']}, Narxi: {sale['prise']} sum")
            else:
                print("  Sotib olgan raqamlar yo'q.")

class User(Person):
    def __init__(self, name, isAdmin, addres, login, password):
        super().__init__(name, isAdmin)
        self.userSalesNumber = []
        self.addres = addres
        self.login = login
        self.password = password

    def userStore(self, admin):
        print("Avtomobil raqamlari sotuvi dasturiga xush kelibsiz!")
        while True:
            print("1. Raqam sotib olish")
            print("2. Mavjud raqamlarni ko'rish")
            print("3. Sotib olgan raqamlarim tarixini ko'rish")
            print("4. Ortga qaytish")
            userChoice = int(input("Tanlovingizni kiriting: "))

            if userChoice == 1:
                self.priseNumber(admin)
            elif userChoice == 2:
                if admin is None:
                    print("Hozircha raqamlar mavjud emas! Admin raqam qoshmagan")
                else:   
                    admin.allNumberShow()
            elif userChoice == 3: 
                self.showSaleHistory()
            elif userChoice == 4:
                break
            else:
                print("Noto'g'ri tanlov!")

    def priseNumber(self, admin):
        userSale = input("Sotib olmoqchi bo'lgan raqamni kiriting (masalan: 01A123BD): ")
        for car in admin.carNumbers:
            if car["number"] == userSale and car["status"] == "mavjud":
                print("Raqam haqida ma'lumotlar:")
                print(f"ID: {car['id']}, Raqam: {car['number']}, Narx: {car['prise']} sum, Holat: {car['status']}")
                saleChoice = input("Raqamni sotib olasizmi? (ha/yo'q): ")
                if saleChoice.lower() == "ha":
                    car["status"] = "sotilgan"
                    self.userSalesNumber.append(car)
                    print(f"Raqam {car['number']} sotib olindi.")
                return
        print("Bu raqam mavjud emas yoki allaqachon sotilgan.")

    def showSaleHistory(self):
        if not self.userSalesNumber:
            print("Hozircha hech qanday raqam sotib olmadingiz.")
            return
        print("Sotib olgan raqamlaringiz tarixi:")
        for sale in self.userSalesNumber:
            print(f"Raqam: {sale['number']}, Narx: {sale['prise']} sum")
    