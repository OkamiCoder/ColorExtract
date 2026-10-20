#Made with <3 by OkamiCoder

import os
import re
import sys

if os.name == 'nt':
    os.system('')

class ColorConverter:
    @staticmethod
    def hex_to_rgb(hex_color: str) -> tuple:
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 3:
            hex_color = ''.join(c * 2 for c in hex_color)
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int) -> str:
        return f"#{r:02x}{g:02x}{b:02x}"

    @staticmethod
    def is_valid_hex(hex_color: str) -> bool:
        return bool(re.match(r'^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$', hex_color))

    @staticmethod
    def is_valid_rgb(r: int, g: int, b: int) -> bool:
        return all(0 <= c <= 255 for c in (r, g, b))

class TerminalUI:
    RESET = "\033[0m"
    
    @classmethod
    def print_color_block(cls, r: int, g: int, b: int):
        bg_code = f"\033[48;2;{r};{g};{b}m"
        block_line = f"{bg_code}      {cls.RESET}"
        
        print("\n🎨 Визуализация цвета:")
        print(block_line)
        print(block_line)
        print(block_line)
        print()

    @classmethod
    def print_header(cls):
        print("\033[1;36m" + "="*45)
        print("       ColorExtract (Color Converter)")
        print("="*45 + "\033[0m")
        print("1. Конвертировать HEX ➡️  RGB")
        print("2. Конвертировать RGB ➡️  HEX")
        print("3. Выход")
        print("-" * 45)

def main():
    converter = ColorConverter()
    ui = TerminalUI()

    while True:
        ui.print_header()
        choice = input("Выберите действие (1-3): ").strip()

        if choice == '1':
            hex_input = input("Введите HEX цвет (например, #ff5733 или #f53): ").strip()
            if not converter.is_valid_hex(hex_input):
                print("\033[31m❌ Ошибка: Неверный формат HEX!\033[0m")
                continue
            
            r, g, b = converter.hex_to_rgb(hex_input)
            hex_normalized = f"#{hex_input.lstrip('#').lower()}"
            if len(hex_input.lstrip('#')) == 3:
                 hex_normalized = f"#{''.join(c*2 for c in hex_input.lstrip('#').lower())}"

            print(f"\n\033[32m✅ Успешно!\033[0m")
            print(f"HEX: \033[1m{hex_normalized}\033[0m")
            print(f"RGB: \033[1mrgb({r}, {g}, {b})\033[0m")
            ui.print_color_block(r, g, b)

        elif choice == '2':
            rgb_input = input("Введите RGB цвет (например, 255, 87, 51): ").strip()
            try:
                parts = [int(x.strip()) for x in rgb_input.split(',')]
                if len(parts) != 3:
                    raise ValueError
                
                r, g, b = parts
                if not converter.is_valid_rgb(r, g, b):
                    raise ValueError

                hex_result = converter.rgb_to_hex(r, g, b)
                
                print(f"\n\033[32m✅ Успешно!\033[0m")
                print(f"RGB: \033[1mrgb({r}, {g}, {b})\033[0m")
                print(f"HEX: \033[1m{hex_result}\033[0m")
                ui.print_color_block(r, g, b)
                
            except (ValueError, IndexError):
                print("\033[31m❌ Ошибка: Введите ровно 3 числа от 0 до 255 через запятую!\033[0m")

        elif choice == '3':
            print("\033[33m👋 До свидания!\033[0m")
            sys.exit(0)
        
        else:
            print("\033[31m❌ Неверный выбор. Попробуйте снова.\033[0m")
        
        input("\033[90mНажмите Enter для продолжения...\033[0m")

if __name__ == "__main__":
    main()