# definitions

# defining the general measures
def general_measures():
    print("Identify and treat the underlying cause of hyponatremia")
    print("Identify drugs taken by the patient that could contribute to hyponatremia. Discontinue those drugs if possible")
    print("Reduce intake of electrolyte-free water")
    print("Other therapies in patients with SIADH and chronic hyponatremia include loop diuretics, salt tablets")

# defining plan A
def plan_A():
    print("Monitor serum Na+ hourly until it has increased 4-6mEq/l above nadir")
    print("Further decline indicates no autocorrection or delayed absorption of ingested water. Give 50ml 3% NS bolus")

# defining plan B
def plan_B():
    print("Give 50 ml bolus of 3% NaCl to prevent further decline in serum Na+")
    print("Monitor serum Na+ hourly to determine need of repeat bolus")

# defining plan C
def plan_C():
    print("Give 100 ml of 3% NaCl IV and repeat twice more, as needed, if symptoms persist")
    print("Monitor serum sodium hourly until it has increased by 4-6mEq/l after which the frequency of monitoring can be reduced")
    print("In case of recurrent hyponatremia repeat treatment as above")

# defining plan D
def plan_D():
    print("Give infusion of 3% NaCl at 15-30 ml/hr + INJ FUROSEMIDE 40 mg (or higher) IV BD")
    print("Monitor serum Na+ every 2-4 hours.")

# defining plan E
def plan_E():
    print("Give infusion of 3% NaCl at 15-30 ml/hr + IV/SC DESMOPRESSIN 1-2mcg TDS/QDS")
    print("Monitor serum Na+ every 2-3 hours initially and then every 4-6 hours after water losses have been controlled.")

# defining plan F
def plan_F():
    print("Give infusion of 3% NaCl at 15-30 ml/hr")
    print("Monitor serum Na+ every 4-6 hours.")

# defining plan G
def plan_G():    
    print("Monitor serum Na+ every 6-12 hours")

#defining outpatient
def outpatient():
    print("Monitor as outpatient")

# defining the rate of correction and discontinuation of regimen    
def plan_rate_target():
    print("Adjust the rate of 3% NaCl to achieve 4-6 mEq/l increase in 24hours")
    print("Discontinue regimen when serum Na+ has increased to at least 125 mEq/l")

# defining the printing of inpatient management
def inpatient():
    print("Manage the patient as inpatient.")

# to check if input is correct
def incorrect_input(input):
    if input == "y" or input == "n":
        return False
    else:
        return True

#defining the heading
def heading():
    print()
    print("The management")
    print("--------------")

# defining the symptoms
mild_symptoms = ["nausea","headache","fatigue"]
moderate_symptoms = ["confusion", "muscle cramps", "weakness"]
severe_symptoms = ["seizures", "coma", "respiratory arrest"]
error = True

# printing the title
print("Hyponatremia Treatment")
print("----------------------")

# enter duration of symptoms
duration = int(input("What is the duration of hyponatremia (in hours)? "))

# algorithm for hyponatremia correction

# if acute onset
if duration < 48:
    while error:
        symptoms = input("Does the patient have any symptoms (y/n)? ")
        error = incorrect_input(symptoms)
    error = True
    if symptoms == "y":
        heading()
        inpatient()
        plan_C()
        general_measures()
    else:
        while error:
            autocorrection = input("Is the hyponatremia already autocorrecting due to a water diuresis? (y/n):")
            error = incorrect_input(autocorrection)
        error = True
        if autocorrection == "y":
            heading()
            inpatient()
            plan_A()
            general_measures()
        else:
            heading()
            inpatient()
            plan_B()
            general_measures()

# if chronic onset
else:
    print("Does the patient have the following symptoms?")
    for features in severe_symptoms:
        print(f"-{features}")
    while error:
        severe = input("y/n? ")
        error = incorrect_input(severe)
    error = True
    if severe == "y":
        heading()
        inpatient()
        plan_C()
        general_measures()
    else:
        print("Does the patient have known intracranial pathology?")
        print("[recent traumatic brain injury, intracranial surgery, hemorrhage, or intracranial neoplasm/SOL]")
        while error:
            brain = input("y/n? ")
            error = incorrect_input(brain)
        error = True
        if brain == "y":
            heading()
            inpatient()
            plan_C()
            general_measures()
        else:
            na = int(input("What is the sodium level? "))
            if na < 120:
                print("Is the patient's hyponatremia due in part to self-induced water intoxication?")
                while error:
                    self = input("y/n? ")
                    error = incorrect_input(self)
                error = True
                if self =="y":
                    heading()
                    inpatient()
                    plan_G()
                    general_measures()
                else:
                    while error:
                        edema = input("Is the patient edematous (i.e due to heart failure or cirrhosis)? y/n: ")
                        error = incorrect_input(edema)
                    error = True
                    if edema == "y":
                        heading()
                        inpatient()
                        plan_D()
                        plan_rate_target()
                        general_measures()
                    else:
                        print("Is the cause of hyponatremia rapidly reversible?")
                        print("-due to true hypovolemia")
                        print("-due to adrenal insufficiency")
                        print("-due to transient SIADH (from surgery, pain, or drug induced)")
                        while error:    
                            reversible = input ("y/n? ")
                            error = incorrect_input(reversible)
                        error = True
                        if reversible == "y":
                            heading()
                            inpatient()
                            plan_E()
                            plan_rate_target()
                            general_measures()
                        else:
                            print("Is the patient at high risk of osmotic demyelination syndrome?")
                            print("Such as:")
                            print("-serum Na+ < = 105 mEq/l")
                            print("-concurrent hypokalemia")
                            print("-patient with alcohol use disorder")
                            print("-malnourished patient")
                            print("-concurrent liver disease")
                            while error:
                                cpm = input("y/n? ")
                                error = incorrect_input(cpm)
                            error = True
                            if cpm == "y":
                                heading()
                                inpatient()
                                plan_E()
                                plan_rate_target()
                                general_measures()
                            else:
                                heading()
                                inpatient()
                                plan_F()
                                plan_rate_target()
                                general_measures()                 
            else:
                print("Does the patient have mild to moderate symptoms?")
                for features in mild_symptoms:
                    print(f"-{features}")
                for features in moderate_symptoms:
                    print(f"-{features}")
                while error:
                    mild_moderate = input("y/n? ")
                    error = incorrect_input(mild_moderate)
                error = True
                if mild_moderate == "y":
                    heading()
                    inpatient()
                    plan_G()
                    general_measures()
                else:
                    heading()
                    outpatient()
                    general_measures()
print()
print("Thank you!")
input("Press enter to continue.")
