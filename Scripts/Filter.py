from QueryBuilder import QueryBuilder
builder = QueryBuilder()

def add_sort_menu_1(): return builder.add_condition("menu = 1")

# Do the same for the other add_sort_* and remove_sort_* functions
def add_sort_menu_2(): return builder.add_condition("menu = 2")
def add_sort_menu_3(): return builder.add_condition("menu = 3")
def add_sort_menu_4(): return builder.add_condition("menu = 4")
def add_sort_menu_5(): return builder.add_condition("menu = 5")
def add_sort_menu_6(): return builder.add_condition("menu = 6")

def remove_sort_menu_1(): return builder.remove_condition("menu = 1")
def remove_sort_menu_2(): return builder.remove_condition("menu = 2")
def remove_sort_menu_3(): return builder.remove_condition("menu = 3")
def remove_sort_menu_4(): return builder.remove_condition("menu = 4")
def remove_sort_menu_5(): return builder.remove_condition("menu = 5")
def remove_sort_menu_6(): return builder.remove_condition("menu = 6")

def add_sort_KVV_TRUE(): return builder.add_condition("kvv = 1")
def add_sort_KVV_FALSE(): return builder.add_condition("kvv = 0")

def remove_sort_KVV_TRUE(): return builder.remove_condition("kvv = 1")
def remove_sort_KVV_FALSE(): return builder.remove_condition("kvv = 0")

def sort_by_date(): return builder.add_order_by("Date")