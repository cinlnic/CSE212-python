def permutations(letters, size, word=""):

        if len(letters) == 0:   # Base Case
            print(word)
        if len(word) == size:
            print(word)
    
        else:
            for index in range(len(letters)):
            # Make a copy of the letters to pass to the
            # the next call to permutations.  We need
            # to remove the letter we just added before
            # we call permutations again.

                letters_left = letters[:]
                del letters_left[index]
            
                
            # Add the new letter to the word we have so far
                permutations(letters_left, size, word + letters[index])
            
permutations(list("ABCDEFGHI"), 6)
