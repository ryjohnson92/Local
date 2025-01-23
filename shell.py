import subprocess,os,signal
class cmd:
    def __init__(self,cmd:str,root:bool=False,listen:bool=False):
        self.iter = listen
        self.cmd = cmd
        self.__root = root
        self.shell = True
        self.__root_cmd = ''
        pass
    def __enter__(self):
        if self.__root:
            self.process = subprocess.Popen(self.__root_cmd, encoding='utf-8',universal_newlines=True, shell=self.shell, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, preexec_fn=os.setsid)
        else:
            self.process = subprocess.Popen(self.cmd, encoding='utf-8',universal_newlines=True, shell=self.shell, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, preexec_fn=os.setsid)
        
        if self.iter:
            # print('Self iter')
            # self.lines = str(self.process.stdout.read()).split('\n')
            return self
        else:
            text = self.process.stdout.read()
            retcode = self.process.wait()
            return text
    def __iter__(self):
        while True:
            line = self.process.stdout.readline()
            if not line:
                break
            yield line.rstrip()
        pass
    def __exit__(self,a,b,c):
        try:
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
        except Exception as err:
            print(err)
        pass
    pass
