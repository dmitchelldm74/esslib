# ESS:A Styler for html

### How to use ESS
    Comments:
        /* this is a comment */
        ? this is also a comment
        #& another comment
        #! yet another comment
    Variables:
        $favcol=purple
    To use the variable:
        background-color=$favcol
    Syntax:
        body:
            background-color=purple
            color=white
    for active states:
        #id&hover:
            color=blue
    for types:
        #id[type%text]:
            color=red
    or 
        #id[type@check]:
            color=white
    escapes:
        \& = &
        \: = :
        \\ = \
        \% = %      
        \$ = $
        \? = ?
        \= = =  
    
### Python Library
    To INSTALL:
        sudo python setup.py install
    To Use:
        see use.py
