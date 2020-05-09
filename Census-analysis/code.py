# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path,delimiter=',',skip_header=1)
print(data)
census = np.concatenate((data,new_record))
print(census)


# --------------
#Code starts here
import statistics
import numpy as np 
age=census[:,0]
print(age)
max_age=max(age)
print(max_age)
min_age=min(age)
print(min_age)
age_mean = statistics.mean(age)
# age_mean=(age)/
print(round(age_mean,2))
age_std = np.std(age)
print(round(age_std,2))


# --------------
#Code starts here

#Creating new subsets based on 'Age'
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


#Finding the length of the above created subsets
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

#Printing the length of the above created subsets
print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))

#Code ends here


# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
sumi=senior_citizens[:,6]
working_hours_sum = sumi.sum()
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=(working_hours_sum)/(senior_citizens_len)
print(avg_working_hours)


# --------------
#Code starts here
import numpy as np
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high = np.mean(high[:,7])
print(round(avg_pay_high,2))
# print(avg_pay_high)
avg_pay_low=np.mean(low[:,7])
# print(avg_pay_low)
print(round(avg_pay_low,2))


