

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