def myfnc():
   print('m1 module name=%s' %(__name__))
if __name__ == '__main__':
   print('call myfnc()')
   myfnc()
