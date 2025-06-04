# Energy Efficiency Report

**Estimated energy cost:** `360` units

- **Loop count:** 1

- **Recursive calls:** 3

- **I/O calls:** 1


### Detailed I/O Calls:
- `open` at line 8

### Suggestions:
- Consider converting recursion to iteration to reduce call overhead.
- Move I/O operations outside of loops where possible.

### Profiling Summary (Top 10 by cumulative time):

```text
         57 function calls (52 primitive calls) in 0.063 seconds

   Ordered by: cumulative time
   List reduced from 14 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.063    0.063 {built-in method builtins.exec}
        1    0.000    0.000    0.063    0.063 <string>:1(<module>)
        1    0.000    0.000    0.063    0.063 <string>:6(process)
       11    0.060    0.005    0.060    0.005 {built-in method io.open}
       11    0.002    0.000    0.002    0.000 {method '__exit__' of '_io._IOBase' objects}
       10    0.000    0.000    0.000    0.000 /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/codecs.py:186(__init__)
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
       10    0.000    0.000    0.000    0.000 {method 'write' of '_io.TextIOWrapper' objects}
      6/1    0.000    0.000    0.000    0.000 <string>:1(recurse)
        1    0.000    0.000    0.000    0.000 /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/codecs.py:319(decode)


```
