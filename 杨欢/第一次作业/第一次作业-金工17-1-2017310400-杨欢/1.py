w=47.5
h=1.59
t=w/h**2
if t<18:
    判断="低体重"
elif t<=25:
    判断="正常体重"
elif t<=27:
    判断="超重体重"
else:
    判断="肥胖"
print("您的体重指数为"+str(t)+",是"+str(判断)+"。")
