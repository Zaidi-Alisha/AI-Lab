class SecurityAgent:
    def __init__(self):
        states = ["Safe", "Low Risk", "High Risk", "Safe", "Low Risk", "High Risk", "Safe", "Low Risk", "High Risk"]
        self.components = {chr(65 + i): states[i] for i in range(9)}

    def display(self, stage):
        print(f"\n{stage} System State:")
        for component, status in self.components.items():
            print(f"{component}: {status}")

    def scan(self):
        print("\nUpon scanning:")
        for component, status in self.components.items():
            if status == "Safe":
                print(f"Component {component} is safe")
            else:
                print(f"Component {component} is having state {status} ")

    def correction(self):
        print("\nFixing low risk vulnerabilities")
        for component, status in self.components.items():
            if status == "Low Risk":
                self.components[component] = "Safe"
                print(f"Low risk vulnerability of component {component}has been fixed")
            elif status == "High Risk":
                print(f"You need premium service to patch vulnerability of component {component}")

security_agent = SecurityAgent()
security_agent.display("First run")
security_agent.scan()
security_agent.correction()
security_agent.display("After fixing:")
