from datetime import datetime, timedelta

class Item:
    def __init__(self, item_id, title, author, category):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.category = category
        self.is_checked_out = False
        self.due_date = None

class Book(Item):
    def __init__(self, item_id, title, author, category, isbn):
        super().__init__(item_id, title, author, category)
        self.isbn = isbn

class Magazine(Item):
    def __init__(self, item_id, title, author, category, issue_number):
        super().__init__(item_id, title, author, category)
        self.issue_number = issue_number

class DVD(Item):
    def __init__(self, item_id, title, author, category, duration):
        super().__init__(item_id, title, author, category)
        self.duration = duration

class Library:
    def __init__(self):
        self.items = []
        self.checked_out_items = {}

    def add_item(self):
        item_type = input("Enter item type (book, magazine, dvd): ").strip().lower()
        item_id = int(input("Enter item ID: "))
        title = input("Enter title: ")
        author = input("Enter author: ")
        category = input("Enter category: ")

        if item_type == "book":
            isbn = input("Enter ISBN: ")
            item = Book(item_id, title, author, category, isbn)
        elif item_type == "magazine":
            issue_number = int(input("Enter issue number: "))
            item = Magazine(item_id, title, author, category, issue_number)
        elif item_type == "dvd":
            duration = int(input("Enter duration in minutes: "))
            item = DVD(item_id, title, author, category, duration)
        else:
            print("Invalid item type.")
            return

        self.items.append(item)
        print(f"Added {item_type}: {title}")

    def check_out_item(self):
        item_id = int(input("Enter item ID to check out: "))
        user_id = input("Enter user ID: ")
        for item in self.items:
            if item.item_id == item_id:
                if not item.is_checked_out:
                    item.is_checked_out = True
                    item.due_date = datetime.now() + timedelta(days=14)  # 2 weeks
                    self.checked_out_items[item_id] = user_id
                    print(f"Item {item_id} checked out by user {user_id}. Due date: {item.due_date}")
                else:
                    print(f"Item {item_id} is already checked out.")
                return
        print(f"Item {item_id} not found.")

    def return_item(self):
        item_id = int(input("Enter item ID to return: "))
        if item_id in self.checked_out_items:
            for item in self.items:
                if item.item_id == item_id:
                    item.is_checked_out = False
                    self.checked_out_items.pop(item_id)
                    print(f"Item {item_id} returned.")
                    return
        print(f"Item {item_id} not found or not checked out.")

    def manage_overdue_fines(self):
        now = datetime.now()
        for item in self.items:
            if item.is_checked_out and item.due_date < now:
                overdue_days = (now - item.due_date).days
                fine = overdue_days * 1  # $1 fine per day
                print(f"Item {item.item_id} is overdue by {overdue_days} days. Fine: ${fine}")

    def search_items(self):
        title = input("Enter title to search (or leave blank): ").strip().lower()
        author = input("Enter author to search (or leave blank): ").strip().lower()
        category = input("Enter category to search (or leave blank): ").strip().lower()

        results = []
        for item in self.items:
            if (title and title in item.title.lower()) or \
               (author and author in item.author.lower()) or \
               (category and category in item.category.lower()):
                results.append(item)

        if results:
            print("Search results:")
            for item in results:
                print(f"ID: {item.item_id}, Title: {item.title}, Author: {item.author}, Category: {item.category}, Checked out: {item.is_checked_out}")
        else:
            print("No items found.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add item")
        print("2. Check out item")
        print("3. Return item")
        print("4. Manage overdue fines")
        print("5. Search items")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.add_item()
        elif choice == "2":
            library.check_out_item()
        elif choice == "3":
            library.return_item()
        elif choice == "4":
            library.manage_overdue_fines()
        elif choice == "5":
            library.search_items()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
