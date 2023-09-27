import json

class admin:

    def __init__(self):

        self.data={}
        with open("food_main.json","r") as file:
            data=json.load(file)
            if data:
                self.data=data

        self.user_data={}
        with open("admin_list.json","r") as file:
            data1=json.load(file)
            if data1:
                self.user_data=data1

    def login(self):

        with open('admin_list.json','r') as f:
            user=json.load(f)

            email=input("enter your email: ")
            password=input("enter your password: ")
            for k in  (user):
                if  user[k]['email']==email and user[k]["password"]==password :
                    print("\n\t\t\tWELCOME TO ADMIN PANNEL \n")

                else:
                    print("invalid credentials")
                    

    def edit(self):
        key=input("enter the key to upadat/edit : ")
        parameter=input("enter the parameter you want to update/edit (price,discount,stock) : ")
        self.data[key][parameter]=int(input("enter the new value: "))

        with open("food_main.json","w") as file:
            json.dump(self.data,file)
            print("edited successfully")
            
    def view(self):

        #for food_item in self.food_items:
            #print(food_item)   
            
        for k,v in self.data.items():
            print("food item ",k)

            for i,j in v.items():
                print(i,"---->",j)
                print("----->")

    def delete(self):
        Key=input("enter the key to delete  : ")

        del self.data[Key]

        with open("food_main.json","w") as file:
            json.dump(self.data,file)
            print("item deleted successfully")

class user:

    def __init__(self):
        self.data={}
        with open("food_main.json","r") as file:
            data=json.load(file)
            if data:
                self.data=data 

        self.user_data={}
        with open ("user_list.json","r") as file:
            data1=json.load(file)
            if data1:
                self.user_data=data1 
    def registration(self,):
        user={}
        user["name"] = input("Enter Your Name:")
        user["email"] = input("Enter Email Id:")
        user["phone_no"]=int(input("enter the contact number: "))
        while True:
            try:
                phone_no=int(user["phone_no"])
                break
            except ValueError:
                print("invalid phone number")
        user["password"]=input("enter a strong password: ")

        with open ("user_list.json","w") as f:
            keys = list(self.user_data.keys())
        if len(keys)>0:
            new_key = int(keys[-1]) + 1
        else:
            new_key = "01"
        self.user_data[str(new_key)] = user

        with open("user_list.json","w") as file:
            json.dump(self.user_data,file)
            print("Signed up successfully!!!")    

    def login(self):
         with open('user_list.json','r') as f:
            user1=json.load(f)

            email=input("enter your email: ")
            password=input("enter your password: ")
            for k in user1:
                if user1[k] ['email']==email and user1[k] ['password']==password:
                    print("\n\t\t\tWELCOME TO USER PANNEL \n")

                else:
                    print("invalid credentials")


        
    def view_options(self):

        choice=int(input("enter your choice: "))

        if choice==1:
            self.creat_new_order()
            

        elif choice==2:
            self.order_history()
            

        elif choice==3:
            self.update_profile()
            

        else:
            print("invalid input")


    def creat_new_order(self):

        self.order={"item":"",}
        item={}
        with open("food_main.json","r") as f:
            Data=json.load(f)
        key=input("enter the key number : ")
        quantity=input("enter the quantity: ")
        tax=int(input("enter the tax percentage : "))
        
        item['name']=Data[key]["name"]
        item['price']=Data[key]['price']
        item['tax']=round((float(item['price'])*tax)/100)
        item['total_price']= round(((float(item['price']))+ float(item['tax'])) * int(quantity))
        item['quantity']=quantity
        print('your order is',item,'\n')

        choice=int(input("enter your choice: "))

        if  choice==1:

            with open("order_history.json","r") as file:
                order=json.load(file)

            if len(order)!=0:
                for i in range (len(order)):
                    if str(order[i]) ==str([item]):
                        break
                    if i!=len(order)-1 and i!=-1:
                        pass
                    else:
                        order.append(item)
                
                with open("order_history.json",'w+')as file:
                    json.dump(order,file ,indent =4 )


            print("order created successfully")
                

        elif choice==2:

            
            with open("cart.json","r") as file:
                cart=json.load(file)

            if len(cart)!=0:
                for i in range (len(cart)):
                    if str(cart[i]) ==str([item]):
                        break
                    if i!=len(cart)-1 and i!=-1:
                        pass
                    else:
                        cart.append(item)
                
                with open("cart.json",'w+')as file:
                    json.dump(cart,file ,indent =4 )


            print("item added to cart successfully")                

        else:
            print("invalid input")

        
    
    def view_cart(self):
        with open ("cart.json","r") as file:
            view_cart=json.load(file)

        return view_cart    

    def order_history(self):

        with open ("order_history.json","r") as file:
            order_history=json.load(file)

        print("your order history is ",order_history)

    def update_profile(self):
        key=input("enter the key to upadat/edit : ")
        parameter=input("enter the parameter you want to update/edit (name,email,password) : ")
        self.user_data[key][parameter]=input("enter the new details: ")

        with open("user_list.json","w") as file:
            json.dump(self.user_data,file)
            print("profile updated successfully")