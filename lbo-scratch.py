from thinkbayes import Pmf

# make empty pmf
pmf = Pmf()
pmf.Set('Bowl 1', .5)               # P(Bowl 1)
pmf.Set('Bowl 2', .5)               # P(Bowl 2)
pmf.Print()

# picks vanilla cookie - what is P of bowl
pmf.Mult('Bowl 1', .75)             # P(Vanilla | Bowl 1)
pmf.Mult('Bowl 2', .5)              # P(Vanilla | Bowl 2)
pmf.Print()

print pmf.Normalize()
pmf.Print()

# picks chocolate cookie - update the pmf
pmf.Mult('Bowl 1', .25)             # P(Chocolate | Bowl 1)
pmf.Mult('Bowl 2', .5)              # P(Chocolate | Bowl 2)
pmf.Print()

print pmf.Normalize()
pmf.Print()

