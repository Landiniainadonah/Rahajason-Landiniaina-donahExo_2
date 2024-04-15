from itertools import product

def karnaugh_minimization(boolean_function):
    variables = sorted(list(set(boolean_function.replace('+', '').replace('.', ''))))
    minterms = [term.replace(' ', '') for term in boolean_function.split('+')]
    truth_table = {}
    for term in minterms:
        binary = ''.join(['1' if var in term else '0' for var in variables])
        truth_table[binary] = 1
    
    for term in boolean_function.split('+'):
        binary = ''.join(['0' if var[0] == '~' else '1' for var in term.split()])
        truth_table[binary] = 0
    
    minterms_dict = {term: 1 for term in minterms}
    for key, value in truth_table.items():
        if value == 1:
            for minterm in minterms:
                if all([minterm[i] == '-' or minterm[i] == key[i] for i in range(len(key))]):
                    minterms_dict[minterm] = 0
    
    simplified_terms = []
    for term, value in minterms_dict.items():
        if value == 1:
            simplified_terms.append(term)
    
    simplified_function = '+'.join(simplified_terms)
    return simplified_function

boolean_function = input("Entrez la fonction logique à minimiser : ")
simplified_function = karnaugh_minimization(boolean_function)
print("La fonction logique minimisée est : ", simplified_function)