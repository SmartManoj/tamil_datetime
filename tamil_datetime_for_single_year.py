from datetime import datetime, timedelta

tamil_month_names = [
    'சித்திரை', 'வைகாசி', 'ஆனி', 'ஆடி', 'ஆவணி', 'புரட்டாசி', 
    'ஐப்பசி', 'கார்த்திகை', 'மார்கழி', 'தை', 'மாசி', 'பங்குனி',
]

days_in_tamil_months = [30, 32, 32, 31, 31, 31, 29, 30]

start_date = datetime(2024, 4, 14).date()
year_name = 'குரோதி'
def get_tamil_date(dt):
    # Calculate the difference in days from the start date
    delta_days = (dt - start_date).days
    
    # Find the corresponding Tamil month and day
    month_index = 0
    while delta_days >= days_in_tamil_months[month_index]:
        delta_days -= days_in_tamil_months[month_index]
        month_index += 1
    
    tamil_month = tamil_month_names[month_index]
    tamil_day = delta_days + 1  # Day is 1-based
    return f"{tamil_day} - {tamil_month}, {year_name}"


if __name__ == "__main__":
    # Example usage
    tamil_start_dates = [14,14,15,17,17,17,18,16,16]
    for month in range(4,12):
        dt = datetime(2024, month, tamil_start_dates[month-4]).date()
        print(dt)
        tamil_date = get_tamil_date(dt)
        print(tamil_date)
        assert tamil_date == f"1 - {tamil_month_names[month-4]}, {year_name}"
