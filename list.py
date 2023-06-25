## kumpulan data numbers
data_List = [1,5,2,3]
print(data_List)

#kumpulan data string
data_string=["saya","aku","kamu"]
print(data_string)

#kumpulan data char
data_char=['a','v','c','d']
print(data_char)

#kumpulan data boolean
data_bolean=[True,False,True,False]
print(data_bolean)

#kumpulan data float
data_float=[1.3,2.1,31.3,413.3]
print(data_float)

#data mix 
Dmix=[1,"saya",True,3.14,'b']
print(Dmix)

# cara alternatif memnuat list
dRange = range(0,10) #range(start,stop,step)
print(dRange)

Newdata_List = list(dRange)
print(Newdata_List)

#list pake loop
list_for = [i*2 for i in range(0,10)]
print(list_for)

#membuat list pale for dan if
list_For_If = [i for i in range(0,10) if i != 5]
print(list_For_If)

list_For_If = [i for i in range(0,10) if i%2 ==0]
print(list_For_If)

list_For_If = [i for i in range(0,10) if i%2 !=0]
print(list_For_If)
