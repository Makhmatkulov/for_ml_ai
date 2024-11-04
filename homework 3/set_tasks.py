# set_tasks.py

import random

def union_of_sets(set1, set2):
    return set1 | set2

def intersection_of_sets(set1, set2):
    return set1 & set2

def difference_of_sets(set1, set2):
    return set1 - set2

def check_subset(set1, set2):
    return set1 <= set2 or set2 <= set1

def check_element(s, element):
    return element in s

def set_length(s):
    return len(s)

def convert_list_to_set(lst):
    return set(lst)

def remove_element(s, element):
    s.discard(element)
    return s

def clear_set(s):
    return set()

def is_set_empty(s):
    return len(s) == 0

def symmetric_difference(set1, set2):
    return set1 ^ set2

def add_element(s, element):
    s.add(element)
    return s

def pop_element(s):
    return s.pop() if s else None

def find_maximum(s):
    return max(s) if s else None

def find_minimum(s):
    return min(s) if s else None

def filter_even_numbers(s):
    return {x for x in s if x % 2 == 0}

def filter_odd_numbers(s):
    return {x for x in s if x % 2 != 0}

def create_set_of_range(start, end):
    return set(range(start, end + 1))

def merge_and_deduplicate(lst1, lst2):
    return set(lst1 + lst2)

def check_disjoint_sets(set1, set2):
    return set1.isdisjoint(set2)

def remove_duplicates_from_list(lst):
    return list(set(lst))

def get_unique_elements_in_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def create_nested_sets(*args):
    return {frozenset(arg) for arg in args}

def count_unique_elements(lst):
    return len(set(lst))

def generate_random_set(size, start, end):
    return {random.randint(start, end) for _ in range(size)}


sample_set1 = {1, 2, 3, 4, 5}
sample_set2 = {4, 5, 6, 7, 8}
sample_list = [1, 2, 2, 3, 4, 4, 5]

print(union_of_sets(sample_set1, sample_set2))
# print(intersection_of_sets(sample_set1, sample_set2))
# print(difference_of_sets(sample_set1, sample_set2))
# print(check_subset(sample_set1, sample_set2))
# print(check_element(sample_set1, 3))
# print(set_length(sample_set1))
# print(convert_list_to_set(sample_list))
# print(remove_element(sample_set1.copy(), 2))
# print(clear_set(sample_set1))
# print(is_set_empty(sample_set1))
# print(symmetric_difference(sample_set1, sample_set2))
# print(add_element(sample_set1.copy(), 9))
# print(pop_element(sample_set1.copy()))
# print(find_maximum(sample_set1))
# print(find_minimum(sample_set1))
# print(filter_even_numbers(sample_set1))
# print(filter_odd_numbers(sample_set1))
# print(create_set_of_range(1, 10))
# print(merge_and_deduplicate(sample_list, [4, 5, 6, 7]))
# print(check_disjoint_sets(sample_set1, sample_set2))
# print(remove_duplicates_from_list(sample_list))
# print(get_unique_elements_in_order(sample_list))
# print(create_nested_sets({1, 2}, {3, 4}, {5}))
# print(count_unique_elements(sample_list))
# print(generate_random_set(5, 1, 10))
