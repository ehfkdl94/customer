from package import CRUD_data as CRUD
from package import search as s
custlist=[]
page=-1

while True:
    choice = s.menu_select()

    if choice=="I":
        custlist, page = CRUD.input_data(custlist, page)
    elif choice=="C":
        custlist, page = s.search_now(custlist, page)
    elif choice == 'P':
        custlist, page = s.search_p(custlist, page)  
    elif choice == 'N':
        custlist, page = s.search_n(custlist, page)
    elif choice=='D':
        custlist, page = CRUD.delete_data(custlist, page)
    elif choice=="U": 
        custlist, page = CRUD.update_data(custlist, page)    
    elif choice=="Q":
        break
