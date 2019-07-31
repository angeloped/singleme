# singleme
#### A cross-platform single instance python module based on socket.

Usage (demo): `python demo.py`

This code is from `demo.py`:
```python
fromm singleme import singleme

# the default port is 8989, but you can change it by changing the port address. me = singleme(port=7070)
me = singleme()# will sys.exit() if similar program is running

while 1:
	print("hello world")
```

To install: `python setup.py install`

That's all!
