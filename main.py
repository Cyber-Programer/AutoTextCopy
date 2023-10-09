import os 
import sys

try:
    import clipboard
except:
    os.system('pip install clipboard')

data = []
def main(text,lemet):
    try:
        lemet = int(lemet)
    except ValueError:
        print("\nPlease enter a valid number for 'lemet'")
        return

    print()
    for i in range(int(lemet)):
        
        print(text+'\n')
        data.append(text)

    clipboard.copy('\n'.join(data))
    
    
    
    
        
if __name__ == '__main__':
    user_text = input("\nEnter text which you want to type many time: ")
    user_lemet = input("\nEnter howmany line you want: ")
    main(user_text,user_lemet)