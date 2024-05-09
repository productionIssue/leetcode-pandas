#Solution 1
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    studentId = []
    age = []
    for data in student_data:
        studentId.append(data[0])
        age.append(data[1])
    df_dict = {"student_id": studentId, "age": age}
    generated_df = pd.DataFrame(df_dict)
    return generated_df

#Solution 2
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id','age'])
    
