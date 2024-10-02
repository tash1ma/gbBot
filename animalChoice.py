from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from AnimalKeyboards import make_row_keyboard  # Импортируем клавиатуру из вашего файла AnimalKeyboards
from keyboards.keyboards import kb2
# Создаем роутер для обработки команд в этом файле
router = Router()

# Списки животных и типов действий
animals_Array = [
    "fox",
    "cat",
    "dog",
    "pig",
    "cow"
]

animals_choise = [
    "pic",
    "verb",
    "voice"
]

# Определяем состояния для машины состояний
class AnimalChoice(StatesGroup):
    animal = State()
    type = State()

# Обработчик команды /prof
@router.message(Command("prof"))
async def command_start(message: types.Message, state: FSMContext):
    await message.answer(
        text="Выбери животное",
        reply_markup=make_row_keyboard(animals_Array)
    )
    await state.set_state(AnimalChoice.animal)  # Ждем выбора животного

# Обработчик выбора животного
@router.message(AnimalChoice.animal)
async def handle_animal_choice(message: types.Message, state: FSMContext):
    chosen_animal = message.text.lower()
    if chosen_animal in animals_Array:
        await state.update_data(chosen_animal=chosen_animal)
        await message.answer(
            text="Теперь выбери тип действия:",
            reply_markup=make_row_keyboard(animals_choise)
        )
        await state.set_state(AnimalChoice.type)
    else:
        await message.answer("Выбери животное из списка!")

# Обработчик выбора типа действия
@router.message(AnimalChoice.type)
async def handle_type_choice(message: types.Message, state: FSMContext):
    chosen_type = message.text.lower()
    if chosen_type in animals_choise:
        data = await state.get_data()
        chosen_animal = data['chosen_animal']
        await message.answer(f"Вы выбрали {chosen_animal} с действием {chosen_type}.", reply_markup = kb2)

        await state.clear()
    else:
        await message.answer("Выбери тип действия из списка!")
