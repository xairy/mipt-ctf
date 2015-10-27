Keeping stdin open
==================

Bad:
```
echo $(python -c 'print "payload"') | ./stdin
```

Good:
```
cat <(python -c 'print "payload"') - | ./stdin
```
