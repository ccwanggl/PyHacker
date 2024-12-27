from typing import List
from typing import Set, Tuple
from typing import Dict

def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_full_name2(first_name:str, last_name:str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def process_items(items:List[str]):
    for item in items:
        print(item)

def process_items2(items_t:Tuple[int, int, str], item_s: Set[bytes]):
    return items_t, item_s

def process_items3(prices:Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


print(get_full_name("John", "Smith"))
print(get_full_name2("John", "Smith"))
