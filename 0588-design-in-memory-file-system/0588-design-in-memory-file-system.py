class FileSystem:

    def __init__(self):
        self.root={}
        self.cache={}
        

    def ls(self, path: str) -> List[str]:
        # print('ls for path; ',path)
        croot=self.root
        if path[0]=='/':
            if '/' not in croot:
                return []
            else:
                croot=croot['/']
        path=path[1:]
        fDir=path.split('/')
        # print('fDir',fDir,croot)
        for f in fDir:
            if f=='':
                break
            if f not in croot:
                # print('ls',croot )
                return []
            if type(croot[f])==str:
                return [f]
            else:
                croot=croot[f]

    
        return sorted(list(croot.keys()))        

    def mkdir(self, path: str) -> None:
        croot=self.root
        if path[0]=='/':
            if '/' not in croot:
                croot['/']={}
            
            croot=croot['/']
        # print(croot)
        path=path[1:]
        fDir=path.split('/')
        # print(path)
    
        for f in fDir:
            if f not in croot:
                croot[f]={}
            croot=croot[f]
        # print('mkdir',self.root)

        

    def addContentToFile(self, filePath: str, content: str) -> None:
        croot=self.root
        if filePath[0]=='/':
            if '/' not in croot:
                croot['/']={}
            croot=croot['/']
        filePath=filePath[1:]
        fDir=filePath.split('/')
        x=fDir.pop()
        # print('add content',filePath,content)
        # print(x,croot)
        for f in fDir:
            if f=='':
                break
            if f not in croot:
                croot[f]={}
            croot=croot[f]
        if x not in croot:
            croot[x]=""
        croot[x]+=content

        
        

    def readContentFromFile(self, filePath: str) -> str:
        croot=self.root
        if filePath[0]=='/':
            if '/' not in croot:
                croot['/']={}
            else:
                croot=croot['/']
        filePath=filePath[1:]
        fDir=filePath.split('/')
        x=fDir.pop()
        for f in fDir:
            if f not in croot:
                return []
            croot=croot[f]
        return croot[x]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)