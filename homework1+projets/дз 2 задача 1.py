stroka=str(input())
u=stroka.lower()
oshibki=["жы","шы","чя","щя"]
k=0
for i in range(len(oshibki)):
    if u.find(oshibki[i])!=-1:
        print("Ошибка: "+str(oshibki[i]))
        k=k+1
if k==0:
    print("Все верно")