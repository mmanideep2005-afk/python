{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a3edc591-3d9c-4874-95ec-2c78366018a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n",
      "27\n",
      "36\n",
      "0\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "def add_num(x,y):\n",
    "    return x+y\n",
    "def sub_num(x,y):\n",
    "    return x-y\n",
    "def mul_num(x,y):\n",
    "    return x*y\n",
    "def divi_num(x,y):\n",
    "    return x//y\n",
    "def modu_div(x,y):\n",
    "    return x%y\n",
    "print(add_num(2,6))\n",
    "print(sub_num(30,3))\n",
    "print(mul_num(6,6))\n",
    "print(divi_num(2,12))\n",
    "print(modu_div(200,98))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9b3fa0b4-d574-4858-9f80-bec58366ec07",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 1 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-1\n"
     ]
    }
   ],
   "source": [
    "def sub_num(x,y):\n",
    "    return x-y\n",
    "num1,num2=map(int,input().split())\n",
    "s = sub_num(num1,num2)\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb185a67-e6a2-4e1e-a70c-44883d19daa1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
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
   "version": "3.14.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
