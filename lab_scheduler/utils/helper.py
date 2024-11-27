from lab_scheduler import static

def sort_list_of_tuples_by_first_value(arr:list):
    return arr.sort(key=lambda x: x[0])

def get_months(semester):
    start_month = static.SEMESTERS_INFO[semester]["start_month"]
    end_month = static.SEMESTERS_INFO[semester]["end_month"]
    return start_month, end_month