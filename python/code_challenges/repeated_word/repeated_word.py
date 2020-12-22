def strip_down(some_text):
  replacement = ''
  for char in some_text:
    if char in ".,!@#$%^&*()_+=<>?`~?/|\\[]{}:;()":
      char = ""
    replacement += char
  return replacement

def not_split(some_text):
  output =[]
  temp = ''
  for word in some_text:
    if word == ' ':
      output.append(temp)
      temp = ''
    else:
      temp += word
  if temp:
    output.append(temp)
  return output

def seen_word(arr):
  seen_words = []
  for item in arr:
    if item in seen_words:
      return item
    else:
      seen_words.append(item)

def which_word_is_repeated_first(input):
  uniform_string = input.lower()
  stripped = strip_down(uniform_string)
  in_array = not_split(stripped)
  return seen_word(in_array)
