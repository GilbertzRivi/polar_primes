from math import sqrt, sin, cos
from PIL import Image, ImageDraw
from time import time

def check_primes(number: int) -> bool:
    for i in range(2, (int)(sqrt(number))+1):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    limit = int(input('Input limit: '))
    size_x = int(input('Input x: '))
    size_y = int(input('Input y: '))

    start = time()

    primes = []
    for i in range(2, limit):
        if check_primes(i):
            primes.append(i)

    end = time()
    print(f'Found {len(primes)} primes in {end-start} seconds')

    image = Image.new('1', size=(size_x, size_y))
    draw = ImageDraw.Draw(image)
    for prime in primes:
        x = (prime * cos(prime))/100 + size_x/2
        y = (prime * sin(prime))/100 + size_y/2
        draw.point(xy=(x, y), fill=1)

    image.save(fp='./image.png')