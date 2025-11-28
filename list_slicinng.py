#same as string

marks = [85,65,89,45,96,100]
print(marks[1:4]) 
print(marks[-6:-2])  #negative slicing     

# LIST SPECIFIC METHOD  /list ke uper kuch kaam perform kar ke denge

list = [2,1,3] 
#1st method (LIST APPEND)  kisi chiz ko last me joor dena for that we use append method 
list.append(5)
print(list)

#2nd method (SORT ASCENDING ORDER) chizo ko sahi order me arrange kar dena / there are two type of shorting 
list = [1,3,2]     # list = ["banana" , "litchi" , "apple"]
list.sort()   #print(list.sort())
print(list)

#(SORT DECENDING ORDER)
list = ["banana" , "litchi" , "apple"]      #list =[5,9,3]
list.sort(reverse=True)  #print(list.sort(reverse=True)) 
print(list)

#3rd method (REVERSED METHOD) 
list = ['g','r','d','w','v']
list.reverse()
print(list)

#4th method (INSERT METHOD)             similar to append but there is litbit difference [list.insert(idx , el)]
list = [2,1,3]
list.insert(2, 5)  #/ index 2 pe vlaue 5 
print(list)

#5th method (REMOVE METHOD)
list = [1,3,2,3,4]
list.remove(3)
print(list)

list = [1,3,2,3,4]   #index remove
list.pop(2)
print(list) 
