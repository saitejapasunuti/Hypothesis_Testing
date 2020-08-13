#######################QUESTION 1 #############################
import numpy as np
#pandas is used data for manipulation,analysis and data cleaning.
import pandas as pd
#scipy is a library used to solve scitific and  mathematical problems.
import scipy 
#scipy stats consists of all statistical functions.
from scipy import stats 
import statsmodels.api as sm 
########2 sample t test(diameter of cutlets)##########
############normality test###########
cutlet=pd.read_csv("D:\\360digiTMG\\module 5\\Datasets (2)\\Cutlets.csv",encoding='latin1')
cutlet
cutlet.columns="Unit_A","Unit_B"
cutlet
cutlet=cutlet.iloc[0:35,0:2]
cutlet
cutlet=pd.DataFrame(cutlet)
print(stats.shapiro(cutlet.Unit_A))
#p value=0.3199819028377533)
print(stats.shapiro(cutlet.Unit_B))
#p value=0.5224985480308533
#########variance test################
scipy.stats.levene(cutlet.Unit_A,cutlet.Unit_B)
#pvalue=0.4176162212502553> 0.05 so p high null fly => Equal variances

########2 Sample T test##############
scipy.stats.ttest_ind(cutlet.Unit_A,cutlet.Unit_B)
#pvalue=0.4722394724599501> 0.05 so p high null fly =>accept H0


########################QUESTION 2##############################

###########ONE WAY ANOVA#################
from statsmodels.formula.api import ols
lab=pd.read_csv("D:\\360digiTMG\\module 5\\Datasets (2)\\LabTAT.csv")
lab
lab= lab.iloc[0:120,0:4]
lab
lab.columns="Laboratory_1","Laboratory_2","Laboratory_3","Laboratory_4"
##############normality test###############
print(stats.shapiro(lab.Laboratory_1))
#p value=0.5506953597068787>0.05=>p high =>H0 fly
print(stats.shapiro(lab.Laboratory_2))
#p value=0.8637524843215942>0.05=>p high =>H0 fly
print(stats.shapiro(lab.Laboratory_3))
#p value=0.4205053448677063>0.05=>p high =>H0 fly
print(stats.shapiro(lab.Laboratory_4))
#p value=0.6618951559066772>0.05=>p high =>H0 fly
#######vavrience test############
scipy.stats.levene(lab.Laboratory_1,lab.Laboratory_2)
#pvalue=0.06078228171776711
scipy.stats.levene(lab.Laboratory_2,lab.Laboratory_3)
# pvalue=0.33220021420602397
scipy.stats.levene(lab.Laboratory_3,lab.Laboratory_4)
#pvalue=0.15472618294425391
scipy.stats.levene(lab.Laboratory_4,lab.Laboratory_1)
#pvalue=0.22188001348277267
#p high =>H0 fly =>all variances are equal
#########one way anova############

F, p = stats.f_oneway(lab['Laboratory_1'], lab['Laboratory_2'], lab['Laboratory_3'], lab['Laboratory_4'])
#p low =>H0 go=>accept Ha hypothesis.


###########################QUESTION 3######################################

buy=pd.read_csv("D:\\360digiTMG\\module 5\\Datasets (2)\\BuyerRatio.csv",encoding='latin1')
buy
buy1=buy.iloc[0:2,1:5]
buy1
Chisquares_results=scipy.stats.chi2_contingency(buy1)
Chi_square=[['','Test Statistic','p-value'],['Sample Data',Chisquares_results[0],Chisquares_results[1]]]
#[['', 'Test Statistic', 'p-value'], ['Sample Data', 1.595945538661058, 0.6603094907091882]]
#p high null fly =>accept H0
#conclusions=all propportions are equal


##########################QUESTION 4######################################

cof=pd.read_csv("D:\\360digiTMG\module 5\Datasets (2)\CustomerOrderform.csv")
cof
cof1=cof.iloc[0:300,:5]
cof1
#unique function is used to get the unique values of a particular column.
unique, counts1=np.unique(cof1.Phillippines,return_counts=True)
unique, counts2 = np.unique(cof1.Indonesia, return_counts=True)
unique, counts3 = np.unique(cof1.Malta, return_counts=True)
unique, counts4 = np.unique(cof1.India, return_counts=True)

cofdata=np.array([counts1,counts2,counts3,counts4])
chi2_stat, p_val, dof, ex = stats.chi2_contingency(cofdata)
p_val
#0.25827985306698553>0.05=> p high h0 fly=>accept H0 

##########################QUESTION 5######################################


fantaloon=pd.read_csv("D:\\360digiTMG\module 5\Datasets (2)\Fantaloons.csv")
fantaloon
fanta=fantaloon.iloc[0:400,0:2]
fanta
from statsmodels.stats.proportion import proportions_ztest
tab1= fanta.Weekdays.value_counts()
tab1
#Female    287
#Male      113
tab2=fanta.Weekend.value_counts()
tab2
#Female    233
#Male      167
counts=np.array([287,113])
nobs=np.array([233,167])

stats,pval=proportions_ztest(counts,nobs,alternative="two-sided")
pval
#pvalue=0.0<0.05=> p low =>H0 go=>accept Ha 
#conclusion a is not = to proportion b
stats,pval=proportions_ztest(counts,nobs,alternative="larger")
pval
#pval=0.0<0.05=> p low =>H0 go=>accept Ha 
#conclusion:proportion a is greater

