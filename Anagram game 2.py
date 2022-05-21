import random
import time

solutions = ('helicopter',
             'generator',
             'television',)
guide = ('-a flying object',
         '-produces electricity',
         '-transmits audio-visual content')
congrats = ('You are correct!',
            'Nice! You got it!',
            'You are smart!',
            'Good Job!')


def anagram_generator(random1,solutions):
        anagram= []
        random2 = random.randint(0,(solutions[random1].__len__() - 1)) # use choice here instead
        for item in list(solutions[random1]):
                anagram.insert(random2,item)

        print (''.join(anagram),guide[random1])

print ("Welcome to my Anagram Game!! \n I am glad to have you here")
resume = 1

while resume == 1:
        length = solutions.__len__() - 1
        random1 = random.randint(0,length)
        time.sleep(1)
        print ("Are you ready to play? \n Enter y for yes or n for no")
        response = input()
        resume2 = 1

        while resume2 == 1:
                if response == 'y':
                        print ('Alright')
                        time.sleep(1)
                        print ('Unscramble the word that appears on the screen')
                        time.sleep(1)
                        anagram_generator(random1,solutions)
                        answer = input()
                        if answer == solutions[random1]:
                                print(congrats[random.randint(0,3)])
                                time.sleep(2)
                        else:
                                print( 'Unfortunately, you were wrong. The right answer is ', solutions[random1])
                                time.sleep(2)
                        print('Do you still want to play? \n Enter y for yes or n for no')
                        answer2 = input()
                        if answer2 == 'n':
                                resume = 0
                                resume2 =0
                                print('Thanks for your time')
                                time.sleep(1)
                                print('Have a lovely day')
                        else:
                                if answer2 !=('y'):
                                        print('Wrong input')
                                        print('Thanks for your time')
                                        time.sleep(1)
                                        print('Have a lovely day')
                                        resume = 0
                                        resume2 =0
                                
                else:
                        if response == 'n':
                                print('Thanks for your time')
                                time.sleep(1)
                                print('Have a lovely day')
                                resume = 0
                                resume2 = 0
                        else:
                                print('Please enter a valid response')
                                resume2 = 0
         
