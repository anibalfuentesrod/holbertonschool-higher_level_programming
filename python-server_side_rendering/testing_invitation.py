from task_00_intro import generate_invitations

def test_missing_data_in_object():
    template = "Hello {name},\n\nYou are invited to the {event_title} on {event_date} at {event_location}.\n\nBest regards,\nEvent Team"
    attendees = [
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template, attendees)

    with open("output_1.txt", "r") as f:
        content = f.read()
        print("Generated content:")
        print(content)
        assert "on N/A" in content, "Failed: Missing data should be replaced with 'N/A'"

if __name__ == "__main__":
    test_missing_data_in_object()
    print("Test passed.")