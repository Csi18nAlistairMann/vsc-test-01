from class_Maffs import Maffs

maffs = Maffs()

num1 = 'a'
num2 = 50
num3 = 60
av = maffs.average_of_three_non_zeroes(num1, num2, num3)
if (av == -1):
    msg = "Your numbers are bad and you should feel bad"
else:
    msg = ("Average of " + str(num1) + ", " + str(num2) + ", and " + \
            str(num3) + " is: " + str(av))
print (msg)