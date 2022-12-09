data = [x.strip() for x in open("day7-example.txt").readlines()]

class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.subfolders = {}
        self.files = {}
        self.parent = parent
    
    def addSubFolder(self, subName):
        newSub = Folder(subName, parent=self)
        self.subfolders[subName] = newSub
        return newSub
    
    def addFile(self, fName, fSize):
        self.files[fName] = fSize
    
    def folderSize(self):
        fileSizes = sum(self.files.values())
        folderSizes = sum([f.folderSize() for f in self.subfolders.values()])

        # total_folders_size = 0
        # for f in self.subfolders.values():
        #     total_folder_size += f.folderSize()

        return fileSizes + folderSizes

    def isSmall(self):
        return self.folderSize() <= 100000

# class Directory():
#     def __init__(self, name, parent):
#         self.name = name
#         self.contents = []
#         self.parent = parent

# class Leaf_file():
#     def __init__(self, name, size):
#         self.name = name
#         self.size = int(size)

root = Folder("/")
workingDir = root

allFolders = [root]

for line in data[1:]:
    if line.startswith("$"):
        # is a command
        if line.startswith("$ cd"):
            destination = line.split(" ")[2]
            if destination == "..":
                workingDir = workingDir.parent
            else:
                workingDir = workingDir.subfolders[destination]
        elif line.startswith("$ ls"):
            pass # do nothing here
    else:
        # is a file or directory (directories are files shhh)
        if line.startswith("dir"):
            newFolder = workingDir.addSubFolder(line.split(" ")[1])
            allFolders.append(newFolder)
        else:
            fSize, fName = line.split(" ")
            workingDir.addFile(fName, int(fSize))

print("All small folders:", sum([x.folderSize() for x in allFolders if x.isSmall()]))

# total = 0
# for x in allFolders:
#     if x.isSmall():
#         total += x.folderSize()
# print("All small folders:", total)

TOTAL_SIZE = 70000000
NEEDED_FREE = 30000000

freeSpace = TOTAL_SIZE - root.folderSize()
neededClearance = NEEDED_FREE - freeSpace

foldersBySize = sorted(allFolders, key=lambda x : x.folderSize())

for f in foldersBySize:
  if f.folderSize() >= neededClearance:
    print("Folder to delete and size:", f.name, f.folderSize())
    break

# def example_lambda(x):
#     return x.folderSize()