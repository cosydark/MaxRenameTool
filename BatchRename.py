import sys
import datetime
import pymxs
import csv
import os
Rt = pymxs.runtime

LogFilePath = f'D:/QP_Log/MaxRenameTool/MaxRenameToolLog {datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.txt'
CsvPath = r'C:\Users\cosyd\Desktop\RenameTool\AnimationPaths.csv'
QuadSpace = r'    '
OctSpace = QuadSpace + QuadSpace

def ClearScene():
    Rt.execute("resetMaxFile #noPrompt")

def ImportFbx(FilePath):
    try:
        Rt.ImportFile(FilePath, Rt.name("noPrompt"))
        print(f"Successfully Imported: {FilePath}")
        return True
    except Exception as Error:
        print(f"Error Importing FBX: {Error}")
        return False

def SaveFbx(FilePath):
    try:
        Rt.ExportFile(FilePath, Rt.name("noPrompt"), selectedOnly = False)
        print(f"Successfully Saved: {FilePath}")
    except Exception as Error:
        print(f"Error Saving FBX: {Error}")

def ModifyNodeNames(LegacyName, LogFile):
    for Node in Rt.objects:
        OldName = Node.name
        if LegacyName in OldName:
            if LegacyName == OldName:
                Node.name = 'Renderer'
                LogFile.write(f'{OctSpace}Renamed Node: [{OldName}] -> [Renderer]\n')
            else:
                NewName = OldName.replace(f'{LegacyName}_', '')
                Node.name = NewName
                LogFile.write(f'{OctSpace}Renamed Node: [{OldName}] -> [{NewName}]\n')

def Main(FbxPath, ModelName, LogFile):
    ClearScene()
    if not ImportFbx(FbxPath):
        LogFile.write(f'{QuadSpace}Import Error On [{FbxPath}]\n')
        return
    LogFile.write(f'{QuadSpace}Try Rename Nodes In [{ModelName}]\n')
    ModifyNodeNames(ModelName, LogFile)
    SaveFbx(FbxPath)

if __name__ == "__main__":
    # Check Dir Validity
    LogDir = os.path.dirname(LogFilePath)
    if not os.path.exists(LogDir):
        os.makedirs(LogDir)
    # Go
    with open(LogFilePath, 'w', encoding='utf-8') as LogFile:# Start Recording Log
        with open(CsvPath, 'r', encoding='utf-8') as CsvFile:# Read Paths In Csv
            CsvReader = csv.reader(CsvFile)
            Index = 0
            for Row in CsvReader:
                Index += 1
                FbxFilePath = Row[0].split('<<<')[0]
                ModelName = Row[0].split('<<<')[1]
                LogFile.write(f'\n')
                LogFile.write(f'No.{Index} Working On [{FbxFilePath}] Named [{ModelName}]\n')
                Main(FbxFilePath, ModelName, LogFile)