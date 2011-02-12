import glob,shlex
"""
module for various subprocess commands
"""
#http://article.gmane.org/gmane.comp.python.general/487577/match=getstatusoutput+subprocess
def command(command_line):
     """
     usage: status,output=command(commandstring)
     """ 
     from subprocess import Popen, PIPE, STDOUT
     args = shlex.split(command_line)
     p = Popen(args, stdout=PIPE, stderr=STDOUT, shell=False)
     s = p.stdout.read()
     return p.wait(), s

 
thefiles=glob.glob("*mp3")
for a_file in thefiles:
    the_command=r"""eyeD3 --to-v2.4 "%s" """ % a_file
    error,output=command(the_command)
    print error
    print output
    
    

