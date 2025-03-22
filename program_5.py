def course_info(course_index):
    subject = str(input("Select a subject (eg. COS):")).upper()
    result = [course_name for course_id, course_name in course_index.items() if course_id.startswith(subject)]
    return result if result else "Error: Subject not found"

def main():
    course_index = {}
    while True:
        course_id = input("Please enter a course ID (eg. COS 2005):").upper()
        course_name = input("Please enter the name of that course (eg. Python Programming):")
        course_index[course_id] = course_name
        i = input("Would you like to enter another course? (type Y for yes or anything else for no):")
        if i.lower() != 'y':
            break

    subject_list = course_info(course_index)

    print("Here are a list of courses in that subject:", subject_list)

main()
# Program #5, Donovan Thompson 3/21/2025
