import random

def initial():
    #list to store elements A through I
    components = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    system_state = {component: random.choice(['safe', 'vulnerable']) for component in components}
    return system_state


def system_scan(system_state):
    fixing_list = []
    logs = []
    
    for component, status in system_state.items():
        if status == 'vulnerable':
            logs.append(f"Component {component} is vulnerable so it is being fixed")
            fixing_list.append(component)
        else:
            logs.append(f"Component {component} is safe")
    
    return fixing_list, logs

def fix(system_state, fixing_list):
    for component in fixing_list:
        system_state[component] = 'safe'
        print(f"Component {component} has been fixed and is now safe.")
    
def final_check(system_state):
    print("\nFinal state:")
    for component, status in system_state.items():
        print(f"Component {component}: {status}")

def run_code():
    #system check at the beginning of the program
    print("Initiale state of components assigned randomly\n")
    system_state = initial()
    
    print("Initial state of componenets is:")
    for component, status in system_state.items():
        print(f"Component {component}: {status}")
    
    #scanning to check which componenets are vulnerable
    print("\nSystem is being scanned and results are:")
    fixing_list, logs = system_scan(system_state)
    
    for log in logs:
        print(log)
    
    #fixing vulnerabilities
    print("\nFixing all vulnerabilities:")
    fix(system_state, fixing_list)
    
    #check system to see whether all vulnerabilitis have been fixed
    final_check(system_state)

run_code()
