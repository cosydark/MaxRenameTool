import os
import csv

# InputCsv = "Paths.csv"
InputCsv = "Paths_Test.csv"
OutputCsv = "AnimationPaths.csv"

with open(InputCsv, mode='r', encoding='utf-8') as InFile:
    CsvReader = csv.reader(InFile)
    with open(OutputCsv, mode='w', newline='', encoding='utf-8') as OutFile:
        CsvWriter = csv.writer(OutFile)
        for Row in CsvReader:
            FbxPath = Row[0]
            FbxName = Row[0].split('\\')[-1].split('.')[0]
            CsvWriter.writerow([f'{FbxPath}<<<{FbxName}'])
            if not FbxName.endswith('_Shiny'):
                AniFolder = os.path.join(os.path.dirname(FbxPath), 'Ani')
                if os.path.exists(AniFolder) and os.path.isdir(AniFolder):
                    for File in os.listdir(AniFolder):
                        if File.endswith('.fbx'):
                            CsvWriter.writerow([os.path.join(AniFolder, f'{File}<<<{FbxName}')])