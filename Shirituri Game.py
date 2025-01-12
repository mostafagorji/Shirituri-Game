import random
import time
try:
    from colorama import Fore

    time.sleep(2)
    print(Fore.RED + 'In the name of God' + Fore.LIGHTGREEN_EX)
    time.sleep(1)
    print('Shirituri Game          Age group 9 years to 99 years old          Games for Everyone')
    time.sleep(3)
    print(Fore.BLUE + 'Write "start" to begin the game.')
    k = input()
    if k == 'start':
        print('pleas waite')
        time.sleep(3)
        print(Fore.YELLOW + ' To begin,', end="")
        time.sleep(1)
        print(Fore.YELLOW + ' I will', end="")
        time.sleep(1)
        print(Fore.YELLOW + ' give you', end="")
        time.sleep(1)
        print(Fore.YELLOW + ' a word;', end="")
        time.sleep(1)
        print(Fore.YELLOW + ' you must', end="")
        time.sleep(1)
        print(Fore.YELLOW + ' examine', end="")
        time.sleep(1)
        print(Fore.YELLOW + ' the last', end="")
        time.sleep(1)
        print(Fore.YELLOW + ' letter of this word', end="")
        time.sleep(1)
        print(Fore.YELLOW + ' and then write', end="")
        time.sleep(1)
        print(Fore.YELLOW + ' a word that starts', end="")
        time.sleep(1)
        print(Fore.YELLOW + ' with that letter.')
        time.sleep(6)

        print(Fore.CYAN + 'Hoping for success' + Fore.WHITE)
        time.sleep(1)
        input('prees enter' + Fore.RESET)
        a = []


        def one(word, wordInput):
            c = random.randrange(3)
            d = word[c]
            wordInput.append(d)
            return wordInput


        one(word=['apple', 'banana', 'cheri'], wordInput=a)
        print(a)


        def inpute(inputing, chance):
            while True:
                e = len(inputing) - 1
                f = inputing[e]
                g = len(f) - 1
                h = f[g]
                i = input('enter the word:')
                j = i[0]
                if j == h:
                    inputing.append(i)
                    print(inputing)
                else:
                    if chance > 0:
                        chance -= 1
                    else:
                        print(Fore.LIGHTRED_EX+'You lost'+Fore.RESET)
                        break
                    print('Your chances are equal to:', chance)
                    print('You have entered the incorrect word, please try again.')


        inpute(inputing=a, chance=10)
except:
    print(Fore.LIGHTRED_EX+'Error in operation')
    print(Fore.BLUE+'Thank you for being with us.')
    print('so long')
finally:
    print(Fore.BLUE + 'Thank you for being with us.')
    print('so long')