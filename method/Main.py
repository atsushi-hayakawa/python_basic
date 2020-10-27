from method.MethodHolder import *


def main():
    print("main_start")

    # T1：The initial value is 0.
    if MethodHolder.index == 0:
        print("T1:OK")
    else:
        print("T1:NG")

    # T2：Cannot be access without creating an instance.
    try:
        MethodHolder.InstanceMethod()
        print("T2:NG")
    except TypeError as e:
        print("T2:OK")

    # T3：Can be access by creating an instance.
    try:
        MethodHolder().InstanceMethod()
        print("T3:OK")
    except TypeError as e:
        print("T3:NG")

    # T3-2：The index is 0.
    if MethodHolder.index == 0:
        print("T3-2:OK")
    else:
        print("T3-2:NG")

    # T4：Can be access without creating an instance.
    try:
        MethodHolder.ClassMethod()
        print("T4:OK")
    except TypeError as e:
        print("T4:NG")

    # T4-2：The index is 1.
    if MethodHolder.index == 1:
        print("T4-2:OK")
    else:
        print("T4-2:NG")

    # T4-3：Undo
    MethodHolder.index = 0

    # T5：Can be access without creating an instance.
    try:
        MethodHolder.StaticMethod()
        print("T5:OK")
    except TypeError as e:
        print("T5:NG")

    # T5-2：The index is 1.
    if MethodHolder.index == 1:
        print("T5-2:OK")
    else:
        print("T5-2:NG")

    # T5-3：Undo
    MethodHolder.index = 0

    # T6：Can be access without creating an instance.
    try:
        MethodHolderExtended.ClassMethod()
        print("T6:OK")
    except TypeError as e:
        print("T6:NG")

    # T6-2：The index is 101.
    if MethodHolderExtended.index == 101:
        print("T6-2:OK")
    else:
        print("T6-2:NG")

    # T6-3：Undo
    MethodHolderExtended.index = 100

    # T7：Can be access without creating an instance.
    try:
        MethodHolderExtended.StaticMethod()
        print("T7:OK")
    except TypeError as e:
        print("T7:NG")

    # T7-2：The index is 100.
    if MethodHolderExtended.index == 100:
        print("T7-2:OK")
    else:
        print("T7-2:NG")

    # T7-3：Undo
    MethodHolderExtended.index = 100

    # T7-4：The index is 1.
    if MethodHolder.index == 1:
        print("T7-4:OK")
    else:
        print("T7-4:NG")

    # T7-5：Undo
    MethodHolder.index = 0


main()
