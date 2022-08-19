#! /usr/bin/env python
# author: vin

'''
object
异常的父类  BaseException
第二层父类   Exception

try exception else finally
ok: try --> else --> finally
no ok: try --> except --> finally
'''


# try:
#     pass
# except Exception as e:
#     pass
# else:
#     pass
# finally:
#     pass

def division():
    try:
        return 1/0
    except RuntimeError as e:
        print(e.args[0])
    except ValueError as e:
        print(e.args[0])
    except EnvironmentError as e:
        print(e.args[0])
    except Exception as e:
        print('Exception异常', e.args[0])
    except ZeroDivisionError as e:
        print('Zero Exception', e.args[0])

if __name__ == '__main__':
    division()