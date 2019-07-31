# singleme
#### A cross-platform single instance python module based on socket.

Usage (demo): `python demo.py`

This is code from `demo.py`:
```python
m singleme import singleme

# the default port is 8989, but you can change it by changing the port address. me = singleme(port=7070)
me = singleme()# will sys.exit() if similar program is running

while 1:
	print("hello world")
```

That's all!
