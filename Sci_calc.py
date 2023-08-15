import math
#----------functions call----------
#input_sec

def ask1():
    global z
    z=int(input("Enter no.= "))
    
def ask_ang():
    global z2
    print("Choose:")
    print("1 Degree ")
    print("2 Radian")
    ang=int(input("Enter = "))
    if (ang==1):
        ask1()
        z2= (math.pi)/180
    elif(ang==2):
        ask1()
        z2=z
    else:
        print("Wrong Input")

def ask2():
    global x
    global y
    x=int(input("Enter n1= "))
    y=int(input("Enter n2= "))

#----------------------------algb_fn
def add(x,y):
    sum= x +y
    print("Sum =",sum )

def sub(x,y):
    print("Subtraction =",(x-y) )

def prd(x,y):
    print("Product =",(x*y) )

def div(x,y):
    print("Division =",(x/y) )

def exp(x,y):
    print("Exponent of",x ,"raise to power",y, "is", x**y)
    print("Exponent of",y ,"raise to power",x, "is", y**x)

def sqt(z):
    print("Square root is ", math.sqrt(z))

#---------------trig_fn
#pre-defined used

#--------------log_fn
def log(x,y):
    print("Division =",(x/y) )


#-------------LWT conversion
#simple calculations used

#choose 1 domain & input of dom_sub

print("Choose one by selecting the Index")
print(" ")
print("1 Algebric operators")
print("2 Trignometric operators")
print("3 Logarithmic operators")
print("4 Length/Time/Weight conversion")
n=int(input("Enter="))

#----------------//choose sub-domain//------------

if (n==1):
    print("Algebric Functions are (Choose Index)-")
    print(" 1 Addition")
    print(" 2 Subtraction")
    print(" 3 Multiplication")
    print(" 4 Division")
    print(" 5 Exponential")
    print(" 6 Square root")
    agb=int(input("Enter="))

    if (agb==1):
        ask2()
        add(x,y)
    elif (agb==2):
        ask2()
        sub(x,y)
    elif (agb==3):
        ask2()
        prd(x,y)
    elif (agb==4):
        print("n1=Numerator, n2=Denominator")
        ask2()
        div(x,y)
    elif (agb==5):
        ask2()
        exp(x,y)
    elif (agb==6):
        ask1()
        sqt(z)
    else:
        print("Wrong Input")
    
   
elif (n==2):
  print("Trignometry Functions are (Choose Index)-")
  print(" 1 sin(x)")
  print(" 2 cos(x)")
  print(" 3 tan(x)")
  print(" 4 cot(x)")
  print(" 5 cosec(x)")
  print(" 6 sec(x)")
  trg=int(input("Enter="))
  
  if (trg==1):
        ask_ang()
        print("sin(",z2,") =",math.sin(z2))
  elif (trg==2):
        ask_ang()
        print("cos(",z2,") =",math.cos(z2))
        
  elif (trg==3):
        ask_ang()
        print("tan(",z2,") =",math.tan(z2))
        
  elif (trg==4):
        ask_ang()
        temp=1/(math.tan(z2))
        print("cot(",z2,") =",temp)
        
  elif (trg==5):
        ask_ang()
        temp=1/(math.sin(z2))
        print("cosec(",z2,") =",temp)
        
  elif (trg==6):
        ask_ang()
        temp=1/(math.cos(z2))
        print("sec(",z2,") =",temp)
        
  else:
        print("Wrong Input")
  

elif (n==3):
  print("Logarithmic Functions are (Choose Index)-")
  print(" 1 Log ")
  print(" 2 anti-log ")
  logg=int(input("Enter="))
  if (logg==1):
      ask1()
      print("log(",z,")=",math.log(z))
  elif (logg==2):
      ask1()
      temp=math.log(z)
      temp2=10**(temp)
      print("log(",z,")=",temp2)
  else:
        print("Wrong Input")
  
  
 
elif (n==4):
  print("Length/Time/Weight conversion are (Choose Index)-")
  print(" 1 Length")
  print(" 2 Time")
  print(" 3 Weight")
  ltw=int(input("Enter="))
  
  if(ltw==1):
      print("1 Centimeter to Meter")
      print("2 Meter to centimeter")
      t=int(input("Enter="))
      if(t==1):
          ask1()
          print("Lenth= ",z/100,"m")
      elif(t==2):
          ask1()
          print("Length= ",z*100,"cm")
  
  elif(ltw==2):
      print("1 Hour to Minutes")
      print("2 Minutes to Hour")
      print("3 Hours to Second")
      print("4 Seconds to Hour")
      print("5 Minutes to Seconds")
      print("6 Seconds to Minutes")
      t=int(input("Enter="))
      if(t==1):
          ask1()
          print("Input= ",z*60,"min")
      elif(t==2):
          ask1()
          print("Input= ",z/60,"sec")
      elif(t==3):
          ask1()
          print("Input= ",z*3600,"sec")
      elif(t==4):
          ask1()
          print("Input= ",z/3600,"hr")
      elif(t==5):
          ask1()
          print("Input= ",z*60,"sec")
      elif(t==6):
          ask1()
          print("Input= ",z/60,"min")
    
  elif(ltw==3):
        print("1 Kilograms to gram")
        print("2 Gram to Kilogram")
        t=int(input("Enter="))
        if(t==1):
            ask1()
            print("Weight= ",z*1000,"g")
        elif(t==2):
            ask1()
            print("Weight= ",z/1000,"kg")
          

else:
    print("Wrong Input")
    
