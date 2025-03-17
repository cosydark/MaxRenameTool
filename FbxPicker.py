import os
import csv

TargetDir = r"C:\yuanhangwu_HZPCC1360037_5625\unity_project\Assets\Res\Character\Parmon"
OutputCsv = "Paths.csv"

FbxPaths = []
for SubDir in os.listdir(TargetDir):
    SubDirPath = os.path.join(TargetDir, SubDir)
    if os.path.isdir(SubDirPath):  # 确保是子目录
        for File in os.listdir(SubDirPath):
            if File.endswith(".fbx"):
                FbxPaths.append(os.path.join(SubDirPath, File))

with open(OutputCsv, mode="w", newline="", encoding="utf-8") as CsvFile:
    Writer = csv.writer(CsvFile)
    for Path in FbxPaths:
        Writer.writerow([Path])

print(f"Saved To [{OutputCsv}]")