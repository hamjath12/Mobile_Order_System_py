print(":-) *** HAMJATH MOBILE SHOP *** (-:")
print("iphone , oppo , vivo , samsumg , redmi")

#.....Product Name....#
iphone_4gb=129999
iphone_8gb=149999
oppo_4gb=19999
oppo_8gb=29999
vivo_4gb=29999
vivo_8gb=39999
samsung_4gb=35999
samsung_8gb=39999
redmi_4gb=31999
redmi_8gb=35999


# .......gst=18%.....#
gst=18

def mobile_phone():


    #....menu card....#
    menus=["iphone","oppo","vivo","samsung","redmi"]

        #....user choice...#
    userchoice=input("Enter Mobile Name :").lower()

    if (userchoice in menus):
            
            print(f" Yes...{userchoice} is available")
            print(f"{userchoice} 4GB or 8GB")

            #...RAM user input...#
            ramquantity=input(f"enter Ram in {userchoice} :").lower()

            #....Quantity user input...#
            userquantity=int(input(f"{userchoice} how many quantity you Want :"))
            
            #...condition statement...#
            if(userchoice=="iphone"):
                #....quantity ram...#
                if(ramquantity=="4gb"):
                    bill=(iphone_4gb*userquantity)
                elif(ramquantity=="8gb"):
                    bill=(iphone_8gb*userquantity)
                else:
                    print("pls enter correct ram")
                
            elif(userchoice=="oppo"):
                #....quantity ram...#
                if(ramquantity=="4gb"):
                    bill=(oppo_4gb*userquantity)
                elif(ramquantity=="8gb"):
                    bill=(oppo_8gb*userquantity)
                else:
                    print("pls enter correct ram")

            elif(userchoice=="vivo"):
                #....quantity ram...#
                if(ramquantity=="4gb"):
                    bill=(vivo_4gb*userquantity)
                elif(ramquantity=="8gb"):
                    bill=(vivo_8gb*userquantity)
                else:
                    print("pls enter correct ram")

            elif(userchoice=="samsung"):
                #....quantity ram...#
                if(ramquantity=="4gb"):
                    bill=(samsung_4gb*userquantity)
                elif(ramquantity=="8gb"):
                    bill=(samsung_8gb*userquantity)
                else:
                    print("pls enter correct ram")
            elif (userchoice=="redmi"):
                #....quantity ram...#
                if(ramquantity=="4gb"):
                    bill=(samsung_4gb*userquantity)
                elif(ramquantity=="8gb"):
                    bill=(samsung_8gb*userquantity)
                else:
                    print("pls enter correct ram")
            
            #......GST calculation........#
            cgst=bill*((gst/2)/100)
            sgst=cgst
            tot_gst=cgst+sgst
            total=round(bill+cgst+sgst,2)
            print("Bill :",bill)
            print("GST :",gst)
            print("CGST :",cgst)
            print("SGST :",sgst)
            print("Total GST :",tot_gst)
            print(f"your total Bill is :",total)
            
    else:
        print(f"{userchoice} is not available")

    

mobile_phone()
