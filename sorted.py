def sort_dictionary(d):
    sorted_list = []

    for name, (phone_number, age) in sorted(d.items(), key=lambda x: x[1][1]):
        sorted_list.append((name, phone_number))

    return sorted_list

#print(sort_dictionary({'Tom': (5464512, 24), 'Sara': (5446987, 32), 'Mary': (1557896, 20)}))
