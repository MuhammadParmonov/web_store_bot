from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

contact_keyboard = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text="Kontakt yuborish", request_contact = True),
		]
	], 
	resize_keyboard = True
)