# ExchageRateBot
Данный бот служит, для получения курса валют в г.Несвиже
Данный бот состоит из следующих файлов:^
[bot.py] - показывает какие команды бот будет выполнять.

[requirements.txt] - показывет какие нужно загружать библиотеки для работы 
телеграмм бота

[config.py] - в этот файл мы импортирем уникальный ключ из local_config, но
при этом самого ключа не видно. Поэтому в Token- None.

[local_config] - храниться уникальный ключ телеграм-бота.
Token- даёт при помощи ключа доступ
к нашему боту, для текущего человека. Учётная запись. В репозиторий он не
скидывается.
[config]-сюда перемещаем local_config и config.py, и дабавляем
gitignore
