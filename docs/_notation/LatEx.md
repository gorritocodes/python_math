# Latex

To typeset custom operators, you can use the \operatorname and \operatorname\*

<!-- there are also superscripts and subscripts -->

The modulus operator is displayed using the \bmod and \pmod commands:

$`a \bmod b`$

$`a \pmod {b}`$

$`x \equiv a \pmod{b}`$

Custom operators Although many common operators are available in LaTeX,
sometimes you will need to write your own, e.g. to typeset the argmax operator.
The \operatorname and \operatorname* commands[1] display custom operators; the *
version sets the underscored option underneath like the \lim operator:

```math
\operatorname* {arg\,max}_a f(a)
\\
\arg\max_a f(a) = \arg\max_bf(b) \\
{\displaystyle \operatorname {arg\,max}
_{a}f(a)={\underset {b}{\operatorname {arg\,max} }}f(b)}
```

However, if the operator is frequently used, it is preferable to define a new
operator that can be used throughout the entire document. The
\DeclareMathOperator and \DeclareMathOperator\* commands[1] are specified in the
header of the document:

\DeclareMathOperator\*{\argmax}{arg\,max} This defines a new command which may
be referred to in the body:

```math
\[
 \argmax_c f(c)
\]
```

## Other symbols

| Symbol name | Symbol       | Script     |
| ----------- | ------------ | ---------- |
| forall      | $`\forall`$  | `\forall`  |
| in          | $`\in`$      | `\in`      |
| quad        | $`\quad`$    | `\quad`    |
| exists      | $`\exists`$  | `\exists`  |
| geq         | $`\geq`$     | `\geq`     |
| leq         | $`\leq`$     | `\leq`     |
| partial     | $`\partial`$ | `\partial` |
| eth         | $`\eth`$     | `\eth`     |
| hbar        | $`\hbar`$    | `hbar`     |
| imath       | $`\imath`$   | `imath`    |
| jmath       | $`\ell`$     | `\ell`     |
| re          | $`\Re`$      | `\Re`      |
| Im          | $`\Im`$      | `\Im`      |
| wp          | $`\wp`$      | `\wp`      |
| nabla       | $`\nabla`$   | `\nabla`   |
| Box         | $`\Box`$     | `\Box`     |
| infinity    | $`\infty`$   | `\infty`   |

Operators An operator is a function that is written as a word: e.g.
trigonometric functions (sin, cos, tan), logarithms and exponentials (log, exp),
limits (lim), as well as trace and determinant (tr, det). LaTeX has many of
these defined as commands:

\cos (2\theta) = \cos^2 \theta - \sin^2 \theta cos ⁡ ( 2 θ ) = cos 2 ⁡ θ − sin 2
⁡ θ {\displaystyle \cos(2\theta )=\cos ^{2}\theta -\sin ^{2}\theta \,}

For certain operators such as limits, the subscript is placed underneath the
operator:

\lim\limits*{x \to \infty} \exp(-x) = 0 lim x → ∞ exp ⁡ ( − x ) = 0
{\displaystyle \lim *{x\to \infty }\exp(-x)=0}

For the modular operator there are two commands: \bmod and \pmod:

a \bmod b a mod b {\displaystyle a\,{\bmod {\,}}b\,}

x \equiv a \pmod{b} x ≡ a ( mod b ) {\displaystyle x\equiv a{\pmod {b}}\,}

To use operators that are not pre-defined, such as argmax, see custom operators

Powers and indices Powers and indices are equivalent to superscripts and
subscripts in normal text mode. The caret (^; also known as the circumflex
accent) character is used to raise something, and the underscore (\_) is for
lowering. If an expression containing more than one character is raised or
lowered, it should be grouped using curly braces ({ and }).

k*{n+1} = n^2 + k_n^2 - k*{n-1} k n

-   # 1
    n 2
-   k n 2 − k n − 1 {\displaystyle k*{n+1}=n^{2}+k*{n}^{2}-k\_{n-1}\,}

For powers with more than one digit, surround the power with {}.

x^{1.01} x 1.01 {\displaystyle x^{1.01}\,}

An underscore (\_) can be used with a vertical bar ( | {\displaystyle |}) to
denote evaluation using subscript notation in mathematics:

f(n) = n^5 + 4n^2 + 2 |\_{n=17} f ( n ) = n 5

-   4 n 2
-   2 | n = 17 {\displaystyle f(n)=n^{5}+4n^{2}+2|\_{n=17}\,}

Fractions and Binomials A fraction is created using the
\frac{numerator}{denominator} command (for those who need their memories
refreshed, that's the top and bottom respectively!). Likewise, the binomial
coefficient (a.k.a, the Choose function) may be written using the \binom
command:[note 1]

\frac{n!}{k!(n-k)!} = \binom{n}{k} n ! k ! ( n − k ) ! = ( n k ) {\displaystyle
{\frac {n!}{k!(n-k)!}}={\binom {n}{k}}}

You can embed fractions within fractions:

\frac{\frac{1}{x}+\frac{1}{y}}{y-z} 1 x

-   1 y y − z {\displaystyle {\frac {{\frac {1}{x}}+{\frac {1}{y}}}{y-z}}}

Note that when appearing inside another fraction, or in inline text a b
{\displaystyle {\tfrac {a}{b}}}, a fraction is noticeably smaller than in
displayed mathematics. The \tfrac and \dfrac commands[note 1] force the use of
the respective styles, \textstyle and \displaystyle. Similarly, the \tbinom and
\dbinom commands typeset the binomial coefficient.

For relatively simple fractions, especially within the text, it may be more
aesthetically pleasing to use powers and indices instead:

^3/_7 3 / 7 {\displaystyle ^{3}/_{7}\,}

If this looks a little "loose" (i.e., overspaced), a tightened version can be
defined by inserting some negative space

%running fraction with slash - requires math mode.
\newcommand\*\rfrac[2]{{}^{#1}\!/_{#2}}

\rfrac{3}{7} 3 / 7 {\displaystyle {{}^{3}\!/_{7}}}

If you use them throughout the document, usage of xfrac package is recommended.
This package provides \sfrac command to create slanted fractions. Usage:

Take $\sfrac{1}{2}$ cup of sugar, \dots

3\times\sfrac{1}{2}=1\sfrac{1}{2}

Take ${}^1/_2$ cup of sugar, \dots

3\times{}^1/\_2=1{}^1/\_2

If fractions are used as an exponent, curly braces have to be used around the
\sfrac command:

$x^\frac{1}{2}$ % no error $x^\sfrac{1}{2}$ % error $x^{\sfrac{1}{2}}$ % no
error $x^\frac{1}{2}$ % no error t 1 2 {\displaystyle t^{\frac {1}{2}}}

In some cases, using the package alone will result in errors about certain font
shapes not being available. In that case, the lmodern and fix-cm packages need
to be added as well.

Alternatively, the nicefrac package provides the \nicefrac command, whose usage
is similar to \sfrac.

Continued fractions Continued fractions should be written using \cfrac
command:[note 1]

\begin{equation} x = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 +
\cfrac{1}{a_4} } } } \end{equation} x = a 0

