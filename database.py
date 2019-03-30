import os
import pickle
class store:
    def input(self,ad):
        self.id=ad
        self.item=raw_input('enter item ')
        self.stock=input('enter stock ')
    def disp(self):
        print self.id,self.item,self.stock

#UNIQUE ADMINO AND ADDING:
def add():
      C1=store()
      f1=open('items.dat','ab')
      f2=open('ad.txt','r')
      ad=f2.read()
      ad=int(ad)
      f2.close()
      while True:
         ad=ad+1
         C1.input(ad)
         pickle.dump(C1,f1)
         ch=raw_input('do you want to enter more ')
         if ch.lower()!='yes':
             break
      f1.close()
      f2=open('ad.txt','w')
      f2.write(str(ad))
      f2.close()
    
#DISPLAY        
def display():
    if not os.path.isfile('items.dat'):
        print 'sorry file not found'
    else:
        f=open('items.dat','rb')
        c1=store()
        try:
            while True:
                c1=pickle.load(f)
                c1.disp()

        except EOFError: pass
        finally: f.close()
               
#MODIFY        
def mod():
    if not os.path.isfile('items.dat'):
        print 'sorry'
    else:
               f=open('items.dat','rb+')
               c1=store()
               nm=raw_input('enter item ')
               nm2=raw_input('enter name you want to change it to ')
               flag=0
               try:
                  while True:
                    pos=f.tell()
                    s1=pickle.load(f)
                    if s1.item==nm:
                        flag=1
                        s1.item=nm2
                        f.seek(pos)
                        pickle.dump(s1,f)
                        print nm,'has been changed to', nm2
                        break
               except EOFError:
                 if flag==0:
                    print 'sorry record not found'
               finally:
                 f.close()


#SEARCH
def search():
    if not os.path.isfile('items.dat'):
                print 'sorry'
    else:
        nam=raw_input('enter item to search ')
        f=open('items.dat','rb')
        c1=store()
        try:
            fl=0
            while True:
                c1=pickle.load(
                    f)
                if c1.item==nam:
                    c1.disp()
                    fl=1
        except EOFError:
            if fl==0:
                print 'record not found ,Sorry!'

        finally:
            f.close()
#DELETE            
def delete():
  if not os.path.isfile('items.dat'):
      print 'File Not Found'
  else:
      s1=store()
      f1=open('items.dat','rb')
      f2=open('temp.dat','wb')
      item=raw_input('enter item to be deleted ')
      flag=0
      try:
          while True:
              
              s1=pickle.load(f1)
              if s1.item==item:
                  flag=5
                  print 'record deleted'
                  print
              else:
                  pickle.dump(s1,f2)
      except EOFError:
          if flag==0:
              print 'no such item exists '

      except:
          print 'some other error occurred'
      finally:
          f1.close()
          f2.close()
      os.remove('items.dat')
      os.rename('temp.dat','items.dat')
            
        
#MENU
while True:
    print'''
1.add records
2.delete records
3.modify records
4.search records
5.display records
anything else to exit
'''
    ch=input('enter choice')
    if ch==1:
        add()
    elif ch==2:
        delete()
    elif ch==3:
        mod()
    elif ch==4:
        search()
    elif ch==5:
        display()
    else:
        break
