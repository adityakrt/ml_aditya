from sklearn import linear_model as lm
from matplotlib import pyplot as plt
import random 
from matplotlib import style
from statistics import mean
import numpy as np
#y=x1+3*x2+4*x3
count=0
limit=100
x=[]
X=list()
y=list()

#x=[[rand(0,100),rand(0,100),rand(0,100)],[1,2,3]]
#y=[19,27]
for i in range(0,100):
	#if we want to have n we create inner for loop 
	x1=random.randint(0,limit)
	x2=random.randint(0,limit)
	x3=random.randint(0,limit)
	op=x1+3*x2+4*x3
	X.append(x1+3*x2+3*4*x3)#for converting to 1d
	x.append([x1,x2,x3])
	y.append(op)
#print(X)
#print(y)
#plt.grid(color='r', linestyle='-', linewidth=2)

reg = lm.LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=1)
reg.fit (x,y)


#showcase data

for i in range(0,10):
	x1=random.randint(0,limit)
	x2=random.randint(0,limit)
	x3=random.randint(0,limit)
	pred=reg.predict([[x1,x2,x3]])
	calc=x1+3*x2+4*x3
	print (int(pred))
	print (calc)
	
	if int(pred)==calc:
		count=count+1
	else:
		count=count-1
	print(count)
	X.append(x1+3*x2+3*4*x3)#for converting to 1d
	x.append([x1,x2,x3])
	y.append(pred)
	print('~retraining model~')
	reg.fit (x,y)



plt.grid(True)
#plt.plot(x,'g.',y,'ro')
#plt.ylabel('some numbers')
#plt.plot(pred,'b^')
#plt.show()

	
xs = np.array(X, dtype=np.float64)
ys = np.array(y, dtype=np.float64)
#print(xs,ys)

def best_fit_slope_and_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))
    
    b = mean(ys) - m*mean(xs)
    
    return m, b

m, b = best_fit_slope_and_intercept(xs,ys)

print(m,b)
regression_line = []
for x in xs:
    regression_line.append((m*x)+b)
plt.scatter(xs,ys,color='#000000')
plt.plot(xs, regression_line,'g')
plt.show()


#accuraccy

accu=((count/10)*100)
print("accuraccy:")
print(accu)