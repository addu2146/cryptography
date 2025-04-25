#Write a program to implement the Playfair cipher for text encryption and decryption.
import string
import numpy as np
#Prepare the Playfair matrix 
def create_matrix(key:str)->np.ndarray:#get key , return an ndarray
    #CAPITALIZE and replace j with I
    key = key.upper().replace('j','I').replace(' ','')
    #To avoid repetition when filling the array create a set
    seen = set()
    #To Store the key and the remaining (upto 25 elements)
    result=[]
    for ch in key + string.ascii_uppercase: #will iterate over all characters in key and all uppercase alphabets
        if ch == 'J':
            #dont include J
            continue
        if ch not in seen:
            #add all new characters
            seen.add(ch)
            #then append them into result
            result.append(ch)
    #transform the 1d array into 5*5 matrix using numpy reshape
    return np.array(result).reshape(5,5)
#Function to find the position of a character in a matrix
def find_pos(matrix:np.ndarray,ch:str)->tuple:
    #find the i,j where a character is located
    row,col = np.where(matrix==ch)
    #return the row and column number
    return int(row[0]),int(col[0])

def prepare_text(text:str,)->list:
    text = text.upper().replace('J','I').replace(' '.'')
    i,pairs = 0,[]
    while i<len(text):
        #we want to make pairs a and b
        a = text[i]
        #only if there is next element
        b = text[i+1] if i+1<len(text) else 'X'
        if a==b:
            #repeating characters must not match
            pairs.append((a,'X'))
            i+=1
        else : 
            pairs.append((a,b))
            i+=2
    #what if we have a odd length ! add one more X at last
    if len(pairs[-1]) == 1:
        pairs[-1] = (pairs[-1][0], 'X')
    return pairs
def Playfair(pairs:list,matrix:np.ndarray,mode='enc')->str:
    shift =1 if mode =='enc' else -1
    result =''
    for a,b in pairs :
        r1,c1=find_pos(matrix,a)
        r2,c2 =find_pos(matrix,b)
        if r1 ==r2 :
            result+=matrix[r1,(c1+shift)%5]+matrix[r2,(c2+shift)%5]
        elif c1==c2:
            result+=matrix[(r1+shift)%5,c1]+matrix[(r2+shift)%5,c2]
        else:
            result+=matrix[r1,c2]+matrix[r2,c1]
    return result
if __name__ == "__main__":
    key = "Ind Vs Pakf"
    matrix = create_matrix(key)
    print("Matrix:\n", matrix)

    plaintext = "Kashmir"
    pairs = prepare_text(plaintext)

    encrypted = Playfair(pairs, matrix, 'enc')
    decrypted = Playfair(prepare_text(encrypted), matrix, 'decrypt')

    print("Plaintext :", plaintext)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
#Good man  