-   1 a 1
-   1 a 2
-   1 a 3
-   1 a 4 {\displaystyle x=a*{0}+{\cfrac {1}{a*{1}+{\cfrac {1}{a*{2}+{\cfrac
    {1}{a*{3}+{\cfrac {1}{a\_{4}}}}}}}}}}

Multiplication of two numbers To make multiplication visually similar to a
fraction, a nested array can be used. For example, multiplication of numbers
written one below the other can be typeset as follows:

\begin{equation} \frac{ \begin{array}[b]{r} \left( x*1 x_2 \right)\\ \times
\left( x'\_1 x'\_2 \right) \end{array} }{ \left( y_1y_2y_3y_4 \right) }
\end{equation} ( x 1 x 2 ) × ( x 1 ′ x 2 ′ ) ( y 1 y 2 y 3 y 4 ) {\displaystyle
{\frac {\begin{array}{r}\left(x*{1}x*{2}\right)\\\times
\left(x'*{1}x'_{2}\right)\end{array}}{\left(y_{1}y*{2}y*{3}y\_{4}\right)}}}

Roots The \sqrt command creates a square root surrounding an expression. It
accepts an optional argument specified in square brackets ([ and ]) to change
magnitude:

\sqrt{\frac{a}{b}} a b {\displaystyle {\sqrt {\frac {a}{b}}}}

\sqrt[n]{1+x+x^2+x^3+\dots+x^n} 1

-   x
-   x 2
-   x 3
-   ⋯
-   x n n {\displaystyle {\sqrt[{n}]{1+x+x^{2}+x^{3}+\dots +x^{n}}}}

Some people prefer writing the square root "closing" it over its content. This
method arguably makes it more clear what is in the scope of the root sign. This
habit is not normally used while writing with the computer, but if you still
want to change the output of the square root, LaTeX gives you this possibility.
Just add the following code in the preamble of your document:

% New definition of square root: % it renames \sqrt as \oldsqrt
\let\oldsqrt\sqrt % it defines the new \sqrt in terms of the old one
\def\sqrt{\mathpalette\DHLhksqrt} \def\DHLhksqrt#1#2{%
\setbox0=\hbox{$#1\oldsqrt{#2\,}$}\dimen0=\ht0 \advance\dimen0-0.2\ht0
\setbox2=\hbox{\vrule height\ht0 depth -\dimen0}% {\box0\lower0.4pt\box2}}

The new style is on left, the old one on right This TeX code first renames the
\sqrt command as \oldsqrt, then redefines \sqrt in terms of the old one, adding
something more. The new square root can be seen in the picture on the left,
compared to the old one on the right. Unfortunately this code won't work if you
want to use multiple roots: if you try to write a b {\displaystyle
{\sqrt[{b}]{a}}} as \sqrt[b]{a} after you used the code above, you'll just get a
wrong output. In other words, you can redefine the square root this way only if
you are not going to use multiple roots in the whole document.

An alternative piece of TeX code that does allow multiple roots is

