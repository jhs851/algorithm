all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


# 내꺼
# 시간복잡도 O(N)
# def get_absent_student(all_array, present_array):
#     present_array = set(present_array)
#
#     for student in all_array:
#         if student not in present_array:
#             return student


# 답안
# 시간복잡도 O(N)
# 공간복잡도 O(N)
def get_absent_student(all_array, present_array):
    student_dict = {}

    for key in all_array:
        student_dict[key] = True

    for key in present_array:
        del student_dict[key]

    for key in student_dict.keys():
        return key


print(get_absent_student(all_students, present_students))
