import os

def generate_invitations(template, attendees):
    # Tip yoxlanışı
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected string, got {type(template).__name__}.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries.")
        return

    # Boşluq yoxlanışı
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Hər bir iştirakçı üçün emal
    for i, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # Placeholder siyahısı
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            # Əgər açar yoxdursa və ya dəyəri None-dırsa "N/A" yazırıq
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            processed_template = processed_template.replace(f"{{{key}}}", str(value))
        
        # Fayla yazmaq
        filename = f"output_{i}.txt"
        
        # Əgər fayl artıq mövcuddursa, üzərinə yazmaq olar (şərtdə əksinə qeyd olunmayıb)
        try:
            with open(filename, 'w') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
