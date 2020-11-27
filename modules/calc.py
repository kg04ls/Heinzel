import sympy

def get_initial_list():
    return []

def handle_entry(value):
    try:
        answer = sympy.sympify(value)
        if str(answer) == value:
            return[]  
        else:  
            return [answer]
    except:
        return[]  

def handle_click(selected):
    return False 