from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork(
    [
        ('Intelligence', 'Grade'),
        ('StudyHours', 'Grade'),
        ('Difficulty', 'Grade'),
        ('Grade', 'Pass')
    ]
)

cpd_Intelligence = TabularCPD(variable='Intelligence', variable_card=2, values=[[0.7], [0.3]])
cpd_StudyHours = TabularCPD(variable='StudyHours', variable_card=2, values=[[0.6], [0.4]])
cpd_Difficulty = TabularCPD(variable='Difficulty', variable_card=2, values=[[0.4], [0.6]])

cpd_Grade = TabularCPD(variable='Grade',variable_card=3, values=[[0.80, 0.60, 0.50, 0.30, 0.40, 0.20, 0.10, 0.05],[0.15, 0.30, 0.40, 0.50, 0.45, 0.50, 0.40, 0.25],[0.05,0.10, 0.10, 0.20, 0.15, 0.30, 0.50, 0.70]], evidence=['Intelligence', 'StudyHours', 'Difficulty'], evidence_card=[2, 2, 2])

cpd_Pass = TabularCPD(variable='Pass', variable_card=2, values=[[0.95, 0.80, 0.50], [0.05, 0.20, 0.50]], evidence=['Grade'],evidence_card=[3])

model.add_cpds(cpd_Intelligence, cpd_StudyHours, cpd_Difficulty,cpd_Grade,  cpd_Pass)

assert model.check_model(), "Model is incorrect"

inference = VariableElimination(model)

result = inference.query(variables=['Pass'], evidence={'StudyHours': 0, 'Difficulty': 0})
print("What is the probability that the student passes the exam, given: StudyHours = Sufficient, Difficulty = Hard")
print(result)

result=inference.query(variables=['Intelligence'], evidence={'Pass': 0})
print("What is the probability that the student has High Intelligence, given: Pass = Yes")
print(result)