\usepackage{letltxmacro} \makeatletter \let\oldr@@t\r@@t \def\r@@t#1#2{%
\setbox0=\hbox{$\oldr@@t#1{#2\,}$}\dimen0=\ht0 \advance\dimen0-0.2\ht0
\setbox2=\hbox{\vrule height\ht0 depth -\dimen0}% {\box0\lower0.4pt\box2}}
\LetLtxMacro{\oldsqrt}{\sqrt} \renewcommand\*{\sqrt}[2][\ ]{\oldsqrt[#1]{#2} }
\makeatother

$\sqrt[a]{b} \quad \oldsqrt[a]{b}$

However, this requires the \usepackage{letltxmacro} package.

Sums and integrals The \sum and \int commands insert the sum and integral
symbols respectively, with limits specified using the caret (^) and underscore
(\_). The typical notation for sums is:

\sum*{i=1}^{10} t_i ∑ i = 1 10 t i {\displaystyle \textstyle \sum
*{i=1}^{10}t\_{i}\,}

or

\displaystyle\sum*{i=1}^{10} t_i ∑ i = 1 10 t i {\displaystyle \displaystyle
\sum *{i=1}^{10}t\_{i}\,}

The limits for the integrals follow the same notation. It's also important to
represent the integration variables with an upright d {\displaystyle \mathrm {d}
}, which in math mode is obtained through the \mathrm{} command, and with a
small space separating it from the integrand, which is attained with the \,
command.

\int*0^\infty \mathrm{e}^{-x}\,\mathrm{d}x ∫ 0 ∞ e − x d x {\displaystyle \int
*{0}^{\infty }\mathrm {e} ^{-x}\,\mathrm {d} x\,}

There are many other "big" commands which operate in a similar manner:

\sum ∑ {\displaystyle \sum \,} \prod ∏ {\displaystyle \prod } \coprod ∐
{\displaystyle \coprod } \bigoplus ⨁ {\displaystyle \bigoplus } \bigotimes ⨂
{\displaystyle \bigotimes } \bigodot ⨀ {\displaystyle \bigodot } \bigcup ⋃
{\displaystyle \bigcup } \bigcap ⋂ {\displaystyle \bigcap } \biguplus ⨄
{\displaystyle \biguplus } \bigsqcup ⨆ {\displaystyle \bigsqcup } \bigvee ⋁
{\displaystyle \bigvee } \bigwedge ⋀ {\displaystyle \bigwedge } \int ∫
{\displaystyle \int } \oint ∮ {\displaystyle \oint } \iint[note 1] ∬
{\displaystyle \iint } \iiint[note 1] ∭ {\displaystyle \iiint } \iiiint[note 1]
⨌ {\displaystyle \iiiint } \idotsint[note 1] ∫ ⋯ ∫ {\displaystyle \int \!\cdots
\!\int } For more integral symbols, including those not included by default in
the Computer Modern font, try the esint package.

The \substack command[note 1] allows the use of \\ to write the limits over
multiple lines:

\sum*{\substack{ 0<i<m \\ 0<j<n }} P(i,j) ∑ 0 < j < n 0 < i < m P ( i , j )
{\displaystyle \sum *{\overset {\scriptstyle 0<i<m}{\scriptstyle
0<j<n}}P(i,j)\,}

If you want the limits of an integral to be specified above and below the symbol
(like the sum), use the \limits command:

\int\limits*a^b ∫ b c {\displaystyle \int \limits *{b}^{c}\,}

However, if you want this to apply to all integrals, it is preferable to specify
the intlimits option when loading the amsmath package:

\usepackage[intlimits]{amsmath} Subscripts and superscripts in other contexts,
as well as other parameters to amsmath package related to them, are described in
Advanced Mathematics chapter.

For bigger integrals, you may use personal declarations, or the bigints package
[3].

Brackets, braces and delimiters How to use braces in multi line equations is
described in the Advanced Mathematics chapter.

The use of delimiters such as brackets soon becomes important when dealing with
anything but the most trivial equations. Without them, formulas can become
ambiguous. Also, special types of mathematical structures, such as matrices,
typically rely on delimiters to enclose them.

There are a variety of delimiters available for use in LaTeX:

( a ), [ b ], \{ c \}, | d |, \| e \|, \langle f \rangle, \lfloor g \rfloor,
\lceil h \rceil, \ulcorner i \urcorner, / j \backslash ( a ) , [ b ] , { c } , |
d | , ‖ e ‖ , ⟨ f ⟩ , ⌊ g ⌋ , ⌈ h ⌉ , ⌜ i ⌝ , / j ∖ {\displaystyle
(a),[b],\{c\},|d|,\|e\|,\langle f\rangle ,\lfloor g\rfloor ,\lceil h\rceil
,\ulcorner i\urcorner ,/j\backslash }

where \lbrack and \rbrack may be used in place of [ and ].

Automatic sizing Very often, mathematical features will differ in size, in which
case the delimiters surrounding the expression should vary accordingly. This can
be done automatically using the \left, \right, and \middle commands. Any of the
previous delimiters may be used in combination with these:

\left(\frac{x^2}{y^3}\right) ( x 2 y 3 ) {\displaystyle \left({\frac
{x^{2}}{y^{3}}}\right)\,}

P\left(A=2\middle|\frac{A^2}{B}>4\right)

Curly braces are defined differently by using \left\{ and \right\},

\left\{\frac{x^2}{y^3}\right\} { x 2 y 3 } {\displaystyle \left\{{\frac
{x^{2}}{y^{3}}}\right\}\,}

If a delimiter on only one side of an expression is required, then an invisible
delimiter on the other side may be denoted using a period (.).

\left.\frac{x^3}{3}\right|_0^1 x 3 3 | 0 1 {\displaystyle \left.{\frac
{x^{3}}{3}}\right|_{0}^{1}\,}

Manual sizing In certain cases, the sizing produced by the \left and \right
commands may not be desirable, or you may simply want finer control over the
delimiter sizes. In this case, the \big, \Big, \bigg and \Bigg modifier commands
may be used:

( \big( \Big( \bigg( \Bigg( ( ( ( ( ( {\displaystyle ({\big (}{\Big (}{\bigg
(}{\Bigg (}\,}

These commands are primarily useful when dealing with nested delimiters. For
example, when typesetting

\frac{\mathrm d}{\mathrm d x} \left( k g(x) \right) d d x ( k g ( x ) )
{\displaystyle {\frac {\mathrm {d} }{\mathrm {d} x}}\left(kg(x)\right)}

we notice that the \left and \right commands produce the same size delimiters as
those nested within it. This can be difficult to read. To fix this, we write

\frac{\mathrm d}{\mathrm d x} \big( k g(x) \big) d d x ( k g ( x ) )
{\displaystyle {\frac {\mathrm {d} }{\mathrm {d} x}}{\big (}kg(x){\big )}}

Manual sizing can also be useful when an equation is too large, trails off the
end of the page, and must be separated into two lines using an align command.
Although the commands \left. and \right. can be used to balance the delimiters
on each line, this may lead to wrong delimiter sizes. Furthermore, manual sizing
can be used to avoid overly large delimiters — if an \underbrace or a similar
command appears between the delimiters.

Matrices and arrays A basic matrix may be created using the matrix
environment[note 1]: in common with other table-like structures, entries are
specified by row, with columns separated using an ampersand (&) and new rows
separated with a double backslash (\\)

\[ \begin{matrix} a & b & c \\ d & e & f \\ g & h & i \end{matrix} \] a b c d e
f g h i {\displaystyle {\begin{matrix}a&b&c\\d&e&f\\g&h&i\end{matrix}}}

To specify alignment of columns in the table, use starred version[note 2]:

\begin{matrix} -1 & 3 \\ 2 & -4 \end{matrix} = \begin{matrix*}[r] -1 & 3 \\ 2 &
-4 \end{matrix*} − 1 3 2 − 4 = − 1 3 2 − 4 {\displaystyle
{\begin{matrix}-1&3\\2&-4\end{matrix}}={\begin{matrix}-1&\,\;\;3\\\,\;\;2&-4\end{matrix}}}

The alignment by default is c, but it can be any column type valid in array
environment.

However matrices are usually enclosed in delimiters of some kind, and while it
is possible to use the \left and \right commands, there are various other
predefined environments which automatically include delimiters:

Environment name Surrounding delimiter Notes pmatrix[note 1] ( ) {\displaystyle
(\,)} centers columns by default pmatrix*[note 2] ( ) {\displaystyle (\,)}
allows to specify alignment of columns in optional parameter bmatrix[note 1] [ ]
{\displaystyle [\,]} centers columns by default bmatrix*[note 2] [ ]
{\displaystyle [\,]} allows to specify alignment of columns in optional
parameter Bmatrix[note 1] { } {\displaystyle \{\,\}} centers columns by default
Bmatrix*[note 2] { } {\displaystyle \{\,\}} allows to specify alignment of
columns in optional parameter vmatrix[note 1] | | {\displaystyle |\,|} centers
columns by default vmatrix*[note 2] | | {\displaystyle |\,|} allows to specify
alignment of columns in optional parameter Vmatrix[note 1] ‖ ‖ {\displaystyle
\|\,\|} centers columns by default Vmatrix\*[note 2] ‖ ‖ {\displaystyle \|\,\|}
allows to specify alignment of columns in optional parameter When writing down
arbitrary sized matrices, it is common to use horizontal, vertical and diagonal
triplets of dots (known as ellipses) to fill in certain columns and rows. These
can be specified using the \cdots, \vdots and \ddots respectively:

A*{m,n} = \begin{pmatrix} a*{1,1} & a*{1,2} & \cdots & a*{1,n} \\ a*{2,1} &
a*{2,2} & \cdots & a*{2,n} \\ \vdots & \vdots & \ddots & \vdots \\ a*{m,1} &
a*{m,2} & \cdots & a*{m,n} \end{pmatrix} A m , n = ( a 1 , 1 a 1 , 2 ⋯ a 1 , n a
2 , 1 a 2 , 2 ⋯ a 2 , n ⋮ ⋮ ⋱ ⋮ a m , 1 a m , 2 ⋯ a m , n ) {\displaystyle
A*{m,n}={\begin{pmatrix}a*{1,1}&a*{1,2}&\cdots &a*{1,n}\\a*{2,1}&a*{2,2}&\cdots
&a*{2,n}\\\vdots &\vdots &\ddots &\vdots \\a*{m,1}&a*{m,2}&\cdots
&a*{m,n}\end{pmatrix}}}

In some cases, you may want to have finer control of the alignment within each
column, or to insert lines between columns or rows. This can be achieved using
the array environment, which is essentially a math-mode version of the tabular
environment, which requires that the columns be pre-specified:

\begin{array}{c|c} 1 & 2 \\ \hline 3 & 4 \end{array} 1 2 3 4 {\displaystyle
{\begin{array}{c|c}1&2\\\hline 3&4\end{array}}}

You may see that the AMS matrix class of environments doesn't leave enough space
when used together with fractions resulting in output similar to this:

# M

[ 5 6 1 6 0 5 6 0 1 6 0 5 6 1 6 ] {\displaystyle M={\begin{bmatrix}{\frac
{5}{6}}&{\frac {1}{6}}&0\\{\frac {5}{6}}&0&{\frac {1}{6}}\\0&{\frac
{5}{6}}&{\frac {1}{6}}\end{bmatrix}}}

To counteract this problem, add additional leading space with the optional
parameter to the \\ command:

M = \begin{bmatrix} \frac{5}{6} & \frac{1}{6} & 0 \\[0.3em] \frac{5}{6} & 0 &
\frac{1}{6} \\[0.3em] 0 & \frac{5}{6} & \frac{1}{6} \end{bmatrix} M = [ 5 6 1 6
0 5 6 0 1 6 0 5 6 1 6 ] {\displaystyle M={\begin{bmatrix}{\frac {5}{6}}&{\frac
{1}{6}}&0\\[0.3em]{\frac {5}{6}}&0&{\frac {1}{6}}\\[0.3em]0&{\frac
{5}{6}}&{\frac {1}{6}}\end{bmatrix}}}

If you need "border" or "indexes" on your matrix, plain TeX provides the macro
\bordermatrix

M = \bordermatrix{~ & x & y \cr A & 1 & 0 \cr B & 0 & 1 \cr}

Matrices in running text To insert a small matrix without increasing leading in
the line containing it, use smallmatrix environment:

A matrix in text must be set smaller:
$\bigl(\begin{smallmatrix}
a&b \\ c&d
\end{smallmatrix} \bigr)$ to not increase
leading in a portion of text.

Adding text to equations The math environment differs from the text environment
in the representation of text. Here is an example of trying to represent text
within the math environment:

50 apples \times 100 apples = lots of apples^2 50 a p p l e s × 100 a p p l e s
= l o t s o f a p p l e s 2 {\displaystyle 50apples\times
100apples=lotsofapples^{2}\,}

There are two noticeable problems: there are no spaces between words or numbers,
and the letters are italicized and more spaced out than normal. Both issues are
simply artifacts of the maths mode, in that it treats it as a mathematical
expression: spaces are ignored (LaTeX spaces mathematics according to its own
rules), and each character is a separate element (so are not positioned as
closely as normal text).

There are a number of ways that text can be added properly. The typical way is
to wrap the text with the \text{...} command[note 1] (a similar command is
\mbox{...}, though this causes problems with subscripts, and has a less
descriptive name). Let's see what happens when the above equation code is
adapted:

50 \text{apples} \times 100 \text{apples} = \text{lots of apples}^2 50 apples ×
100 apples = lots of apples 2 {\displaystyle 50{\text{apples}}\times
100{\text{apples}}={\text{lots of apples}}^{2}\,}

The text looks better. However, there are no gaps between the numbers and the
words. Unfortunately, you are required to explicitly add these. There are many
ways to add spaces between math elements, but for the sake of simplicity we may
simply insert space characters into the \text commands.

50 \text{ apples} \times 100 \text{ apples} = \text{lots of apples}^2 50 apples
× 100 apples = lots of apples 2 {\displaystyle 50{\text{ apples}}\times
100{\text{ apples}}={\text{lots of apples}}^{2}\,}

Formatted text Using the \text is fine and gets the basic result. Yet, there is
an alternative that offers a little more flexibility. You may recall the
introduction of font formatting commands, such as \textrm, \textit, \textbf,
etc. These commands format the argument accordingly, e.g., \textbf{bold text}
gives bold text. These commands are equally valid within a maths environment to
include text. The added benefit here is that you can have better control over
the font formatting, rather than the standard text achieved with \text.

50 \textrm{ apples} \times 100 \textbf{ apples} = \textit{lots of apples}^2 50
apples × 100 apples = lotsofapples 2 {\displaystyle 50\;{\textrm {apples}}\times
100\;{\textbf {apples}}={\textit {lotsofapples}}^{2}\,}

Formatting mathematics symbols See also: w:Mathematical Alphanumeric Symbols,
w:Help:Displaying a formula#Alphabets and typefaces and w:Wikipedia:LaTeX
symbols#Fonts We can now format text; what about formatting mathematical
expressions? There are a set of formatting commands very similar to the font
formatting ones just used, except that they are specifically aimed at text in
math mode (requires amsfonts)

LaTeX command Sample Description Common use \mathnormal{…} (or simply omit any
command) A B C D E F

a b c d e f

123456 {\displaystyle ABCDEF~abcdef~123456\,} The default math font Most
mathematical notation \mathrm{…} A B C D E F

a b c d e f

123456 {\displaystyle \mathrm {ABCDEF~abcdef~123456} \,} This is the default or
normal font, unitalicised Units of measurement, one word functions \mathit{…} A
B C D E F

a b c d e f

123456 {\displaystyle {\mathit {ABCDEF~abcdef~123456}}\,} Italicised font
Multi-letter function or variable names. Compared to \mathnormal, words are
spaced more naturally and numbers are italicized as well. \mathbf{…} A B C D E F

a b c d e f

123456 {\displaystyle \mathbf {ABCDEF~abcdef~123456} \,} Bold font Vectors
\mathsf{…} A B C D E F

a b c d e f

123456 {\displaystyle {\mathsf {ABCDEF~abcdef~123456}}\,} Sans-serif Categories
\mathtt{…} A B C D E F

a b c d e f

123456 {\displaystyle {\mathtt {ABCDEF~abcdef~123456}}\,} Monospace
(fixed-width) font \mathfrak{…} (requires the amsfonts or amssymb package[note
3]) A B C D E F

a b c d e f

123456 {\displaystyle {\mathfrak {ABCDEF~abcdef~123456}}\,} Fraktur Almost
canonical font for Lie algebras, ideals in ring theory \mathcal{…} A B C D E F
{\displaystyle {\mathcal {ABCDEF}}\,} Calligraphy (uppercase only[note 3]) Often
used for sheaves/schemes and categories, used to denote cryptological concepts
like an alphabet of definition ( A {\displaystyle {\mathcal {A}}}), message
space ( M {\displaystyle {\mathcal {M}}}), ciphertext space ( C {\displaystyle
{\mathcal {C}}}) and key space ( K {\displaystyle {\mathcal {K}}}); Kleene's O
{\displaystyle {\mathcal {O}}}; naming convention in description logic; Laplace
transform ( L {\displaystyle {\mathcal {L}}}) and Fourier transform ( F
{\displaystyle {\mathcal {F}}}) \mathbb{…} (requires the amsfonts or amssymb
package[note 3]) A B C D E F {\displaystyle \mathbb {ABCDEF} \,} Blackboard bold
(uppercase only[note 3]) Used to denote special sets (e.g. real numbers)
\mathscr{…} (requires the mathrsfs package[note 3]) Script (uppercase only[note
3]) An alternative font for categories and sheaves. These formatting commands
can be wrapped around the entire equation, and not just on the textual elements:
they only format letters, numbers, and uppercase Greek, and other math commands
are unaffected.

To bold lowercase Greek or other symbols use the \boldsymbol command[note 1];
this will only work if there exists a bold version of the symbol in the current
font. As a last resort there is the \pmb command[note 1] (poor man's bold): this
prints multiple versions of the character slightly offset against each other.

\boldsymbol{\beta} = (\beta*1,\beta_2,\dotsc,\beta_n) β = ( β 1 , β 2 , … , β n
) {\displaystyle {\boldsymbol {\beta }}=(\beta *{1},\beta _{2},\dotsc ,\beta
_{n})\,}

To change the size of the fonts in math mode, see Changing font size.

Accents So what to do when you run out of symbols and fonts? Well, the next step
is to use accents:

a' or a^{\prime} a ′ {\displaystyle a'\,} a'' a ″ {\displaystyle a''\,} \hat{a}
a ^ {\displaystyle {\hat {a}}\,} \bar{a} a ¯ {\displaystyle {\bar {a}}\,}
\grave{a} a ` {\displaystyle {\grave {a}}\,} \acute{a} a ´ {\displaystyle
{\acute {a}}\,} \dot{a} a ˙ {\displaystyle {\dot {a}}\,} \ddot{a} a ¨
{\displaystyle {\ddot {a}}\,} \not{a} ⧸ a {\displaystyle \not {a}\,}
\mathring{a} å \overrightarrow{AB} A B → {\displaystyle {\overrightarrow
{AB}}\,} \overleftarrow{AB} A B ← {\displaystyle {\overleftarrow {AB}}\,} a''' a
‴ {\displaystyle a'''\,} a'''' a ⁗ {\displaystyle a''''\,} \overline{aaa} a a a
¯ {\displaystyle {\overline {aaa}}\,} \check{a} a ˇ {\displaystyle {\check
{a}}\,} \breve{a} a ˘ {\displaystyle {\breve {a}}\,} \vec{a} a → {\displaystyle
{\vec {a}}\,} \dddot{a}[note 1] \ddddot{a}[note 1] \widehat{AAA} A A A ^
{\displaystyle {\widehat {AAA}}\,} \widetilde{AAA} A A A ~ {\displaystyle
{\widetilde {AAA}}} \stackrel\frown{AAA} A A A ⌢ {\displaystyle {\stackrel
{\frown }{AAA}}} \tilde{a} a ~ {\displaystyle {\tilde {a}}\,} \underline{a} a \_
{\displaystyle {\underline {a}}\,} Color The package xcolor, described in
Colors, allows us to add color to our equations. For example,

k = {\color{red}x} \mathbin{\color{blue}-} 2 k = x − 2 {\displaystyle k={\color
{red}x}{\mathbin {\color {blue}-}}2}

The only problem is that this disrupts the default LaTeX formatting around the -
operator. To fix this, we enclose it in a \mathbin environment, since - is a
binary operator. This process is described here.

Plus and minus signs LaTeX deals with the + and − signs in two possible ways.
The most common is as a binary operator. When two maths elements appear on
either side of the sign, it is assumed to be a binary operator, and as such,
allocates some space to either side of the sign. The alternative way is a sign
designation. This is when you state whether a mathematical quantity is either
positive or negative. This is common for the latter, as in math, such elements
are assumed to be positive unless a − is prefixed to it. In this instance, you
want the sign to appear close to the appropriate element to show their
association. If you put a + or a − with nothing before it but you want it to be
handled like a binary operator you can add an invisible character before the
operator using {}. This can be useful if you are writing multiple-line formulas,
and a new line could start with a − or +, for example, then you can fix some
strange alignments adding the invisible character where necessary.

A plus-minus sign is written as:

\pm ± {\displaystyle \pm }

Similarly, there exists also a minus-plus sign:

\mp ∓ {\displaystyle \mp }

Controlling horizontal spacing LaTeX is obviously pretty good at typesetting
maths—it was one of the chief aims of the core TeX system that LaTeX extends.
However, it can't always be relied upon to accurately interpret formulas in the
way you did. It has to make certain assumptions when there are ambiguous
expressions. The result tends to be slightly incorrect horizontal spacing. In
these events, the output is still satisfactory, yet any perfectionists will no
doubt wish to fine-tune their formulas to ensure spacing is correct. These are
generally very subtle adjustments.

There are other occasions where LaTeX has done its job correctly, but you just
want to add some space, maybe to add a comment of some kind. For example, in the
following equation, it is preferable to ensure there is a decent amount of space
between the maths and the text.

\[ f(n) = \begin{cases} n/2 & \quad \text{if } n \text{ is even}\\ -(n+1)/2 &
\quad \text{if } n \text{ is odd} \end{cases} \] f ( n ) = { n / 2 if n is even
− ( n

-   1 ) / 2 if n is odd {\displaystyle f(n)={\begin{cases}n/2&\quad {\text{if
    }}n{\text{ is even}}\\-(n+1)/2&\quad {\text{if }}n{\text{ is
    odd}}\end{cases}}}

This code produces errors with Miktex 2.9 and does not yield the results seen on
the right. Use \mathrm instead of just \text.

(Note that this particular example can be expressed in more elegant code by the
cases construct provided by the amsmath package described in Advanced
Mathematics chapter.)

LaTeX has defined two commands that can be used anywhere in documents (not just
maths) to insert some horizontal space. They are \quad and \qquad

A \quad is a space equal to the current font size. So, if you are using an 11pt
font, then the space provided by \quad will also be 11pt (horizontally, of
course.) The \qquad gives twice that amount. As you can see from the code from
the above example, \quads were used to add some separation between the maths and
the text.

OK, so back to the fine tuning as mentioned at the beginning of the document. A
good example would be displaying the simple equation for the indefinite integral
of y with respect to x:

∫ y d x {\displaystyle \int y\,\mathrm {d} x}

If you were to try this, you may write:

\int y \mathrm{d}x ∫ y d x {\displaystyle \int y\mathrm {d} x}

However, this doesn't give the correct result. LaTeX doesn't respect the
white-space left in the code to signify that the y and the dx are independent
entities. Instead, it lumps them altogether. A \quad would clearly be overkill
in this situation—what is needed are some small spaces to be utilized in this
type of instance, and that's what LaTeX provides:

Command Description Size \, small space 3/18 of a quad \: medium space 4/18 of a
quad \; large space 5/18 of a quad \! negative space -3/18 of a quad NB you can
use more than one command in a sequence to achieve a greater space if necessary.

So, to rectify the current problem:

\int y\, \mathrm{d}x ∫ y d x {\displaystyle \int y\,\mathrm {d} x}

\int y\: \mathrm{d}x ∫ y d x {\displaystyle \int y\;\;\!\!\mathrm {d} x}

\int y\; \mathrm{d}x ∫ y d x {\displaystyle \int y\;\mathrm {d} x}

The negative space may seem like an odd thing to use, however, it wouldn't be
there if it didn't have some use! Take the following example:

\left( \begin{array}{c} n \\ r \end{array} \right) = \frac{n!}{r!(n-r)!} ( n r )
= n ! r ! ( n − r ) ! {\displaystyle
\left({\begin{matrix}n\\r\end{matrix}}\right)={\frac {n!}{r!(n-r)!}}}

The matrix-like expression for representing binomial coefficients is too padded.
There is too much space between the brackets and the actual contents within.
This can easily be corrected by adding a few negative spaces after the left
bracket and before the right bracket.

\left(\! \begin{array}{c} n \\ r \end{array} \!\right) = \frac{n!}{r!(n-r)!} ( n
r ) = n ! r ! ( n − r ) ! {\displaystyle
\left(\!{\begin{matrix}n\\r\end{matrix}}\!\right)={\frac {n!}{r!(n-r)!}}}

In any case, adding some spaces manually should be avoided whenever possible: it
makes the source code more complex and it's against the basic principles of a
What You See is What You Mean approach. The best thing to do is to define some
commands using all the spaces you want and then, when you use your command, you
don't have to add any other space. Later, if you change your mind about the
length of the horizontal space, you can easily change it modifying only the
command you defined before. Let us use an example: you want the d of a dx in an
integral to be in roman font and a small space away from the rest. If you want
to type an integral like \int x \, \mathrm{d} x, you can define a command like
this:

\newcommand{\dd}{\mathop{}\,\mathrm{d}} in the preamble of your document. We
have chosen \dd just because it reminds the "d" it replaces and it is fast to
type. Doing so, the code for your integral becomes \int x \dd x. Now, whenever
you write an integral, you just have to use the \dd instead of the "d", and all
your integrals will have the same style. If you change your mind, you just have
to change the definition in the preamble, and all your integrals will be changed
accordingly.

Manually Specifying Formula Style To manually display a fragment of a formula
using text style, surround the fragment with curly braces and prefix the
fragment with \textstyle. The braces are required because the \textstyle macro
changes the state of the renderer, rendering all subsequent mathematics in text
style. The braces limit this change of state to just the fragment enclosed
within. For example, to use text style for just the summation symbol in a sum,
one would enter

\begin{equation} C^i_j = {\textstyle \sum_k} A^i_k B^k_j \end{equation} The same
thing as a command would look like this:

\newcommand{\tsum}[1]{{\textstyle \sum_{#1}}} Note the extra braces. Just one
set around the expression won't be enough. That would cause all math after \tsum
k to be displayed using text style.

To display part of a formula using display style, do the same thing, but use
\displaystyle instead.

Advanced Mathematics: AMS Math package The AMS (American Mathematical Society)
mathematics package is a powerful package that creates a higher layer of
abstraction over mathematical LaTeX language; if you use it it will make your
life easier. Some commands amsmath introduces will make other plain LaTeX
commands obsolete: in order to keep consistency in the final output you'd better
use amsmath commands whenever possible. If you do so, you will get an elegant
output without worrying about alignment and other details, keeping your source
code readable. If you want to use it, you have to add this in the preamble:

\usepackage{amsmath} Introducing dots in formulas amsmath defines also the \dots
command, that is a generalization of the existing \ldots. You can use \dots in
both text and math mode and LaTeX will replace it with three dots "…" but it
will decide according to the context whether to put it on the bottom (like
\ldots) or centered (like \cdots).

Dots LaTeX gives you several commands to insert dots (ellipses) in your
formulae. This can be particularly useful if you have to type big matrices
omitting elements. First of all, here are the main dots-related commands LaTeX
provides:

Code Output Comment \dots … {\displaystyle \dots } generic dots (ellipsis), to
be used in text (outside formulae as well). It automatically manages whitespaces
before and after itself according to the context, it's a higher level command.
\ldots … {\displaystyle \ldots } the output is similar to the previous one, but
there is no automatic whitespace management; it works at a lower level. \cdots ⋯
{\displaystyle \cdots } These dots are centered relative to the height of a
letter. There is also the binary multiplication operator, \cdot, mentioned
below. \vdots ⋮ {\displaystyle \vdots } vertical dots \ddots ⋱ {\displaystyle
\ddots } diagonal dots \iddots inverse diagonal dots (requires the mathdots
package) \hdotsfor{n} … … {\displaystyle \ldots \ldots } to be used in matrices,
it creates a row of dots spanning n columns. Instead of using \ldots and \cdots,
you should use the semantically oriented commands. It makes it possible to adapt
your document to different conventions on the fly, in case (for example) you
have to submit it to a publisher who insists on following house tradition in
this respect. The default treatment for the various kinds follows American
Mathematical Society conventions.

Code Output Comment A_1,A_2,\dotsc, for "dots with commas" A_1+\dotsb+A_N for
"dots with binary operators/relations" A_1 \dotsm A_N for "multiplication dots"
\int_a^b \dotsi for "dots with integrals" A_1\dotso A_N for "other dots" (none
of the above) Write an equation with the align environment How to write an
equation with the align environment with the amsmath package is described in
Advanced Mathematics.

List of mathematical symbols All the pre-defined mathematical symbols from the
\TeX\ package are listed below. More symbols are available from extra packages.

Relation Symbols Symbol Script Symbol Script Symbol Script Symbol Script Symbol
Script < {\displaystyle <\,} <

>

# {\displaystyle >\,} >

{\displaystyle =\,} = ∥ {\displaystyle \parallel \,} \parallel ∦ {\displaystyle
\nparallel \,} \nparallel ≤ {\displaystyle \leq \,} \leq ≥ {\displaystyle \geq
\,} \geq ≐ {\displaystyle \doteq \,} \doteq ≍ {\displaystyle \asymp \,} \asymp ⋈
{\displaystyle \bowtie \,} \bowtie ≪ {\displaystyle \ll \,} \ll ≫ {\displaystyle
\gg \,} \gg ≡ {\displaystyle \equiv \,} \equiv ⊢ {\displaystyle \vdash \,}
\vdash ⊣ {\displaystyle \dashv \,} \dashv ⊂ {\displaystyle \subset \,} \subset ⊃
{\displaystyle \supset \,} \supset ≈ {\displaystyle \approx \,} \approx ∈
{\displaystyle \in \,} \in ∋ {\displaystyle \ni \,} \ni ⊆ {\displaystyle
\subseteq \,} \subseteq ⊇ {\displaystyle \supseteq \,} \supseteq ≅
{\displaystyle \cong \,} \cong ⌣ {\displaystyle \smile \,} \smile ⌢
{\displaystyle \frown \,} \frown ⊈ {\displaystyle \nsubseteq \,} \nsubseteq ⊉
{\displaystyle \nsupseteq \,} \nsupseteq ≃ {\displaystyle \simeq \,} \simeq ⊨
{\displaystyle \models \,} \models ∉ {\displaystyle \notin \,} \notin ⊏
{\displaystyle \sqsubset \,} \sqsubset ⊐ {\displaystyle \sqsupset \,} \sqsupset
∼ {\displaystyle \sim \,} \sim ⊥ {\displaystyle \perp \,} \perp ∣ {\displaystyle
\mid \,} \mid ⊑ {\displaystyle \sqsubseteq \,} \sqsubseteq ⊒ {\displaystyle
\sqsupseteq \,} \sqsupseteq ∝ {\displaystyle \propto \,} \propto ≺
{\displaystyle \prec \,} \prec ≻ {\displaystyle \succ \,} \succ ⪯ {\displaystyle
\preceq \,} \preceq ⪰ {\displaystyle \succeq \,} \succeq ≠ {\displaystyle \neq
\,} \neq ∢ {\displaystyle \sphericalangle \,} \sphericalangle ∡ {\displaystyle
\measuredangle \,} \measuredangle ∴ {\displaystyle \therefore \,} \therefore ∵
{\displaystyle \because \,} \because Binary Operations Symbol Script Symbol
Script Symbol Script Symbol Script ± {\displaystyle \pm \,} \pm ∩ {\displaystyle
\cap \,} \cap ⋄ {\displaystyle \diamond \,} \diamond ⊕ {\displaystyle \oplus \,}
\oplus ∓ {\displaystyle \mp \,} \mp ∪ {\displaystyle \cup \,} \cup △
{\displaystyle \bigtriangleup \,} \bigtriangleup ⊖ {\displaystyle \ominus \,}
\ominus × {\displaystyle \times \,} \times ⊎ {\displaystyle \uplus \,} \uplus ▽
{\displaystyle \bigtriangledown \,} \bigtriangledown ⊗ {\displaystyle \otimes
\,} \otimes ÷ {\displaystyle \div \,} \div ⊓ {\displaystyle \sqcap \,} \sqcap ◃
{\displaystyle \triangleleft \,} \triangleleft ⊘ {\displaystyle \oslash \,}
\oslash ∗ {\displaystyle \ast \,} \ast ⊔ {\displaystyle \sqcup \,} \sqcup ▹
{\displaystyle \triangleright \,} \triangleright ⊙ {\displaystyle \odot \,}
\odot ⋆ {\displaystyle \star \,} \star ∨ {\displaystyle \vee \,} \vee ◯
{\displaystyle \bigcirc \,} \bigcirc ∘ {\displaystyle \circ \,} \circ †
{\displaystyle \dagger \,} \dagger ∧ {\displaystyle \wedge \,} \wedge ∙
{\displaystyle \bullet \,} \bullet ∖ {\displaystyle \setminus \,} \setminus ‡
{\displaystyle \ddagger \,} \ddagger ⋅ {\displaystyle \cdot \,} \cdot ≀
{\displaystyle \wr \,} \wr ⨿ {\displaystyle \amalg \,} \amalg Set and/or Logic
Notation Symbol Script Symbol Script ∃ {\displaystyle \exists \,} \exists →
{\displaystyle \rightarrow \,} \rightarrow or \to ∄ {\displaystyle \nexists \,}
\nexists ← {\displaystyle \leftarrow \,} \leftarrow or \gets ∀ {\displaystyle
\forall \,} \forall ↦ {\displaystyle \mapsto \,} \mapsto ¬ {\displaystyle \neg
\,} \neg ⟹ {\displaystyle \implies \,} \implies ∩ {\displaystyle \cap } \cap ∪
{\displaystyle \cup } \cup ⊂ {\displaystyle \subset \,} \subset ⟸ \impliedby ⊃
{\displaystyle \supset \,} \supset ⇒ {\displaystyle \Rightarrow \,} \Rightarrow
or \implies ∈ {\displaystyle \in } \in ↔ {\displaystyle \leftrightarrow \,}
\leftrightarrow ∉ {\displaystyle \notin \,} \notin ⟺ {\displaystyle \iff \,}
\iff ∋ {\displaystyle \ni \,} \ni ⇔ {\displaystyle \Leftrightarrow \,}
\Leftrightarrow (preferred for equivalence (iff)) ∧ {\displaystyle \land \,}
\land ⊤ {\displaystyle \top \,} \top ∨ {\displaystyle \lor \,} \lor ⊥
{\displaystyle \bot \,} \bot ∠ {\displaystyle \angle \,} \angle ∅ {\displaystyle
\emptyset \,} and ∅ {\displaystyle \varnothing \,} \emptyset and \varnothing[1]
⇌ {\displaystyle \rightleftharpoons \,} \rightleftharpoons Delimiters Symbol
Script Symbol Script Symbol Script Symbol Script | {\displaystyle |\,} | or \mid
(difference in spacing) ‖ {\displaystyle \|\,} \| / {\displaystyle /\,} / ∖
{\displaystyle \backslash \,} \backslash { {\displaystyle \{\,} \{ }
{\displaystyle \}\,} \} ⟨ {\displaystyle \langle \,} \langle ⟩ {\displaystyle
\rangle \,} \rangle ↑ {\displaystyle \uparrow \,} \uparrow ⇑ {\displaystyle
\Uparrow \,} \Uparrow ⌈ {\displaystyle \lceil \,} \lceil ⌉ {\displaystyle \rceil
\,} \rceil ↓ {\displaystyle \downarrow \,} \downarrow ⇓ {\displaystyle
\Downarrow \,} \Downarrow ⌊ {\displaystyle \lfloor \,} \lfloor ⌋ {\displaystyle
\rfloor \,} \rfloor Note: To use the Greek Letters in LaTeX that have the same
appearance in the Latin alphabet, just use Latin: e.g., A instead of Alpha, B
instead of Beta, etc.
