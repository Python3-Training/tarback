# Tarback Mission?
**Quickly back-up our Linux workstations using date-named archives.**

Greetings 'Pythoneers!

I wanted to share a handy little script that I created to help us back-up / archive our files. The ability to tally, archive, as well as to save recently-changed files into incrementally-named backups on our desktop, are the key benefits.

Designed to run wherever the `find` and `tar` commands are installed (Linux, Cygwin, MacOS, etc,) I hope you will find this code usefull, as well as instructive. 

# Next Mission?
* Update the script to use YOUR directory base.
* Change `~/Desktop` to an external device / networked location.
* Add to `cron` so as to run automatically.

There is a reason why I post things on the holidays - I've lots more features to add as time permits.


Happy July 4th!

-- Rn

If you enjoy this type of DevOps enginnering, then you will also enjoy my [Python 4000 educational opportunity](https://www.udemy.com/course/python-4000-gnu-devops/). If you are new to Python 3, then you will enjoy my [primer training]([https://www.udemy.com/course/python-1000/](https://www.udemy.com/course/python-1000/?referralCode=D3A7B607149F46D12A28)), as well.

## p.s:
At the time of this retelling, Pythoneers should note that the `~/Desktop` location is *still* **not** a valid path prefix!

Once we get away from the `~/Desktop` however, we will be able to use `os.path.exists(...)` to verify that the archive was created.

## Facebook:
At the moment all things new + python are streamed together on my [python facebook page](https://www.facebook.com/groups/nagyspythontraining). Feel free to check-in there, to see what's up [here](https://github.com/soft9000), on [YouTube](https://www.youtube.com/watch?v=X3-s38YFQwM&fbclid=IwAR38MdN9lUvHz-kM-Vm_wSlnJjyE13NklI3PCXDRaTfFBv7ju6vn7DwVIaE), as well as [elsewhere](https://www.amazon.com/~/e/B08ZJLH1VN?fbclid=IwAR3FFMtBWNZxNtZY81Ex6YIHJSsY-62kcIWRH74IvasxWdONKGgphqrW-IE).

## Keychain Backup

![Keychain Backup](https://github.com/Python3-Training/tarback/blob/main/PrintedCases.png)

Boldly carry your backups where few [3D Design](https://www.thingiverse.com/thing:4931272)s dare go?
