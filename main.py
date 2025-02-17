from PIL import Image
import os

def add_icon_to_image(base_image_path, icon_path, position):
    """
    Добавляет значок на базовое изображение в указанную позицию.
    
    :param base_image_path: Путь к базовому изображению.
    :param icon_path: Путь к значку.
    :param position: Кортеж (x, y) для позиционирования значка.
    :return: Объект изменённого изображения.
    """
    # Открываем базовое изображение и значок
    base_image = Image.open(base_image_path).convert("RGBA")
    icon = Image.open(icon_path).convert("RGBA")

    # Создаём новое изображение, на котором будем объединять базовое изображение и значок
    result = Image.new("RGBA", base_image.size)

    # Накладываем базовое изображение
    result.paste(base_image, (0, 0))

    # Накладываем значок в указанной позиции
    result.paste(icon, position, mask=icon)

    return result

def save_image(image, output_path):
    """
    Сохраняет изображение в указанный путь.
    
    :param image: Объект изображения.
    :param output_path: Путь для сохранения.
    """
    image.convert("RGB").save(output_path)
    print(f"Изображение успешно сохранено по пути: {output_path}")

if __name__ == "__main__":
    # Пути к файлам
    input_folder = "input"
    output_folder = "output"
    icons_folder = "icons"

    # Проверяем наличие папок
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Загружаем базовое изображение
    base_image_path = os.path.join(input_folder, "base_image.jpg")  # Замените на ваше имя файла
    if not os.path.exists(base_image_path):
        print("Базовое изображение не найдено!")
        exit()

    # Загружаем значок
    icon_path = os.path.join(icons_folder, "icon1.png")  # Замените на нужный значок
    if not os.path.exists(icon_path):
        print("Значок не найден!")
        exit()

    # Указываем позицию для значка (например, верхний левый угол)
    position = (50, 50)  # (x, y)

    # Добавляем значок к изображению
    result_image = add_icon_to_image(base_image_path, icon_path, position)

    # Сохраняем результат
    output_path = os.path.join(output_folder, "result_image.jpg")
    save_image(result_image, output_path)
