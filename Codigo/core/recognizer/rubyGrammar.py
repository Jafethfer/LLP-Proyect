# -*- coding: utf-8 -*-
"""
    ! Gramaticas terminadas:
    ? Strings, booleanos, ints, floats
    ? Asignación de variables, Método puts
    ? Condicional if
    ? Bucles for y while
    ? Comentarios (Revisar)
    ? Comparaciones
    ? Operaciones aritméticas
    ? Definicion de funcion
    ? Gramatica de llamado a funcion
    ? Concatenacion en strings.
"""


rubyGrammar = """

    //Initial axiom
    ?start : exp+

    //Definition of an expresion
    ?exp : var "=" string -> assignvar
        | var "=" boolean -> assignvar
        | var "=" NONE -> assignvar
        | var "=" arithmeticoperation 
        | "puts" "("? string ")"? 
        | "puts" "("? string "%" "["? params "]"? ")"? 
        | "puts" "("? var ")"? 
        | arithmeticoperation
	    | conditional
        | loop
        | definefunction
        | callfunction
        | return  

    //Definition of an arithmeticoperation
    ?arithmeticoperation: arithmeticoperationatom
        | arithmeticoperation "+" arithmeticoperationatom 
        | arithmeticoperation "-" arithmeticoperationatom 
        | arithmeticoperation "*" arithmeticoperationatom 
        | arithmeticoperation "/" arithmeticoperationatom 

    //Definition of an arithmeticoperationatom
    ?arithmeticoperationatom: var -> getvar
        | number
        | "-" arithmeticoperation
        | "(" arithmeticoperation ")"
    
    //Definition of return
    ?return: "return" string
        | "return" number
        | "return" boolean
        | "return" NONE

    //Definition of definefunction
    ?definefunction: "def" var "("?  params ")"? instruction END -> createfunction

    //Definition of callfunction
    ?callfunction: var "(" params ")" -> callfunction

    //Definition of params
    ?params: string
        | number
        | var
        | callfunction
        | string "," params
        | number "," params
        | var "," params
        | callfunction "," params

    //Definition of loop
    ?loop: for
        | while

    //Definition of for
    ?for: "for" var "in" "(" int ".." int ")" instruction END

    //Definition of while   
    ?while: "while" "("? condition ")"? instruction END

    //Definition of conditional  
    ?conditional: "if" "("? condition ")"? instruction END

    //Definition of conditionn
    ?condition: var compare var
        | var compare number
        | var equals boolean
        | var equals string
        | string equals string
        | number compare number

    //Definition of compare     
    ?compare: ">"
        | "<"
        | "<="
        | ">="
        | equals

    //Definition of equals   
    ?equals: "=="
    
    //Definition of instruction
    ?instruction: exp*
        | /[^(END)]/*
    
    END: "end"
    
    // Definition of string
    ?string: /"[^"]*"/
        | /'[^']*'/
        
    
    // Definition of var
    ?var: /[a-zA-Z]\w*/

    NONE: "None"

    // Definition of number
    ?number: int
        | float

    //Definition of int
    ?int: /\d+/

    //Definition of float
    ?float: /\d+(\.\d+)/

    //Definition of boolean
    ?boolean: /[(True)|(False)]/
    	
    //Definition of COMMENT
    COMMENT: "#" /[^\\n]/*
        | OPEN /[^(CLOSE)]/* CLOSE
    
    OPEN: /\// "comment"
    
    CLOSE: "uncomment" /\//

    //Ignore COMMENT  
    %ignore COMMENT

    //Ignore spaces
    %ignore /\s+/

"""