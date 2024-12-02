class MyCart:
    def __init__(self) :
        self.cart={}
      
        
        
    def product(self,prdct,price):
        self.cart[prdct]=price
        print(self.prdct,self.price)
      
    
    def addtocart(self,prdct,price):
        self.cart[prdct]=price
        
    def display(self):
        
        print(self.cart)
    
    def bill(self):
        self.total=0 
        for price in self.cart.values():
            
            self.total=self.total+price
        print(self.total)
    
    def discount(self):
        if self.total>500 and self.total<1000:
            discount=(self.total/100)*3
            billafterdisct=self.total-discount
            print( billafterdisct)
        elif self.total>1000 and self.total<2000:
            discount=(self.total/100)*5
            billafterdisct=self.total-discount
            print(billafterdisct)
        elif self.total>2000:
            discount=(self.total/100)*10
            billafterdisct=self.total-discount
            print(billafterdisct)
        else:
            print("no discount")
            
        
            
myobj=MyCart()
myobj.addtocart("book",25)
myobj.addtocart("bag",350)
myobj.addtocart("pen",10)
myobj.addtocart("pencil box",200)
myobj.addtocart("bottle",350)

myobj.display()
myobj.bill()
myobj.discount()
    