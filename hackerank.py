# #KANGAROO

# a=[0,2,5,3]
# step1=a[1]
# step2=a[3]
# count=0
# if step1>step2:
#     print step1
#     count+=1
#     kangroo1=a[0]
#     kangroo2=a[2]
# else:
#     print step2
#     kangroo1=a[0]
#     kangroo2=a[2]
    
# if count==0:
#     while True:
#         kangroo2+=step2
#         kangroo1+=step1
#         if kangroo2>kangroo1:
#             print "No"
#             break
#         elif kangroo2==kangroo1:
#             print "Yes"
#             break
# else:
#      while True:
#         kangroo2+=step2
#         kangroo1+=step1
#         if kangroo1>kangroo2:
#             print "No"
#             break
#         elif kangroo2==kangroo1:
#             print "Yes"
#             break
##########################################################################################

##GRADING STUDENTS

user1=int(input())
marksList=[]
newMarks=[]

for i in range(user1):
    user2=int(input())
    marksList.append(user2)

for marks in marksList:
    if marks<=36:
        newMarks.append(marks)
    elif marks % 5 == 0:
        newMarks.append(marks)
        break
    elif marks % 5 != 0:
        
        for new in range(0,3):
            if marks % 5 == 0:
                newMarks.append(marks)
                break
            else:
                   marks +=1
        else:
            marks-=3
            newMarks.append(marks)
for marking in newMarks:
    print (marking)