import sys
 
# total arguments
n = len(sys.argv)
# splits the emission factors to process the right indices
first_half = int(((n-1)/2)+1)
second_half = int(((n-1)/2)*-1)
emission_factors_supplier= sys.argv[1:first_half]
emission_factors_LCA = sys.argv[second_half:]

print("emission factors for this footprint are the following:")
print("emmision factor from  LCA Databases ")
print(emission_factors_LCA)
print("emmision factor from  Suppliers ")
print(emission_factors_supplier)

# example amounts --> e.g. 1 piece,2 pieces, 3 pieces,...
# product identifer is the index
amounts =[1,2,3,4,5,6]

Sum = 0
# checks if for used product a emissionfactor is present
# factors from suppliers are prioritized --> only if not present LCA factors 
for i in range(0, int((n-1)/2)):
    if int(emission_factors_supplier[i]) != 0:
        factor = emission_factors_supplier[i]
    elif int(emission_factors_LCA[i]) != 0:
        factor = emission_factors_LCA[i]
    else: 
        factor = 0
    #print("calculations is gonna be: "+ str(Sum) + " = "+str(amounts[i])+ " * " + str(factor) )
    Sum += (amounts[i] *int(factor))

# save result 
with open("result.txt", "w") as f:
        f.write(str(Sum))
     
print("\n\nResult:", Sum)


result = open("result.txt", "r")
print("\n\nResult:", result.readline())

