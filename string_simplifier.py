#!/usr/bin/env python
#!/usr/bin/python

import sys

special_characters = ['!','@','$','%','^','&','*','(',')','_','-','+',
'=','{','}','|',':',';','.','>','<','/','?','`','~']

def main():
  
  cnt = 0
  
  data = sys.stdin
  
  parsed_data = data.split(' ')
  
  for i in parsed_data:
    if special_characters in i:
      parsed_data.pop(cnt)
    cnt += 1
  
  file = open('strings_output_clean.txt', 'x')
  file.write(parsed_data)
 
if __name__ == "__main__"
  main()

      
        
