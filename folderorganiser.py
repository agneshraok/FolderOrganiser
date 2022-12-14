import os, shutil

class FilePy:
    def __init__(self, projectName, sourcePath):
        self.projectName = projectName
        self.sourcePath = sourcePath
        self.backupPath = sourcePath + '\\' + projectName + 'Backup'
        self.groupedFoldersPath = sourcePath + '\\' + projectName + 'Folders'
        self.organisedFilesPath = sourcePath + '\\' + projectName + 'Files'

        self.logic()
    
    def logic(self):
        """Execution code """
        self.createBackup()
        self.groupFolders()
        self.organiseFiles()
        
    
    def createBackup(self):
        """ Creates a backup folder which is exact replica of given source path """
        for path, dir, files in os.walk(self.sourcePath):
            if dir or files:
                shutil.copytree(self.sourcePath, self.backupPath)
            break

    def groupFolders(self):
        """Groups all the folders present in the given source path into one folder """ 
        for path, dir, files in os.walk(self.sourcePath):

            if dir:
                os.makedirs(self.groupedFoldersPath)
                for sourceSubDir in dir:
                    originalPath = self.sourcePath + f'\{sourceSubDir}'
                    destinationPath = self.groupedFoldersPath + f'\{sourceSubDir}'
                    os.rename(originalPath,destinationPath)

        #Move the Backup Folder back to sourcePath
        os.rename(self.groupedFoldersPath + '\\' + projectName + 'Backup', self.backupPath)


    def organiseFiles(self):
        """ creates folder for every fileextension present in sourcePath and organises them accordingly."""

        for sourcePath, sourceDir, sourceFiles in os.walk(self.sourcePath):
            if sourceFiles:
                os.makedirs(self.organisedFilesPath)
                for sourceFile in sourceFiles:
                    fileExtension = sourceFile.split('.')[1]
                    #print(fileExtension)
                    for destinationPath, destinationDir, destinationFiles in os.walk(self.organisedFilesPath):
                        folderForFileType = fileExtension.title()+'Files'

                        originalPath = sourcePath + '\\' +sourceFile 
                        destinationPath = self.organisedFilesPath + '\\' + folderForFileType + '\\' +sourceFile 

                        if folderForFileType not in destinationDir:
                            os.makedirs(self.organisedFilesPath + '\\' + folderForFileType)
                            os.rename(originalPath, destinationPath)
                        else:
                            os.rename(originalPath, destinationPath)
                        break
            break



projectName = 'FilePy'
sourcePath = 'D:\\PC\\Code\\1. Projects\\2.FolderOrganiser\\Test'

run = FilePy(projectName,sourcePath)




"""


ToDo
--------------------------------------------------------------------------------------------
1. while grouping folders, make the code to skip the Backup folder, As of now, it is being  
   grouped into the groupedFolders and then again moved back to the sourcePath.

2. ideal to add an if condition before creating FilePy folders. avoid error of recreating it.

3. Add a feature : delete empty folders




Dev Notes
---------------------------------------------------------------------------------------------

@DN1
- FilePy creates folders to categorise all the files and folders.
- if the name of the folder that is going to be created alaready exists in the sourcePath,
  Then the entire process will fail due to name conflict.
- projectName is supposed to be a unique identifier which hopefully will make the name of the
  folder names unique.




"""