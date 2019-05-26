# Квалификационная работа бакалавра

> Маркин Кирилл

## Активность

* [График коммитов](https://github.com/Kirmark/bachelor-qualification-work/graphs/commit-activity)

## Документы

* [РПЗ](/note/note.pdf)
* [Презентация](/presentation/presentation.pdf)

## Реализация

* Парсер
  * Берет все страницы, которые найходит на сайте, переходит по всем ссылкам, нажимает на все кнопки дополнительной подгрузки контента, скачивает html код страниц и кладет их в базу SQLite
  * Код не выгружен в git так как там лютое спагетти
  * База не выгружена в git так как она весит несколько гигабайт
* Преобразование html в текст и сохранение в базу в отдельное поле
  * Код не выгружен в git так как там лютое спагетти
* Преобразование текста в формат vowpal_wabbit и сохранение в базу в отдельное поле
  * [1_base_text_to_base_vw.py](/application/data_clean/1_base_text_to_base_vw.py)
* Сбор данных в формате vowpal_wabbit из базы и выгрузка в текстовый файл
  * [2_base_vm_to_txt_vm.py](/application/data_clean/2_base_vm_to_txt_vm.py)
* Преобразование текстовго файла в формате vowpal_wabbit в формат bigartm - batches
  * [3_txt_vw_to_batches.py](/application/data_clean/3_txt_vw_to_batches.py)
* [Эксперименты с bigartm](/application/models/create_model.ipynb)
