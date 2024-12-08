"""
Script contains a version of a Ceasar cipher that uses a different shift for vowels vs consonants.
Author: Mary Grace Albright (marygrace.albright@uconn.edu)
"""
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
alphabet_lower = 'abcdefghijklmnopqrstuvwzyz!@#$%^&*()'
vowels = 'aeiouAEIOU'

def shift_letter(letter, shift):
  """
  Returns the new letter that results from a designated shift for the Ceasar cipher.
  Inputs:
    letter (str): letter to be shifted
    shift (int): number of places in the alphabet the letter is shifted
  Returns:
    letter (str): new shifted letter
  """
  if letter in alphabet_upper:
    old_index = alphabet_upper.index(letter)
    new_index = (old_index + shift) % 36
    return alphabet_upper[new_index]
  elif letter in alphabet_lower:
    old_index = alphabet_lower.index(letter)
    new_index = (old_index + shift) % 36
    return alphabet_lower[new_index]
  else:
    return letter


def encode_caesar(message, vowel_shift, other_shift):
  """
  Function to encode an original message based on a variation of a Ceasar cipher.
  Inputs:
    message (str): message to encode
    vowel_shift (int): how much to shift the vowels in the message
    other_shift (int): how much to shift all other characters in the message (besides spaces)
  Returns:
    encoded_message (str): the encoded message
    shift_types (str list): the types of shifts that were done for each index in the original message. 
  """
  encoded_message = ''
  shift_types = []
  for letter in message:
    if letter in vowels:
      shift = vowel_shift
      shift_types.append('vowel')
    else:
      shift = other_shift
      shift_types.append('other')
    encoded_message += shift_letter(letter, shift)
      
  return encoded_message, shift_types

def decode_caesar(encoded_message, shift_types, vowel_shift, other_shift):
"""
Function to decode a messaged encoded by encode_ceasar()
Inputs:
  encoded_message (str): Message encoded by encode_ceasar()
  shift_types (str list): types of shifts done by encode_ceasar() for each index
  vowel_shift (int): how much vowels were shifted in encode_ceasar()
  other_shift (int): how much other characters were shifted in encode_ceasar()
Returns:
  decoded_message (str): the original message before encoding
"""
  decoded_message = ''
  for i,letter in enumerate(encoded_message):
    if shift_types[i] == 'vowel':
      shift = -vowel_shift
    else:
      shift = -other_shift
    decoded_message += shift_letter(letter, shift)
  return decoded_message


original_message = 'I am at the Zoo!'
vowel_shift = 12
other_shift = 2

encoded_message, shift_types = encode_caesar(original_message, vowel_shift, other_shift)

print(f"Encoded message: {encoded_message}")

decoded_message = decode_caesar(encoded_message, shift_types, vowel_shift, other_shift)
print(f"Decoded message: {decoded_message}")
