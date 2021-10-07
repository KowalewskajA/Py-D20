# Py-D20

Is a short commandline tool that evaluates dice strings that you would find in an DnD related calculations.

# Input

It processes:

sum:=expression{+|-}expression
expression:={number|''}d{number}

# Output

It will calculate the roll twice so you would see what it would be with dis|-advantage:

{expression}: (1){result_1} (2){result_2}

# Example

If you provite the same expression more than one the cache Object will be reused, which will be mentioned in the output.

```console
foo@bar:~$ py Py-D20.py
>3d12+4d6-2d2
3d12+4d6-2d2: (1)42 (2)42
>3d12+4d6-2d2
Cached 3d12+4d6-2d2: (1)36 (2)33
>3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2                
Cached 3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2+3d12+4d6-2d2: (1)330 (2)307
```

# Potential improvement

- [ ] "> expression name", so you can call it 'axe' for example and use it afterwards as "> axe"
- [ ] "> list", so you can see which expression you have saved with what references
- [ ] capabilty to save your expressions in a file
- [ ] capabilty to load your expressions from a file

