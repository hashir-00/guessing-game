def guess():
  n="hashir"
  y=input("guess the secret word:")
  guess_count=0
  guess_limit=2#not necessary
  out_of_guesses=False
  turn=0
  turn += 1


  while y!= n and not(out_of_guesses):
     if guess_count<guess_limit:
        y=(input("guess again:"))
        guess_count += 1

     else:
          out_of_guesses=True


  if out_of_guesses :
    print("out of guesses.you lose!!!.\nyou lost.do you want to retry?\n\nyes\nno\n")
    P = input("")

    if P == "yes" and turn<2:
      return guess()


    else:
        print("game over")



  else :
    print("you win from "+str(guess_count+1)+"/"+"3 chances")






guess()



