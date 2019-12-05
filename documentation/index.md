

## Expression Trees

If the parser is able to understand what a student has typed, then it produces an *expression tree* of what they have typed.

An expression tree is a *collection of linked nodes*. Each node represents an **operand** (like a variable or a number) or an **operation** (like addition or subtraction) or simply a **group of operands**.

For example, the image below shows an expression tree for 'a+b'.

![](example-1.png)

The green nodes represent the identifiers *a* and *b*. 

*a* and *b* are operands in an *addition* operation, so they are subnodes of the red *addition* node.

Addition is a binary operation ('binary' meaning that it has two operands). Any other binary operation can be represented in the same way. The image below shows an expression tree for 'a*b'.

![](example-2.png)

An operation can in itself be an operand of *another* operation, as shown in the following expression tree.

![](example-3.png)

This expression tree shows the number 2 and the identifier *p* as operands of a *multiplication* operation, which is then the first operand of an *addition* operation. This expression tree is represented in plain text as '2*p+c'.

Notice how the expression tree retains information about the Order Of Operations (BODMAS). In the above expression tree, the 2 and the *p* are multiplied first, and the result of that operation is what becomes the first operand in the addition. This is essential for parsing mathematical notation.

Expression trees can be used to represent very complex expressions. The image below shows the expression tree for '3x^2+2x+5'

![](example-4.png)

Lots of different things can be considered to be operations. Functions can be considered to be operations, where the parameters of the function are the operands.

![](example-5.png)

Radicals can also be considered to be a type of operation.

![](example-6.png)