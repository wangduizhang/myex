# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) == 0:
        return ''
    else:
        return aStr[-1] + reverseString(aStr[0:len(aStr)-1])


#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(x) == 0:
        return True
    elif (len(word) == 0 and len(x) != 0) or (len(word) != 0 and x[0] not in word):
        return False
    elif word != 0 and len(x) != 0:
        if x[0] in word:
            word = word[1:]
            if x[0] not in word:
                return x_ian(x[1:], word)
            else:
                return  x_ian(x, word)


# Problem 5: Typewriter
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    if len(text) <= lineLength:
        return text
    else:
        return text[0:lineLength] +'\n' + insertNewlines(text[lineLength:], lineLength)


print reverseString('dsfgdadsljfklasjfoi')
print x_ian('asd', 'ahdkjsuiop')
print insertNewlines('as,,,d,j,hga,sdfha,,lsklfh,sajdf,kjadf abhdk,fh,ca,dshfk,jhdsk,jhf,hasdkj,fhaksdf.,' ,6)