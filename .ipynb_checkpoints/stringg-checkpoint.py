{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ba3ff355-381a-4773-b998-77e31aa053ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mani deep\n",
      "mani mani mani mani mani mani mani mani mani mani \n"
     ]
    }
   ],
   "source": [
    "s1 =\"mani\"\n",
    "s2=\"deep\"\n",
    "print(s1 +\" \"+ s2)\n",
    "print((s1+\" \")*10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6a5ddb73-e527-4cfc-8070-a4546b6ce0ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "no of students: 2\n",
      "enter roll no 1 attendance : 1\n",
      "enter roll no 2 attendance : 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "2\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"no of students:\"))\n",
    "absent=0\n",
    "present=0\n",
    "for i in range(1,n+1):\n",
    "    val=int(input(f\"enter roll no {i} attendance :\"))\n",
    "    if val==0:\n",
    "        present+=1\n",
    "    else:\n",
    "        absent+=1\n",
    "print(present)\n",
    "print(absent)\n",
    "total=present+absent\n",
    "print((absent//total)*100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "47f36d0d-167e-44ef-abb5-d376f21411f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MANIDEEP MANI\n",
      "manideep mani\n",
      "Manideep mani\n",
      "Manideep Mani\n",
      "False\n",
      "True\n",
      "m@nideep m@ni\n",
      "MANIDEEP MANI\n",
      "['manideep', 'mani']\n",
      "['m', 'deep m', '']\n",
      "m,a,n,i,d,e,e,p, ,m,a,n,i\n",
      "manideep mani\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "s = \"manideep mani\"\n",
    "print(s.upper())\n",
    "print(s.lower())\n",
    "print(s.capitalize())\n",
    "print(s.title())\n",
    "print(s.isupper())\n",
    "print(s.islower())\n",
    "print(s.replace('a','@'))\n",
    "print(s.swapcase())\n",
    "print(s.split())\n",
    "print(s.split(sep='ani'))\n",
    "print(','.join(s))\n",
    "print(s.strip())\n",
    "print(s.find('m')) #substring index value , if not there returns -1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a34ee528-e3da-4f80-a3d0-09a8ae9b4a2c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "strong password\n"
     ]
    }
   ],
   "source": [
    "password = \"Mani@123\"\n",
    "#indicators char.isupper true , char.islower\n",
    "#check length of password should 8 >\n",
    "#if allindicators true \n",
    "upper_ind=lower_ind=digit_ind=special_ind=False\n",
    "for char in password:\n",
    "    if char.isupper():\n",
    "        upper_ind= True\n",
    "    elif char.islower():\n",
    "        lower_ind= True\n",
    "    elif char.isdigit():\n",
    "        digit_ind= True\n",
    "    elif char in '@#$%^&*':\n",
    "        special_ind= True\n",
    "if upper_ind & lower_ind & digit_ind & special_ind :\n",
    "    print(\"strong password\")\n",
    "else:\n",
    "    print(\"weak password\")\n",
    "if not upper_ind: # not false =true block executes\n",
    "    print(\"missing upper case letter\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "46e5f0ac-f413-406f-b7b5-8eac4af7dd98",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "program done\n",
      "even\n"
     ]
    }
   ],
   "source": [
    "def even_odd(x):\n",
    "    if x%2==0:\n",
    "        return 'even' #program terminates here \n",
    "        print(\"mem\")\n",
    "    else:\n",
    "        return 'odd'\n",
    "print(\"program done\")\n",
    "res=even_odd(10)\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "0d2454f2-f369-4dd8-be2a-bbdac304644a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 12345\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n"
     ]
    }
   ],
   "source": [
    "def list_sum(x):\n",
    "    s=0\n",
    "    for num in x:\n",
    "        s+=num\n",
    "    return s\n",
    "lst= list(map(int,input()))\n",
    "sr = list_sum(lst)\n",
    "print(sr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a52c6c09-9aaa-4c09-838f-e391fd794adf",
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
