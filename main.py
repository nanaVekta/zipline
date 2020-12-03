products = []


def init_catalog(product_info):
    # iterate through product_info and add quantity
    for product in product_info:
        product.update({"quantity": 0})

    # set products as a global variable and equate to product_info
    global products
    products = product_info

    return products


product_info = [{"mass_g": 700, "product_name": "RBC A+ Adult", "product_id": 0},
                {"mass_g": 700, "product_name": "RBC B+ Adult", "product_id": 1},
                {"mass_g": 750, "product_name": "RBC AB+ Adult", "product_id": 2},
                {"mass_g": 680, "product_name": "RBC O- Adult", "product_id": 3},
                {"mass_g": 350, "product_name": "RBC A+  Child", "product_id": 4},
                {"mass_g": 200, "product_name": "RBC AB+ Child", "product_id": 5},
                {"mass_g": 120, "product_name": "PLT AB+", "product_id": 6},
                {"mass_g": 80, "product_name": "PLT O+", "product_id": 7},
                {"mass_g": 40, "product_name": "CRYO A+", "product_id": 8},
                {"mass_g": 80, "product_name": "CRYO AB+", "product_id": 9},
                {"mass_g": 300, "product_name": "FFP A+", "product_id": 10},
                {"mass_g": 300, "product_name": "FFP B+", "product_id": 11},
                {"mass_g": 300, "product_name": "FFP AB+", "product_id": 12}]


def process_order(order):
    requested = order["requested"]
    order_id = str(order['order_id'])
    # iterate through request
    for request in requested:
        r_quantity = request['quantity']
        r_product_id = request['product_id']
        for product in products:
            product_id = product['product_id']
            quantity = product['quantity']
            if (r_product_id == product_id):
                # calculate total mass of item
                mass = product['mass_g']
                total_mass = mass * r_quantity

                # if mass if greater that 1.8kg
                # check quantity that can be transported
                # that does not exceed the mass limit
                if (total_mass > 1800):
                    while (r_quantity > 0):
                        r_quantity -= 1
                        new_mass = r_quantity * mass
                        if (new_mass < 1800):
                            return "Mass limit exceeded. Only " + r_quantity + " processed"
                            break
                        else:
                            return "Mass of item exceeds 1.8kg"

                else:
                    # if quantity left is less that requested
                    # quantity check reminder left to send
                    if (r_quantity > quantity):
                        reminder = r_quantity - quantity
                        return "order processed successfully but " + reminder + " items are remaining"
                    else:
                        # if all parameters are met process order
                        return "Order " + order_id + " processed successfully"

            return "Items not found in catalog"


order = {"order_id": 123, "requested": [{"product_id": 0, "quantity": 2}, {"product_id": 10, "quantity": 4}]}


def process_restock(restock):
    # iterate through stock and product
    # and increase quantity
    for stock in restock:
        for product in products:
            if (stock['product_id'] == product['product_id']):
                product['quantity'] = product['quantity'] + stock['quantity'];
    return products


restock = [{"product_id": 0, "quantity": 30}, {"product_id": 1, "quantity": 25}, {"product_id": 2, "quantity": 25},
           {"product_id": 3, "quantity": 12}, {"product_id": 4, "quantity": 15}, {"product_id": 5, "quantity": 10},
           {"product_id": 6, "quantity": 8}, {"product_id": 7, "quantity": 8}, {"product_id": 8, "quantity": 20},
           {"product_id": 9, "quantity": 10}, {"product_id": 10, "quantity": 5}, {"product_id": 11, "quantity": 5},
           {"product_id": 12, "quantity": 5}]


def ship_package(shipment):
    shipped = shipment['shipped']
    order_id = str(shipment['order_id'])

    # iterate through shipment and check if
    # product exits
    for ship in shipped:
        for product in products:
            if (ship['product_id'] == product["product_id"]):
                # reduce the number of quantity if shipment is fulfilled
                product['quantity'] = product['quantity'] - ship['quantity']
                return "Order " + order_id + " shipped successfully"

    return "Product not available in catalog"

    shipment = {"order_id": 123, "shipped": [{"product_id": 0, "quantity": 1}, {"product_id": 10, "quantity": 2}]}