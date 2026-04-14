# Object-oriented Address Book with threading for long-running operations

import threading
import time


class Email:
    def __init__(self, email):
        self.email = email

    def __str__(self):
        return self.email


class Address:
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return self.address


class Person:
    def __init__(self, name):
        self.name = name
        self.emails = []
        self.addresses = []

    def add_email(self, email):
        self.emails.append(Email(email))

    def add_address(self, address):
        self.addresses.append(Address(address))

    def __str__(self):
        return f"Name: {self.name}, Emails: {[str(e) for e in self.emails]}, Addresses: {[str(a) for a in self.addresses]}"


class AddressBook:
    def __init__(self):
        self.persons = []
        self.lock = threading.Lock()

    def add_person(self, person):
        def _add():
            time.sleep(0.1)  # Simulate long-running operation
            with self.lock:
                self.persons.append(person)
            print(f"Added person: {person.name}")

        t = threading.Thread(target=_add)
        t.start()
        t.join()

    def remove_person(self, name):
        def _remove():
            time.sleep(0.1)  # Simulate long-running operation
            with self.lock:
                self.persons = [p for p in self.persons if p.name != name]
            print(f"Removed person: {name}")

        t = threading.Thread(target=_remove)
        t.start()
        t.join()

    def sort_persons(self):
        def _sort():
            time.sleep(0.1)  # Simulate long-running operation
            with self.lock:
                self.persons.sort(key=lambda p: p.name)
            print("Sorted persons by name")

        t = threading.Thread(target=_sort)
        t.start()
        t.join()

    def search_person(self, criteria):
        # Search by name, email, or address
        with self.lock:
            results = []
            seen = set()
            for p in self.persons:
                if p not in seen:
                    if p.name.lower() == criteria.lower():
                        results.append(p)
                        seen.add(p)
                        continue
                    for e in p.emails:
                        if criteria.lower() in e.email.lower():
                            results.append(p)
                            seen.add(p)
                            break
                    for a in p.addresses:
                        if criteria.lower() in a.address.lower():
                            results.append(p)
                            seen.add(p)
                            break
            return results


# Example usage
if __name__ == "__main__":
    address_book = AddressBook()

    # Create persons
    jovi = Person("Jovi")
    jovi.add_email("jovi@example.com")
    jovi.add_address("123 Main St")

    lima = Person("Lima")
    lima.add_email("lima@example.com")
    lima.add_address("456 Oak Ave")

    # Add persons (threaded)
    address_book.add_person(jovi)
    address_book.add_person(lima)

    # Sort (threaded)
    address_book.sort_persons()

    # Search (not threaded for simplicity)
    results = address_book.search_person("Jovi")
    for p in results:
        print(p)

    # Remove (threaded)
    address_book.remove_person("Lima")
