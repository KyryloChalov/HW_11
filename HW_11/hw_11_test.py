from classes import Record, AddressBook, Phone, Name
    # =========================================
    #               test for HW 11
    # =========================================
def print_address_book():
    # Виведення всіх записів у книзі
    print(f"  ==== Address book ====")
    for name, record in book.data.items():
            print(record)  


if __name__ == '__main__':
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone(Phone("(123)456-78-90"))
    john_record.add_phone(Phone("(555)555.55.55"))
    
    # Додавання запису John до адресної книги
    book.add_record(john_record)
    print(">>> book.add_record(john_record) - OK")

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone(Phone("+380987654321"))
    jane_record.add_phone(Phone("+38(066)765 43 21"))
    jane_record.birthday = ("20-10-1999")
    book.add_record(jane_record)
    print(">>> book.add_record(jane_record) - OK")
    
    # Створення запису для Fil - одним рядком телефон та день народження
    fil_record = Record("Fil", Phone("(054) 644-45-54"), "15-10-2001")
    
    # Додавання запису Fil до адресної книги
    book.add_record(fil_record)
    print(">>> book.add_record(fil_record) одним рядком телефон та день народження - OK")
        
    print_address_book()

    print("\n>>> john.edit_phone:")
    # Знаходження та редагування телефону для John
    john = book.find("John")
    print(john)
    john.edit_phone(Phone("1234567890"), Phone("+380933903357"))
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    print('\n>>> john.find_phone("5555555555"): ')
    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone(Phone("5555555555"))
    print("{:<10} : {}".format(john.name, found_phone))  # Виведення: 5555555555
    print('>>> john.find_phone("5554445555"): ') 
    found_phone = john.find_phone("5554445555")
    print("{:<10} : {}".format(john.name, found_phone))  # Виведення: Number 5554445555 not found
    
    # Видалення запису Jane
    book.delete("Jane")  
    print('\n>>> book.delete("Jane") - OK')
    
    print_address_book()

         
    print("\n>>> add many records: ")
    record_01 = Record("Person 1", Phone("(067)797-71-66"), "28-03-1968")
    record_01.add_phone(Phone("0935394457"))
    record_02 = Record("Person 2", Phone("0677973166"))
    record_02.add_phone(Phone("0937737357"))
    record_02.add_phone(Phone("0997666845"))
    record_03 = Record("Person 3", Phone("0677977166"), "25-10-2011")
    record_03.add_phone(Phone("0933966357"))
    record_04 = Record("Person 4", Phone("0677977166"))
    record_04.add_phone(Phone("0933978857"))
    record_05 = Record("Person 5", Phone("0677457166"), "04-09-1988")
    record_05.add_phone(Phone("0934503357"))
    record_05.add_phone(Phone("0997044565"))
    record_06 = Record("Person 6", Phone("0677974566"))
    record_06.add_phone(Phone("0933876557"))
    record_07 = Record("Person 7", Phone("0677767166"))
    record_07.add_phone(Phone("0976673357"))
    record_08 = Record("Person 8", Phone("0677976666"), "15-12-2016")
    record_08.add_phone(Phone("0937876557"))
    record_08.add_phone(Phone("0998858845"))
    record_08.add_phone(Phone("0997077845"))
    record_09 = Record("Person 9", Phone("0677933366"), "21-03-1965")
    record_09.add_phone(Phone("0993378845"))
    
    book.add_record(record_01)
    book.add_record(record_02)
    book.add_record(record_03)
    book.add_record(record_04)
    book.add_record(record_05)
    book.add_record(record_06)
    book.add_record(record_07)
    book.add_record(record_08)
    book.add_record(record_09)


    # Виведення всіх записів у книзі з використанням iterator'
    print(f"  ==== Address book with iterator ====")
    count = 0
    for _ in book.iterator(4):
        for item in _:
            print(item)
            count += 1
        if count < len(book):
            input(" >>> Press Enter for next records: ")
    print(" >>> End of List ")
