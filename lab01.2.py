print("Inserisci una stringa: ")
str = input()
if(len(str)<2):
    print(" ")
else:
    print(str[0] + str[1] + str[len(str)-2] + str[len(str)-1])
