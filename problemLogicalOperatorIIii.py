#Question:Define four variables: p, q, r, and s.
#Create a logical expression that evaluates to True if at least two of the conditions p and q, r or s, and not p are true.

p=True
q=False
r=True
s=False

result= (p and q) + (r or s ) and (not p) >=2
print(result)




