# Math Notation

this is for me to learn how to write mah notation in Markdown.

## Symbols

Mathematics has many symbols! The following is a set of symbols that can be
accessed directly from the keyboard:

```math
+ \ - \ = \! \ / \ ( \ ) \ [ \ ] \ < \ > \ | \ ' \ : \ *
```

Beyond those listed above, distinct commands must be issued in order to display
the desired symbols. There are many examples such as
[Operators](#operators),[Greek letters](#greek-letters), set and relations
symbols, arrows, binary operators, etc.

## White Space

```math
\text{this is a way to express regular text. is very useful for unit notations} \\
\text{to write the equivalent of an 'enter' you'll use doble inverted / you can also add brackets with a measurement to add more space.  }
```

## Operators

There are many operators in mathematics:

### Arithmetic Operators

| Operator       | Command                                       | Script                             |
| -------------- | --------------------------------------------- | ---------------------------------- |
| addition       | $a + b$                                       | `a + b`                            |
| subtraction    | $a - b$                                       | `a - b`                            |
| multiplication | $a \times b $ or $ a \cdot b $ and $a b$      | `a \times b`, `a \cdot b`, `a b`   |
| division       | $a / b $ or $ a \div b \ $ and $ \frac{a}{b}$ | `a / b`, `a \div b`, `\frac{a}{b}` |
| square root    | $\sqrt{a}$                                    | `\sqrt{a}`                         |
| nth root       | $\sqrt[n]{a}$                                 | `\sqrt[n]{a}`                      |
| exponent       | $a^n $ or $a^{n + 1}$                         | `a^n`, `a^{n + 1}`                 |
| logarithm      | $\log(a) $ or $ \ln(a) $ and $ \log_n(a)$     | `\log(a)`, `\ln(a)`, `\log_n(a)`   |
| subscript      | $a_{n} $ or $ a_n$                            | `a_{n}`, `a_n`                     |
| superscript    | $a^{n} $  or $ a^n$                           | `a^{n}`, `a^n`                     |
| evaluation     | $\|_{n=17} f(n)$                              | `\|_{n=17} f(n)`                   |
| factorial      | $a! $                                         | `a!`                               |
| binomial       | ${n} \choose {k}$ or $\binom{n}{k}$           | `${n} \choose {k}`, `\binom{n}{k}` |

### Trigonometric operators

| Symbol name | Symbol    | Script    |
| ----------- | --------- | --------- |
| sine        | $\sin$    | `\sin`    |
| cosine      | $\cos$    | `\cos`    |
| tangent     | $\tan$    | `\tan`    |
| cotangente  | $\cot$    | `\cot`    |
| arc sine    | $\arcsin$ | `\arcsin` |
| arc cos     | $\arccos$ | `\arccos` |
| arctan      | $\arctan$ | `\arctan` |
| arc cot     | $arccot$  | `arccot`  |
| sinh        | $\sinh$   | `\sinh`   |
| cosh        | $\cosh$   | `\cosh`   |
| tanh        | $\tanh$   | `\tanh`   |
| coth        | $\coth$   | `\coth`   |
| sec         | $\sec$    | `\sec`    |
| csc         | $\csc$    | `\csc`    |

### Other Operators

comparison and logical operators

| Operator                 | Command     | Script      |
| ------------------------ | ----------- | ----------- |
| equality                 | $a = b$     | `a = b`     |
| inequality               | $a \neq b$  | `a \neq b`  |
| less than                | $a < b$     | `a < b`     |
| greater than             | $a > b$     | `a > b`     |
| less than or equal to    | $a \leq b$  | `a \leq b`  |
| greater than or equal to | $a \geq b$  | `a \geq b`  |
| logical and              | $a \land b$ | `a \land b` |
| logical or               | $a \lor b$  | `a \lor b`  |
| logical not              | $a \lnot b$ | `a \lnot b` |

### Custom operators

## Greek letters

Greek letters Greek letters are commonly used in mathematics, and they are very
easy to type in math mode. You just have to type the name of the letter after a
backslash:

-   if the first letter is lowercase, you will get a lowercase Greek letter
-   if the first letter is uppercase (and only the first letter), then you will
    get an uppercase letter.

> Note that some uppercase Greek letters look like Latin ones, so they are not
> provided by LaTeX (e.g. uppercase Alpha and Beta are just "A" and "B",
> respectively).

-   Lowercase epsilon, theta, kappa, phi, pi, rho and sigma are provided in two
    different versions. The alternate, or variant version is created by adding
    "var" before the name of the letter:

| Greek Letter           | Symbol                                        | Script                                            |
| ---------------------- | --------------------------------------------- | ------------------------------------------------- |
| Alpha                  | $\Alpha$ and $ \alpha$                        | `A`, `\Alpha` and`\alpha`                         |
| Beta                   | $\Beta $ , $ B $  and $ \beta$                | `B` , `\Beta` and `\beta`                         |
| Gamma                  | $\Gamma$ and $ \gamma $                       | `\Gamma` and `\gamma`                             |
| Delta                  | $\Delta $ and $ \delta$                       | `\Delta` and `\delta`                             |
| Epsilon and Varepsilon | $\Epsilon $ , $ \epsilon $ and $ \varepsilon$ | `E`, `\Epsilon` and `\epsilon` also `\varepsilon` |
| Zeta                   | $\Zeta $ and $ \zeta$                         | `Z` , `\Zeta` and `\zeta`                         |
| Eta                    | $\Eta $ and $ \eta $                          | `H` , `\Eta` and `\eta`                           |
| Theta and Vartheta     | $\Theta $ , $ \theta $ and $ \vartheta$       | `\Theta` and `\theta` also `\vartheta`            |
| Iota                   | $\Iota $ and $\iota $                         | `I` , `\Iota` and `\iota`                         |
| Kappa and Varkappa     | $K$ ,$\Kappa $, $ \kappa $ and $ \varkappa $  | `K` , `\Kappa`, `\kappa` also `\varkappa`         |
| Lambda                 | $ \Lambda $ and $ \lambda$                    | `\Lambda` and `\lambda`                           |
| Mu                     | $M$ , $\Mu $ and $ \mu $                      | `M`, `\Mu` and `\mu`                              |
| Nu                     | $ N $, $\Nu $,  and $ \nu$                    | `N`, `\Nu` and `\nu`                              |
| Xi                     | $\Xi $ and $ \xi$                             | `\Xi` and `\xi`                                   |
| Omicron                | $O $  and $ o$                                | `O` and `o`                                       |
| Pi and Varpi           | $ \Pi $ , $ \pi $ and $ \varpi $              | `\Pi` and `\pi` also `\vapi`                      |
| Rho $`P`$ and Varrho   | $P$ ,$\Rho $ , $ \rho $ and $ \varrho $       | `P`, `\Rho` and `\rho` also `\varrho`             |
| Sigma and Varsigma     | $\Sigma $ , $ \sigma $  and  $\varsigma$      | `\Sigma` and `\sigma` also `\varsigma`            |
| Tau                    | $\Tau $ and $ \tau $                          | `T`, `\Tau` and `\tau`                            |
| Upsilon $`Y`$          | $ Y $ , $ \Upsilon $ and $ \upsilon $         | `Y`, `\Upsilon` and `\upsilon`                    |
| Phi and Varphi         | $\Phi $, $ \phi $ and $ \varphi $             | `\Phi` and `\phi` also `\varphi`                  |
| Chi                    | $ X$ , $\Chi $ and $ \chi$                    | `X`,`\Chi` and `chi`                              |
| Psi                    | $\Psi $ and $\psi $                           | `\Psi` and `\psi`                                 |
| Omega                  | $\Omega $ and $ \omega$                       | `\Omega` and `\omega`                             |

## Other symbols

| Symbol name            | Symbol      | Script     |
| ---------------------- | ----------- | ---------- |
| forall                 | $\forall$   | `\forall`  |
| in                     | $\in$       | `\in`      |
| quad (the white space) | $ a\quad b$ | `\quad`    |
| exists                 | $\exists$   | `\exists`  |
| geq                    | $\geq$      | `\geq`     |
| leq                    | $\leq$      | `\leq`     |
| partial                | $\partial$  | `\partial` |
| eth                    | $\eth$      | `\eth`     |
| hbar                   | $\hbar$     | `hbar`     |
| imath                  | $\imath$    | `imath`    |
| jmath                  | $\ell$      | `\ell`     |
| re                     | $\Re$       | `\Re`      |
| Im                     | $\Im$       | `\Im`      |
| wp                     | $\wp$       | `\wp`      |
| nabla                  | $\nabla$    | `\nabla`   |
| Box                    | $\Box$      | `\Box`     |
| infinity               | $\infty$    | `\infty`   |
