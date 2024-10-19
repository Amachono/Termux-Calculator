#!/bin/bash

# Функция для запуска всех .py и .pyc файлов в указанном каталоге
echo "Loading...do NOT click enter"
run_scripts() {
    for script in "$1"/*; do
        if [ -d "$script" ]; then
            # Если это каталог, рекурсивно вызываем функцию
            run_scripts "$script"
        elif [[ "$script" == *.py || "$script" == *.pyc ]]; then
            python "$script" 2>/dev/null  # Скрываем только ошибки
        fi
    done
}

# Запускаем функцию для текущего каталога
run_scripts "."