def word_count(str):
  words = 0
  last = ' '
  for i in range(0, len(str)):
    if((not str[i].isalpha()) and (last == 'r' or last == 's')):
      words += 1
    last = str[i]
  if(last == 'r' or last == 's'):
    words += 1
  return words