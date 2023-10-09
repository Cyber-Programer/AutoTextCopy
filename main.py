import os 
import sys

try:
    import clipboard
except:
    os.system('pip install clipboard')
try:
    from termcolor import colored
except:
    os.system('pip install termcolor')
data = []
banner = '''
   _         _       _____          _     ___                  
  /_\  _   _| |_ ___/__   \_____  _| |_  / __\___  _ __  _   _ 
 //_\\| | | | __/ _ \ / /\/ _ \ \/ / __|/ /  / _ \| '_ \| | | |
/  _  \ |_| | || (_) / / |  __/>  <| |_/ /__| (_) | |_) | |_| |
\_/ \_/\__,_|\__\___/\/   \___/_/\_\\__\____/\___/| .__/ \__, |
                                                  |_|    |___/ 
'''
def main(text,lemet):
    
    try:
        lemet = int(lemet)
    except ValueError:
        print(colored("\nPlease enter a valid number for 'lemet'",'red'))
        return

    print()
    for i in range(int(lemet)):
        
        print(colored(text+'\n','red'))
        data.append(text)

    clipboard.copy('\n'.join(data))
    
    
    
    
        
if __name__ == '__main__':
    print(colored(banner,'red'))
    user_text = input(colored("\nEnter text which you want to type many time: ",'red'))
    user_lemet = input(colored("\nEnter howmany line you want: ",'red'))
    main(user_text,user_lemet)
