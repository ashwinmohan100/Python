class MultipleFunctions():
    def Subfields():
        aiSubFields = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for fields in aiSubFields:
            print(fields)
    
    def OddEven():
        number = int(input("Enter a Number: "))
        if(number % 2 == 0):
            print(f"{number} is Even number")
        else :
            print(f"{number} is Odd number")
    
    def Elegible():
        Gender = input("Your Gender : ")
        age = int(input("Your Age : "))
        if((Gender == "Male" and age >= 21) or (Gender == "Female" and age >= 18)):
            print("Elegible")
        else:
            print("Not Elegible")
    
    def percentageCalculation(s1, s2, s3, s4, s5):
        print("Subject1= ",s1)
        print("Subject2= ",s2)
        print("Subject3= ",s3)
        print("Subject4= ",s4)
        print("Subject5= ",s5)
        sum = s1 + s2 + s3 + s4 + s5
        percentage = (sum / 500) * 100
        print("Total : ", sum)
        print("Percentage : ",percentage) 
    
    def Triangle():
        height = int(input("Enter the height : "))
        breadth = int(input("Enter the breadth : "))
        height1 = int(input("Enter height1 : "))
        height2 = int(input("Enter height2 : "))
        breadthPerimeter = int(input("Enter the breadth value"))
        
        area = (height * breadth) / 2
        print("Area Formula : (Height*Breadth)/2")
        print("Area Of Triangle", area)
    
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter = height1 + height2 + breadthPerimeter
        print("Perimeter of Triangle", perimeter)
