def nested_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result
student_section = ["Yashan", "Sumit", "Yuvraj", "choori"]
student_name = ["C2", "C1", "C2", "C3"]
student_marks = [85,98,89,92]
print("Original strings:")
print(student_section)
print(student_name)
print(student_marks)
print("\nNested dictionary:")
print(nested_dictionary(student_section, student_name, student_marks))
print()