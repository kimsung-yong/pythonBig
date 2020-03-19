class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print("이름 :", self.name)
        print("전화번호 :", self.phone)
        print("이메일 :", self.email)


def set_contact():
    name = input("이름 :")
    phone = input("전화번호 :")
    email = input("이메일 :")
    contact = Contact(name, phone, email)
    return contact


def display_contact(Contact_list):
    for contact in Contact_list:
        contact.display()


def delete_contact(Contact_list, name):
    for contact in Contact_list:
        for i in range(0, len(Contact_list)):
            if contact.name == name:
                del Contact_list[i]


def menu():
    print("1. 연락처 입력 2. 연락처 출력 3. 연락쳐 삭제 4. 종료")
    num = input("메뉴 선택 :")
    return int(num)


def start():
    contact_list = []
    while True:
        sel = menu()
        if sel == 1:
            print("연락처 입력:")
            c_list = set_contact()
            contact_list.append(c_list)
        elif sel == 2:
            display_contact(contact_list)
        elif sel == 3:
            name = input("이름 :")
            delete_contact(contact_list, name)
        elif sel == 4:
            break
        else:
            print("잘못된 입력입니다.")


if __name__ == "__main__":
    start()


