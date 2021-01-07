import win32com.client as com
import os

dirpath = os.getcwd()
folderPath = dirpath + "/argosincludes"
fso = com.Dispatch("Scripting.FileSystemObject")
folder = fso.GetFolder(folderPath)
print(folder.Size)