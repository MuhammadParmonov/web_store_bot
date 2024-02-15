from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from loader import dp, db
from keyboards.default.contact import contact_keyboard
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(Command("phone_number"))
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Telefon aqamingizni kiriting", reply_markup=contact_keyboard )
    await state.set_state("phone_number")


@dp.message_handler(state="phone_number", content_types='contact')
async def enter_email(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    db.update_user_phone_number(phone_number=phone_number, id=message.from_user.id)
    user = db.select_user(id=message.from_user.id)
    await message.answer(f"Baza yangilandi: {user}", reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(state="phone_number", content_types='contact')
async def enter_email(message: types.Message, state: FSMContext):
    
    await message.answer(f"Iltimos telefon raqamingizni jonating")