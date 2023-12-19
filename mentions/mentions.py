import pandas as pd

def readMentions(pathFile = r".\Game and mentions_Validated.xlsx"):
    mentionsDF = pd.read_excel(rf'{pathFile}')
    print(mentionsDF)
    targetGameNames = list(mentionsDF['Game name'])
    print(targetGameNames)
    return mentionsDF, targetGameNames



