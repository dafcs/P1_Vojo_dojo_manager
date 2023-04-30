from models.gym_class import GymClass
from models.gym_member import GymMember
from models.gym_room import GymRoom
import repositories.gym_class_repository as class_repo
import repositories.gym_member_repository as member_repo
import repositories.gym_room_repository as room_repo

class_repo.delete_all()

#testing class_repo **********************

#tested - works
gym_class_1 = GymClass('Pilates')
# print(f'PRINTING console //>>> {gym_class_1.name,gym_class_1.id}')
class_repo.save(gym_class_1)
results = class_repo.select_all()
for result in results:
    print(f'PRINTINT....>>>{result.__dict__}')
class_repo.delete(3)
results = class_repo.select_all()
for result in results:
    print(f'PRINTINT....>>>{result.__dict__}')

