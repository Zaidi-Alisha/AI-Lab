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

# Define the CPTs
cpd_disease = TabularCPD('Disease', 2, [[0.3], [0.7]])  # Flu, Cold

cpd_fever = TabularCPD(
    'Fever', 2,
    values=[[0.1, 0.5],  # Fever = No
            [0.9, 0.5]], # Fever = Yes
    evidence=['Disease'],
    evidence_card=[2]
)

cpd_cough = TabularCPD(
    'Cough', 2,
    values=[[0.2, 0.4],  # Cough = No
            [0.8, 0.6]], # Cough = Yes
    evidence=['Disease'],
    evidence_card=[2]
)

cpd_fatigue = TabularCPD(
    'Fatigue', 2,
    values=[[0.3, 0.7],  # Fatigue = No
            [0.7, 0.3]], # Fatigue = Yes
    evidence=['Disease'],
    evidence_card=[2]
)

cpd_chills = TabularCPD(
    'Chills', 2,
    values=[[0.4, 0.6],  # Chills = No
            [0.6, 0.4]], # Chills = Yes
    evidence=['Disease'],
    evidence_card=[2]
)

# Add the CPDs
model.add_cpds(cpd_disease, cpd_fever, cpd_cough, cpd_fatigue, cpd_chills)
assert model.check_model()

# Inference engine
inference = VariableElimination(model)

# Inference Task 1: P(Disease | Fever=Yes, Cough=Yes)
print("P(Disease | Fever=Yes, Cough=Yes):")
query1 = inference.query(variables=['Disease'], evidence={'Fever': 1, 'Cough': 1})
print(query1)

# Inference Task 2: P(Fatigue | Disease=Flu)
print("\nP(Fatigue | Disease=Flu):")
query2 = inference.query(variables=['Fatigue'], evidence={'Disease': 0})  # Flu = 0
print(query2)
