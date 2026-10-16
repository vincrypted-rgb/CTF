```ord & chr```

ord("a") gives you the ASCII decimal value (97, in this case)
chr(97) gives you the letter character of the number ("a" in this case)

built in python function, which saves me from making an A1Z26 cypher heartemoji.
***
```% 26```

% is called **modulo**. 

This gives the remainder after division.
My first thought, upon learning this is "where are we dividing?" And lo and behold, we're not! We're subtracting!!! (...????)

> (ConfusedNickYoung.jpeg)
> (PedroPascalLaughingThenCrying.mp4)
> ###### note: that's my sense of humor, not missing media.

The idea with modulo is that you subtract the base value as many times as you can before you go negative, and then take the remainder/number equaling the distance to 0 as your answer.

### An example:
> Let's say we have a shifted value of 55, and we need to figure out the character that goes with it.
> There are 26 letters in the alphabet.
> 
> 55-26 = 29
> 29-26 = 3
> 3-26 = -23 ####🚫 **too far**
> 55 % 26 = 2 remainder 3 --> 3
