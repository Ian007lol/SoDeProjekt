# Filter.py
from QueryBuilder import QueryBuilder
builder = QueryBuilder()

def add_sort_menu_1(): builder.add_condition("menu = 1")
def add_sort_menu_2(): builder.add_condition("menu = 2")
def add_sort_menu_3(): builder.add_condition("menu = 3")
def add_sort_menu_4(): builder.add_condition("menu = 4")
def add_sort_menu_5(): builder.add_condition("menu = 5")
def add_sort_menu_6(): builder.add_condition("menu = 6")

def remove_sort_menu_1(): builder.remove_condition("menu = 1")
def remove_sort_menu_2(): builder.remove_condition("menu = 2")
def remove_sort_menu_3(): builder.remove_condition("menu = 3")
def remove_sort_menu_4(): builder.remove_condition("menu = 4")
def remove_sort_menu_5(): builder.remove_condition("menu = 5")
def remove_sort_menu_6(): builder.remove_condition("menu = 6")

def add_sort_KVV_TRUE(): builder.add_condition("kvv = 1")
def add_sort_KVV_FALSE(): builder.add_condition("kvv = 0")

def remove_sort_KVV_TRUE(): builder.remove_condition("kvv = 1")
def remove_sort_KVV_FALSE(): builder.remove_condition("kvv = 0")

def sort_by_date(): builder.add_order_by("Date")
