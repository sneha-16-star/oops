class Parrot:

  species = "oiro"

  def __init__(self,name,age):
    self.name = name
    self.age  =age


blu = Parrot("Blu",10)
woo = Parrot("Woo",15)

print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))