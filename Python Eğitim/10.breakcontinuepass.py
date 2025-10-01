my_list= [10,20,30,40,50,60]    

for number in my_list:
    if number == 30:
       
       break            #number 30 olunca dur dedik o yüzden 10 ile 20 yi 5 le çarptı 30da durdu
    print(number*5)     #print mantığı da şu şekilde number 10 iken if'e baktı 30mu değil dedi,
                        #sonra print yaptı 20'de aynı şekilde sonra 30 geldi direkt durdu print kısmına geçmedi

print("-"*50)

for number in my_list:
    if number == 30:
       
       continue         #continue işlem yapmadan devam et anlamına gelir burda da 30'u pas geçti
    print(number*5)     #yani dahil etmedi ama işlem devam etti.
                     

for number in my_list:
  pass                  #pass'in mantığı uzun uzun kod yazıcam bu kısmı şimdilik boş geçmek istiyorum
                        #ancak boş geçersem hata alıcam hata almamak için pass yazıyoruz.
                     