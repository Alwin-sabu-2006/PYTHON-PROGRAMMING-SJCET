def count_upper_lower_case_characters():
 input_string=input('Enter a string')
 upper_character=0
 lower_character=0
   for character in input_string:
      if character.isupper():
          upper_character +=1
      elif character.islower():
          lower_character+=1

