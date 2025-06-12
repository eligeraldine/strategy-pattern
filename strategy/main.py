from context import CounselorFilter
from strategy import (FilterByRating, FilterByPrice, FilterBySpecialization, FilterByName)
from data import Counselor_list

def print_results(title, results, value=None):
    if value is not None:
        print(f"\n{title} = {value}")
    else:
        print("\n" + title)
    for k in results:
        print(k)

filter = CounselorFilter()

# Filter by different criteria and print results
filter.set_strategy(FilterByName("Al"))
print_results("Filtered by Name", filter.filter(Counselor_list), "Al")

filter.set_strategy(FilterBySpecialization("anxi"))
print_results("Filtered by Specialization", filter.filter(Counselor_list), "anxi")

filter.set_strategy(FilterByRating(4.5))
print_results("Filtered by Exact Rating", filter.filter(Counselor_list), 4.5)

filter.set_strategy(FilterByPrice(100000))
print_results("Filtered by Exact Price", filter.filter(Counselor_list), 100000)
