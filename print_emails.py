#coding=gbk
import re
def email(emi):
    pattern1=re.compile(r'(\w+)\.*(\w*)\@(\w+)\.(\w+)')
    m1=pattern1.match(emi).groups()
    m1=tuple(filter(lambda x:len(x)!=0,list(m1)))
    print(m1)

email1='bill.gates@microsoft.com'
email2='someone@gmail.com'
email(email1)
email(email2)

pattern2=re.compile(r'^\<(\w+) (\w+)\> (\w+)\@(\w+)\.(\w+)')
m3=pattern2.match("<Tom Paris> tom@voyager.org").groups()
print(m3)