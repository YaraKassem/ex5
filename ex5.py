import json
import os




def names_of_registered_students(input_json_path, course_name):
    names = []
    with open(input_json_path, 'r') as file:
        loaded_dict = json.load(file)
    for v in loaded_dict.values():
        if course_name in v["registered_courses"]:
            names.append(v["student_name"])
    return names


def enrollment_numbers(input_json_path, output_file_path):
    courses_dict = {}
    with open(input_json_path, 'r') as file:
        loaded_dict = json.load(file)
    for v in loaded_dict.values():
        for i in v["registered_courses"]:
            if i in courses_dict:
                courses_dict[i] += 1
            else:
                courses_dict[i] = 1
    with open(output_file_path, 'w') as file:
        for key in sorted(courses_dict):
            file.write('"%s" %s\n' % (key, courses_dict[key]))



def courses_for_lecturers(json_directory_path, output_json_path):
    lecturers_dict = {}
    list =[file for file in os.listdir(json_directory_path) if file.endswith('.json')]
    for file in os.listdir(json_directory_path):
        if file.endswith('.json'):
            file_path = f"{json_directory_path}/{file}"
            with open(file_path, 'r') as curr_file:
                loaded_dict = json.load(curr_file)
            for v in loaded_dict.values():
                for lec in v["lecturers"]:
                    if lec in lecturers_dict:
                        if not (v["course_name"] in lecturers_dict[lec]):
                            lecturers_dict[lec].append((v["course_name"]))
                    else:
                        lecturers_dict[lec] = [v["course_name"]]
    with open(output_json_path, 'w') as file:
        json.dump(lecturers_dict, file)




