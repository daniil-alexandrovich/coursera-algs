# -*- coding: utf-8 -*-
'''
Created on January 8, 2018 for Timothy Roughgarden's Algorithms Specialization
'''

# A class for performing Karatsuba Multiplication. 

class Karatsuba:
   
    def multiply(self, x, y):
    '''Returns the product of two string-formatted integers.
    
    The divide-and-conquer algorithm takes two integers of (equal) length equal
    to a power of two. This sole public method formats the two integers as such
    by padding them with zeroes and continues to pass them to the recursive
    algorithm.
    
    Since Python doesn't impose a bit limit on integers, this is technically
    moot for this language. However, it was fun to implement, and Python's
    growing on me.
    '''
        if type(x) is not str or type(y) is not str:
            raise Exception("Numbers must be passed as strings.")
        if ord(i) > 57 or ord(i) < 48 for i in x+y:
            raise Exception("Input strings cannot contain non-integer characters.")      
        x,y = self.__format(x,y)
        return self.__multiply(x,y)

    def __multiply(self,x,y):
    '''Runs the Karatsuba multiplication algorithm on two input integers
    formatted as strings. These integers are of equal length, and their length
    is a power of two.
    
    Consider integers i, j of length m.
    
    Base case: i*j can be considered a primitive step if m=1.
    
    Recursive step: i can be rewritten as i_1*10^(m/2) + i_2, where (conceptually)
    i_1 consists of the first m/2 digits of i and i_2 consists of the last m/2
    digits. Same for j. Therefore:
        
                * i*j = (i_1*10^(m/2) + i_2)(j_1*10^(m/2) + j_2)
                      = i_1*j_1*10^(m) + (i_1*j_2+i_2*j_1)*10^(m/2) + i_2*j_2
                      = z_1*10^(m) + (i_1*j_2+i_2*j_1)*10^(m/2) + z_2
    
    ...where we have essentially transformed a single multiplication into four
    multiplications on integers of half the length. It is possible to lower
    this number to three multiplications with a bit of alever algebra:
        
      i_1*j_2+i_2*j_1 = i_1*j_2+i_2*j_1 + (i_1*j_1+i_2*j_2) - (i_1*j_1+i_2*j_2)
                      = (i_1+i_2)(j_1+j_2) - (i_1*j_1+i_2*j_2)
                      
    ...where i_1*j_1 and i_2*j_2 have already been calculated.
    '''
        if len(x) > 1:
            # Recursive step: split x and y into front and back halves
            x_end = x[len(x)//2:]
            x_front = x[:len(x)//2]
            y_end = y[len(y)//2:]
            y_front = y[:len(y)//2]
            # Calculate necessary products
            z_1 = self.__multiply(x_front, y_front)
            z_2 = self.__multiply(x_end, y_end)
            # Since it is not necessarily true that (i_1 + i_2) or (j_1 + j_2)
            # are of length equal to a power of 2, they must be reformatted
            # and are therefore passed to multiply().
            z_intermediate = self.multiply(str(int(x_end)+int(x_front)),
                                           str(int(y_end)+int(y_front)))
            z_3 = z_intermediate - z_1 - z_2
            return 10**len(x)*z_1 + 10**(len(x)//2)*(z_3) + z_2
            
        else:
            # Base case: just multiply them. Feels like cheating but hey it's
            # less code.
            return int(x)*int(y)

    def __format(self, x, y):
        '''Properly formats two input strings such that:
                a) They are of equal length
                b) That length is equal to a power of 2
        '''
        length = 1
        while len(x) > length or len(y) > length:
            length = length * 2
        return self.__fill_zeroes(x, length), self.__fill_zeroes(y, length)
    
    def __fill_zeroes(self, x, length):
        '''Pads 'x' with zeroes until it is of length 'length''''
        if len(x) > length:
            raise Exception("Input integer longer than target length")
        return '0' * (length-len(x)) + x

