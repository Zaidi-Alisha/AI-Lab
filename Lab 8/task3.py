from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure
model = BayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue'),
    ('Disease', 'Chills')
])

# Define CPDs
cpd_disease = TabularCPD(variable='Disease', variable_card=2,
                         values=[[0.3], [0.7]], state_names={'Disease': ['Flu', 'Cold']})

cpd_fever = TabularCPD(variable='Fever', variable_card=2,
                       values=[[0.9, 0.5],
                               [0.1, 0.5]],
                       evidence=['Disease'],
                       evidence_card=[2],
                       state_names={'Fever': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']})

cpd_cough = TabularCPD(variable='Cough', variable_card=2,
                       values=[[0.8, 0.6],
                               [0.2, 0.4]],
                       evidence=['Disease'],
                       evidence_card=[2],
                       state_names={'Cough': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']})

cpd_fatigue = TabularCPD(variable='Fatigue', variable_card=2,
                         values=[[0.7, 0.3],
                                 [0.3, 0.7]],
                         evidence=['Disease'],
                         evidence_card=[2],
                         state_names={'Fatigue': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']})

cpd_chills = TabularCPD(variable='Chills', variable_card=2,
                        values=[[0.6, 0.4],
                                [0.4, 0.6]],
                        evidence=['Disease'],
                        evidence_card=[2],
                        state_names={'Chills': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']})

# Add CPDs to the model
model.add_cpds(cpd_disease, cpd_fever, cpd_cough, cpd_fatigue, cpd_chills)

# Verify model correctness
assert model.check_model()

# Inference
infer = VariableElimination(model)

# Task 1: P(Disease | Fever=Yes, Cough=Yes)
query1 = infer.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes'})
print("Task 1: P(Disease | Fever=Yes, Cough=Yes)")
print(query1)

# Task 2: P(Disease | Fever=Yes, Cough=Yes, Chills=Yes)
query2 = infer.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes', 'Chills': 'Yes'})
print("\nTask 2: P(Disease | Fever=Yes, Cough=Yes, Chills=Yes)")
print(query2)

# Task 3: P(Fatigue=Yes | Disease=Flu)
query3 = infer.query(variables=['Fatigue'], evidence={'Disease': 'Flu'})
print("\nTask 3: P(Fatigue=Yes | Disease=Flu)")
print(query3)
