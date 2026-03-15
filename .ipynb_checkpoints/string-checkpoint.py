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
   "execution_count": 4,
   "id": "47f36d0d-167e-44ef-abb5-d376f21411f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<built-in method upper of str object at 0x000002AE0522F270>\n",
      "<built-in method lower of str object at 0x000002AE0522F270>\n",
      "<built-in method capitalize of str object at 0x000002AE0522F270>\n",
      "<built-in method title of str object at 0x000002AE0522F270>\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'str' object has no attribute 'swap'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mAttributeError\u001b[39m                            Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 6\u001b[39m\n\u001b[32m      4\u001b[39m \u001b[38;5;28mprint\u001b[39m(s.capitalize)\n\u001b[32m      5\u001b[39m \u001b[38;5;28mprint\u001b[39m(s.title)\n\u001b[32m----> \u001b[39m\u001b[32m6\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[43ms\u001b[49m\u001b[43m.\u001b[49m\u001b[43mswap\u001b[49m(a,\u001b[33m'\u001b[39m\u001b[33m@\u001b[39m\u001b[33m'\u001b[39m))\n\u001b[32m      7\u001b[39m \u001b[38;5;28mprint\u001b[39m(s.isupper())\n\u001b[32m      8\u001b[39m \u001b[38;5;28mprint\u001b[39m(s.islower())\n",
      "\u001b[31mAttributeError\u001b[39m: 'str' object has no attribute 'swap'"
     ]
    }
   ],
   "source": [
    "s = \"manideep\"\n",
    "print(s.upper)\n",
    "print(s.lower)\n",
    "print(s.capitalize)\n",
    "print(s.title)\n",
    "print(s.isupper())\n",
    "print(s.islower())\n",
    "      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a34ee528-e3da-4f80-a3d0-09a8ae9b4a2c",
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
