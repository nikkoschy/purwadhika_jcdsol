# Simple Warehouse / Stock Keeping Python Program 

# 0.1 Importing modules
from textwrap import dedent

# 0.2 Initial list
list_stock = [
    {'name': 'TV - Samsung - 1045',
     'stock': 5,
     'value_usd': 500}
    ,{'name':'Speaker - Vivan - 2037', 
      'stock':12,
      'value_usd': 50}
    ,{'name':'Vacuum - Philips - 3048', 
      'stock':7,
      'value_usd': 225}
    ,{'name':'Rice Cooker - Cosmos - 4556', 
      'stock':21,
      'value_usd': 45}
    ,{'name':'Air Fryer - Mito - 4571', 
      'stock':24,
      'value_usd': 38}
]

# 1. Functions

#Read Function
#Called in menu 1
#View data consisting of 5 columns : index/number, SKU name, SKU stock, SKU price(each), and total price (stock x price)
def view_balance(list_stock_mod):
    list_stock_mod = add_total_value_column(list_stock_mod)
    print('CURRENTLY AVAILABLE STOCK')
    print('-' * 68) 
    print(f'| {'No':<3} | {'SKU':<35} | {'Stock':<5} | {'Price':<5} | {'Total':<5} |') 
    print('-' * 68) 

    for i in range(len(list_stock_mod)) :
        print(f'| {i+1:<3} | {list_stock_mod[i]['name']:<35} | {list_stock_mod[i]['stock']:<5} | {list_stock_mod[i]['value_usd']:<5} | {list_stock_mod[i]['total_value_usd']:<5} |')
    print('-' * 68) 
    
#Inserting/updating list:in_total into list:list_stock_mod
def updt_list_stock(inout, list_stock_mod, list_inout):
    if list_inout[0] == 'e':
        for j in range (len(list_stock_mod)):
            if list_stock_mod[j]['name'] == list_inout[1]:
                list_stock_mod[j]['stock'] += list_inout[2]
    elif list_inout[0] == 'n':
        list_stock_mod.append({'name': list_inout[1], 'stock': list_inout[2], 'value_usd':list_inout[3]})

    return list_stock_mod

#Create Function
#Called in menu 2 and 3
#Create data in three ways :
#1. Add into stock for existing item
#2. Add into the data: SKU name, stock amount, harga in USD
#3. Substract from the data: As an outgoing stock (could be due to being sold/moved from warehouse)
def input_inout_stock(inout, list_stock_mod):
    view_balance(list_stock_mod)
    
    if inout > 0:
        iis_checker = True
        while iis_checker == True:
            new_name = str(input('Existing / New SKU (E/N) : ')).lower()
            if (new_name=='e'):
                sku_id      = int(input('Insert SKU number : '))
                if sku_id <= len(list_stock_mod):
                    sku_in_qty  = int(input('Insert quantity of incoming stock : '))
                    list_inout = [new_name, list_stock_mod[sku_id-1]['name'], sku_in_qty, None]
                    iis_checker = False
                else:
                    print('Index out of bounds')
            elif (new_name=='n'):
                sku_name    = str(input('Insert SKU name : '))
                sku_in_qty  = int(input('Insert quantity of incoming stock : '))
                price_each = int(input('Insert price in USD : '))
                list_inout = [new_name, sku_name, sku_in_qty, price_each]
                iis_checker = False
            else:
                print('\nInvalid input\n')
                
    elif inout < 0:
        iis_checker = True
        
        while iis_checker == True:
            sku_id      = int(input('Insert SKU ID : '))
            if sku_id <= len(list_stock_mod):
                sku_out_qty  = int(input('Insert quantity of outgoing stock : '))
                if list_stock_mod[sku_id-1]['stock'] >= sku_out_qty:
                    list_inout = [ 'e', list_stock_mod[sku_id-1]['name'], sku_out_qty*(-1)]
                    print()
                    iis_checker = False   
                else:
                    print('Check quantity')           
            elif sku_id > len(list_stock_mod):
                print('Index out of bounds')
                print()
            else:
                print('Invalid input')
                print()
    return list_inout

#Update Function
#Called in menu 4
#To change stock of an SKU based on user's choice of item    
def chge_list_stock(list_stock_mod):
    view_balance(list_stock_mod)
    cls_check = True
    while cls_check == True:
        change_index = int(input('Insert index to change : '))
        
        if change_index <= len(list_stock_mod):
            change_stock = int(input('Insert new stock : '))
            list_stock_mod[change_index-1]['stock'] = change_stock
            cls_check = False
            
        else:
            print('Index out of bounds')
            print()
    
    return list_stock_mod

#Delete Function
#Called in menu 5
#To delete a whole row of data
def del_inout_stock(list_stock_mod):
    dis_check = True
    while dis_check == True:
        del_index = int(input('Insert index of stock to delete : '))
        if del_index <= len(list_stock_mod):
            del list_stock_mod[del_index-1]
            dis_check = False
        else:
            print('Index out of bounds')
            print()
    return list_stock_mod

#Function to calculate total value per SKU (stock x price each)    
def add_total_value_column(var):
    for i in range(len(var)):
        var[i]['total_value_usd'] = var[i]['stock'] * var[i]['value_usd']
    return var
    
# Main program function
def main():
    is_running = True
    list_inout =[]
    list_out = []
    menu_pick = 0
    list_stock_mod = add_total_value_column(list_stock)

    while is_running == True:
        print(dedent('''
            MAIN MENU
            
            Options :
            1. Read
            2. Incoming Stock
            3. Outgoing Stock
            4. Update/Change Stock
            5. Delete Stock
            0. Exit Program

            Insert input : '''))
        
        menu_list = int(input(''))
        print()
        
        if menu_list == 1:
            view_balance(list_stock_mod)
            
        elif menu_list == 2:
            list_inout = input_inout_stock(1, list_stock_mod)
            list_stock_mod = updt_list_stock(1, list_stock_mod, list_inout)
        
        elif menu_list == 3:
            list_inout = input_inout_stock(-1, list_stock_mod)
            list_stock_mod = updt_list_stock(-1, list_stock_mod, list_inout)
        
        elif menu_list == 4:
            list_stock_mod = chge_list_stock(list_stock_mod)
            
        elif menu_list == 5:
            list_stock_mod = del_inout_stock(list_stock_mod)
            
        elif menu_list == 0:
            print('Program end')
            is_running=False
        
        else:
            print('Input invalid')

main()