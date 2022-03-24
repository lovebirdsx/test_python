import os
path = os.path.normpath('D:\Aki/Source/Client/Saved/Editor/DefaultFlowList.csv')
cmd = r'explorer /select, "{path}"'.format(path=path)
print(cmd)
os.system(cmd)
