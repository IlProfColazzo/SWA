def addProduct(mysql,productName,supplierID,price):
        cursor = mysql.connection.cursor()
        query = '''SELECT * FROM suppliers WHERE supplierID=%s'''
        cursor.execute(query,(supplierID,))
        dati = cursor.fetchall() #torna il risultato della query
        if len(dati)==0:
            return False
        query = '''INSERT INTO products(ProductName, SupplierID, Price) value(%s,%s,%s)'''
        cursor.execute(query,(productName,supplierID,price))
        mysql.connection.commit()
        cursor.close()
        return True

def allOrders(mysql):
    cursor = mysql.connection.cursor()
    query = '''SELECT * FROM orders'''
    cursor.execute(query)
    dati = cursor.fetchall()
    cursor.close()
    return dati

def details(mysql, id):
    cursor = mysql.connection.cursor()
    query = '''SELECT * FROM orders WHERE customerID = %s'''
    cursor.execute(query,(id,))
    dati = cursor.fetchall()
    cursor.close()
    return dati
     
        