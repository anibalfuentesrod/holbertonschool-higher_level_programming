import os

def generate_invitations(template, attendees):
    """Checks what type of input is"""
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    """Checks if template is not empty and if yes prints an error"""
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    """Iterates over the list of atten.. and replace the placeholder in the template"""
    for i, attendee in enumerate(attendees, start=1):
        output = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace(f"{{{key}}}", str(value))

        """writes to a file"""
        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w') as f:
            f.write(output)
        print(f"Generated {output_filename}")

"""example of usage"""
if __name__ == "__main__":
    """Read a template frrom a file"""
    with open('template.txt', 'r') as file:
        template_content = file.read()

    """list of atterndees"""
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    """call the fun with the template and attendees"""
    generate_invitations(template_content, attendees)