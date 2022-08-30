from page_1 import side_menu
from page_2 import pub_pincodes
from page_3 import main
from streamlit_option_menu import option_menu

def horizontal_menu():
 selected = option_menu("Main Menu",
                        options=["Home Page", "Nearby Pubs", "Find a Pub"],
                        icons=[" ", " ", " "],
                        default_index=0,
                        orientation="horizontal")
 pages(selected)

def pages(selected):
    
    if selected == "Home Page":
        side_menu()
        
    elif selected == "Nearby Pubs":
        pub_pincodes() 
        
    elif selected == "Find a Pub":
        main()
      
if __name__ == '__main__':
    horizontal_menu()