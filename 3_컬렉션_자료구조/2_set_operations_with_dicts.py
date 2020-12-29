def set_operations_with_dict():
    pairs = [("a", 1), ("b", 2), ("c", 3)]
    d1 = dict(pairs)
    print("딕셔너리1\t: {0}".format(d1))
    
    d2 = {"a": 1, "c": 2, "d": 3, "e": 4}
    print("딕셔너리2\t: {0}".format(d2))
    
    intersection = d1.keys() & d2.keys()
    print("d1 n d2 (키)\t: {0}".format(intersection))

    intersection_items = d1.items() & d2.items()
    print("d1 n d2 (키,값)\t: {0}".format(intersection_items))

    subtraction1 = d1.keys() - d2.keys()
    print("d1 - d2 (키)\t: {0}".format(subtraction1))

    subtraction2 = d2.keys() - d1.keys()
    print("d2 - d1 (키)\t: {0}".format(subtraction2))

    subtraction_itmes = d1.items() - d2.items()
    print("d1 - d2 (키)\t: {0}".format(subtraction_itmes))

    d3 = {key: d2[key] for key in d2.keys() - {"c", "d"}}
    print("d2 - {{c, d}}\t: {0}".format(d3))

if __name__ == "__main__":
    set_operations_with_dict()