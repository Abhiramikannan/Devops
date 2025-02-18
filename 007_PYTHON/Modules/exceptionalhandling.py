try:
    #print(10+'50')
    # print(50/0)
    print(str(70+0.60))

# except:
#     print("somethg went wrong")
except TypeError:
     print("something went wrong")
except ValueError:
    print("this is the value error")
except ZeroDivisionError:
    print("this is the Zerodivision error")
finally:
    print("success")
