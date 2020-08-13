################################question 1###########################


Cutlets <- read.csv(file.choose())
attach(Cutlets)
View(Cutlets)
#############normality test###########
shapiro.test(Unit.A)
#p-value = 0.32
shapiro.test(Unit.B)
#p-value = 0.5225
#p high=>H0 fly=>accept H0
#conclusion=data is normal

#########variance test###########
var.test(Unit.A,Unit.B)
#p-value = 0.3136>0.05=>p high=>H0 fly=>accept H0
#conclusion all variances are equal

t.test(Unit.A,Unit.B,alternative = "two.sided",conf.level = 0.95)
#p-value = 0.4723>0.05=>p high=>H0 fly=>accept H0


################################question 2##########################


LabTAT<-read.csv(file.choose())
View(LabTAT)
attach(LabTAT)
#normality test
shapiro.test(Laboratory.1)
# p-value = 0.5508
shapiro.test(Laboratory.2)
#p value=0.8637
shapiro.test(Laboratory.3)
p-value = 0.4205
shapiro.test(Laboratory.4)
# p-value = 0.6619
#p high=>H0 fly=>accept H0
#conclusion= data is normal

############variance test############
var.test(Laboratory.1,Laboratory.2)
#p-value = 0.1675
var.test(Laboratory.2,Laboratory.3)
#p-value = 0.2742
var.test(Laboratory.3,Laboratory.4)
#p-value = 0.3168
var.test(Laboratory.4,Laboratory.1)
#p-value = 0.1408
#p high=>H0 fly=>accept H0
#conclusion all variances are equal

Stacked_data1 <- stack(LabTAT)
View(Stacked_data1)
attach(Stacked_data1)
colnames(Stacked_data1)
###########one way anova test###########
Anova_result <- aov(values~ind, data=Stacked_data1)
summary(Anova_result)
# pvalue=<2e-16<0.05=> p low H0 go=>accept Ha



############Question 3###########
#Pearson's Chi-squared test -Karl pearson

# All Proportions all equal 
#BuyerRatio =>unstacked
BuyerRatio <- read.csv(file.choose())
View(BuyerRatio)
attach(BuyerRatio)
stackeddata2 <- stack(BuyerRatio)
attach(stackeddata2)
View(stackeddata2)#stacked data
table(stackeddata2$ind,stackeddata2$values)
chisq.test(table(stackeddata2$ind,stackeddata2$values))
#Pearson's Chi-squared test

#data:  table(stackeddata2$ind, stackeddata2$values)
#X-squared = 24, df = 21, p-value = 0.2931

#p high=>H0 fly=>accept H0
#conclusion=all proportions are equal


############################QUESTION 4#####################################

#Pearson's Chi-squared test
cof <- read.csv(file.choose())
View(cof)#unstacked
attach(cof)
cof <- cof[1:300,1:4]
cof
#as there is no vector column to process create vector columns
cof$Phillippines <- as.vector(cof$Phillippines)
cof$Indonesia <- as.vector(cof$Indonesia)
cof$Malta <- as.vector(cof$Malta)
cof$India <- as.vector(cof$India)
stacked_cof <- stack(cof)#countries are in there own coloum so we need to stack the data
attach(stacked_cof)
stacked_cof#stacked data
#create contingency table
table(stacked_cof$ind,stacked_cof$values)
chisq.test(table(stacked_cof$ind,stacked_cof$values))

#data:  table(stacked_cof$ind, stacked_cof$values)
#X-squared = 3.859, df = 3, p-value = 0.2771
#p high=> H0 fly =>accept H0 
#conclusion :defects among all the centers are equal.


############################QUESTION 5#####################################

fantaloon <- read.csv(file.choose())
View(fantaloon)
#y is discrete in 2 categories & x is discrete in two categories=>2 proportion test
####################=>2 proportion test################################
#remove the empty data cell present in the dataset
fantaloon <- fantaloon[1:400,1:2]
attach(fantaloon)
#converting the data into vector format in order to get seperate values for each column
fantaloon$Weekdays <- as.vector(fantaloon$Weekdays)
fantaloon$Weekend <- as.vector(fantaloon$Weekend)
#convert the unstacked data into stacked data
stack_fantalooon <- stack(fantaloon)
View(stack_fantalooon)
# table
table(stack_fantalooon$values,stack_fantalooon$ind)
######2 proportion test##########
prop.test(table(stack_fantalooon$values,stack_fantalooon$ind),conf.level = 0.95,alternative = "two.sided")
# two. sided -> means checking for equal proportions of males and females entering the store
#p-value = 8.543e-05<0.05=>p low =>Ho go=>accept Ha 
# Unequal proportions 
#conclusiono: males enterimg the store not= females entering the store
prop.test(table(stack_fantalooon$values,stack_fantalooon$ind),conf.level = 0.95,alternative = "greater")
# H0 -> Proportions of males<=Proportions of females
# Ha -> Proportions of males > Proportions of females
# p-value = 4.272e-05<0.05=> p low Ho go=>accept Ha
#conclusion:males entring the store is >females entnering the store







