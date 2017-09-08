from flask import session, request
from werkzeug.security import generate_password_hash
class User(object):
    """Create and store a user oblect"""
    user_id = 0
    users = {}
    def __init__(self, Username, Email, Password, Password2):
        """initialize the object User"""
        User.user_id += 1
        self.email = Email
        self.username = Username
        self.password = Password
        self.password2 = Password2
        

    def create_user(self):
        """Function to create and store a user in the dictionary Users"""
        self.users.update({
            self.user_id: {
                'username': self.username,
                'email': self.email,
                'password': self.password,
                'password2': self.password2
            }
        })

        return self.users
            
        


class shoppinglists(object):
    """Create a class shoppinglist which is used to create, update and delete
     a shoppinglist"""
    list_id = 0
    shoppinglists = {}
    def __init__(self, listName, description):
        """Function to initialise the class"""
        shoppinglists.list_id += 1
        self.listname = listName
        self.description = description
    
    def create_shoppinglist(self):
        """Function to allow creating a shopping list"""
        self.shoppinglists.update({
            self.list_id: {
                'listname': self.listname,
                'description': self.description,
            }
        })
        return self.shoppinglists
    def edit_shoppinglist(self):
        """A function that will allow for editing of the shopping list"""
        shoppinglist_dict = shoppinglists.shoppinglists
        for item in shoppinglist_dict.values():
            if session['user_id'] == item['user_id']:
                for key, val in shoppinglist_dict.items():
                    if key == int(request.form['key']):
                        print('To be edited =', shoppinglist_dict[key])
                        existing_owner = val['user_id']
                        shoppinglist_dict[key] = {'user_id': existing_owner, 'listname': self.listname, 'description': self.description}

                        return shoppinglist_dict

    def delete_shoppinglist(self):
        """
        Deletes a single shoppinglist created by a logged in user
        """
        # Retrieve a user's shopping list using it's ID
        shoppinglist_dict = shoppinglists.shoppinglists
        for item in shoppinglist_dict.values():
            if session['user_id'] == item['user_id']:
                for key in shoppinglist_dict:
                    if key == int(request.form['key']):
                        print('List to be deleted =', shoppinglist_dict[key])
                        del shoppinglist_dict[key]

                        print('Should have been deleted =', shoppinglist_dict)

                        return shoppinglist_dict
class items(object):
    """Create a class that will allow for items to be added, updated and deleted
     to the shoppinh List"""
    item_id = 0
    items = {}
    def __init__(self, itemname, Price, Quantity):
        items.item_id+=1
        self.itemname = itemname
        self.price = Price
        self.quantity = Quantity
    
    def add_item(self, shoppinglist_id):
        """function to add items to the list"""
        self.items.update({self.item_id:{'shoppinglist_id': shoppinglist_id, 'item name':self.itemname, 'price': self.price, 'quantity': self.quantity}})
        return self.items

    def delete_item(self, shoppinglist_id, key):
        """Function to delete an item in the shopping list"""
        items_dict = items.items
        for item in items_dict:
            if shoppinglist_id== item[shoppinglist_id]:
                if key == int(request.form['key']):
                    for k in items_dict:
                        if k == key:
                            print ('item to be deleted is ', items_dict[key])
                            del items_dict[key]
                    print ('item to be deleted is ', items_dict[key])
                    del items_dict[key]
                    return items_dict

    def edit_item(self, shoppinglist_id, key):
        """Function to edit an item in the shopping list"""
        items_dict = items.items
        for k, val in items_dict.items():
            if k == key and val['shoppinglist_id']== shoppinglist_id:
                print ('item to be edited is ', items_dict[key])
                existing_list_id = val[shoppinglist_id]
                items_dict[k] = {'shoppinglist_id':existing_list_id, 'item name':self.itemname, 'price': self.price, 'quantity': self.quantity}
                return items_dict
            
    
