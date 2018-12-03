class Reception(object):
    def __init__(self, loaned=[], people=[]):
        self._loaned = loaned
        self._people = people

    def check_out(self):
        pass

    def check_in(self):
        pass

    def add_item(self, item):
        self._loaned.append(item)

    def remove_item(self, id):
        for i in self._loaned:
            if i._id == id:
                self._loaned.remove(i)
                break

    def update_item(self, id, name):
        for i in self._loaned:
            if i._id == id:
                i._name = name
                break

    def register_person(self, person):
        self._people.append(person)

    def delete_person(self):
        for i in self._people:
            if i._id == id:
                self._people.remove(i)
                break

    def update_person(self, id, name="", age=0):
        print(len(name), age)
        for i in self._people:
            if i._id == id:
                if len(name) > 0:
                    i._name = name
                if age > 0:
                    i._age = age
                break

    def library_contents(self):
        if len(self._loaned) == 0:
            print("Empty: No items in library")
        else:
            for i in self._loaned:
                print(i.to_string())

    def customers(self):
        if len(self._people) == 0:
            print("Empty: No customers")
        else:
            for i in self._people:
                print(i.to_string())
