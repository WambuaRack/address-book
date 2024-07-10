from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        return self.contacts

address_book = AddressBook()

# Route to display all contacts
@app.route('/')
def display_address_book():
    contacts = address_book.display_contacts()
    return render_template('index.html', contacts=contacts)

# Route to add a new contact
@app.route('/add_contact', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone_number = request.form['phone_number']
    email = request.form['email']
    new_contact = Contact(name, phone_number, email)
    address_book.add_contact(new_contact)
    return redirect(url_for('display_address_book'))

if __name__ == '__main__':
    app.run(debug=True)
