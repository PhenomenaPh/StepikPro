student_height = [int(height.strip()) for height in open(0)]

if len(student_height):
    print(
        f"""
Рост самого низкого ученика: {min(student_height)}
Рост самого высокого ученика: {max(student_height)}
Средний рост: {sum(student_height) // len(student_height)}
        """
    )
else:
    print("нет учеников")
