# <span style="color:#a44ae5"> **gamedev-demos-sp2023** </span>
*Little pygame demos for Hack110 sp2023.*

## <span style="color:#a44ae5"> **match statements for events** </span>
### <span style="color:#e6eaeda5"> what is a match statement? </span> 
*note: you will use 'match' statements if you decide to continue on to other compsci courses! however, they will be called 'switch' statements. python is weird.*   
a match statement is another way to write a set of if-elif-else statements with reduced syntax, making the whole code block more readable and easier to understand.  
here's a basic example of a match statement:
```python
    usr_score: int = 0
    my_var: str  = "I love Hack110!"

    match my_var:
        case "I hate Hack110!":
            usr_score -= 2 
        case "I love Hack110!":
            usr_score += 1
        case _:
            usr_score -= 1
    
    print(usr_score)
```
would print
```
    1
```
hopefully it's easy to imagine how this is similar to an if-elif-else block.   
*so how is this helpful for building a game?*  
each time a user gives you input for your game, you have to decide what to do. 
TODO: make code and then finish this to 
things that need to be in switch statement:
use documentation page for pygame.key - right below list of methods


## physics in a basic platformer

primary-blue: #7acdfa;
white: #ffffff;
purple: #a44ae5;
pink: #f30dff;
green: #4EC9B0;
yellow: #eaeea2;
orange: #CE9178;
dark-blue: #3175ad;
gray: #e6eaeda5;
