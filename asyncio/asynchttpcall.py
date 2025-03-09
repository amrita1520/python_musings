import asyncio
import aiohttp
import time

BASE_URL = "https://jsonplaceholder.typicode.com/todos/1"

# Asynchronous Weather API call
async def get_weather_async():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL) as response:
            if response.status == 200:
                data = await response.json()
                print("Weather API Response:", data)
            else:
                print(f"Error: {response.status}")

# Synchronous Prime Number Calculation
def print_prime_numbers():
    primes = []
    for num in range(1, 10**6):  # Reduced range for better performance
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):  # Optimized check using sqrt
                if num % i == 0:
                    break
            else:
                primes.append(num)
    print(f"Total primes found: {len(primes)}")

async def main():
    # Start the async weather API call
    weather_task = asyncio.create_task(get_weather_async())

    # Run prime number calculation synchronously (blocking)
    print_prime_numbers()

    # Wait for the async task to complete
    await weather_task

# Run the event loop
asyncio.run(main())
