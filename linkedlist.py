class node:
    def __init__(self,value):
        self.info=value
        self.link=None
class linkedlist:
    def __init__(self):
        self.start=None

    def display(self):
        if(self.start==None):
            print('List is empty')
            return
        else:
            print('List is:')
            p=self.start
            while p is not None:
                print(p.info,end=' ')
                p=p.link
            print()
    def count(self):
        p=self.start
        n=0
        while p is not None:
            n+=1
            p=p.link
        print('count:',n)
    def insertbegin(self,data):
        temp=node(data)
        temp.link=self.start
        self.start=temp
    def insertend(self,data):
        temp=node(data)
        if(self.start==None):
            self.start=temp
            return
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp
    def createlist(self):
        n=int(input("Enter the number of nodes:"))
        if(n==0):
            return
        for i in range(n):
            data=int(input('Enter the data:'))
            self.insertend(data)

    # def insertafter(self,data,x):
    #     p=self.start
    #     while p.link is not None:
    #         p.link==x
    #         break
    #     p=p.link
    #
    #     if p is None:
    #         print(x,'is not in list')
    #     else:
    #         temp=node(data)
    #         temp.link=p.link
    #         p.link=temp
    #
    # def insertbefore(self,data,x):
    #
    #     if(self.start==None):
    #         print('List is empty')
    #
    #     if(x==self.start.info):
    #         temp=node(data)
    #         temp.link=self.start
    #         self.start=temp
    #         return
    #     p=self.start
    #     while p.link is not None:
    #         p.link.info==x
    #         break
    #     p=p.link
    #
    #     if(p.link is None):
    #         print(x,'Is not in list')
    #     else:
    #         temp=node(data)
    #         temp.link=p.link
    #         p.link=temp

    def insertatposition(self,data,k):
        if(k==1):
            temp=node(data)
            temp.link=self.start
            self.start=temp
            return

        p=self.start
        i=1
        while i<k-1 and p is not None:
            p=p.link
            i+=1
        if(p is None):
            print('you can only insert upto the position',i)
        else:
            temp=node(data)
            temp.link=p.link
            p.link=temp

    def deletebigin(self):
        if(self.start is None):
            return
        self.start=self.start.link

    def deletenode(self,x):
        if(self.start is None):
            print('List is empty')
            return
        if(self.start.info==x):
            self.start=self.start.link
            return
        p=self.start

        while p.link is not None:
            if(p.link.info==x):
                break
            p=p.link
        if(p.link is None):
            print(x,' is not in list')
        else:
            p.link=p.link.link
    def deleteend(self):
        if(self.start is None):
            return
        if(self.start.link is None):
            self.start=None
        p=self.start
        while p.link.link is not None:
            p=p.link
        p.link=None
    def reverse(self):
        prev=None
        p=self.start
        while p is not None:
            next=p.link
            p.link=prev
            prev=p
            p=next
        self.start=prev


list=linkedlist()
list.createlist()
list.display()
list.insertbegin(11)
list.insertend(22)
list.insertatposition(33,5)
list.display()
list.deletebigin()
list.display()
list.deleteend()
list.display()
list.deletenode(33)
list.display()
list.reverse()
list.display()
