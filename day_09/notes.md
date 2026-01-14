# Day 9 Notes: Dictionaries and Nesting

## Dictionaries
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

### Syntax
```python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
```

### Retrieving items
```python
print(programming_dictionary["Bug"])
```

### Adding/Editing items
```python
# Adding
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Editing
programming_dictionary["Bug"] = "A moth in your computer."
```

### Looping through dictionaries
```python
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
```

## Nesting
Nesting is putting one dictionary or list inside another.

### Dictionary in a Dictionary
```python
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
```

### List in a Dictionary
```python
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
```

### Dictionary in a List
```python
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    },
]
```

## Project: Blind Auction
The goal of the project was to create a blind auction program where multiple users can bid, and the highest bidder wins.
Key concepts used:
- While loop for continuous input.
- Dictionaries to store name and bid.
- Function to find the maximum bid.
- `os.system("clear")` to clear the screen (simulating blind auction).
