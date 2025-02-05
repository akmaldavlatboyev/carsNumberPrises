from person import*
def runApp():
    users = {}
    userCounter = 1
    admin = None

    while True:
        roll = input("\nKim bo'lib dasturga kirasiz (admin/user):  ").strip().lower()
        name = input("Ismingizni kirting: ")
        if roll not in ["admin", "user"]:
            print("Faqat 'admin' yoki 'user' ni tanlang!")
            continue

        if roll == "admin":
            admin = Admin(name,roll)
            if admin.checkPasswd():

                while True:
                    print("\nAdmin menyusi:")
                    print("1. Raqam qo'shish")
                    print("2. Raqam tahrirlash")
                    print("3. Raqam o'chirish")
                    print("4. Mavjud raqamlarni ko'rish")
                    print("5. Foydalanuvchilar ma'lumotlarini va sotuv tarixi") 
                    print("6. Ortga qaytish")

                    try:
                        adminChoice = int(input("Tanlovingizni kiriting: "))
                    except ValueError:
                        print("Faqat raqam kiriting!")
                        continue

                    if adminChoice == 1:
                        admin.addNumber()
                    elif adminChoice == 2:
                        admin.upgradeNumber()
                    elif adminChoice == 3:
                        admin.removeNumber()
                    elif adminChoice == 4:
                        admin.allNumberShow()
                    elif adminChoice == 5:
                        admin.showUserInfo(users)
                    elif adminChoice == 6:
                        break
                    else:
                        print("Noto'g'ri tanlov!")
        
        elif roll == "user":
            login = input("Loginingizni kiriting: ").strip()
            if not login:
                print("Login bo'sh bo'lishi mumkin emas!")
                continue
            password = input("Parolingizni kiriting: ").strip()
            if not password:
                print("Parol bo'sh bo'lishi mumkin emas!")
                continue


            userFound = None
            for userId, userObj in users.items():
                if userObj.login == login and userObj.password == password:
                    userFound = userObj
                    break

            if userFound:
                print(f"Xush kelibsiz, {userFound.name}!")
                userFound.userStore(admin)
            else:
                print("Login yoki parol noto'g'ri! Tizimda yangi bo'lsangiz ro'yhatdan o'ting.")
                name = input("Ismingizni kiriting: ").strip()
                addres = input("Manzilingizni kiriting: ").strip()
                login = input("Yangi login yarating: ").strip()
                password = input("Parol yarating: ").strip()
                users[userCounter] = User(name, "user", addres, login, password)
                print(f"Foydalanuvchi {name} muvaffaqiyatli ro'yxatdan o'tdi!")
                userCounter += 1

        else:
            print("Noto'g'ri roll kiritildi!")

        chiqish = input("\nDasturdan chiqmoqchimisiz? (ha/yo'q): ").lower()
        if chiqish == "ha":
            print("Dastur tugadi")
            break
        