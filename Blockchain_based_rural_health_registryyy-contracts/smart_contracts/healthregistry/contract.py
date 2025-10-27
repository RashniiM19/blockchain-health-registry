from algokit_utils import OnCompleteAction
from pyteal import *

@Subroutine(TealType.uint64)
def add_patient_record(patient_id: Expr, diagnosis: Expr, doctor_id: Expr):
    return Seq([
        App.globalPut(Bytes("patient_" + patient_id), diagnosis),
        App.localPut(Int(0), Bytes("doctor"), doctor_id),  # Local state for doctor
        Return(Int(1))
    ])

@Subroutine(TealType.uint64)
def get_patient_record(patient_id: Expr):
    return App.globalGet(Bytes("patient_" + patient_id))

def approval_program():
    return Cond(
        [Txn.application_id() == Int(0), Return(Int(1))],  # Create app
        [Txn.on_completion() == OnComplete.NoOp, Cond(
            [Txn.application_args[0] == Bytes("add_record"), add_patient_record(
                Txn.application_args[1], Txn.application_args[2], Txn.application_args[3])],
            [Txn.application_args[0] == Bytes("get_record"), get_patient_record(Txn.application_args[1])]
        )],
        [Txn.on_completion() == OnComplete.DeleteApplication, Return(Int(1))],
        [Txn.on_completion() == OnComplete.UpdateApplication, Return(Int(0))],
    )

def clear_program():
    return Return(Int(1))
