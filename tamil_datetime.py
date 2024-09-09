tamil_year_names =[
'பிரபவ',
'விபவ',
'சுக்ல',
'பிரமோதூத',
'பிரஜோத்பத்தி',
'ஆங்கிரச',
'ஸ்ரீமுக',
'பவ',
'யுவ',
'தாது',
'ஈஸ்வர',
'பகுதான்ய',
'பிரமாதி',
'விக்ரம',
'விஷு',
'சித்ரபானு',
'சுபானு',
'தாரண',
'பார்த்திப',
'விய',
'ஸர்வஜித்து',
'ஸர்வதாரி',
'விரோதி',
'விக்ருதி',
'கர',
'நந்தன',
'விஜய',
'ஜய',
'மன்மத',
'துர்முகி',
'ஹேவிளம்பி',
'விளம்பி',
'விகாரி',
'சார்வரி',
'பிலவ',
'சுபகிருது',
'சோபகிருது',
'குரோதி',
'விசுவாவசு',
'பராபவ',
'பிலவங்க',
'கீலக',
'சௌமிய',
'சாதாரண',
'விரோதிகிருது',
'பரிதாபி',
'பிரமாதீச',
'ஆனந்த',
'ராக்ஷஸ',
'நள',
'பிங்கள',
'காளயுக்தி',
'சித்தார்த்திரி',
'ரௌத்த்ரி',
'துன்மதி',
'துந்துபி',
'ருத்ரோத்காரி',
'ரக்தாக்ஷி',
'குரோதன',
'அக்ஷய',
]


tamil_month_names = [
    'சித்திரை',
    'வைகாசி',
    'ஆனி',
    'ஆடி',
    'ஆவணி',
    'புரட்டாசி',
    'ஐப்பசி',
    'கார்த்திகை',
    'மார்கழி',
    'தை',
    'மாசி',
    'பங்குனி',
]


from datetime import datetime, timedelta
days_sequence=[
[30,32,31,32,31,30,30,30,29,30,29,31],
[31,31,32,31,31,31,30,29,29,30,30,30],
[31,31,32,31,31,31,30,29,30,29,30,30],
[31,32,31,32,31,30,30,30,29,29,30,31],
]

start_date = datetime(1900, 4, 13).date()
start_year = 'சார்வரி'
start_year_index = tamil_year_names.index(start_year)
start_month_index = 1
start_day_index = 1

def get_tamil_date(dt):
    # Calculate total days difference between the current date and the start date
    days_diff = (dt - start_date).days

    # Initialize the indices for years, months, and days
    current_year_index = start_year_index
    current_month_index = start_month_index
    current_day_index = start_day_index

    # Move forward if days_diff is positive (after the start date)
    if days_diff >= 0:
        # Move forward through the years
        while days_diff >= 365:  # Approximate check for a year
            year_days = sum(days_sequence[current_year_index % 4])  # Cycle through days_sequence
            if days_diff >= year_days:
                days_diff -= year_days
                current_year_index = (current_year_index + 1) % len(tamil_year_names)  # Move to next year

        # Now process the months within the current year
        while days_diff >= days_sequence[current_year_index % 4][current_month_index]:
            days_diff -= days_sequence[current_year_index % 4][current_month_index]
            current_month_index = (current_month_index + 1) % 12  # Move to the next month

        # Remaining days are the current day in the month
        current_day = days_diff + 1  # Since days_diff counts from 0

    # Move backward if days_diff is negative (before the start date)
    else:
        if current_day_index > 1:
        # Just subtract one day if not at the start of the month
            current_day_index -= 1
        else:
            # Move to the previous month
            current_month_index = (current_month_index - 1) % 12
            if current_month_index == 11:  # If we moved from 'சித்திரை' (month 0) to 'பங்குனி' (month 11)
                current_year_index = (current_year_index - 1) % len(tamil_year_names)  # Move to the previous year

            # Set the day to the last day of the new current month
            current_day_index = days_sequence[current_year_index % 4][current_month_index]

        days_diff = abs(days_diff)
        # Move backward through the years
        while days_diff >= 365:  # Approximate check for a year
            current_year_index = (current_year_index - 1) % len(tamil_year_names)  # Move to previous year
            print(current_year_index, days_diff)
            year_days = sum(days_sequence[current_year_index % 4])  # Cycle through days_sequence
            if days_diff >= year_days:
                days_diff -= year_days

        # Now process the months within the current year
        while days_diff >= days_sequence[current_year_index % 4][current_month_index]:
            current_month_index = (current_month_index - 1) % 12  # Move to the previous month
            days_diff -= days_sequence[current_year_index % 4][current_month_index]

        # Remaining days are the current day in the month
        current_day = days_sequence[current_year_index % 4][current_month_index] - days_diff

    
    # Get the corresponding Tamil year and month
    tamil_year = tamil_year_names[current_year_index]
    tamil_month = tamil_month_names[current_month_index-1]

    return f"{current_day} {tamil_month}, {tamil_year}"

# Example usage
if __name__ == "__main__":
    # dt = datetime.now().date()
    dt = datetime(1998, 4, 14).date()
    tamil_date = get_tamil_date(dt)
    assert tamil_date != "2 சித்திரை, பகுதான்ய"
    print(tamil_date)
    # bug in prior date calculation
    # dt = start_date - timedelta(days=1)



