import random

def generate_password(length: int, lower: bool = True, upper: bool = True, numbers: bool = True, symbols: bool = True) -> str:
  """
  Генерирует случайный пароль заданной длины.

  Args:
    length: Длина пароля.
    lower: Включать ли в пароль строчные буквы.
    upper: Включать ли в пароль заглавные буквы.
    numbers: Включать ли в пароль цифры.
    symbols: Включать ли в пароль символы.
  Returns:
    Сгенерированный пароль.
  """

  characters = ""
  if lower:
    characters += "abcdefghijklmnopqrstuvwxyz"
  if upper:
    characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  if numbers:
    characters += "0123456789"
  if symbols:
    characters += "!@#$%^&*()_-+={}[]<>,./?;:`~"

  password = ""
  for _ in range(length):
    password += random.choice(characters)

  return password


print(generate_password(15))