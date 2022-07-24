import pandas as pd
df= pd.read_csv("data.csv")
course_teacher={}  
teacher_course={}
year_course={}
year_department_cource={}
departments=["cse","ece","cce","me","cse+ece+me+cce","cse+cce","ece+cce"]
days=["mon","tue","wed","thu","fri"]
years=["1","2","3","4"]

for index, row in df.iterrows():
    
    #mapping course -> teacher 
    course = row["Course_Name"].strip()
    t=[x.strip() for x in row["Instructors"].split(',')]  
    course_teacher[course]=t

    #mapping teacher -> course

    for x in row["Instructors"].split(','):
        instructorname =x.strip()
        if instructorname not in teacher_course:
            teacher_course[instructorname]=[]
        teacher_course[instructorname].append(row["Course_Name"].strip())

    #mapping year -> course
    year = row["Year"].strip()
    if year not in year_course:
        year_course[year]=[]
    year_course[year].append(course)

        
        