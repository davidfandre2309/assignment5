import sys
# this is for assigment 5

def process_data(numbers):
    try:
        numbers = [float(n) for n in numbers]
    except ValueError:
        return "<p>Error: All inputs must be numeric.</p>"

    if any(n < 0 for n in numbers):
        return "<p>Error: All numbers must be non-negative.</p>"

    avg = sum(numbers) / len(numbers)
    avg_message = "<p>The average is " + ("greater than 50." if avg > 50 else "not greater than 50.") + "</p>"

    positive_count = sum(1 for n in numbers if n > 0)
    parity_message = "<p>Count of positive numbers is " + ("even." if positive_count % 2 == 0 else "odd.") + "</p>"

    greater_than_10 = sorted([n for n in numbers if n > 10])
    original_list = "<p>Original Values: " + ", ".join(map(str, numbers)) + "</p>"
    sorted_list = "<p>Sorted Values (greater than 10): " + ", ".join(map(str, greater_than_10)) + "</p>"

    return original_list + sorted_list + avg_message + parity_message

if __name__ == "__main__":
    values = sys.argv[1:]
    if len(values) != 5:
        print("Content-type: text/html\n")
        print("<p>Error: Five input values are required.</p>")
    else:
        print("Content-type: text/html\n")
        print(process_data(values))