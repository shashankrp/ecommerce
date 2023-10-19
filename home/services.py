# temp variables which should be removed in the future

productinfo = {"1":"Electronics","2":"Cloths","3":"Kitchen", "4":"Books"}
ProductsList = {"Electronics": ["Mobiles", "Smart TV's", "Android TV's", "Laptops", "Tablets","Earbuds"],
                "Cloths":["T-Shirts", "Shirts", "Jeans", "Formal Pants", "Casual wares"],
                "Kitchen":["Spoon", "Non-stick Pans", "Pans", "Stoves", "Utincils"],
                "Books": ["Adventure", "DSA", "Computer", "Management", "Business Logic", "Suspence"]
                }
subProducts = {"Mobiles": ["IPhone", "OnePlus", "Samsung", "Oppo", "Vivo", "Realme", "Micromax"]}
subsubProducts = {"IPhone": [{"id":"101","discount":79900,"price":61999,"name":"Apple iPhone 13(128GB) - Blue"},{"id":"102","discount":89900,"price":70999,"name":"Apple iPhone 13(128GB) - Midnight"},{"id":"103","discount":69900,"price":51499,"name":"Apple iPhone 13(128GB) - Starlight"}]}
cart = []
total = 0


def cartLen():
    return len(cart)

def cartInformation():
    return ProductsList

def loginValidation(user, password):
    if user == "admin" and password == "":
        print("Login Successful")
        return True
    else:
        return False

def productSelected(id):
    return productinfo[id]

def ProductDetails(id):
    ProductsList[productSelected(id)]
    return ProductsList[productinfo[id]]

def subPud(id):
    return subProducts[id]

def subsubProd(id):
    return subsubProducts[id]

def check(name, id):
    test = subsubProducts[name]
    for item in test:
        if item['id'] == id:
            cart.append({'name':item['name'], "price": item['price']})
            return True
        else:
            return False

def cartInfo():
    return cart

def cartcalculate(cartData):
    total = sum([item['price'] for item in cartData])
    return total