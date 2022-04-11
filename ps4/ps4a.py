# Problem Set 4A
# Name: <Magy Gamal>
# Collaborators:Sherif Hesham
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    l=[]
    perm=[]
    if len(sequence)==1:
        return [sequence]
    else:
        for i in sequence:
            perm=get_permutations(sequence.replace(i,""))
            for j in perm:
                l.append(i+j)
    return l
            
if __name__ == '__main__':
   #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example1_input= 'is'
    print("Input:",example1_input)
    print("Expected Output:",["is","si"])
    print("Actual Output:",get_permutations(example1_input))
    
    example2_input="but"
    print("Input:",example2_input)
    print("Expected Output:",["but","btu","ubt","utb","tbu","tub"])
    print("Actual Output:",get_permutations(example2_input))
    

