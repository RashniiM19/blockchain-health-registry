from pyteal import *

@Subroutine(TealType.uint64)
def add_record(key: Expr, value: Expr) -> Expr:
    return Seq(
        App.globalPut(key, value),
        Return(Int(1))
    )

@Subroutine(TealType.uint64)
def get_record(key: Expr) -> Expr:
    return App.globalGet(key)  # Returns the value

approval_program = Cond(
    [Txn.application_args[0] == Bytes("add"), add_record(Txn.application_args[1], Txn.application_args[2])],
    [Txn.application_args[0] == Bytes("get"), get_record(Txn.application_args[1])]
)

clear_program = Return(Int(1))

if __name__ == "__main__":
    print(compileTeal(approval_program, Mode.Application, Version.v5))
    print(compileTeal(clear_program, Mode.Application, Version.v5))
