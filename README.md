# Tarback Mission?
**Quickly back-up our Linux workstations using date-named archives.**

![Logo](./_images/tarback.jpg)

Greetings 'Pythoneers!

I wanted to share a handy little script that I created to help us back-up / archive our files. The ability to tally, archive, as well as to save recently-changed files into incrementally-named backups on our desktop, are the key benefits. 

Using your platform's ***native file recovery*** format is also seldom a bad idea! ;-)

Designed to run wherever the `find` and `tar` commands are installed (Linux, Cygwin, WSL, macOS, etc,) I hope you will find this code useful, as well as instructive. --I've even a [3D print](https://www.thingiverse.com/thing:4931272) for TF cards on keychains.

p.s. I've kept `tarback.py` for educational reasons - it works fine, but the latest version is `tarback2.py`. 

# MISSION: Customize tarback2.py before using!
* Add YOUR key folders (pun intended) to **Options**.`locations`.
* Define your default key in **Options**.`option`.
* Change **Options**.`DEFAULT_FOLDER` to YOUR backup location.
* (optional) Add to `cron` so as to run automatically?

Since 2023/07/13 dynamic option [re]configuration, online backup reporting, as well as an oh-so-cool backup 'gap-days' set of 'ops are also presently possible. Use `tarback2.py --help` to check-out the new options.

I've more features to add (`tarback3`?) as time permits... 


-- Rn

If you enjoy this type of DevOps engineering, then you will also enjoy my [Python 4000 educational opportunity](https://www.udemy.com/course/python-4000-gnu-devops/). If you are new to Python 3, then you will enjoy my [primer training opportunity](https://www.udemy.com/course/python-1000-the-python-primer/?referralCode=A22C48BD99DBF167A3DE), as well.

## Options.DEFAULT_ALL
Decades ago - when I was writing for BYTE Magazine - a fellow author mused that the reason WHY wee geeks have
such cool tools is because we actually USE what we CREATE?

In that spirit I hope you'll enjoy the new **DEFAULT_ALL** feature. Presently implemented as a 'key option' (yes, more puns :)
we can use that token whenever we want to 'Jedi' ('JUST DO IT') `all.`

## Related Productions:
If you would like to encourage these and other geeky efforts, then consider purchasing one of [my books on Amazon](https://www.amazon.com/~/e/B08ZJLH1VN?fbclid=IwAR33PujdptzBfukQQuwATJ05mxm--xSB31ApgdJyJeNFzPXvmgrFgI1coS4) and / or one of [my other educational videos](https://www.udemy.com/user/randallnagy2/).


## Protfolio:
Feel free to see what's up [here](https://github.com/soft9000), as well as [elsewhere](https://soft9000.com).

## Keychain Backup

![Keychain Backup](https://github.com/Python3-Training/tarback/blob/main/PrintedCases.png)

Boldly carry your backups where few [3D Design](https://www.thingiverse.com/thing:4931272)s dare go?
