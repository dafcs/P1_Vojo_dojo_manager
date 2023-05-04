from models.lesson import Lesson
from models.member import Member
from models.room import Room
import repositories.lesson_repository as lesson_repo
import repositories.member_repository as member_repo
import repositories.room_repository as room_repo

lesson_repo.delete_all()
member_repo.delete_all()

#testing class_repo **********************

# #tested - works
lesson_1 = Lesson('JiuJitsu')
lesson_2 = Lesson('Taekwondo')
lesson_3 = Lesson('Body Combat')
lesson_4 = Lesson('Judo')
lesson_5 = Lesson('Karate')
lesson_6 = Lesson('MMA')
class_list = [lesson_1,lesson_2,lesson_3,lesson_4,lesson_5,lesson_6]
for lesson in class_list:
    lesson_repo.save(lesson)
# print(f'PRINTING::console::/LESSON.SAVE>>{gym_lesson_1.name,gym_lesson_1.id}')

results = lesson_repo.select_all()
# for result in results:
    # print(f'PRINTING::console::LESSON.SELECT_ALL>>{result.__dict__}')

lesson_repo.delete(lesson_4.id)

#testing member_repo **********************

member_1 = Member('Rafa','Freit')
member_2 = Member('Kai','Bon')
member_3 = Member('Mart','Cos')
member_4 = Member('Al','Gor')
member_5 = Member('Pete','Smit')
member_6 = Member('Bae','Watzh')
member_7 = Member('Ter','Minat')
member_8 = Member('Soma','Nyna')
member_9 = Member('Mes','Hier')

member_list =[member_1,member_2,member_3,member_4,member_5,member_6,member_7,member_8,member_9]
for member in member_list:
    member_repo.save(member)
    # print(f'PRINTING::console::MEMBER.SAVE//>>> {member.first_name,member.id}')
results = member_repo.select_all()
# for result in results:
#     print(f'PRINTING::console::MEMBER.SELECT_ALL>>{result.__dict__}')

