# Tarback Mission?
Quickly back-up our Linux workstations using date-named archives.

Greetings 'Pythoneers!

I wanted to share a handy little script that I created to help us back-up / archive our files. The ability to tally, archive, as well as to save recently-changed files into incrementally-named backups on our desktop, are the key benefits.

Designed to run wherever the `find` and `tar` commands are installed (Linux, Cygwin, MacOS, etc,) I hope you will find this code usefull, as well as instructive. 

There is a reason why I post things on the holidays - I've lots more features to add as time permits.

# Next Mission?
* Update the script to use YOUR directory base.
* Change `~/Desktop` to an external device / networked location.
* Add to `cron` so as to run automatically.

Happy July 4th!

-- Rn

If you enjoy this type of project, then you should also enjoy my [Python 4000 educational opportunity](https://www.udemy.com/course/python-4000-gnu-devops/).

## p.s:
At the time of this retelling, Pythoneers should note that the `~/Desktop` location is *still* **not** a valid file-path!

Once we get away from the `~/Desktop` however, we will be able to use `os.path.exists(...)` so as to verify that the archive was created.
