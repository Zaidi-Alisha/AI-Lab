from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define network structure (edges)
model = BayesianNetwork([
    ('Burglary', 'Alarm'),
    ('Earthquake', 'Alarm'),
    ('Alarm', 'JohnCalls'),
    ('Alarm', 'MaryCalls')
])

# Step 2: Define CPDs
cpd_burglary = TabularCPD('Burglary', 2, [[0.999], [0.001]])
cpd_earthquake = TabularCPD('Earthquake', 2, [[0.998], [0.002]])

cpd_alarm = TabularCPD(
    variable='Alarm', variable_card=2,
    values=[[0.999, 0.71, 0.06, 0.05],    # Alarm = False
            [0.001, 0.29, 0.94, 0.95]],   # Alarm = True
    evidence=['Burglary', 'Earthquake'],
    evidence_card=[2, 2]
)

cpd_john = TabularCPD(
    variable='JohnCalls', variable_card=2,
    values=[[0.3, 0.9], [0.7, 0.1]],  # [False, True]
    evidence=['Alarm'],
    evidence_card=[2]
)

cpd_mary = TabularCPD(
    variable='MaryCalls', variable_card=2,
    values=[[0.2, 0.99], [0.8, 0.01]],  # [False, True]
    evidence=['Alarm'],
    evidence_card=[2]
)

# Step 3: Add CPDs to the model
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary)

# Step 4: Validate the model
assert model.check_model(), "Bayesian network is invalid!"

# Step 5: Inference
inference = VariableElimination(model)

# Query: What is the probability of Burglary given that both John and Mary called?
query_result = inference.query(variables=['Burglary'], evidence={'JohnCalls': 1, 'MaryCalls': 1})
print("P(Burglary | JohnCalls=True, MaryCalls=True):")
print(query_result)
