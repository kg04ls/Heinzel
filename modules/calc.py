import sympy

def get_initial_list():
    return []

def handle_entry(value):
    try:
        value = value + "+0.0"
        answer = sympy.sympify(value)
        if str(answer) == value:
            return[]  
        elif answer%1 == 0:  
            return[int(answer)]
        elif str(answer) == 'zoo':
            return[]
        else:
            answer = round(answer,4)
            return[answer]
    except:
        return[]  

def handle_click(selected):
    return False 