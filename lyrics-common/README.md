# Common phrases in lyrics

The other day as I was waiting to pick up my son from school, I was listening to a [local radio station](https://q1043.iheart.com/) that has a daily feature called "Three at three". Basically, they play three songs that have something in common and ask listeners to call in if they can figure out what it is. That day's three songs were "You Never Give Me Your Money" by the Beatles, "Lonely" by The Police and "Born in the USA" by Bruce Springsteen and the E Street Band. The common phrase in the three songs was "nowhere to go". 

Another thing that happened this week is, I was sick. And while I was lying in bed in a feverish state, I thought it might be fun to make a little Python script to check song lyrics for common phrases. A more ambitious plan is to hook the script up to a song lyrics API, and I might do that at some point, but for now it'll just read the lyrics from text files.

If you download the lyrics for those three songs and run the program, this is the output you should see (with your own filenames):

```
lc.py you-never-give-me-your-money.txt born-in-the-usa.txt lonely.txt
Phrases of length 1
go
up
you
in
all
my
nowhere
i
your
the
me
and
to


Phrases of length 2
to go
nowhere to


Phrases of length 3
nowhere to go


Phrases of length 4


Phrases of length 5
```
