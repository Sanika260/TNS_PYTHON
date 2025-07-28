#movies name
"""
movie = []

movie1 = input("Enter movie: ")
movie2 = input("Enter movie: ")
movie3 = input("Enter movie: ")

movie.append(movie1)
movie.append(movie2)
movie.append(movie3)

print(movie)
"""

# palindrome
list = [1,2,3,1]

copy_list = list.copy()
copy_list.reverse()
print(copy_list)

if(copy_list == list):
    print("Palindrome")
else:
    print("Not a palindrome")
    
# tuple count method 
tup = ("C","D","A","A","B","B","A")
print(tup.count("A"))

#sorting list in descending order
list = ["C","D","A","A","B","B","A"]

list.sort()
print(list)


dict = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"    
}

print(dict)

set = {"python","java","c++","python","javascript"}
set1 = {"java","python","java","c++","c"}

print(set.union(set1))
print(len(set.union(set1)))


dic = {}

sub1 = input("enter marks :")
dic.update({"phy" : sub1})
sub2 = input("enter marks :")
dic.update({"chem" : sub2})
sub3 = input("enter marks :")
dic.update({"bio" : sub3})

print(dic)

val = {9, "9.0"}
print(val)

count = 1
while count <= 5 :
    print("hello")
    count += 1  #itrator

print(count)   
i = 1
while i <= 5 :
    print(i)
    i += 1

