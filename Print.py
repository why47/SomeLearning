
a = 20 ## variabel
b = "hello"
c = 2904

e = 10 ## variabel type data int
d = 1.29341 ## variabel type data float
kalimat = "saya" ## variabel type data String 
kata = 'a' ## variabel type data Char


## Output print atau menampilkan 
print("hello workld",a,b ,c)
print (a) 
print (b)
print (c) 
print (a + c)
print (e,d,kalimat,kata)
print (type(a),type(b)) ## menampilakn tipe data di suatu variabel

##casting type data atau mengubabh tipe data
int_data = 9
float_data = float(int_data)
string_data = str(int_data)
bool_data = bool(int_data)

data = 0
move = 0


print(int_data, type(int_data)) ##int data 
print(float_data, type(int_data))##mengubah int data ke float
print(string_data, type(string_data))##
print(bool_data,type(bool_data ))

data = int_data + float_data 
move = data * int_data + float_data / data 
int_move=int(move) ## mengubah tipe float ke int


print("data =",int_data)
print(data )
print(move)
print(int_move, type(int_move))