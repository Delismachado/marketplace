from marketplace import Marketplace
from categories import Category

marketplaces = ["mark1", "mark2", "mark3", "mark4", "mark5", "mark6"]
categories = ["cat1", "cat2", "cat3", "cat4", "cat5", "cat6"]
subCategories = ["subCat1", "subCat2", "subCat3", "subCat4"]

def list_marketplaces():
    print('\nMarketplaces: ')    
    for m in marketplaces:
        print(m)
list_marketplaces()

def list_categories():
    print('\nCategories: ')    
    for c in categories:
        print(c)
list_categories()