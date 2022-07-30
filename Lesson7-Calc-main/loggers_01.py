# import sys
# import logging
# from logging import StreamHandler, Formatter, LogRecord, LoggerAdapter, LogRecord

# # Конфигурация logging
# # конфигурировать logging нужно через python-словарь. 
# # Для этого необходимо вызвать функцию 
# # logging.config.dictConfig и передать ей специальный словарь. 
#     # version — ключ указывает версию конфига, 
#     # рекомендуется наличие этого ключа со значением 1, 
#     # нужно для обратной совместимости в случае, 
#     # если в будущем появятся новые версии конфигов.
#     # disable_existing_loggers — запрещает или разрешает
#     # настройки для существующих логеров (на момент запуска), 
#     # по умолчанию равен True
#     # formatters — настройки форматов логов
#     # handlers — настройки для обработчиков логов
#     # loggers — настройки существующих логеров
# import logging.config
# LOGGING_CONFIG = {
#     'version': 1,
#     'disable_existing_loggers': False,

#     'formatters': {
#         'default_formatter': {
#             'format': '[%(levelname)s:%(asctime)s] %(message)s'
#         },
#     },

#     'handlers': {
#         'stream_handler': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'default_formatter',
#         },
#     },

#     'loggers': {
#         'my_package': {
#         'handlers': ['stream_handler'],
#         'level': 'DEBUG',
#         'propagate': False
#         }
#     }
# }

# logging.config.dictConfig(LOGGING_CONFIG)
# logger = logging.getLogger('my_logger')
# logger.debug('debug log')

# # Наследование в logging
# # - - - - - - - - - - - - -
# # Ещё одним удобным механизмом в logging является "наследование"
# # настроек корневого логера его потомками. 
# # Наследование задаётся через символ .
# # в названии логера. 
# # То есть логер с названием my_package.logger1 
# # унаследует все настройки, 
# # заданные для my_package. 
# # _________________________________________________________
# # LoggerAdapter
# # Адаптер нужен для передачи дополнительной 
# # контекстной информации при каждой записи лога через Logger.
# class CustomLoggerAdapter(LoggerAdapter):
#     def process(self, msg, kwargs):
#         return f'{msg} from {self.extra["username"]}', kwargs

# logger2 = logging.getLogger('adapter')
# logger2.setLevel(logging.DEBUG)

# handler = StreamHandler(stream=sys.stdout)
# handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))

# adapter = CustomLoggerAdapter(logger2, {'username': 'Неудачник :)'})

# logger2.addHandler(handler)
# adapter.error('failed to save')

# # Filter
# # Задача класса фильтровать сообщения
# # по заданной разработчиком логике.

# def filter_python(record: LogRecord) -> bool:
#   return record.getMessage().find('python') != -1

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# handler = StreamHandler(stream=sys.stdout)
# handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
# logger.addHandler(handler)
# logger.addFilter(filter_python)

# logger.debug('debug info')
# Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s, response: %(response)s')

# # Formatter
# # Formatter это ёщё один класс в семействе logging, отвечающий за отображение лога. 
# # Если класс Handler ответственный за то куда будет происходить запись,
# # то класс Formatter отвечает на вопрос как будет записано сообщение.

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# handler = StreamHandler(stream=sys.stdout)
# handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
# logger.addHandler(handler)

# logger.info('debug information')


# logger = logging.getLogger(__name__) # нужно использовать эту запись
# logger.setLevel(logging.WARNING)
# handler = StreamHandler(stream=sys.stdout)
# logger.addHandler(handler)

# logger.warning('debug information')


# # logger.setLevel(logging.DEBUG)
# # logger.setLevel(logging.INFO)
# # logger.setLevel(logging.WARNING)
# # logger.setLevel(logging.ERROR)
# # logger.setLevel(logging.CRITICAL)

# logger.debug('debug info')
# logger.info('info')
# logger.warning('warning')
# logger.error('debug info')
# logger.critical('debug info')

# # Handler
# # Задача класса Handler и его потомков обрабатывать запись сообщений/логов. 
# # Т.е. Handler отвечает за то куда будут записаны сообщения. 
# # В базовом наборе logging предоставляет ряд готовых классов-обработчиков:
# #SteamHandler — запись в поток, например, stdout или stderr.
# #FileHandler — запись в файл, 
# # класс имеет множество производных классов с различной функциональностью 
# # (ротация файлов логов по размеру, времени и т.д.)
# #SocketHandler — запись сообщений в сокет по TCP
# #DatagramHandler — запись сообщений в сокет по UDP
# #SysLogHandler — запись в syslog
# # HTTPHandler — запись по HTTP
  
# #Возвращает новый экземпляр класса StreamHandler. 
# #Если указан поток, то экземпляр будет использовать его для регистрации выходных данных;
# #в противном случае будет использоваться sys.stderr.
# # class logging.StreamHandler(stream=None) 


# # emit(record)
# #Если указан форматор, то он используется для форматирования записи. 
# #Затем запись записывается в поток, за которым следует терминатор. 
# #Если информация об исключении присутствует,
# #она отформатируется с помощью traceback.print_exception() и добавляется к потоку.
# # try.
# # 1/0
# # expept:
# #   logger.exception('exception')



# from datetime import datetime as dt
# from time import time 

# with open("Log_"+time+".txt", 'w') as data:
#   def logDt(Variable,Reader, Log_):
#     files_ = open(log_, "a")
#     files_.write("{0} -- {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"), Variable,Reader))
#     files_.close()


# def Calculator_logger(data):
#   time = dt.now().strftime('%H:%M')
#   with open('log.txt', 'a') as file:
#     file.write('{}; Calculator_logger;{}\n'
#                 .format(time, data))
    
    
# def inpt_logger(data):
#   time = dt.now().strftime('%H:%M')
#   with open('log.txt', 'a') as file:
#     file.write('{}; inpt_logger;{}\n'
#                 .format(time, data))
        
        
# def Controller_logger(data):
#   time = dt.now().strftime('%H:%M')
#   with open('log.txt', 'a') as file:
#     file.write('{}; Controller_logger;{}\n'
#                 .format(time, data))


# path = 'Log_.txt'
# data = open(path, 'r')
# for line in data:
#   print(line)
# data.close()
# exit()




# def _______________logger(data):
#   time = dt.now().strftime('%H:%M')
#   with open('log.txt', 'a') as file:
#     file.write('{}; __________________;{}\n'
#                 .format(time, data))
    
    
# def ___________logger(data):
#   time = dt.now().strftime('%H:%M')
#   with open('log.txt', 'a') as file:
#     file.write('{}; ________;{}\n'
#                 .format(time, data))
        
        
# def ______________logger(data):
#   time = dt.now().strftime('%H:%M')
#   with open('log.txt', 'a') as file:
#     file.write('{}; ****;{}\n'
#                 .format(time, data))
    