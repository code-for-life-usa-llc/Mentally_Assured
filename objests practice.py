class student:
    def __init__(self,name,age,shirt):
        self.name = name
        self.age = age
        self.shirt = shirt
def main():
    Elisha = student("Elisha", 22,True)
    print("Hello his name is "+ Elisha.name "and he is"+ Elisha.age ):
  

main()