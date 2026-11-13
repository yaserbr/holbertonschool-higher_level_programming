def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Invalid input: template must be a string")
        return

    if not isinstance(attendees, list):
        print("Invalid input: attendees must be a list")
        return
    if not all(isinstance(item, dict) for item in attendees):
        print("Invalid input: all attendees must be dictionaries")
        return

    if not template:
        print("Template is empty, no output files generated")
        return

    if not attendees:
        print("No data provided, no output files generated")
        return

    for index, attende in enumerate(attendees):
        newRow = template
        fields = ["name", "event_title", "event_date", "event_location"]

        for field in fields:
            newRow = newRow.replace("{" + field + "}", (attende.get(field) or "N/A"))
        print(index, newRow)
