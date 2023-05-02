from models.lesson import Lesson
from models.member import Member
from models.room import Room
import repositories.lesson_repository as class_repo
import repositories.member_repository as member_repo
import repositories.room_repository as room_repo

class_repo.delete_all()
member_repo.delete_all()

#testing class_repo **********************

# #tested - works
gym_lesson_1 = Lesson('Judo',2023/4/1,12:00:00)
gym_lesson_2 = Lesson('Taekwondo',2023/4/2,13:00:00)
gym_lesson_3 = Lesson('Body Combat',2023/4/5,14:00:00)
gym_lesson_4 = Lesson('Judo',2023/4/5,15:00:00)
class_list = [gym_lesson_1,gym_lesson_2,gym_lesson_3,gym_lesson_4]
for lesson in class_list:
    class_repo.save(lesson)
print(f'PRINTING::console::/LESSON.SAVE>>{gym_lesson_1.name,gym_lesson_1.id}')

results = class_repo.select_all()
for result in results:
    print(f'PRINTING::console::LESSON.SELECT_ALL>>{result.__dict__}')
class_repo.delete(gym_lesson_4.id)

#testing member_repo **********************

gym_member_1 = Member('Rafaela','Freitas')
gym_member_2 = Member('Daniel','Simoes')
gym_member_3 = Member('Marton','Costa')
gym_member_4 = Member('Peter','Smith')
member_list =[gym_member_1,gym_member_2,gym_member_3,gym_member_4]
for member in member_list:
    member_repo.save(member)
    # print(f'PRINTING::console::MEMBER.SAVE//>>> {member.first_name,member.id}')
results = member_repo.select_all()
for result in results:
    print(f'PRINTING::console::MEMBER.SELECT_ALL>>{result.__dict__}')

