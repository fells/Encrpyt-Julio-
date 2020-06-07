import collections
import string


def ceaser (rotate_string,num_to_rotate_by):
     lower = collections.deque(string.ascii_lowercase)
     upper = collections.deque(string.ascii_uppercase)

     upper.rotate(num_to_rotate_by)
     lower.rotate(num_to_rotate_by)

     lower =''.join(list(lower))
     upper = ''.join(list(upper))

     return rotate_string.translate(str.maketrans(string.ascii_lowercase, lower)).translate(str.maketrans(string.ascii_uppercase, upper))

print(ceaser('vjgtg ku pq vguv nkmg rtqfwevkqp. wpmpqyp',2))