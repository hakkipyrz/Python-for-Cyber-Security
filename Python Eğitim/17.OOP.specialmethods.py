class Fruits():
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __str__(self): #oluşturulacak olan instance'ın string gösterimi yapar
        return f"{self.name} has {self.calories}"
    
    def __len__(self):
        return self.calories

my_fruit = Fruits("Banana", 200)

print(my_fruit) #str kısmını yazmasaydık bunu yazdırmazdı bize
        
len(my_fruit)