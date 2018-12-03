import Contents
import Person
import Reception

reception = Reception.Reception()
book1 = Contents.Book("B1", "Python", False)

reception.add_item(book1)
reception.library_contents()
# reception.remove_item("B1")
reception.update_item("B1", "Java")
reception.library_contents()

reception.register_person(Person.Person("P1", "Jenny", "Female", 24))
reception.customers()
reception.update_person("P1", "Kerry")
reception.customers()
reception.update_person("P1", "", 25)
reception.customers()
