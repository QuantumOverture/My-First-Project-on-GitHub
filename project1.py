def primes(num):
  for i in range(2,num):
    if((num%i)==0):
      return print("Not a prime number")

  return print("A prime, indeed!")




primes(int(input("Enter a number to check if primaility!: ")))
