'''
Created on 30-Aug-2017

@author: bigdata
'''
def varlenArg(narg,*agrv):
    print "Normal argument",narg
    for x in agrv:
        print "variable length argv:",x
        
if __name__=='__main__':
    narg="Narasimman"
    args=(1,2,3,"Lakshmi")
    varlenArg(narg,*args)
  