{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.4"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python394jvsc74a57bd04ce0e62306dd6a5716965d4519ada776f947e6dfc145b604b11307c10277ef29",
   "display_name": "Python 3.9.4 64-bit"
  },
  "metadata": {
   "interpreter": {
    "hash": "4ce0e62306dd6a5716965d4519ada776f947e6dfc145b604b11307c10277ef29"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "a = 1\n",
      "Hello Robert.\n"
     ]
    }
   ],
   "source": [
    "#TASK1\n",
    "#A\n",
    "\n",
    "import random\n",
    "a = random.randint(1, 10)\n",
    "print (\"a =\", a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#B\n",
    "\n",
    "name = input(\"Hello, what is your name? \")\n",
    "print (\"Hello \" + name +\".\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "You need to guess lower. Try again\n",
      "You guessed correctly!\n"
     ]
    }
   ],
   "source": [
    "#C/D\n",
    "\n",
    "import random\n",
    "number = random.randrange(1, 10)\n",
    "guess = int(input(\"Guess a number between 1 and 10:\"))\n",
    "while guess != number:\n",
    "    if guess < number:\n",
    "        print (\"You need to guess higher. Try again.\")\n",
    "        guess = int(input(\"Guess a number between 1 and 10:\"))\n",
    "    else:\n",
    "        print (\"You need to guess lower. Try again\")\n",
    "        guess = int(input(\"Guess a number between 1 and 10:\"))\n",
    "\n",
    "print (\"You guessed correctly!\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Guess a number between 1 and 100\n"
     ]
    },
    {
     "output_type": "error",
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: ''",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-20-a418e7a238b1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Guess a number between 1 and 100'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m     \u001b[0mguess\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m     \u001b[0mi\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mguess\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mi\u001b[0m \u001b[1;33m==\u001b[0m \u001b[0mnum\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Congratulations, you finaly passed 1st grade!'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: ''"
     ]
    }
   ],
   "source": [
    "#Task 2\n",
    "\n",
    "import random\n",
    "num = random.randint(1, 100)\n",
    "while True:\n",
    "    print('Guess a number between 1 and 100')\n",
    "    guess = input()\n",
    "    i = int(guess)\n",
    "    if i == num:\n",
    "        print('Congratulations, you finaly passed 1st grade!')\n",
    "        break\n",
    "    elif i < num:\n",
    "               print('Stop counting on your fingers!')\n",
    "    elif i > num:\n",
    "               print('Did you use a calculator?')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Your favorite meal is  with a glass of \n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "metadata": {},
     "execution_count": 41
    }
   ],
   "source": [
    "#Task 3\n",
    "\n",
    "first = input(\"Hello, what's your favorite dish? \")\n",
    "second = input(\"You have good tastes, what about drink? \")\n",
    "\n",
    "print(\"Your favorite meal is\", first ,\"with a glass of\", second)\n",
    "\n",
    "input(\"\\n\\nPress the enter key to exit.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "2000\n1800.0\n1620.0\n1458.0\n1312.2\n1180.98\n1062.882\n"
     ]
    }
   ],
   "source": [
    "#Task 4\n",
    "\n",
    "motorbike = 2000\n",
    "while motorbike > 1000:\n",
    "    print (motorbike)\n",
    "    motorbike=motorbike*0.9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "1.0\n"
     ]
    }
   ],
   "source": [
    "#Task 5\n",
    "\n",
    "def add(a,b):\n",
    "    result=a+b\n",
    "    print(result)\n",
    "\n",
    "def sub(a,b):\n",
    "    result=a-b\n",
    "    print(result)\n",
    "\n",
    "def mul(a,b):\n",
    "    result=a*b\n",
    "    print(result)\n",
    "\n",
    "def div(a,b):\n",
    "    result=a/b\n",
    "    print(result)\n",
    "\n",
    "def pow(a,b):\n",
    "    result=a**b\n",
    "    print(result)\n",
    "\n",
    "a=int(input(\"Enter the first number: \"))\n",
    "b=int(input(\"Enter the second number: \"))\n",
    "op=input(\"Enter the operator: \")\n",
    "\n",
    "if op==\"+\":\n",
    "    add(a,b)\n",
    "\n",
    "elif op==\"-\":\n",
    "    sub(a,b)\n",
    "\n",
    "elif op==\"*\":\n",
    "    mul(a,b)\n",
    "\n",
    "elif op==\"/\":\n",
    "    div(a,b)\n",
    "\n",
    "elif op==\"**\":\n",
    "    pow(a,b)\n",
    "\n",
    "else:\n",
    "    print(\"Invalid Operation\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}