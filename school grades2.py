school_grades = {"Mario": {"Matematica": 6, "Italiano": 6, "Scienze": 7, "Inglese": 4},
"Giovanni": {"Matematica": 4, "Italiano": 6, "Scienze": 5, "Inglese": 7},
"Paola": {"Matematica": 9, "Italiano": 6, "Scienze": 8, "Inglese": 8}}
n_school_grades = len(school_grades["Mario"])
school_average_Mario = ((school_grades["Mario"]["Matematica"]) + (school_grades["Mario"]["Italiano"]) + (school_grades["Mario"]["Scienze"]) + (school_grades["Mario"]["Inglese"])) / int(n_school_grades)
print("School_average_Mario: ", school_average_Mario)
school_average_Giovanni = ((school_grades["Giovanni"]["Matematica"]) + (school_grades["Giovanni"]["Italiano"]) + (school_grades["Giovanni"]["Scienze"]) + (school_grades["Giovanni"]["Inglese"])) / int(n_school_grades)
print("School_average_Giovanni: ", school_average_Giovanni)
school_average_Paola = ((school_grades["Paola"]["Matematica"]) + (school_grades["Paola"]["Italiano"]) + (school_grades["Paola"]["Scienze"]) + (school_grades["Paola"]["Inglese"])) / int(n_school_grades)
print("School_average_Paola: ", school_average_Paola)