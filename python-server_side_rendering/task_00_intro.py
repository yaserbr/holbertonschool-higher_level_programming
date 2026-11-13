#!/usr/bin/python3
"""Generate personalized invitation files from a template."""


def generate_invitations(template, attendees):
    """Write output_X.txt for each attendee, filling template placeholders."""
    if not isinstance(template, str):
        print("Invalid input: template must be a string, got {}."
              .format(type(template).__name__))
        return

    if not isinstance(attendees, list) or \
            not all(isinstance(item, dict) for item in attendees):
        print("Invalid input: attendees must be a list of dictionaries, "
              "got {}.".format(type(attendees).__name__))
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    fields = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for field in fields:
            value = attendee.get(field)
            if value is None or value == "":
                value = "N/A"
            content = content.replace("{" + field + "}", str(value))

        filename = "output_{}.txt".format(index)
        try:
            with open(filename, "w") as f:
                f.write(content)
        except OSError as e:
            print("Error writing {}: {}".format(filename, e))
